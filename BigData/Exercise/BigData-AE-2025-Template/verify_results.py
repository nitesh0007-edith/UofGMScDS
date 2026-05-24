"""
Ground-truth verifier for AssessedExercise results.

Replicates the exact logic from the original Java classes:
  NullPriceFilter, DateFilter, PriceReaderMap,
  CalculateFeaturesMap (Volitility + Returns), VolatilityFilter,
  AssetMetadataPairing, PERatioFilter, sorting by returns desc.

Run:  python3 verify_results.py
"""

import json
import math
import csv
from collections import defaultdict

# ── Configuration (mirrors AssessedExercise.java) ─────────────────────────────
PRICES_FILE   = "resources/all_prices-noHead.csv"
ASSETS_FILE   = "resources/stock_data.json"
END_DATE      = "2020-04-01"
VOL_CEILING   = 4.0
PE_THRESHOLD  = 25.0
RETURNS_DAYS  = 5        # Returns.calculate(5, ...)
VOLATILITY_WINDOW = 251  # CalculateFeaturesMap: last 251 days

# ── Step 0: load asset metadata (AssetMetadataPairing) ────────────────────────
print("Loading asset metadata …")
with open(ASSETS_FILE) as f:
    raw_assets = json.load(f)

metadata = {}
for a in raw_assets:
    sym = a.get("symbol")
    if sym:
        metadata[sym] = {
            "name":     a.get("name", ""),
            "industry": a.get("industry", ""),
            "sector":   a.get("sector", ""),
            "pe_ratio": float(a["price_earning_ratio"]) if "price_earning_ratio" in a and a["price_earning_ratio"] is not None else 0.0,
        }

print(f"  {len(metadata):,} assets loaded")

# ── Step 1: read + NullPriceFilter + DateFilter ────────────────────────────────
# CSV columns (0-based): Date, Open, High, Low, Close, AdjClose, Volume, Stock
print("Reading and filtering prices …")

end_date_str = END_DATE  # "2020-04-01"

prices_by_ticker = defaultdict(list)
rows_read = rows_kept = 0

with open(PRICES_FILE, newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        rows_read += 1

        # NullPriceFilter: skip if any of the 8 fields is empty
        if len(row) < 8 or any(v == "" or v is None for v in row[:8]):
            continue

        date_str = row[0]

        # DateFilter: keep rows where date <= END_DATE (string comparison works for YYYY-MM-DD)
        if date_str > end_date_str:
            continue

        try:
            close_price = float(row[4])
        except ValueError:
            continue

        ticker = row[7]
        prices_by_ticker[ticker].append((date_str, close_price))
        rows_kept += 1

print(f"  Read {rows_read:,} rows, kept {rows_kept:,} rows across {len(prices_by_ticker):,} tickers")

# ── Step 2: sort by date per ticker ───────────────────────────────────────────
# CalculateFeaturesMap sorts ascending by date before computing indicators
for ticker in prices_by_ticker:
    prices_by_ticker[ticker].sort(key=lambda x: x[0])

# ── Helper: Volitility.java formula ───────────────────────────────────────────
def signed_log_daily_change(prev, curr):
    """Replicates Volitility.java's per-day transformation."""
    if prev == 0:
        return 0.0
    vol = (curr - prev) / prev
    if vol > 0:
        return math.log(vol)
    elif vol < 0:
        return -math.log(-vol)
    return 0.0

def population_std(values):
    """MathUtils.std(): population std dev (divide by N, not N-1)."""
    n = len(values)
    if n == 0:
        return 0.0
    mean = sum(values) / n
    return math.sqrt(sum((x - mean) ** 2 for x in values) / n)

# ── Step 3: compute AssetFeatures per ticker (CalculateFeaturesMap) ───────────
print("Computing volatility and returns …")

features = {}
for ticker, price_list in prices_by_ticker.items():
    close_prices = [p[1] for p in price_list]
    n = len(close_prices)

    # ── Volatility (Volitility.java) ──────────────────────────────────────────
    # Use last VOLATILITY_WINDOW prices if enough data, else all prices
    vol_prices = close_prices[-VOLATILITY_WINDOW:] if n >= VOLATILITY_WINDOW else close_prices

    if len(vol_prices) < 2:
        volatility = 0.0
    else:
        daily_changes = [
            signed_log_daily_change(vol_prices[i], vol_prices[i + 1])
            for i in range(len(vol_prices) - 1)
        ]
        volatility = population_std(daily_changes)

    # ── Returns (Returns.java: numDays=5) ─────────────────────────────────────
    # Requires at least numDays+1 = 6 prices
    if n < RETURNS_DAYS + 1:
        asset_return = 0.0
    else:
        prev_price = close_prices[-(RETURNS_DAYS + 1)]   # close_prices[n-6]
        curr_price = close_prices[-1]
        asset_return = (curr_price - prev_price) / prev_price if prev_price != 0 else 0.0

    features[ticker] = {"return": asset_return, "volatility": volatility}

print(f"  Features computed for {len(features):,} tickers")

# ── Step 4: VolatilityFilter ───────────────────────────────────────────────────
low_vol = {t: f for t, f in features.items() if f["volatility"] < VOL_CEILING}
print(f"  After volatility filter (<{VOL_CEILING}): {len(low_vol):,} tickers")

# ── Step 5: join with metadata + PERatioFilter ────────────────────────────────
assets = []
no_meta = pe_filtered = 0
for ticker, feat in low_vol.items():
    meta = metadata.get(ticker)
    if meta is None:
        no_meta += 1
        continue
    pe = meta["pe_ratio"]
    # PERatioFilter: keep if pe > 0 AND pe < PE_THRESHOLD
    if pe <= 0 or pe >= PE_THRESHOLD:
        pe_filtered += 1
        continue
    assets.append({
        "ticker":     ticker,
        "name":       meta["name"],
        "industry":   meta["industry"],
        "sector":     meta["sector"],
        "return":     feat["return"],
        "volatility": feat["volatility"],
        "pe_ratio":   pe,
    })

print(f"  No metadata: {no_meta}, P/E filtered: {pe_filtered}, remaining: {len(assets):,}")

# ── Step 6: sort by return descending, take top 5 ─────────────────────────────
assets.sort(key=lambda a: a["return"], reverse=True)
top5 = assets[:5]

# ── Print results ──────────────────────────────────────────────────────────────
print()
print("=" * 50)
print("EXPECTED TOP 5 (Python ground truth)")
print("=" * 50)
for i, a in enumerate(top5, 1):
    print(f"Rank {i}: {a['name']} ({a['ticker']})")
    print(f"  - Industry:   {a['industry']}")
    print(f"  - Sector:     {a['sector']}")
    print(f"  - Returns:    {a['return']}")
    print(f"  - Volatility: {a['volatility']}")
    print(f"  - P/E Ratio:  {a['pe_ratio']}")
    print()

# ── Compare against Spark output ──────────────────────────────────────────────
spark_output = [
    ("TOPS",  1.555555500366074),
    ("ATHX",  1.1868131342695454),
    ("SNMP",  0.6956520809568411),
    ("BATL",  0.6769231897839469),
    ("AIM",   0.5698925020626091),
]

print("=" * 50)
print("COMPARISON vs Spark output")
print("=" * 50)
print(f"{'Rank':<5} {'Python ticker':<10} {'Spark ticker':<10} {'Match?':<8} {'Δ return'}")
all_match = True
for i, ((spark_ticker, spark_ret), py_asset) in enumerate(zip(spark_output, top5), 1):
    py_ticker = py_asset["ticker"]
    ticker_match = py_ticker == spark_ticker
    ret_diff = abs(py_asset["return"] - spark_ret)
    match_str = "YES" if ticker_match else "NO !!!"
    if not ticker_match:
        all_match = False
    print(f"  {i:<4} {py_ticker:<10} {spark_ticker:<10} {match_str:<8} {ret_diff:.2e}")

print()
if all_match:
    print("✓ All 5 tickers match — Spark output is CORRECT")
else:
    print("✗ Mismatch detected — check implementation")
