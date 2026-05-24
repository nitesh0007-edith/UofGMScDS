package bigdata.objects;

import java.io.Serializable;
import java.util.ArrayList;

/**
 * Holds per-ticker summary stats for the map-side aggregation approach.
 * We keep a window of the last 252 close prices so we can compute
 * volatility over the most recent ~1 year of trading days.
 */
public class TickerStats implements Serializable {

    private static final long serialVersionUID = 1L;
    private static final int WINDOW_SIZE = 252;

    // each entry is [encodedDate, closePrice]
    private ArrayList<double[]> closePrices;

    // last 6 prices needed for the 5-day returns calc
    private ArrayList<double[]> recentPrices;

    private int totalPrices;

    public TickerStats() {
        closePrices = new ArrayList<>();
        recentPrices = new ArrayList<>(7);
    }

    /** Turn a date into YYYYMMDD so we can sort numerically */
    public static long encodeDate(short year, short month, short day) {
        return year * 10000L + month * 100L + day;
    }

    public void addClosePrice(long encodedDate, double closePrice) {
        closePrices.add(new double[]{encodedDate, closePrice});
    }

    /** Drop older prices if we have more than 252 */
    private void trimWindow() {
        if (closePrices.size() > WINDOW_SIZE) {
            closePrices = new ArrayList<>(
                    closePrices.subList(closePrices.size() - WINDOW_SIZE, closePrices.size()));
        }
    }

    public void addRecentPrice(long encodedDate, double closePrice) {
        recentPrices.add(new double[]{encodedDate, closePrice});
    }

    /**
     * Combines stats from two different partitions for the same ticker.
     * We just put all the close prices together, sort them, and keep
     * the 252 most recent ones.
     */
    public static TickerStats merge(TickerStats a, TickerStats b) {
        TickerStats result = new TickerStats();
        result.totalPrices = a.totalPrices + b.totalPrices;

        // combine both price windows and keep latest 252
        result.closePrices = new ArrayList<>(a.closePrices.size() + b.closePrices.size());
        result.closePrices.addAll(a.closePrices);
        result.closePrices.addAll(b.closePrices);
        result.closePrices.sort((x, y) -> Double.compare(x[0], y[0]));
        result.trimWindow();

        // same idea for the recent prices - merge and keep last 6
        result.recentPrices = new ArrayList<>(a.recentPrices);
        result.recentPrices.addAll(b.recentPrices);
        if (result.recentPrices.size() > 6) {
            result.recentPrices.sort((x, y) -> Double.compare(x[0], y[0]));
            result.recentPrices = new ArrayList<>(
                    result.recentPrices.subList(result.recentPrices.size() - 6, result.recentPrices.size()));
        }

        return result;
    }

    /**
     * Turns the accumulated price data into an AssetFeatures object.
     * Uses the same signed-log volatility formula as Volitility.java
     * and computes 5-day returns from the most recent prices.
     */
    public AssetFeatures toAssetFeatures() {
        AssetFeatures features = new AssetFeatures();

        // 5-day returns: (latest price - price 5 days ago) / price 5 days ago
        if (recentPrices.size() >= 6) {
            recentPrices.sort((x, y) -> Double.compare(x[0], y[0]));
            double currentPrice = recentPrices.get(recentPrices.size() - 1)[1];
            double priceBack5 = recentPrices.get(recentPrices.size() - 6)[1];
            features.setAssetReturn((currentPrice - priceBack5) / priceBack5);
        } else {
            features.setAssetReturn(0.0);
        }

        // volatility: population std dev of signed-log daily price changes
        if (closePrices.size() >= 2) {
            closePrices.sort((x, y) -> Double.compare(x[0], y[0]));

            int n = closePrices.size();
            ArrayList<Double> logChanges = new ArrayList<>(n - 1);
            for (int i = 1; i < n; i++) {
                double prevClose = closePrices.get(i - 1)[1];
                double currClose = closePrices.get(i)[1];
                double change = (currClose - prevClose) / prevClose;
                double logChange;
                if (change > 0) logChange = Math.log(change);
                else if (change < 0) logChange = -Math.log(-change);
                else logChange = 0.0;
                logChanges.add(logChange);
            }

            // population std dev (same as MathUtils.std)
            double sum = 0;
            for (double v : logChanges) sum += v;
            double mean = sum / logChanges.size();

            double squareResiduals = 0;
            for (double v : logChanges) {
                double diff = v - mean;
                squareResiduals += diff * diff;
            }
            features.setAssetVolitility(Math.sqrt(squareResiduals / logChanges.size()));
        } else {
            features.setAssetVolitility(Double.MAX_VALUE);
        }

        features.setPeRatio(0.0);
        return features;
    }

    public int getTotalPrices() { return totalPrices; }
    public void setTotalPrices(int totalPrices) { this.totalPrices = totalPrices; }
}
