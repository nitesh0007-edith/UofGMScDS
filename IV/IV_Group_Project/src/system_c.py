"""System C — Full Exploration with Legend Filtering.

The most flexible system: large scatter plot as the centrepiece, clickable
colour and shape legends, bar chart for ranking, heatmap for composition.
Multi-hue palette throughout.
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

# Each weather type gets a distinct vivid colour
WEATHER_COLORS = alt.Scale(
    domain=['rain', 'clear-day', 'partly-cloudy-day', 'cloudy', 'fog', 'unknown'],
    range=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'],
)

# Different shape per season so you can tell them apart in the scatter
SEASON_SHAPES = alt.Scale(
    domain=['Winter', 'Spring', 'Summer', 'Autumn'],
    range=['circle', 'diamond', 'square', 'triangle-up'],
)

MONTH_ORDER = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

HOW_TO_USE_HTML = """<ul>
<li>Click on items in the <strong>colour legend</strong> (weather type) on the scatter
plot to filter the scatter, heatmap, and season chart. Click again to deselect.</li>
<li>Click on items in the <strong>shape legend</strong> (season) on the scatter plot to
filter by season. Click again to deselect.</li>
<li>Drag to <strong>brush</strong> (select a horizontal region) on the scatter plot to
filter the heatmap and season chart below by date range.</li>
<li><strong>Scroll to zoom</strong> on the scatter plot to zoom in/out for precise
point inspection.</li>
<li>Click on a cell in the <strong>heatmap</strong> to filter the scatter plot to
that month-year combination (<strong>bidirectional linking</strong>).
Double-click to reset.</li>
<li>Use the <strong>"Metric"</strong> dropdown to change the Y-axis variable in the
scatter plot and the ranking metric in the bar chart. Select
<strong>"Count (Frequency)"</strong> to rank by number of days.</li>
<li>Use the <strong>"Group bars by"</strong> dropdown to change the bar chart grouping
(Weather Type, Season, Month, or Year).</li>
<li>Use the <strong>sliders</strong> to filter data by minimum humidity, minimum
wind speed, and maximum cloud cover.</li>
<li>To <strong>reset</strong> all filters, refresh the page.</li>
</ul>"""

TASKS_HTML = """<ol>
<li>Identify the season or month with the highest average temperature range.</li>
<li>Find the top 3 weather types (desc) by frequency across the dataset.</li>
<li>Determine which year had the highest average wind speed.</li>
<li>Find the weather type with the highest average visibility, filtered by a
minimum humidity threshold (e.g., <strong>humidity &gt; 0.85</strong>).</li>
<li>Identify months where wind speed is above a user-set threshold AND humidity is
above a user-set threshold. Find the top 3 seasons with the highest average
cloud cover.</li>
</ol>"""


# --- HTML template (same look as the other systems) ---

def save_system_page(chart, system_name, how_to_use_html, tasks_html,
                     output_path, nav_links=None):
    """Wrap the chart in the standard page template and write to disk."""
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


# --- Parameters ---

def _build_params():
    """Create metric dropdown, group-by dropdown, and the three threshold sliders."""
    metric_param = alt.param(
        name='selected_metric',
        bind=alt.binding_select(
            options=['tempMax', 'windSpeed', 'humidity', 'visibility',
                     'tempRange', 'cloudCover', '_count'],
            labels=['Avg Max Temp', 'Avg Wind Speed', 'Avg Humidity',
                    'Avg Visibility', 'Avg Temp Range', 'Avg Cloud Cover',
                    'Count (Frequency)'],
            name='Metric: ',
        ),
        value='tempMax',
    )
    group_param = alt.param(
        name='group_by',
        bind=alt.binding_select(
            options=['desc', 'season', 'monthName', 'year'],
            labels=['Weather Type', 'Season', 'Month', 'Year'],
            name='Group bars by: ',
        ),
        value='desc',
    )
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
    return metric_param, group_param, humidity_param, wind_param, cloud_param


# --- Chart builders ---

def _build_bar_chart(df, metric_param, group_param, humidity_param,
                     wind_param, cloud_param, legend_desc, legend_season):
    """Horizontal bar chart — ranks groups by whatever metric is selected."""
    bar = (
        alt.Chart(df, title='Top [Group] by [Metric]')
        .transform_filter('datum.humidity >= min_humidity')
        .transform_filter('datum.windSpeed >= min_wind')
        .transform_filter('datum.cloudCover <= max_cloud')
        .transform_calculate(
            group_key="group_by == 'desc' ? datum.desc : "
                      "(group_by == 'season' ? datum.season : "
                      "(group_by == 'monthName' ? datum.monthName : "
                      "toString(datum.year)))"
        )
        .transform_joinaggregate(_group_count='count()', groupby=['group_key'])
        .transform_calculate(
            selected_value="selected_metric == '_count'"
                           " ? datum._group_count"
                           " : toNumber(datum[selected_metric])"
        )
        .mark_bar()
        .encode(
            x=alt.X('mean(selected_value):Q', title='Metric Value'),
            y=alt.Y('group_key:N', title='Group',
                     sort=alt.EncodingSortField(field='selected_value', op='mean', order='descending')),
            color=alt.Color('group_key:N', legend=None),
            tooltip=[
                alt.Tooltip('group_key:N', title='Group'),
                alt.Tooltip('mean(selected_value):Q', title='Metric Value', format='.2f'),
                alt.Tooltip('count():Q', title='Count'),
            ],
        )
        .properties(width=250, height=300)
        .add_params(metric_param, group_param, humidity_param, wind_param, cloud_param)
    )
    return bar


def _build_scatter_chart(df, humidity_param, wind_param, cloud_param,
                         legend_desc, legend_season, heatmap_click):
    """Big scatter plot — the main exploration chart. Uses colour for weather
    type and shape for season. Has brush + scroll-zoom + legend filtering."""
    brush = alt.selection_interval(encodings=['x'])
    zoom = alt.selection_interval(bind='scales', translate=False, zoom='wheel!')

    scatter = (
        alt.Chart(df, title='Day vs [Selected Metric]')
        .transform_filter('datum.humidity >= min_humidity')
        .transform_filter('datum.windSpeed >= min_wind')
        .transform_filter('datum.cloudCover <= max_cloud')
        .transform_filter(heatmap_click)
        .transform_calculate(selected_value='datum[selected_metric]')
        .mark_point(size=60, filled=True)
        .encode(
            x=alt.X('day:T', title='Date'),
            y=alt.Y('selected_value:Q', title='Selected Metric Value'),
            color=alt.Color('desc:N', scale=WEATHER_COLORS, title='Weather Type'),
            shape=alt.Shape('season:N', scale=SEASON_SHAPES, title='Season'),
            opacity=alt.condition(
                legend_desc & legend_season,
                alt.value(0.8), alt.value(0.1),
            ),
            tooltip=[
                alt.Tooltip('day:T', title='Date'),
                alt.Tooltip('desc:N', title='Weather Type'),
                alt.Tooltip('season:N', title='Season'),
                alt.Tooltip('tempMax:Q', title='Max Temp (C)', format='.1f'),
                alt.Tooltip('tempMin:Q', title='Min Temp (C)', format='.1f'),
                alt.Tooltip('windSpeed:Q', title='Wind Speed (km/h)', format='.1f'),
                alt.Tooltip('humidity:Q', title='Humidity', format='.2f'),
                alt.Tooltip('visibility:Q', title='Visibility (km)', format='.1f'),
                alt.Tooltip('cloudCover:Q', title='Cloud Cover', format='.2f'),
            ],
        )
        .properties(width=550, height=300)
        .add_params(brush, zoom, legend_desc, legend_season)
    )
    return scatter, brush


def _build_heatmap(df, brush, humidity_param, wind_param, cloud_param,
                   legend_desc, legend_season, heatmap_click):
    """Month x year heatmap showing how many days fall in each cell.
    Linked to the scatter brush and legend filtering."""
    heatmap = (
        alt.Chart(df, title='Monthly Weather Composition')
        .transform_filter('datum.humidity >= min_humidity')
        .transform_filter('datum.windSpeed >= min_wind')
        .transform_filter('datum.cloudCover <= max_cloud')
        .transform_filter(legend_desc)
        .transform_filter(legend_season)
        .transform_filter(brush)
        .mark_rect()
        .encode(
            x=alt.X('monthName:O', title='Month', sort=MONTH_ORDER),
            y=alt.Y('year:O', title='Year'),
            color=alt.Color('count():Q', title='Number of Days',
                            scale=alt.Scale(scheme='blues')),
            opacity=alt.condition(heatmap_click, alt.value(1.0), alt.value(0.4)),
            tooltip=[
                alt.Tooltip('monthName:O', title='Month'),
                alt.Tooltip('year:O', title='Year'),
                alt.Tooltip('count():Q', title='Number of Days'),
            ],
        )
        .properties(width=700, height=150)
        .add_params(heatmap_click)
    )
    return heatmap


def _build_season_chart(df, brush, humidity_param, wind_param, cloud_param,
                        legend_desc, legend_season):
    """Small bar chart showing average cloud cover per season."""
    season_order = ['Winter', 'Spring', 'Summer', 'Autumn']
    chart = (
        alt.Chart(df, title='Avg Cloud Cover by Season')
        .transform_filter('datum.humidity >= min_humidity')
        .transform_filter('datum.windSpeed >= min_wind')
        .transform_filter('datum.cloudCover <= max_cloud')
        .transform_filter(legend_desc)
        .transform_filter(legend_season)
        .transform_filter(brush)
        .mark_bar()
        .encode(
            x=alt.X('season:N', title='Season', sort=season_order),
            y=alt.Y('mean(cloudCover):Q', title='Avg Cloud Cover'),
            color=alt.Color('season:N', legend=None,
                            scale=alt.Scale(domain=season_order,
                                            range=['#4c78a8', '#54a24b', '#f58518', '#e45756'])),
            tooltip=[
                alt.Tooltip('season:N', title='Season'),
                alt.Tooltip('mean(cloudCover):Q', title='Avg Cloud Cover', format='.3f'),
                alt.Tooltip('count():Q', title='Days'),
            ],
        )
        .properties(width=250, height=150)
    )
    return chart


# --- Dashboard assembly ---

def build_system_c(df):
    """Wire up all four charts with shared params, legends, and selections."""
    metric_param, group_param, humidity_param, wind_param, cloud_param = _build_params()

    # Clickable legends — these filter every chart at once
    legend_desc = alt.selection_point(fields=['desc'], bind='legend')
    legend_season = alt.selection_point(fields=['season'], bind='legend')

    # Click a heatmap cell to filter the scatter (bidirectional)
    heatmap_click = alt.selection_point(
        name='heatmap_sel', fields=['monthName', 'year'],
        on='click', clear='dblclick',
    )

    bar_chart = _build_bar_chart(df, metric_param, group_param, humidity_param,
                                 wind_param, cloud_param, legend_desc, legend_season)
    scatter_chart, brush = _build_scatter_chart(df, humidity_param, wind_param,
                                                cloud_param, legend_desc, legend_season,
                                                heatmap_click)
    heatmap = _build_heatmap(df, brush, humidity_param, wind_param, cloud_param,
                             legend_desc, legend_season, heatmap_click)
    season_chart = _build_season_chart(df, brush, humidity_param, wind_param, cloud_param,
                                       legend_desc, legend_season)

    # Layout: bar + scatter on top, heatmap + season summary on bottom
    row1 = alt.hconcat(bar_chart, scatter_chart).resolve_scale(
        color='independent', shape='independent',
    )
    row2 = alt.hconcat(heatmap, season_chart)
    full_dashboard = (
        alt.vconcat(row1, row2)
        .resolve_scale(color='independent')
        .configure_concat(spacing=30)
    )
    return full_dashboard


def main():
    """Generate System_C.html."""
    data_path = _resolve_path(
        os.path.join(_SCRIPT_DIR, 'data', 'clean_weather_data.csv'),
        os.path.join(_SCRIPT_DIR, '..', 'data', 'clean_weather_data.csv'),
    )
    output_dir = (
        os.path.join(_SCRIPT_DIR, '..', 'output')
        if os.path.isdir(os.path.join(_SCRIPT_DIR, '..', 'output'))
        else _SCRIPT_DIR
    )
    output_path = os.path.join(output_dir, 'System_C.html')

    df = load_and_prepare(data_path)
    df['day'] = df['day'].dt.strftime('%Y-%m-%d')

    dashboard = build_system_c(df)

    save_system_page(
        chart=dashboard,
        system_name='SYSTEM C',
        how_to_use_html=HOW_TO_USE_HTML,
        tasks_html=TASKS_HTML,
        output_path=output_path,
        nav_links=[
            {'label': 'System A', 'href': 'System_A.html'},
            {'label': 'System B', 'href': 'System_B.html'},
        ],
    )


if __name__ == '__main__':
    main()
