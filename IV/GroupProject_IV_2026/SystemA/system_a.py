"""
System A: Glasgow Weather Visualization
Multi-view composition with bidirectional brushing and linking

Views:
1. Time Series Line Chart (Temperature over time) - T4: Temporal trends
2. Scatter Plot (Humidity vs Visibility) - T3: Correlation exploration
3. Bar Chart (Seasonal Temperature Comparison) - T1: Seasonal comparison
4. Histogram (Wind Speed Distribution) - T2: Extreme event identification

Interaction:
- Interval brush selection on time series
- Interval brush selection on scatter plot
- Point click selection on bar chart
- Bidirectional linking across all views
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

# Calculate average temperature
df['tempAvg'] = (df['tempMin'] + df['tempMax']) / 2

# Handle missing values for visualization
df = df.fillna({'cloudCover': df['cloudCover'].median(),
                'desc': 'unknown',
                'summary': 'No summary available'})

# Configure Altair
alt.data_transformers.disable_max_rows()

# ============================================================================
# SELECTION PARAMETERS
# ============================================================================

# Interval selection for brushing on time series
brush_time = alt.selection_interval(encodings=['x'], name='brush_time')

# Interval selection for brushing on scatter plot
brush_scatter = alt.selection_interval(name='brush_scatter')

# Point selection for clicking on bar chart
click_season = alt.selection_point(fields=['season'], name='click_season')

# Combine selections
combined_selection = brush_time | brush_scatter | click_season

# ============================================================================
# VIEW 1: TIME SERIES LINE CHART (T4: Temporal Trends)
# ============================================================================

time_series = alt.Chart(df).mark_line(point=True, strokeWidth=2).encode(
    x=alt.X('day:T',
            title='Date',
            axis=alt.Axis(format='%b %Y', labelAngle=-45)),
    y=alt.Y('tempAvg:Q',
            title='Average Temperature (°C)',
            scale=alt.Scale(domain=[-10, 32])),
    color=alt.condition(combined_selection,
                       alt.value('steelblue'),
                       alt.value('lightgray')),
    opacity=alt.condition(combined_selection,
                         alt.value(1.0),
                         alt.value(0.3)),
    tooltip=[
        alt.Tooltip('day:T', title='Date', format='%Y-%m-%d'),
        alt.Tooltip('tempMin:Q', title='Min Temp (°C)', format='.1f'),
        alt.Tooltip('tempMax:Q', title='Max Temp (°C)', format='.1f'),
        alt.Tooltip('tempAvg:Q', title='Avg Temp (°C)', format='.1f'),
        alt.Tooltip('desc:N', title='Weather Type')
    ]
).add_params(
    brush_time
).properties(
    width=800,
    height=200,
    title='Temperature Trends Over Time (2015-2019) - Brush to Filter'
)

# ============================================================================
# VIEW 2: SCATTER PLOT (T3: Correlation Exploration)
# ============================================================================

scatter = alt.Chart(df).mark_circle(size=60).encode(
    x=alt.X('humidity:Q',
            title='Humidity (0-1)',
            scale=alt.Scale(domain=[0, 1])),
    y=alt.Y('visibility:Q',
            title='Visibility (km)',
            scale=alt.Scale(domain=[0, 11])),
    color=alt.condition(combined_selection,
                       alt.Color('season:N',
                                scale=alt.Scale(
                                    domain=['Winter', 'Spring', 'Summer', 'Fall'],
                                    range=['#3498db', '#2ecc71', '#f39c12', '#e74c3c']
                                ),
                                title='Season'),
                       alt.value('lightgray')),
    opacity=alt.condition(combined_selection,
                         alt.value(0.8),
                         alt.value(0.1)),
    tooltip=[
        alt.Tooltip('day:T', title='Date', format='%Y-%m-%d'),
        alt.Tooltip('humidity:Q', title='Humidity', format='.2f'),
        alt.Tooltip('visibility:Q', title='Visibility (km)', format='.1f'),
        alt.Tooltip('tempAvg:Q', title='Avg Temp (°C)', format='.1f'),
        alt.Tooltip('season:N', title='Season')
    ]
).add_params(
    brush_scatter
).properties(
    width=400,
    height=300,
    title='Humidity vs Visibility - Brush to Select'
)

# Add regression line for selected data
regression = scatter.transform_filter(
    combined_selection
).transform_regression(
    'humidity', 'visibility'
).mark_line(color='red', strokeWidth=3)

scatter_with_regression = scatter + regression

# ============================================================================
# VIEW 3: BAR CHART (T1: Seasonal Comparison)
# ============================================================================

# Aggregate by season
seasonal_data = df.groupby('season').agg({
    'tempMin': 'mean',
    'tempMax': 'mean',
    'tempAvg': 'mean'
}).reset_index()

# Order seasons
season_order = ['Winter', 'Spring', 'Summer', 'Fall']
seasonal_data['season'] = pd.Categorical(seasonal_data['season'],
                                         categories=season_order,
                                         ordered=True)
seasonal_data = seasonal_data.sort_values('season')

bar_chart = alt.Chart(seasonal_data).mark_bar().encode(
    x=alt.X('season:N',
            title='Season',
            sort=season_order),
    y=alt.Y('tempAvg:Q',
            title='Average Temperature (°C)'),
    color=alt.condition(click_season,
                       alt.Color('season:N',
                                scale=alt.Scale(
                                    domain=['Winter', 'Spring', 'Summer', 'Fall'],
                                    range=['#3498db', '#2ecc71', '#f39c12', '#e74c3c']
                                ),
                                legend=None),
                       alt.value('lightgray')),
    opacity=alt.condition(click_season,
                         alt.value(1.0),
                         alt.value(0.5)),
    tooltip=[
        alt.Tooltip('season:N', title='Season'),
        alt.Tooltip('tempMin:Q', title='Avg Min Temp (°C)', format='.1f'),
        alt.Tooltip('tempMax:Q', title='Avg Max Temp (°C)', format='.1f'),
        alt.Tooltip('tempAvg:Q', title='Overall Avg Temp (°C)', format='.1f')
    ]
).add_params(
    click_season
).properties(
    width=400,
    height=300,
    title='Seasonal Temperature Comparison - Click to Select'
)

# ============================================================================
# VIEW 4: HISTOGRAM (T2: Extreme Event Identification)
# ============================================================================

histogram = alt.Chart(df).mark_bar(opacity=0.7).encode(
    x=alt.X('windSpeed:Q',
            bin=alt.Bin(maxbins=30),
            title='Wind Speed (km/h)'),
    y=alt.Y('count()', title='Number of Days'),
    color=alt.condition(combined_selection,
                       alt.value('darkgreen'),
                       alt.value('lightgray')),
    tooltip=[
        alt.Tooltip('windSpeed:Q', bin=alt.Bin(maxbins=30), title='Wind Speed Range'),
        alt.Tooltip('count()', title='Number of Days')
    ]
).properties(
    width=400,
    height=300,
    title='Wind Speed Distribution - Showing Extreme Events'
)

# ============================================================================
# COMPOSE ALL VIEWS
# ============================================================================

# Top row: Time series (full width)
# Bottom row: Scatter (with regression) | Bar chart
# Third row: Histogram (centered)

top_row = time_series
middle_row = scatter_with_regression | bar_chart
bottom_row = histogram

final_chart = alt.vconcat(
    top_row,
    middle_row,
    bottom_row
).properties(
    title=alt.TitleParams(
        text='System A: Glasgow Weather Analysis (2015-2019)',
        fontSize=20,
        anchor='middle'
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
    html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'system_a_visualization.html')
    json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'system_a_spec.json')

    final_chart.save(html_path)
    final_chart.save(json_path)

    print("✓ System A visualization created successfully!")
    print(f"  - {html_path} (saved)")
    print(f"  - {json_path} (saved)")
    print("\nFeatures:")
    print("  • Brush on time series to filter by date range")
    print("  • Brush on scatter plot to select humidity-visibility patterns")
    print("  • Click on bar chart to filter by season")
    print("  • All views linked bidirectionally")
    print("  • Red regression line shows correlation for selected data")
    print("\n🚀 Opening in browser...")

    # Open in browser
    webbrowser.open('file://' + html_path)
