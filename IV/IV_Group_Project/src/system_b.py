"""System B — Temporal Decomposition + Heatmap dashboard.

How weather varies across months, seasons, and years. Green/yellow/blue palette.

Charts:
  1. Horizontal bar — ranking by selected metric and grouping
  2. Calendar heatmap — month x year grid of mean metric values
  3. Grouped bar — seasonal wind speed vs humidity comparison
  4. Generalised selection — yearly overview with drill-down to season/month
"""

import json
import os
import sys

import altair as alt
import pandas as pd

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _SCRIPT_DIR)
from data_prep import load_and_prepare


def _resolve_path(*candidates: str) -> str:
    """Return the first candidate path that exists, or the last one as default."""
    for p in candidates:
        if os.path.exists(p):
            return p
    return candidates[-1]

MONTH_ORDER = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
]
SEASON_ORDER = ["Winter", "Spring", "Summer", "Autumn"]

WEATHER_COLORS = alt.Scale(
    domain=["rain", "clear-day", "partly-cloudy-day", "cloudy", "fog", "unknown"],
    range=["#4c78a8", "#f58518", "#e45756", "#72b7b2", "#54a24b", "#bab0ac"],
)


# --- HTML page builder (same template as other systems) ---

def save_system_page(chart, system_name, how_to_use_html, tasks_html,
                     output_path, nav_links=None):
    """Wrap the Altair chart in a full HTML page and save it."""
    spec_json = json.dumps(chart.to_dict(), indent=2)

    nav_buttons = ""
    if nav_links:
        nav_buttons = "".join(
            f'<a class="nav-sys-btn" href="{lnk["href"]}">{lnk["label"]}</a>'
            for lnk in nav_links
        )

    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{system_name}</title>
    <script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
    <script src="https://cdn.jsdelivr.net/npm/vega-lite@5.20.1"></script>
    <script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>
    <style>
        *, *::before, *::after {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: Georgia, 'Times New Roman', serif; margin: 0; background: #fff; }}
        .navbar {{
            background: #003865;
            display: flex; align-items: center; justify-content: space-between;
            padding: 8px 36px; border-bottom: 3px solid #00a3e0;
        }}
        .nav-brand {{ display: flex; align-items: center; text-decoration: none; }}
        .nav-brand img {{ height: 44px; }}
        .nav-right {{ display: flex; align-items: center; gap: 10px; }}
        .nav-sys-btn {{
            display: inline-block; padding: 7px 18px;
            background: rgba(255,255,255,0.12); color: #fff;
            border: 1px solid rgba(255,255,255,0.25); border-radius: 6px;
            text-decoration: none; font-family: 'Segoe UI', Tahoma, sans-serif;
            font-size: 0.82em; font-weight: 600; letter-spacing: 0.3px;
            transition: background 0.2s;
        }}
        .nav-sys-btn:hover {{ background: rgba(255,255,255,0.22); }}
        .page-body {{ padding: 20px 28px 30px; max-width: 1200px; margin: 0 auto; }}
        h1 {{ text-align: center; color: #8b0000; font-size: 2.5em; margin-bottom: 5px; }}
        hr.title-rule {{ border: none; border-top: 2px solid #8b0000; margin-bottom: 30px; }}
        h2 {{ font-size: 1.3em; margin-top: 30px; }}
        .info-box {{ background: #f5f5f5; padding: 15px 25px; border-radius: 4px; margin: 10px 0 25px; font-family: 'Segoe UI', Tahoma, sans-serif; }}
        .info-box ul {{ margin: 8px 0; padding-left: 20px; }}
        .info-box li {{ margin: 6px 0; line-height: 1.5; font-size: 0.95em; }}
        .info-box ol {{ margin: 8px 0; padding-left: 20px; }}
        .info-box ol li {{ margin: 8px 0; line-height: 1.5; font-size: 0.95em; }}
        #controls-panel {{
            background: #f8f9fa; border: 1px solid #dee2e6; border-radius: 8px;
            padding: 14px 22px; margin: 10px 0 16px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.08);
        }}
        #controls-panel .vega-bindings {{
            display: flex; flex-wrap: wrap; gap: 8px 20px; align-items: center;
            font-family: 'Segoe UI', Tahoma, sans-serif; font-size: 0.9em;
        }}
        .vega-bind {{ display: flex; align-items: center; gap: 5px; }}
        .vega-bind label {{ font-weight: 600; white-space: nowrap; color: #444; }}
        #vis {{ display: flex; justify-content: center; margin: 10px 0; }}
    </style>
</head>
<body>
    <nav class="navbar">
        <a class="nav-brand" href="index.html" title="Back to Home">
            <img src="uofg_logo_boxed.png" alt="University of Glasgow — Home">
        </a>
        <div class="nav-right">{nav_buttons}</div>
    </nav>
    <div class="page-body">
        <h1>{system_name}</h1>
        <hr class="title-rule">
        <h2>How to Use</h2>
        <div class="info-box">{how_to_use_html}</div>
        <h2>Tasks</h2>
        <div class="info-box">{tasks_html}</div>
        <div id="controls-panel"></div>
        <div id="vis"></div>
    </div>
    <script>
        var spec = {spec_json};
        vegaEmbed('#vis', spec, {{mode: 'vega-lite', actions: {{export: true, source: false, compiled: false, editor: false}}}})
            .then(function(result) {{
                window.vegaView = result.view;
                var bindings = document.querySelector('#vis .vega-bindings');
                var panel = document.getElementById('controls-panel');
                if (bindings && panel) {{
                    panel.appendChild(bindings);
                }}
            }})
            .catch(console.error);
    </script>
</body>
</html>"""
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w") as f:
        f.write(html)


# --- Bound parameters (dropdowns + sliders) ---

def _make_params():
    """Set up the dropdowns and sliders shared across System B charts."""
    metric_dropdown = alt.binding_select(
        options=["tempMax", "windSpeed", "humidity", "visibility",
                 "tempRange", "cloudCover", "_count"],
        labels=["Avg Max Temp", "Avg Wind Speed", "Avg Humidity",
                "Avg Visibility", "Avg Temp Range", "Avg Cloud Cover",
                "Count (Frequency)"],
        name="Metric: ",
    )
    metric_param = alt.param(name="selected_metric", bind=metric_dropdown, value="tempMax")

    wind_param = alt.param(
        name="min_wind",
        bind=alt.binding_range(min=0, max=30, step=0.5, name="Wind speed greater than: "),
        value=0,
    )
    humidity_param = alt.param(
        name="min_humidity",
        bind=alt.binding_range(min=0, max=1, step=0.01, name="Humidity greater than: "),
        value=0,
    )

    group_dropdown = alt.binding_select(
        options=["monthName", "season", "desc", "year"],
        labels=["By Month", "By Season", "By Weather Type", "By Year"],
        name="Group by: ",
    )
    group_param = alt.param(name="group_by", bind=group_dropdown, value="monthName")

    # For the generalised selection drill-down
    gen_dropdown = alt.binding_select(
        options=["year", "season", "month"],
        labels=["Yearly Overview", "By Season", "By Month"],
        name="Generalisation Level: ",
    )
    gen_param = alt.param(name="gen_level", bind=gen_dropdown, value="year")

    return metric_param, wind_param, humidity_param, group_param, gen_param


# --- Individual chart builders ---

def _build_bar_chart(df, metric_param, wind_param, humidity_param,
                     group_param, month_click, season_click):
    """Horizontal bar chart with dynamic grouping and metric switching."""
    chart = (
        alt.Chart(df)
        .transform_filter("datum.windSpeed >= min_wind")
        .transform_filter("datum.humidity >= min_humidity")
        .transform_filter(season_click)
        .transform_calculate(
            group_key="group_by == 'monthName' ? datum.monthName : "
                      "(group_by == 'season' ? datum.season : "
                      "(group_by == 'desc' ? datum.desc : "
                      "toString(datum.year)))"
        )
        .transform_joinaggregate(_group_count="count()", groupby=["group_key"])
        .transform_calculate(
            selected_value="selected_metric == '_count'"
                           " ? datum._group_count"
                           " : toNumber(datum[selected_metric])"
        )
        .mark_bar()
        .encode(
            x=alt.X("mean(selected_value):Q", title="Metric Value"),
            y=alt.Y("group_key:N", title="Group",
                     sort=alt.EncodingSortField(field="selected_value", op="mean", order="descending")),
            color=alt.condition(month_click, alt.value("#2171b5"), alt.value("#9ecae1")),
            tooltip=[
                alt.Tooltip("group_key:N", title="Group"),
                alt.Tooltip("mean(selected_value):Q", title="Metric Value", format=".2f"),
                alt.Tooltip("count():Q", title="Days"),
            ],
        )
        .add_params(month_click, metric_param, wind_param, humidity_param, group_param)
        .properties(title="Top [Group] by [Metric]", width=350, height=250)
    )
    return chart


def _build_heatmap(df, metric_param, wind_param, humidity_param,
                   month_click, cell_click, season_click):
    """Calendar heatmap showing average metric value by month x year."""
    chart = (
        alt.Chart(df)
        .transform_filter("datum.windSpeed >= min_wind")
        .transform_filter("datum.humidity >= min_humidity")
        .transform_filter(season_click)
        .transform_calculate(selected_value="datum[selected_metric]")
        .mark_rect(stroke="#ffffff", strokeWidth=2)
        .encode(
            x=alt.X("monthName:O", title="Month", sort=MONTH_ORDER),
            y=alt.Y("year:O", title="Year"),
            color=alt.Color("mean(selected_value):Q",
                            scale=alt.Scale(scheme="viridis"),
                            title="Mean Metric Value"),
            opacity=alt.condition(month_click, alt.value(1.0), alt.value(0.4)),
            tooltip=[
                alt.Tooltip("year:O", title="Year"),
                alt.Tooltip("monthName:O", title="Month"),
                alt.Tooltip("mean(selected_value):Q", title="Mean Metric Value", format=".2f"),
                alt.Tooltip("mean(tempMax):Q", title="Mean Max Temp (C)", format=".1f"),
                alt.Tooltip("mean(windSpeed):Q", title="Mean Wind Speed (km/h)", format=".1f"),
                alt.Tooltip("count():Q", title="Days"),
            ],
        )
        .add_params(cell_click)
        .properties(title="Average Weather Metric by Month x Year", width=350, height=250)
    )
    return chart


def _build_grouped_bar(df, wind_param, humidity_param,
                       month_click, cell_click, season_click):
    """Side-by-side bars comparing wind speed and humidity per season."""
    chart = (
        alt.Chart(df)
        .transform_filter("datum.windSpeed >= min_wind")
        .transform_filter("datum.humidity >= min_humidity")
        .transform_filter(cell_click)
        .transform_fold(fold=["windSpeed", "humidity"], as_=["metric", "value"])
        .mark_bar()
        .encode(
            x=alt.X("season:N", title="Season", sort=SEASON_ORDER),
            y=alt.Y("mean(value):Q", title="Mean Value"),
            color=alt.Color("metric:N",
                            scale=alt.Scale(domain=["windSpeed", "humidity"],
                                            range=["#54a24b", "#f58518"]),
                            title="Metric", legend=alt.Legend(title="Metric")),
            xOffset="metric:N",
            opacity=alt.condition(month_click, alt.value(1.0), alt.value(0.4)),
            tooltip=[
                alt.Tooltip("season:N", title="Season"),
                alt.Tooltip("metric:N", title="Metric"),
                alt.Tooltip("mean(value):Q", title="Mean Value", format=".3f"),
                alt.Tooltip("count():Q", title="Days"),
            ],
        )
        .add_params(season_click)
        .properties(title="Season: Wind Speed vs Humidity", width=350, height=250)
    )
    return chart


def _build_generalised_chart(df, wind_param, humidity_param,
                             gen_param, cell_click, year_click):
    """Generalised selection: click a year, then drill down by season or month.

    Two layers — a line overview that fades when you pick a year,
    and a bar chart that shows the breakdown for that year.
    """
    # Distinct colours so weather types are easy to tell apart on lines
    line_colors = alt.Scale(
        domain=["rain", "clear-day", "partly-cloudy-day", "cloudy", "fog", "unknown"],
        range=["#1f77b4", "#ff7f0e", "#d62728", "#9467bd", "#2ca02c", "#e377c2"],
    )

    # Overview: lines for each weather type across years
    overview = (
        alt.Chart(df)
        .transform_filter("datum.windSpeed >= min_wind")
        .transform_filter("datum.humidity >= min_humidity")
        .transform_filter(cell_click)
        .mark_line(point=alt.OverlayMarkDef(size=100), strokeWidth=2.5)
        .encode(
            x=alt.X("year:O", title="Year"),
            y=alt.Y("count():Q", title="Number of Days"),
            color=alt.Color("desc:N", scale=line_colors, title="Weather Type"),
            opacity=alt.condition(year_click, alt.value(0.15), alt.value(1.0)),
            tooltip=[
                alt.Tooltip("year:O", title="Year"),
                alt.Tooltip("desc:N", title="Weather Type"),
                alt.Tooltip("count():Q", title="Days"),
            ],
        )
        .add_params(year_click, gen_param)
    )

    # Detail: bars appear once a year is selected, grouped by the chosen level
    detail = (
        alt.Chart(df)
        .transform_filter("datum.windSpeed >= min_wind")
        .transform_filter("datum.humidity >= min_humidity")
        .transform_filter(cell_click)
        .transform_filter(year_click)
        .transform_calculate(
            group_key="gen_level == 'month' ? datum.monthName : "
                      "(gen_level == 'season' ? datum.season : "
                      "toString(datum.year))"
        )
        .mark_bar()
        .encode(
            x=alt.X("group_key:N", title="Time Group"),
            y=alt.Y("count():Q", title="Number of Days"),
            color=alt.Color("desc:N", scale=line_colors, legend=None),
            tooltip=[
                alt.Tooltip("group_key:N", title="Time Group"),
                alt.Tooltip("desc:N", title="Weather Type"),
                alt.Tooltip("count():Q", title="Days"),
            ],
        )
    )

    return alt.layer(overview, detail).resolve_scale(color="shared").properties(
        title="Generalised Selection: Click a year, then change level",
        width=350, height=250,
    )


# --- Putting it all together ---

def build_system_b(df):
    """Assemble the 2x2 dashboard with all cross-chart interactions."""
    metric_param, wind_param, humidity_param, group_param, gen_param = _make_params()

    # Cross-chart click selections
    month_click = alt.selection_point(
        name="month_sel", fields=["group_key"], on="click", clear="dblclick",
    )
    cell_click = alt.selection_point(
        name="cell_sel", fields=["monthName", "year"], on="click", clear="dblclick",
    )
    season_click = alt.selection_point(
        name="season_sel", fields=["season"], on="click", clear="dblclick",
    )
    year_click = alt.selection_point(
        name="year_sel", fields=["year"], on="click", clear="dblclick",
    )

    chart1 = _build_bar_chart(df, metric_param, wind_param, humidity_param,
                              group_param, month_click, season_click)
    chart2 = _build_heatmap(df, metric_param, wind_param, humidity_param,
                            month_click, cell_click, season_click)
    chart3 = _build_grouped_bar(df, wind_param, humidity_param,
                                month_click, cell_click, season_click)
    chart4 = _build_generalised_chart(df, wind_param, humidity_param,
                                      gen_param, cell_click, year_click)

    row1 = alt.hconcat(chart1, chart2)
    row2 = (alt.hconcat(chart3, chart4)
            .resolve_scale(color="independent")
            .resolve_legend(color="independent"))
    full_dashboard = (
        alt.vconcat(row1, row2)
        .resolve_scale(color="independent")
        .configure_concat(spacing=30)
    )
    return full_dashboard


# --- Page content ---

HOW_TO_USE_HTML = """
<ul>
    <li>Click on a bar in the <strong>Top [Group] by [Metric]</strong> chart to
        highlight that group across charts. Double-click to reset.</li>
    <li>Use the <strong>"Group by"</strong> dropdown to change the bar chart grouping
        (By Month, By Season, By Weather Type, or By Year).</li>
    <li>Click on a cell in the <strong>heatmap</strong> to filter charts below to that
        specific month-year combination. Double-click to reset.</li>
    <li>Click on a season bar in the <strong>Season: Wind Speed vs Humidity</strong>
        chart to filter the bar chart and heatmap to that season
        (bidirectional linking). Double-click to reset.</li>
    <li><strong>Generalised Selection:</strong> Click a year point on the bottom-right
        line chart, then use the <strong>"Generalisation Level"</strong> dropdown to
        drill into that year by season or by month. Double-click the line chart to
        return to the full overview.</li>
    <li>Use the <strong>"Metric"</strong> dropdown to change which variable is shown
        in the bar chart and heatmap. Select <strong>"Count (Frequency)"</strong>
        to rank groups by number of days.</li>
    <li>Use the <strong>sliders</strong> to filter data by minimum wind speed and
        minimum humidity thresholds.</li>
    <li>To reset all filters, refresh the page.</li>
</ul>
"""

TASKS_HTML = """
<ol>
    <li>Identify the season or month with the highest average temperature range.</li>
    <li>Find the top 3 weather types (desc) by frequency across the dataset.</li>
    <li>Determine which year had the highest average wind speed.</li>
    <li>Find the weather type with the highest average visibility, filtered by a
        minimum humidity threshold (e.g., <strong>humidity &gt; 0.85</strong>).</li>
    <li>Identify months where wind speed is above a user-set threshold AND humidity
        is above a user-set threshold. Find the top 3 seasons with the highest
        average cloud cover.</li>
</ol>
"""


def main():
    """Generate System_B.html."""
    data_path = _resolve_path(
        os.path.join(_SCRIPT_DIR, "data", "clean_weather_data.csv"),
        os.path.join(_SCRIPT_DIR, "..", "data", "clean_weather_data.csv"),
    )
    output_dir = (
        os.path.join(_SCRIPT_DIR, "..", "output")
        if os.path.isdir(os.path.join(_SCRIPT_DIR, "..", "output"))
        else _SCRIPT_DIR
    )
    output_path = os.path.join(output_dir, "System_B.html")

    df = load_and_prepare(data_path)
    chart = build_system_b(df)

    save_system_page(
        chart=chart,
        system_name="SYSTEM B",
        how_to_use_html=HOW_TO_USE_HTML,
        tasks_html=TASKS_HTML,
        output_path=output_path,
        nav_links=[
            {"label": "System A", "href": "System_A.html"},
            {"label": "System C", "href": "System_C.html"},
        ],
    )
    print(f"System B saved to {output_path}")


if __name__ == "__main__":
    main()
