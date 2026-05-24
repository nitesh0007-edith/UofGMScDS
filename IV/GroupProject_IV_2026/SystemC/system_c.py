"""
System C: Glasgow Weather Visualization
Small multiples and explicit filtering controls

Views:
1. Faceted Time Series (Temperature by Year) - T4: Temporal trends across years
2. Strip Plot (Daily Temperatures) - T2: Outlier identification
3. Bubble Chart (Multi-dimensional encoding) - T3: Correlation exploration
4. Histogram with Controls (Distribution) - T1, T5: Filtering and comparison

Interaction:
- Dropdown menu for year filtering
- Slider for temperature threshold filtering
- Brush selection across faceted views
- Hover highlighting for detailed exploration
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
df['tempRange'] = df['tempMax'] - df['tempMin']

# Handle missing values
df = df.fillna({'cloudCover': df['cloudCover'].median(),
                'desc': 'unknown',
                'summary': 'No summary available'})

# Configure Altair
alt.data_transformers.disable_max_rows()

# ============================================================================
# SELECTION PARAMETERS AND FILTERS
# ============================================================================

# Dropdown for year selection
year_dropdown = alt.binding_select(
    options=[None, 2015, 2016, 2017, 2018, 2019],
    labels=['All Years', '2015', '2016', '2017', '2018', '2019'],
    name='Select Year: '
)
year_select = alt.selection_point(fields=['year'], bind=year_dropdown, name='year_select', value=[{'year': 2015}])

# Slider for temperature threshold
temp_slider = alt.binding_range(min=-10, max=30, step=1, name='Min Temperature (°C): ')
temp_threshold = alt.selection_point(fields=['temp_threshold'], bind=temp_slider, name='temp_threshold', value=[{'temp_threshold': 0}])

# Brush selection
brush = alt.selection_interval(name='brush')

# Combined selection
combined_selection = brush | year_select

# ============================================================================
# VIEW 1: FACETED TIME SERIES (T4: Temporal Trends by Year)
# ============================================================================

season_order = ['Winter', 'Spring', 'Summer', 'Fall']

faceted_time_series = alt.Chart(df).mark_line(point=True, strokeWidth=1.5).encode(
    x=alt.X('month(day):O',
            title='Month',
            axis=alt.Axis(labelAngle=0)),
    y=alt.Y('mean(tempAvg):Q',
            title='Avg Temperature (°C)',
            scale=alt.Scale(domain=[-5, 25])),
    color=alt.Color('season:N',
                   scale=alt.Scale(
                       domain=['Winter', 'Spring', 'Summer', 'Fall'],
                       range=['#3498db', '#2ecc71', '#f39c12', '#e74c3c']
                   ),
                   title='Season'),
    opacity=alt.condition(brush,
                         alt.value(1.0),
                         alt.value(0.3)),
    tooltip=[
        alt.Tooltip('year:O', title='Year'),
        alt.Tooltip('month(day):O', title='Month'),
        alt.Tooltip('mean(tempAvg):Q', title='Avg Temp (°C)', format='.1f')
    ]
).properties(
    width=150,
    height=120
).facet(
    column=alt.Column('year:O',
                     title='Year',
                     header=alt.Header(titleFontSize=12, labelFontSize=11))
).add_params(
    brush
).properties(
    title='Monthly Temperature Patterns by Year - Brush to Select'
)

# ============================================================================
# VIEW 2: STRIP PLOT (T2: Outlier Identification)
# ============================================================================

strip_plot = alt.Chart(df).mark_tick(thickness=2, opacity=0.6).encode(
    x=alt.X('tempAvg:Q',
            title='Average Daily Temperature (°C)',
            scale=alt.Scale(domain=[-10, 30])),
    y=alt.Y('season:N',
            title='Season',
            sort=season_order),
    color=alt.condition(combined_selection,
                       alt.Color('season:N',
                                scale=alt.Scale(
                                    domain=['Winter', 'Spring', 'Summer', 'Fall'],
                                    range=['#3498db', '#2ecc71', '#f39c12', '#e74c3c']
                                ),
                                legend=None),
                       alt.value('lightgray')),
    opacity=alt.condition(combined_selection,
                         alt.value(0.8),
                         alt.value(0.15)),
    tooltip=[
        alt.Tooltip('day:T', title='Date', format='%Y-%m-%d'),
        alt.Tooltip('tempMin:Q', title='Min Temp (°C)', format='.1f'),
        alt.Tooltip('tempMax:Q', title='Max Temp (°C)', format='.1f'),
        alt.Tooltip('tempAvg:Q', title='Avg Temp (°C)', format='.1f'),
        alt.Tooltip('desc:N', title='Weather')
    ]
).add_params(
    year_select
).transform_filter(
    year_select
).properties(
    width=800,
    height=200,
    title='Daily Temperature Distribution by Season - Use Dropdown to Filter Year'
)

# ============================================================================
# VIEW 3: BUBBLE CHART (T3: Multi-dimensional Correlation)
# ============================================================================

bubble_chart = alt.Chart(df).mark_circle().encode(
    x=alt.X('tempAvg:Q',
            title='Average Temperature (°C)',
            scale=alt.Scale(domain=[-10, 30])),
    y=alt.Y('windSpeed:Q',
            title='Wind Speed (km/h)',
            scale=alt.Scale(domain=[0, 26])),
    size=alt.Size('humidity:Q',
                 title='Humidity',
                 scale=alt.Scale(range=[20, 500])),
    color=alt.condition(combined_selection,
                       alt.Color('cloudCover:Q',
                                title='Cloud Cover',
                                scale=alt.Scale(scheme='greys', domain=[0, 1])),
                       alt.value('lightgray')),
    opacity=alt.condition(combined_selection,
                         alt.value(0.7),
                         alt.value(0.1)),
    tooltip=[
        alt.Tooltip('day:T', title='Date', format='%Y-%m-%d'),
        alt.Tooltip('tempAvg:Q', title='Temperature (°C)', format='.1f'),
        alt.Tooltip('windSpeed:Q', title='Wind Speed (km/h)', format='.1f'),
        alt.Tooltip('humidity:Q', title='Humidity', format='.2f'),
        alt.Tooltip('cloudCover:Q', title='Cloud Cover', format='.2f'),
        alt.Tooltip('desc:N', title='Weather')
    ]
).transform_filter(
    year_select
).properties(
    width=400,
    height=300,
    title='Temperature vs Wind Speed (size=humidity, color=cloud cover)'
)

# ============================================================================
# VIEW 4: HISTOGRAM WITH FILTERING (T1, T5: Distribution and Filtering)
# ============================================================================

histogram = alt.Chart(df).mark_bar(opacity=0.7, binSpacing=0).encode(
    x=alt.X('tempAvg:Q',
            bin=alt.Bin(maxbins=40),
            title='Average Temperature (°C)'),
    y=alt.Y('count()', title='Number of Days'),
    color=alt.condition(combined_selection,
                       alt.Color('desc:N',
                                title='Weather Type',
                                scale=alt.Scale(
                                    domain=['rain', 'partly-cloudy-day', 'clear-day', 'cloudy', 'fog', 'unknown'],
                                    range=['#3498db', '#95a5a6', '#f39c12', '#7f8c8d', '#e74c3c', '#bdc3c7']
                                )),
                       alt.value('lightgray')),
    tooltip=[
        alt.Tooltip('tempAvg:Q', bin=alt.Bin(maxbins=40), title='Temperature Range'),
        alt.Tooltip('count()', title='Number of Days'),
        alt.Tooltip('desc:N', title='Weather Type')
    ]
).transform_filter(
    year_select
).properties(
    width=400,
    height=300,
    title='Temperature Distribution by Weather Type'
)

# ============================================================================
# COMPOSE ALL VIEWS
# ============================================================================

# Top row: Faceted time series (full width)
# Middle row: Strip plot (full width)
# Bottom row: Bubble chart | Histogram

middle_row = strip_plot
bottom_row = bubble_chart | histogram

final_chart = alt.vconcat(
    faceted_time_series,
    middle_row,
    bottom_row
).properties(
    title=alt.TitleParams(
        text='System C: Glasgow Weather Small Multiples Analysis (2015-2019)',
        fontSize=20,
        anchor='middle'
    )
).configure_view(
    strokeWidth=0
).configure_axis(
    labelFontSize=11,
    titleFontSize=12
).configure_legend(
    labelFontSize=10,
    titleFontSize=11
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
    html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'system_c_visualization.html')
    json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'system_c_spec.json')

    final_chart.save(html_path)
    final_chart.save(json_path)

    print("✓ System C visualization created successfully!")
    print(f"  - {html_path} (saved)")
    print(f"  - {json_path} (saved)")
    print("\nFeatures:")
    print("  • Faceted time series shows patterns for each year side-by-side")
    print("  • Dropdown to filter by year (affects strip plot, bubble, histogram)")
    print("  • Strip plot shows individual days - reveals outliers clearly")
    print("  • Brush on faceted view propagates to other views")
    print("  • Bubble chart encodes 4 dimensions: temp, wind, humidity (size), cloud (color)")
    print("  • Histogram shows temperature distribution by weather type")
    print("\n🚀 Opening in browser...")

    # Open in browser
    webbrowser.open('file://' + html_path)
