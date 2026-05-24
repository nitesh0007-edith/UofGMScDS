"""System A — Category & Attribute Overview dashboard.

Warm colour palette with four charts (2x2 grid):
  - Horizontal bar chart for weather type ranking
  - Dynamic grouped bar chart (month/season/year)
  - Two scatter plots with bidirectional brushing
"""

import json
import os
import sys

import altair as alt
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))
from data_prep import load_and_prepare

# Colour scale used across charts to keep weather types consistent
WEATHER_COLORS = alt.Scale(
    domain=['rain', 'clear-day', 'partly-cloudy-day', 'cloudy', 'fog', 'unknown'],
    range=['#4c78a8', '#f58518', '#e45756', '#72b7b2', '#54a24b', '#bab0ac'],
)

MONTH_ORDER = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

CHART_WIDTH = 350
CHART_HEIGHT = 250

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def _resolve_path(*candidates: str) -> str:
    """Return the first candidate path that exists, or the last one as default."""
    for p in candidates:
        if os.path.exists(p):
            return p
    return candidates[-1]


# --- HTML page wrapper ---

def save_system_page(chart, system_name, how_to_use_html, tasks_html,
                     output_path, nav_links=None):
    """Wrap the Altair chart in a styled HTML page and write it out."""
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
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(html)
    print(f"Generated {output_path}")


# --- Page content ---

HOW_TO_USE_HTML = """<ul>
<li>Click on a bar in the <strong>"Top Weather Types"</strong> chart to filter all
other charts to that weather type. Double-click to reset.</li>
<li>Use the <strong>"Rank by"</strong> dropdown to change the metric displayed in the
bar chart. Select <strong>"Count (Frequency)"</strong> to rank by number of days.</li>
<li>Use the <strong>"Group by"</strong> dropdown to change the secondary bar chart
grouping (By Month, By Season, or By Year).</li>
<li>Drag to brush (select a region) on <strong>either</strong> scatter plot to
highlight corresponding points in the other scatter plot
(<strong>bidirectional linking</strong>).</li>
<li><strong>Scroll to zoom</strong> on either scatter plot to zoom in/out for precise
point inspection.</li>
<li>Use the <strong>sliders</strong> below the charts to filter data by minimum humidity,
minimum wind speed, and maximum cloud cover.</li>
<li>To reset all filters, <strong>refresh the page</strong>.</li>
</ul>"""

TASKS_HTML = """<ol>
<li>Identify the season or month with the highest average temperature range.</li>
<li>Find the top 3 weather types (<em>desc</em>) by frequency across the dataset.</li>
<li>Determine which year had the highest average wind speed.</li>
<li>Find the weather type with the highest average visibility, filtered by a minimum
humidity threshold (e.g., <strong>humidity &gt; 0.85</strong>).</li>
<li>Identify months where wind speed is above a user-set threshold AND humidity is above
a user-set threshold. Find the top 3 seasons with the highest average cloud cover.</li>
</ol>"""


# --- Chart building ---

def build_system_a(df: pd.DataFrame) -> alt.TopLevelMixin:
    """Build the full System A dashboard — four linked charts with controls."""

    # -- Selections --
    click_selection = alt.selection_point(
        name='click_weather', fields=['desc'],
        on='click', clear='dblclick',
    )
    # Bidirectional brushes between the two scatter plots
    brush_wind = alt.selection_interval(name='brush_wind')
    brush_hv = alt.selection_interval(name='brush_hv')
    # Scroll-to-zoom (no drag pan)
    zoom_wind = alt.selection_interval(
        name='zoom_wind', bind='scales', translate=False, zoom='wheel!',
    )
    zoom_hv = alt.selection_interval(
        name='zoom_hv', bind='scales', translate=False, zoom='wheel!',
    )

    # -- Dropdowns and sliders --
    metric_dropdown = alt.binding_select(
        options=['tempMax', 'windSpeed', 'humidity', 'visibility',
                 'tempRange', 'cloudCover', '_count'],
        labels=['Avg Max Temp', 'Avg Wind Speed', 'Avg Humidity',
                'Avg Visibility', 'Avg Temp Range', 'Avg Cloud Cover',
                'Count (Frequency)'],
        name='Rank by: ',
    )
    metric_param = alt.param(name='selected_metric', bind=metric_dropdown, value='tempMax')

    group_dropdown = alt.binding_select(
        options=['monthName', 'season', 'year'],
        labels=['By Month', 'By Season', 'By Year'],
        name='Group by: ',
    )
    group_param = alt.param(name='group_by', bind=group_dropdown, value='monthName')

    humidity_param = alt.param(
        name='min_humidity',
        bind=alt.binding_range(min=0, max=1, step=0.01, name='Minimum humidity: '),
        value=0,
    )
    wind_param = alt.param(
        name='min_wind',
        bind=alt.binding_range(min=0, max=30, step=0.5, name='Wind speed greater than: '),
        value=0,
    )
    cloud_param = alt.param(
        name='max_cloud',
        bind=alt.binding_range(min=0, max=1, step=0.01, name='Cloud cover less than: '),
        value=1,
    )

    # Shared filter expressions for the sliders
    slider_filters = [
        'datum.humidity >= min_humidity',
        'datum.windSpeed >= min_wind',
        'datum.cloudCover <= max_cloud',
    ]

    # -- Chart 1: Horizontal bar — weather type ranking --
    chart1 = (
        alt.Chart(df, title='Top Weather Types')
        .transform_filter(slider_filters[0])
        .transform_filter(slider_filters[1])
        .transform_filter(slider_filters[2])
        .transform_joinaggregate(_desc_count='count()', groupby=['desc'])
        .transform_calculate(
            selected_value="selected_metric == '_count'"
                           " ? datum._desc_count"
                           " : toNumber(datum[selected_metric])"
        )
        .mark_bar()
        .encode(
            x=alt.X('mean(selected_value):Q', title='Average Metric Value'),
            y=alt.Y('desc:N', sort='-x', title='Weather Type'),
            color=alt.condition(
                click_selection,
                alt.Color('desc:N', scale=WEATHER_COLORS, legend=None),
                alt.value('lightgray'),
            ),
            tooltip=[
                alt.Tooltip('desc:N', title='Weather Type'),
                alt.Tooltip('mean(selected_value):Q', title='Avg Value', format='.2f'),
                alt.Tooltip('count():Q', title='Count'),
            ],
        )
        .properties(width=CHART_WIDTH, height=CHART_HEIGHT)
        .add_params(click_selection, metric_param, group_param,
                    humidity_param, wind_param, cloud_param)
    )

    # -- Chart 2: Bar chart with dynamic grouping --
    chart2 = (
        alt.Chart(df, title='Distribution by [Group]')
        .transform_filter(slider_filters[0])
        .transform_filter(slider_filters[1])
        .transform_filter(slider_filters[2])
        .transform_filter(click_selection)
        .transform_calculate(
            group_key="group_by == 'monthName' ? datum.monthName : "
                      "(group_by == 'season' ? datum.season : "
                      "toString(datum.year))"
        )
        .transform_joinaggregate(_group_count='count()', groupby=['group_key'])
        .transform_calculate(
            selected_value="selected_metric == '_count'"
                           " ? datum._group_count"
                           " : toNumber(datum[selected_metric])"
        )
        .mark_bar(color='#e45756')
        .encode(
            x=alt.X('group_key:N', title='Group',
                     sort=alt.EncodingSortField(field='selected_value', op='mean', order='descending')),
            y=alt.Y('mean(selected_value):Q', title='Mean Metric Value'),
            tooltip=[
                alt.Tooltip('group_key:N', title='Group'),
                alt.Tooltip('mean(selected_value):Q', title='Mean Value', format='.2f'),
                alt.Tooltip('count():Q', title='Days'),
            ],
        )
        .properties(width=CHART_WIDTH, height=CHART_HEIGHT)
    )

    # -- Chart 3: Scatter — Day vs Wind Speed (linked with chart 4) --
    chart3 = (
        alt.Chart(df, title='Day vs Wind Speed')
        .transform_filter(slider_filters[0])
        .transform_filter(slider_filters[1])
        .transform_filter(slider_filters[2])
        .transform_filter(click_selection)
        .mark_circle(size=40)
        .encode(
            x=alt.X('day:T', title='Date'),
            y=alt.Y('windSpeed:Q', title='Wind Speed (km/h)'),
            color=alt.Color('desc:N', scale=WEATHER_COLORS, legend=alt.Legend(title='Weather Type')),
            opacity=alt.condition(brush_hv, alt.value(0.8), alt.value(0.1)),
            tooltip=[
                alt.Tooltip('day:T', title='Date'),
                alt.Tooltip('desc:N', title='Weather Type'),
                alt.Tooltip('windSpeed:Q', title='Wind Speed (km/h)', format='.1f'),
                alt.Tooltip('humidity:Q', title='Humidity', format='.2f'),
                alt.Tooltip('cloudCover:Q', title='Cloud Cover', format='.2f'),
            ],
        )
        .properties(width=CHART_WIDTH, height=CHART_HEIGHT)
        .add_params(brush_wind, zoom_wind)
    )

    # -- Chart 4: Scatter — Humidity vs Visibility (linked with chart 3) --
    chart4 = (
        alt.Chart(df, title='Humidity vs Visibility')
        .transform_filter(slider_filters[0])
        .transform_filter(slider_filters[1])
        .transform_filter(slider_filters[2])
        .transform_filter(click_selection)
        .mark_circle(size=40)
        .encode(
            x=alt.X('humidity:Q', title='Humidity (ratio)'),
            y=alt.Y('visibility:Q', title='Visibility (km)'),
            color=alt.Color('desc:N', scale=WEATHER_COLORS, legend=None),
            opacity=alt.condition(brush_wind, alt.value(0.8), alt.value(0.1)),
            tooltip=[
                alt.Tooltip('day:T', title='Date'),
                alt.Tooltip('desc:N', title='Weather Type'),
                alt.Tooltip('humidity:Q', title='Humidity', format='.2f'),
                alt.Tooltip('visibility:Q', title='Visibility (km)', format='.1f'),
                alt.Tooltip('windSpeed:Q', title='Wind Speed (km/h)', format='.1f'),
            ],
        )
        .properties(width=CHART_WIDTH, height=CHART_HEIGHT)
        .add_params(brush_hv, zoom_hv)
    )

    # -- Compose the 2x2 grid --
    row1 = alt.hconcat(chart1, chart2).resolve_scale(color='independent')
    row2 = alt.hconcat(chart3, chart4).resolve_scale(color='independent')
    full_dashboard = (
        alt.vconcat(row1, row2)
        .resolve_scale(color='independent')
        .configure_concat(spacing=30)
    )

    return full_dashboard


# Keep this alias around in case anything imports it
build_dashboard = build_system_a


def main():
    """Generate System_A.html."""
    # Resolve data path: works both in project layout (src/../data) and zip layout (./data)
    data_path = _resolve_path(
        os.path.join(_SCRIPT_DIR, 'data', 'clean_weather_data.csv'),
        os.path.join(_SCRIPT_DIR, '..', 'data', 'clean_weather_data.csv'),
    )
    # Resolve output path: prefer ../output (project), fallback to . (zip)
    output_dir = (
        os.path.join(_SCRIPT_DIR, '..', 'output')
        if os.path.isdir(os.path.join(_SCRIPT_DIR, '..', 'output'))
        else _SCRIPT_DIR
    )
    output_path = os.path.join(output_dir, 'System_A.html')

    df = load_and_prepare(data_path)
    df['day'] = df['day'].dt.strftime('%Y-%m-%d')

    dashboard = build_system_a(df)

    save_system_page(
        chart=dashboard,
        system_name='SYSTEM A',
        how_to_use_html=HOW_TO_USE_HTML,
        tasks_html=TASKS_HTML,
        output_path=output_path,
        nav_links=[
            {'label': 'System B', 'href': 'System_B.html'},
            {'label': 'System C', 'href': 'System_C.html'},
        ],
    )


if __name__ == '__main__':
    main()
