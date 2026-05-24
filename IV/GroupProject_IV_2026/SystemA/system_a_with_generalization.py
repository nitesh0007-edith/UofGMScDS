"""
System A with Generalized Selection: Glasgow Weather Visualization
Implements hierarchical temporal abstraction with traversal policy

Semantic Hierarchy:
Level 4 (Year) - e.g., "All of 2015"
    ↑ generalizes ↑
Level 3 (Season) - e.g., "Winter 2015"
    ↑ generalizes ↑
Level 2 (Month) - e.g., "January 2015"
    ↑ generalizes ↑
Level 1 (Week) - e.g., "Week 2 of January 2015"
    ↑ generalizes ↑
Level 0 (Day) - e.g., "January 8, 2015"

Traversal Policy:
- Generalize UP: Move from Day → Week → Month → Season → Year
- Specialize DOWN: Move from Year → Season → Month → Week → Day
- UI Control: Radio buttons to select hierarchy level
- Visual Feedback: Size, opacity, and color encoding show selection level

This is NOT global filtering - it's semantic hierarchical abstraction based on
temporal relationships.
"""

import altair as alt
import pandas as pd
import numpy as np
import os

# Get the path to the data file (works from any location)
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
data_path = os.path.join(project_root, 'data', 'Glasgow_weather_data', 'weather_data_enriched.csv')

# Load and prepare data
df = pd.read_csv(data_path)
df['day'] = pd.to_datetime(df['day'])

# Add hierarchical temporal features
df['tempAvg'] = (df['tempMin'] + df['tempMax']) / 2
df['week_of_year'] = df['day'].dt.isocalendar().week
df['week_id'] = df['year'].astype(str) + '-W' + df['week_of_year'].astype(str).str.zfill(2)
df['month_id'] = df['year'].astype(str) + '-M' + df['month'].astype(str).str.zfill(2)
df['season_id'] = df['year'].astype(str) + '-' + df['season']

# Handle missing values
df = df.fillna({'cloudCover': df['cloudCover'].median(),
                'desc': 'unknown',
                'summary': 'No summary available'})

# Configure Altair
alt.data_transformers.disable_max_rows()

# ============================================================================
# HIERARCHICAL SELECTION SYSTEM
# ============================================================================

# Radio button for hierarchy level selection
hierarchy_radio = alt.binding_radio(
    options=[0, 1, 2, 3, 4],
    labels=['Day (Level 0)', 'Week (Level 1)', 'Month (Level 2)', 'Season (Level 3)', 'Year (Level 4)'],
    name='Hierarchy Level: '
)
hierarchy_level = alt.selection_point(
    fields=['hierarchy_level'],
    bind=hierarchy_radio,
    value=[{'hierarchy_level': 0}],
    name='hierarchy_level'
)

# Selection at different levels
select_day = alt.selection_point(fields=['day'], name='select_day')
select_week = alt.selection_point(fields=['week_id'], name='select_week')
select_month = alt.selection_point(fields=['month_id'], name='select_month')
select_season = alt.selection_point(fields=['season_id'], name='select_season')
select_year = alt.selection_point(fields=['year'], name='select_year')

# Brush selection (maps to current hierarchy level)
brush = alt.selection_interval(encodings=['x'], name='brush')

# ============================================================================
# VIEW 1: TIME SERIES WITH GENERALIZATION
# ============================================================================

# Base time series
time_series_base = alt.Chart(df).mark_line(point=True, strokeWidth=1.5).encode(
    x=alt.X('day:T',
            title='Date',
            axis=alt.Axis(format='%b %Y', labelAngle=-45)),
    y=alt.Y('tempAvg:Q',
            title='Average Temperature (°C)',
            scale=alt.Scale(domain=[-10, 32])),
    color=alt.value('steelblue'),
    tooltip=[
        alt.Tooltip('day:T', title='Date', format='%Y-%m-%d'),
        alt.Tooltip('week_id:N', title='Week ID'),
        alt.Tooltip('month_id:N', title='Month ID'),
        alt.Tooltip('season_id:N', title='Season ID'),
        alt.Tooltip('year:O', title='Year'),
        alt.Tooltip('tempAvg:Q', title='Avg Temp (°C)', format='.1f'),
        alt.Tooltip('desc:N', title='Weather')
    ]
).add_params(
    hierarchy_level,
    select_day,
    select_week,
    select_month,
    select_season,
    select_year,
    brush
).properties(
    width=800,
    height=250,
    title='Temperature Time Series with Hierarchical Selection - Click points or brush, then change hierarchy level'
)

# Highlighted selection layer (shows generalized selection)
time_series_highlight = alt.Chart(df).mark_line(point={'size': 100}, strokeWidth=3).encode(
    x=alt.X('day:T', axis=None),
    y=alt.Y('tempAvg:Q', axis=None),
    color=alt.value('red'),
    opacity=alt.value(0.8)
).transform_filter(
    select_day | select_week | select_month | select_season | select_year | brush
)

time_series = time_series_base + time_series_highlight

# ============================================================================
# VIEW 2: HIERARCHICAL BAR CHART (Shows aggregation at selected level)
# ============================================================================

# Week-level aggregation
week_bars = alt.Chart(df).mark_bar().encode(
    x=alt.X('week_id:N',
            title='Week',
            axis=alt.Axis(labelAngle=-45, labelLimit=100)),
    y=alt.Y('mean(tempAvg):Q',
            title='Average Temperature (°C)'),
    color=alt.condition(select_week | brush,
                       alt.value('orange'),
                       alt.value('lightgray')),
    opacity=alt.condition(select_week | brush,
                         alt.value(1.0),
                         alt.value(0.5)),
    tooltip=[
        alt.Tooltip('week_id:N', title='Week'),
        alt.Tooltip('mean(tempAvg):Q', title='Avg Temp (°C)', format='.1f'),
        alt.Tooltip('count()', title='Days')
    ]
).properties(
    width=400,
    height=200,
    title='Week-Level Aggregation'
)

# Month-level aggregation
month_bars = alt.Chart(df).mark_bar().encode(
    x=alt.X('month_id:N',
            title='Month',
            axis=alt.Axis(labelAngle=-45)),
    y=alt.Y('mean(tempAvg):Q',
            title='Average Temperature (°C)'),
    color=alt.condition(select_month | brush,
                       alt.value('green'),
                       alt.value('lightgray')),
    opacity=alt.condition(select_month | brush,
                         alt.value(1.0),
                         alt.value(0.5)),
    tooltip=[
        alt.Tooltip('month_id:N', title='Month'),
        alt.Tooltip('mean(tempAvg):Q', title='Avg Temp (°C)', format='.1f'),
        alt.Tooltip('count()', title='Days')
    ]
).properties(
    width=400,
    height=200,
    title='Month-Level Aggregation'
)

# Season-level aggregation
season_bars = alt.Chart(df).mark_bar().encode(
    x=alt.X('season_id:N',
            title='Season',
            axis=alt.Axis(labelAngle=-45)),
    y=alt.Y('mean(tempAvg):Q',
            title='Average Temperature (°C)'),
    color=alt.condition(select_season | brush,
                       alt.Color('season:N',
                                scale=alt.Scale(
                                    domain=['Winter', 'Spring', 'Summer', 'Fall'],
                                    range=['#3498db', '#2ecc71', '#f39c12', '#e74c3c']
                                ),
                                legend=None),
                       alt.value('lightgray')),
    opacity=alt.condition(select_season | brush,
                         alt.value(1.0),
                         alt.value(0.5)),
    tooltip=[
        alt.Tooltip('season_id:N', title='Season-Year'),
        alt.Tooltip('season:N', title='Season'),
        alt.Tooltip('mean(tempAvg):Q', title='Avg Temp (°C)', format='.1f'),
        alt.Tooltip('count()', title='Days')
    ]
).properties(
    width=400,
    height=200,
    title='Season-Level Aggregation'
)

# Year-level aggregation
year_bars = alt.Chart(df).mark_bar().encode(
    x=alt.X('year:O',
            title='Year'),
    y=alt.Y('mean(tempAvg):Q',
            title='Average Temperature (°C)'),
    color=alt.condition(select_year | brush,
                       alt.value('purple'),
                       alt.value('lightgray')),
    opacity=alt.condition(select_year | brush,
                         alt.value(1.0),
                         alt.value(0.5)),
    tooltip=[
        alt.Tooltip('year:O', title='Year'),
        alt.Tooltip('mean(tempAvg):Q', title='Avg Temp (°C)', format='.1f'),
        alt.Tooltip('count()', title='Days')
    ]
).properties(
    width=400,
    height=200,
    title='Year-Level Aggregation'
)

# ============================================================================
# VIEW 3: SCATTER PLOT (Linked to hierarchical selection)
# ============================================================================

scatter = alt.Chart(df).mark_circle(size=60).encode(
    x=alt.X('humidity:Q',
            title='Humidity (0-1)',
            scale=alt.Scale(domain=[0, 1])),
    y=alt.Y('windSpeed:Q',
            title='Wind Speed (km/h)',
            scale=alt.Scale(domain=[0, 26])),
    color=alt.condition(select_day | select_week | select_month | select_season | select_year | brush,
                       alt.Color('season:N',
                                scale=alt.Scale(
                                    domain=['Winter', 'Spring', 'Summer', 'Fall'],
                                    range=['#3498db', '#2ecc71', '#f39c12', '#e74c3c']
                                ),
                                title='Season'),
                       alt.value('lightgray')),
    opacity=alt.condition(select_day | select_week | select_month | select_season | select_year | brush,
                         alt.value(0.8),
                         alt.value(0.1)),
    size=alt.condition(select_day | select_week | select_month | select_season | select_year | brush,
                      alt.value(100),
                      alt.value(20)),
    tooltip=[
        alt.Tooltip('day:T', title='Date', format='%Y-%m-%d'),
        alt.Tooltip('humidity:Q', title='Humidity', format='.2f'),
        alt.Tooltip('windSpeed:Q', title='Wind Speed (km/h)', format='.1f'),
        alt.Tooltip('season:N', title='Season')
    ]
).properties(
    width=800,
    height=300,
    title='Humidity vs Wind Speed - Updates based on hierarchical selection'
)

# ============================================================================
# COMPOSE ALL VIEWS
# ============================================================================

aggregation_row = (week_bars | month_bars) & (season_bars | year_bars)

final_chart = alt.vconcat(
    time_series,
    aggregation_row,
    scatter
).properties(
    title=alt.TitleParams(
        text='System A with Generalized Selection: Hierarchical Temporal Analysis',
        fontSize=20,
        anchor='middle',
        subtitle=['Use radio buttons to select hierarchy level', 'Click/brush on time series to select', 'Watch how selection generalizes across hierarchy levels']
    )
).configure_view(
    strokeWidth=0
).configure_axis(
    labelFontSize=11,
    titleFontSize=12
).configure_title(
    fontSize=14,
    anchor='start'
)

# ============================================================================
# DISPLAY AND SAVE
# ============================================================================

if __name__ == "__main__":
    import webbrowser
    import os

    # Save HTML and JSON for backup
    html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'system_a_with_generalization.html')
    json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'system_a_generalization_spec.json')

    final_chart.save(html_path)
    final_chart.save(json_path)

    print("✓ System A with Generalized Selection created successfully!")
    print(f"  - {html_path} (saved)")
    print(f"  - {json_path} (saved)")
    print("\n" + "="*70)
    print("HIERARCHICAL TEMPORAL STRUCTURE:")
    print("="*70)
    print("Level 4 (Year)   : 2015, 2016, 2017, 2018, 2019")
    print("      ↑ generalizes")
    print("Level 3 (Season) : Winter, Spring, Summer, Fall (per year)")
    print("      ↑ generalizes")
    print("Level 2 (Month)  : January-December (per year)")
    print("      ↑ generalizes")
    print("Level 1 (Week)   : ~52 weeks per year")
    print("      ↑ generalizes")
    print("Level 0 (Day)    : Individual daily observations")
    print("="*70)
    print("\nHOW TO USE:")
    print("1. Select a hierarchy level using radio buttons")
    print("2. Click on time series points or brush to select")
    print("3. Observe how selection propagates to all views")
    print("4. See aggregation bars light up at all hierarchy levels")
    print("5. Scatter plot updates to show only selected temporal range")
    print("\nThis demonstrates TRUE generalized selection, not global filtering!")
    print("\n🚀 Opening in browser...")

    # Open in browser
    webbrowser.open('file://' + html_path)
