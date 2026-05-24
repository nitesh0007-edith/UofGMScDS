"""
Glasgow Weather Visualization Dashboard - PowerBI Style
Information Visualisation (M) | University of Glasgow | 2024/25

Interactive dashboard with embedded Altair visualizations
All filters, radio buttons, and interactions work natively in Streamlit
"""

import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import os

# Page configuration
st.set_page_config(
    page_title="Glasgow Weather Dashboard",
    page_icon="🌦️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configure Altair
alt.data_transformers.disable_max_rows()

# Load data
@st.cache_data
def load_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, 'data', 'Glasgow_weather_data', 'weather_data_enriched.csv')
    df = pd.read_csv(data_path)
    df['day'] = pd.to_datetime(df['day'])
    df['tempAvg'] = (df['tempMin'] + df['tempMax']) / 2
    df['tempRange'] = df['tempMax'] - df['tempMin']

    # Add hierarchical temporal features
    df['week_of_year'] = df['day'].dt.isocalendar().week
    df['week_id'] = df['year'].astype(str) + '-W' + df['week_of_year'].astype(str).str.zfill(2)
    df['month_id'] = df['year'].astype(str) + '-M' + df['month'].astype(str).str.zfill(2)
    df['season_id'] = df['year'].astype(str) + '-' + df['season']

    # Handle missing values
    df = df.fillna({
        'cloudCover': df['cloudCover'].median(),
        'desc': 'unknown',
        'summary': 'No summary available'
    })
    return df

df = load_data()

# Custom CSS for PowerBI-style dashboard
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .system-card {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        margin-bottom: 1rem;
        transition: all 0.3s ease;
    }
    .system-card:hover {
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        transform: translateY(-2px);
    }
    .stat-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 8px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .stat-box h2 {
        margin: 0;
        font-size: 2.5rem;
        font-weight: bold;
    }
    .stat-box p {
        margin: 0.5rem 0 0 0;
        font-size: 0.9rem;
        opacity: 0.9;
    }
    .dashboard-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: #1e3a8a;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #3b82f6;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #f3f4f6;
        border-radius: 4px 4px 0 0;
        padding: 12px 24px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #3b82f6;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🌦️ Glasgow Weather Analytics Dashboard</h1>
    <p>Interactive Multi-View Visualization System | 2015-2019 Weather Data</p>
    <p style="font-size: 0.9em; opacity: 0.9;">University of Glasgow | Information Visualisation (M)</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("📊 Dashboard Navigation")
    st.markdown("---")

    page = st.radio(
        "Select View:",
        ["🏠 Home", "📈 System A", "📊 System B", "📉 System C", "🔄 Generalized Selection"],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown("### 📈 Dataset Overview")
    st.info(f"""
    **Records:** {len(df):,} days
    **Time Period:** 2015-2019
    **Attributes:** 9 metrics
    **Location:** Glasgow, Scotland
    """)

    st.markdown("---")
    st.markdown("### 🎯 Quick Stats")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Avg Temp", f"{df['tempAvg'].mean():.1f}°C")
    with col2:
        st.metric("Records", f"{len(df):,}")

# ============================================================================
# HOME PAGE
# ============================================================================
if page == "🏠 Home":
    # Statistics row
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="stat-box">
            <h2>1,795</h2>
            <p>Daily Observations</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="stat-box" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);">
            <h2>5</h2>
            <p>Years of Data</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="stat-box" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);">
            <h2>9</h2>
            <p>Weather Metrics</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="stat-box" style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);">
            <h2>3+1</h2>
            <p>Visualization Systems</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Systems overview
    st.markdown("## 🎨 Visualization Systems")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="system-card">
            <h3 style="color: #3b82f6;">📈 System A</h3>
            <h4>Temporal Analysis & Correlation</h4>
            <ul>
                <li>Time series line chart</li>
                <li>Scatter plot with regression</li>
                <li>Seasonal bar chart</li>
                <li>Wind speed histogram</li>
            </ul>
            <p><strong>Interaction:</strong> Bidirectional brushing & linking</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="system-card">
            <h3 style="color: #ef4444;">📊 System B</h3>
            <h4>Statistical Distribution</h4>
            <ul>
                <li>Monthly temperature heatmap</li>
                <li>Box plots with outliers</li>
                <li>Dynamic regression scatter</li>
                <li>Weather type distribution</li>
            </ul>
            <p><strong>Interaction:</strong> Click & brush selection</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="system-card">
            <h3 style="color: #10b981;">📉 System C</h3>
            <h4>Small Multiples & Faceting</h4>
            <ul>
                <li>Faceted time series (5 years)</li>
                <li>Strip plot for outliers</li>
                <li>Multi-dimensional bubble chart</li>
                <li>Temperature histogram</li>
            </ul>
            <p><strong>Interaction:</strong> Dropdown & slider controls</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Generalized Selection
    st.markdown("""
    <div class="system-card" style="background: linear-gradient(135deg, #ffeaa7 0%, #fdcb6e 100%); border: none;">
        <h3 style="color: #2d3436;">🔄 Generalized Selection (Advanced)</h3>
        <h4 style="color: #2d3436;">Hierarchical Temporal Abstraction</h4>
        <p style="color: #2d3436;">5-level temporal hierarchy: Day → Week → Month → Season → Year</p>
        <p style="color: #2d3436;"><strong>True semantic abstraction,</strong> not just filtering!</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🚀 Getting Started")
    st.info("""
    **Select a system from the sidebar** to view the interactive visualization dashboard.

    All filters, selections, and interactions work natively in this interface!
    """)

# ============================================================================
# SYSTEM A: TEMPORAL ANALYSIS
# ============================================================================
elif page == "📈 System A":
    st.markdown('<div class="dashboard-title">📈 System A: Temporal Analysis & Correlation</div>', unsafe_allow_html=True)

    st.markdown("""
    **Interactive Features:**
    🖱️ Brush on time series to filter date range | 🖱️ Brush on scatter to select patterns | 🖱️ Click seasons to filter | 🔗 All views linked bidirectionally
    """)

    # Selection parameters
    brush = alt.selection_interval(encodings=['x'], name='brush')
    brush_scatter = alt.selection_interval(name='brush_scatter')
    click_season = alt.selection_point(fields=['season'], name='click_season')

    combined_selection = brush | brush_scatter | click_season

    # View 1: Time Series
    time_series = alt.Chart(df).mark_line(point=True, strokeWidth=2).encode(
        x=alt.X('day:T', title='Date', axis=alt.Axis(format='%b %Y')),
        y=alt.Y('tempAvg:Q', title='Avg Temperature (°C)', scale=alt.Scale(domain=[-10, 32])),
        color=alt.condition(combined_selection, alt.value('steelblue'), alt.value('lightgray')),
        opacity=alt.condition(combined_selection, alt.value(1.0), alt.value(0.3)),
        tooltip=[
            alt.Tooltip('day:T', title='Date', format='%Y-%m-%d'),
            alt.Tooltip('tempAvg:Q', title='Avg Temp', format='.1f'),
            alt.Tooltip('desc:N', title='Weather')
        ]
    ).add_params(brush).properties(width=800, height=250, title='Temperature Time Series')

    # View 2: Scatter Plot
    scatter = alt.Chart(df).mark_circle(size=60).encode(
        x=alt.X('humidity:Q', title='Humidity (0-1)', scale=alt.Scale(domain=[0, 1])),
        y=alt.Y('visibility:Q', title='Visibility (km)', scale=alt.Scale(domain=[0, 12])),
        color=alt.condition(combined_selection,
                          alt.Color('season:N', scale=alt.Scale(
                              domain=['Winter', 'Spring', 'Summer', 'Fall'],
                              range=['#3498db', '#2ecc71', '#f39c12', '#e74c3c']
                          ), title='Season'),
                          alt.value('lightgray')),
        opacity=alt.condition(combined_selection, alt.value(0.7), alt.value(0.1)),
        tooltip=[
            alt.Tooltip('day:T', title='Date', format='%Y-%m-%d'),
            alt.Tooltip('humidity:Q', title='Humidity', format='.2f'),
            alt.Tooltip('visibility:Q', title='Visibility (km)', format='.1f'),
            alt.Tooltip('season:N', title='Season')
        ]
    ).add_params(brush_scatter).properties(width=400, height=300, title='Humidity vs Visibility')

    # Regression line (only for selected data)
    regression = scatter.transform_filter(combined_selection).transform_regression(
        'humidity', 'visibility'
    ).mark_line(color='red', strokeWidth=3)

    scatter_with_reg = scatter + regression

    # View 3: Seasonal Bar Chart
    season_bars = alt.Chart(df).mark_bar().encode(
        x=alt.X('season:N', title='Season', sort=['Winter', 'Spring', 'Summer', 'Fall']),
        y=alt.Y('mean(tempAvg):Q', title='Avg Temperature (°C)'),
        color=alt.condition(combined_selection,
                          alt.Color('season:N', scale=alt.Scale(
                              domain=['Winter', 'Spring', 'Summer', 'Fall'],
                              range=['#3498db', '#2ecc71', '#f39c12', '#e74c3c']
                          ), legend=None),
                          alt.value('lightgray')),
        opacity=alt.condition(combined_selection, alt.value(1.0), alt.value(0.3)),
        tooltip=[
            alt.Tooltip('season:N', title='Season'),
            alt.Tooltip('mean(tempAvg):Q', title='Avg Temp', format='.1f'),
            alt.Tooltip('count()', title='Days')
        ]
    ).add_params(click_season).properties(width=400, height=300, title='Temperature by Season')

    # View 4: Wind Speed Histogram
    histogram = alt.Chart(df).mark_bar(opacity=0.7).encode(
        x=alt.X('windSpeed:Q', bin=alt.Bin(maxbins=30), title='Wind Speed (km/h)'),
        y=alt.Y('count()', title='Number of Days'),
        color=alt.condition(combined_selection, alt.value('steelblue'), alt.value('lightgray')),
        opacity=alt.condition(combined_selection, alt.value(0.8), alt.value(0.2)),
        tooltip=[
            alt.Tooltip('windSpeed:Q', bin=alt.Bin(maxbins=30), title='Wind Speed'),
            alt.Tooltip('count()', title='Days')
        ]
    ).properties(width=800, height=200, title='Wind Speed Distribution')

    # Layout
    row1 = time_series
    row2 = scatter_with_reg | season_bars
    row3 = histogram

    final_chart = alt.vconcat(row1, row2, row3).configure_view(strokeWidth=0)

    st.altair_chart(final_chart, use_container_width=False)

    # Export button
    if st.button("💾 Export to Altair Viewer"):
        final_chart.save('SystemA/system_a_visualization.html')
        st.success("✓ Saved to SystemA/system_a_visualization.html")

# ============================================================================
# SYSTEM B: STATISTICAL DISTRIBUTION
# ============================================================================
elif page == "📊 System B":
    st.markdown('<div class="dashboard-title">📊 System B: Statistical Distribution Focus</div>', unsafe_allow_html=True)

    st.markdown("""
    **Interactive Features:**
    🖱️ Click heatmap cells to filter month-year | 🖱️ Click box plot to filter seasons | 🖱️ Brush scatter to select patterns | 📈 Dynamic polynomial regression
    """)

    # Selection parameters
    click_heatmap = alt.selection_point(fields=['month', 'year'], name='click_heatmap')
    brush_scatter = alt.selection_interval(name='brush_scatter')
    click_season = alt.selection_point(fields=['season'], name='click_season')
    combined_selection = click_heatmap | brush_scatter | click_season

    # View 1: Heatmap
    heatmap_data = df.groupby(['year', 'month']).agg({'tempAvg': 'mean'}).reset_index()

    heatmap = alt.Chart(heatmap_data).mark_rect().encode(
        x=alt.X('year:O', title='Year'),
        y=alt.Y('month:O', title='Month', sort=[1,2,3,4,5,6,7,8,9,10,11,12]),
        color=alt.Color('tempAvg:Q', title='Avg Temp (°C)',
                       scale=alt.Scale(scheme='redyellowblue', reverse=True, domain=[0, 20])),
        stroke=alt.condition(click_heatmap, alt.value('black'), alt.value(None)),
        strokeWidth=alt.condition(click_heatmap, alt.value(3), alt.value(0)),
        tooltip=[
            alt.Tooltip('year:O', title='Year'),
            alt.Tooltip('month:O', title='Month'),
            alt.Tooltip('tempAvg:Q', title='Avg Temp', format='.1f')
        ]
    ).add_params(click_heatmap).properties(width=400, height=300, title='Monthly Temperature Heatmap')

    # View 2: Box Plot
    season_order = ['Winter', 'Spring', 'Summer', 'Fall']
    box_plot = alt.Chart(df).mark_boxplot(size=50).encode(
        x=alt.X('season:N', title='Season', sort=season_order),
        y=alt.Y('tempAvg:Q', title='Avg Temperature (°C)', scale=alt.Scale(domain=[-10, 32])),
        color=alt.condition(combined_selection,
                          alt.Color('season:N', scale=alt.Scale(
                              domain=season_order,
                              range=['#3498db', '#2ecc71', '#f39c12', '#e74c3c']
                          ), legend=None),
                          alt.value('lightgray')),
        opacity=alt.condition(combined_selection, alt.value(1.0), alt.value(0.3)),
        tooltip=[alt.Tooltip('season:N', title='Season')]
    ).add_params(click_season).properties(width=400, height=300, title='Temperature Distribution by Season')

    # View 3: Scatter with Regression
    scatter = alt.Chart(df).mark_circle(size=60, opacity=0.6).encode(
        x=alt.X('cloudCover:Q', title='Cloud Cover (0-1)', scale=alt.Scale(domain=[0, 1])),
        y=alt.Y('humidity:Q', title='Humidity (0-1)', scale=alt.Scale(domain=[0, 1])),
        color=alt.condition(combined_selection,
                          alt.Color('desc:N', scale=alt.Scale(
                              domain=['rain', 'partly-cloudy-day', 'clear-day', 'cloudy', 'fog', 'unknown'],
                              range=['#3498db', '#95a5a6', '#f39c12', '#7f8c8d', '#e74c3c', '#bdc3c7']
                          ), title='Weather'),
                          alt.value('lightgray')),
        opacity=alt.condition(combined_selection, alt.value(0.7), alt.value(0.1)),
        tooltip=[
            alt.Tooltip('day:T', title='Date', format='%Y-%m-%d'),
            alt.Tooltip('cloudCover:Q', title='Cloud Cover', format='.2f'),
            alt.Tooltip('humidity:Q', title='Humidity', format='.2f'),
            alt.Tooltip('desc:N', title='Weather')
        ]
    ).add_params(brush_scatter).properties(width=400, height=300, title='Cloud Cover vs Humidity')

    regression = scatter.transform_filter(combined_selection).transform_regression(
        'cloudCover', 'humidity', method='poly', order=2
    ).mark_line(color='red', strokeWidth=4, strokeDash=[5, 5])

    scatter_with_reg = scatter + regression

    # View 4: Weather Distribution
    weather_dist = df.groupby(['season', 'desc']).size().reset_index(name='count')
    weather_dist['season'] = pd.Categorical(weather_dist['season'], categories=season_order, ordered=True)

    weather_bars = alt.Chart(weather_dist).mark_bar().encode(
        x=alt.X('season:N', title='Season', sort=season_order),
        y=alt.Y('count:Q', title='Number of Days'),
        color=alt.Color('desc:N', title='Weather Type',
                       scale=alt.Scale(
                           domain=['rain', 'partly-cloudy-day', 'clear-day', 'cloudy', 'fog', 'unknown'],
                           range=['#3498db', '#95a5a6', '#f39c12', '#7f8c8d', '#e74c3c', '#bdc3c7']
                       )),
        tooltip=[
            alt.Tooltip('season:N', title='Season'),
            alt.Tooltip('desc:N', title='Weather'),
            alt.Tooltip('count:Q', title='Days')
        ]
    ).properties(width=800, height=250, title='Weather Type Distribution by Season')

    # Layout
    row1 = heatmap | box_plot
    row2 = scatter_with_reg | weather_bars

    final_chart = alt.vconcat(row1, row2).configure_view(strokeWidth=0)

    st.altair_chart(final_chart, use_container_width=False)

    if st.button("💾 Export to Altair Viewer"):
        final_chart.save('SystemB/system_b_visualization.html')
        st.success("✓ Saved to SystemB/system_b_visualization.html")

# ============================================================================
# SYSTEM C: SMALL MULTIPLES
# ============================================================================
elif page == "📉 System C":
    st.markdown('<div class="dashboard-title">📉 System C: Small Multiples & Faceting</div>', unsafe_allow_html=True)

    st.markdown("""
    **Interactive Features:**
    📅 Dropdown to filter by year | 🖱️ Brush on faceted views | 🎯 Strip plot reveals outliers | 🫧 Multi-dimensional bubble chart
    """)

    # Filters in columns
    col1, col2 = st.columns([1, 3])

    with col1:
        selected_year = st.selectbox(
            "Filter by Year:",
            options=[None, 2015, 2016, 2017, 2018, 2019],
            format_func=lambda x: "All Years" if x is None else str(x)
        )

    # Filter data if year selected
    filtered_df = df if selected_year is None else df[df['year'] == selected_year]

    # Selection parameters
    brush = alt.selection_interval(name='brush')
    combined_selection = brush

    season_order = ['Winter', 'Spring', 'Summer', 'Fall']

    # View 1: Faceted Time Series
    faceted_time_series = alt.Chart(filtered_df).mark_line(point=True, strokeWidth=1.5).encode(
        x=alt.X('month(day):O', title='Month'),
        y=alt.Y('mean(tempAvg):Q', title='Avg Temp (°C)', scale=alt.Scale(domain=[-5, 25])),
        color=alt.Color('season:N', scale=alt.Scale(
            domain=season_order,
            range=['#3498db', '#2ecc71', '#f39c12', '#e74c3c']
        ), title='Season'),
        opacity=alt.condition(brush, alt.value(1.0), alt.value(0.3)),
        tooltip=[
            alt.Tooltip('year:O', title='Year'),
            alt.Tooltip('month(day):O', title='Month'),
            alt.Tooltip('mean(tempAvg):Q', title='Avg Temp', format='.1f')
        ]
    ).properties(width=150, height=120).facet(
        column=alt.Column('year:O', title='Year')
    ).add_params(brush).properties(title='Monthly Temperature Patterns by Year')

    # View 2: Strip Plot
    strip_plot = alt.Chart(filtered_df).mark_tick(thickness=2, opacity=0.6).encode(
        x=alt.X('tempAvg:Q', title='Avg Temperature (°C)', scale=alt.Scale(domain=[-10, 30])),
        y=alt.Y('season:N', title='Season', sort=season_order),
        color=alt.condition(combined_selection,
                          alt.Color('season:N', scale=alt.Scale(
                              domain=season_order,
                              range=['#3498db', '#2ecc71', '#f39c12', '#e74c3c']
                          ), legend=None),
                          alt.value('lightgray')),
        opacity=alt.condition(combined_selection, alt.value(0.8), alt.value(0.15)),
        tooltip=[
            alt.Tooltip('day:T', title='Date', format='%Y-%m-%d'),
            alt.Tooltip('tempMin:Q', title='Min Temp', format='.1f'),
            alt.Tooltip('tempMax:Q', title='Max Temp', format='.1f'),
            alt.Tooltip('tempAvg:Q', title='Avg Temp', format='.1f')
        ]
    ).properties(width=800, height=200, title='Daily Temperature Distribution by Season')

    # View 3: Bubble Chart
    bubble_chart = alt.Chart(filtered_df).mark_circle().encode(
        x=alt.X('tempAvg:Q', title='Avg Temperature (°C)', scale=alt.Scale(domain=[-10, 30])),
        y=alt.Y('windSpeed:Q', title='Wind Speed (km/h)', scale=alt.Scale(domain=[0, 26])),
        size=alt.Size('humidity:Q', title='Humidity', scale=alt.Scale(range=[20, 500])),
        color=alt.condition(combined_selection,
                          alt.Color('cloudCover:Q', title='Cloud Cover',
                                   scale=alt.Scale(scheme='greys', domain=[0, 1])),
                          alt.value('lightgray')),
        opacity=alt.condition(combined_selection, alt.value(0.7), alt.value(0.1)),
        tooltip=[
            alt.Tooltip('day:T', title='Date', format='%Y-%m-%d'),
            alt.Tooltip('tempAvg:Q', title='Temp', format='.1f'),
            alt.Tooltip('windSpeed:Q', title='Wind', format='.1f'),
            alt.Tooltip('humidity:Q', title='Humidity', format='.2f'),
            alt.Tooltip('cloudCover:Q', title='Cloud', format='.2f')
        ]
    ).properties(width=400, height=300, title='Temperature vs Wind (size=humidity, color=cloud)')

    # View 4: Histogram
    histogram = alt.Chart(filtered_df).mark_bar(opacity=0.7).encode(
        x=alt.X('tempAvg:Q', bin=alt.Bin(maxbins=40), title='Avg Temperature (°C)'),
        y=alt.Y('count()', title='Number of Days'),
        color=alt.condition(combined_selection,
                          alt.Color('desc:N', title='Weather',
                                   scale=alt.Scale(
                                       domain=['rain', 'partly-cloudy-day', 'clear-day', 'cloudy', 'fog', 'unknown'],
                                       range=['#3498db', '#95a5a6', '#f39c12', '#7f8c8d', '#e74c3c', '#bdc3c7']
                                   )),
                          alt.value('lightgray')),
        tooltip=[
            alt.Tooltip('tempAvg:Q', bin=alt.Bin(maxbins=40), title='Temp Range'),
            alt.Tooltip('count()', title='Days'),
            alt.Tooltip('desc:N', title='Weather')
        ]
    ).properties(width=400, height=300, title='Temperature Distribution by Weather Type')

    # Layout
    row1 = faceted_time_series
    row2 = strip_plot
    row3 = bubble_chart | histogram

    final_chart = alt.vconcat(row1, row2, row3).configure_view(strokeWidth=0)

    st.altair_chart(final_chart, use_container_width=False)

    if st.button("💾 Export to Altair Viewer"):
        final_chart.save('SystemC/system_c_visualization.html')
        st.success("✓ Saved to SystemC/system_c_visualization.html")

# ============================================================================
# GENERALIZED SELECTION
# ============================================================================
elif page == "🔄 Generalized Selection":
    st.markdown('<div class="dashboard-title">🔄 Generalized Selection: Hierarchical Temporal Abstraction</div>', unsafe_allow_html=True)

    st.markdown("""
    **5-Level Temporal Hierarchy:**
    Day (Level 0) ↑ Week (Level 1) ↑ Month (Level 2) ↑ Season (Level 3) ↑ Year (Level 4)
    """)

    # Hierarchy level selector
    col1, col2 = st.columns([1, 3])

    with col1:
        hierarchy_level = st.radio(
            "Select Hierarchy Level:",
            options=[0, 1, 2, 3, 4],
            format_func=lambda x: ['Day (Level 0)', 'Week (Level 1)', 'Month (Level 2)',
                                   'Season (Level 3)', 'Year (Level 4)'][x],
            index=2
        )

    with col2:
        st.info(f"""
        **Current Level: {['Day', 'Week', 'Month', 'Season', 'Year'][hierarchy_level]}**
        Click or brush on the time series to select data at this hierarchy level.
        Watch how the selection propagates to all aggregation levels!
        """)

    # Selection parameters
    select_day = alt.selection_point(fields=['day'], name='select_day')
    select_week = alt.selection_point(fields=['week_id'], name='select_week')
    select_month = alt.selection_point(fields=['month_id'], name='select_month')
    select_season = alt.selection_point(fields=['season_id'], name='select_season')
    select_year = alt.selection_point(fields=['year'], name='select_year')
    brush = alt.selection_interval(encodings=['x'], name='brush')

    combined_selection = select_day | select_week | select_month | select_season | select_year | brush

    # View 1: Time Series with Hierarchical Selection
    time_series_base = alt.Chart(df).mark_line(point=True, strokeWidth=1.5).encode(
        x=alt.X('day:T', title='Date'),
        y=alt.Y('tempAvg:Q', title='Avg Temperature (°C)', scale=alt.Scale(domain=[-10, 32])),
        color=alt.value('steelblue'),
        tooltip=[
            alt.Tooltip('day:T', title='Date', format='%Y-%m-%d'),
            alt.Tooltip('week_id:N', title='Week'),
            alt.Tooltip('month_id:N', title='Month'),
            alt.Tooltip('season_id:N', title='Season'),
            alt.Tooltip('year:O', title='Year'),
            alt.Tooltip('tempAvg:Q', title='Temp', format='.1f')
        ]
    ).add_params(select_day, select_week, select_month, select_season, select_year, brush
    ).properties(width=800, height=250, title='Temperature Time Series - Click or Brush to Select')

    time_series_highlight = alt.Chart(df).mark_line(point={'size': 100}, strokeWidth=3).encode(
        x=alt.X('day:T', axis=None),
        y=alt.Y('tempAvg:Q', axis=None),
        color=alt.value('red'),
        opacity=alt.value(0.8)
    ).transform_filter(combined_selection)

    time_series = time_series_base + time_series_highlight

    # View 2: Aggregation Bars
    col1, col2 = st.columns(2)

    with col1:
        # Week aggregation
        week_bars = alt.Chart(df).mark_bar().encode(
            x=alt.X('week_id:N', title='Week', axis=alt.Axis(labelAngle=-45, labelLimit=100)),
            y=alt.Y('mean(tempAvg):Q', title='Avg Temp (°C)'),
            color=alt.condition(select_week | brush, alt.value('orange'), alt.value('lightgray')),
            opacity=alt.condition(select_week | brush, alt.value(1.0), alt.value(0.5)),
            tooltip=[
                alt.Tooltip('week_id:N', title='Week'),
                alt.Tooltip('mean(tempAvg):Q', title='Avg Temp', format='.1f'),
                alt.Tooltip('count()', title='Days')
            ]
        ).properties(width=400, height=200, title='Week-Level Aggregation')

        st.altair_chart(week_bars, use_container_width=False)

        # Season aggregation
        season_bars = alt.Chart(df).mark_bar().encode(
            x=alt.X('season_id:N', title='Season', axis=alt.Axis(labelAngle=-45)),
            y=alt.Y('mean(tempAvg):Q', title='Avg Temp (°C)'),
            color=alt.condition(select_season | brush,
                              alt.Color('season:N', scale=alt.Scale(
                                  domain=['Winter', 'Spring', 'Summer', 'Fall'],
                                  range=['#3498db', '#2ecc71', '#f39c12', '#e74c3c']
                              ), legend=None),
                              alt.value('lightgray')),
            opacity=alt.condition(select_season | brush, alt.value(1.0), alt.value(0.5)),
            tooltip=[
                alt.Tooltip('season_id:N', title='Season-Year'),
                alt.Tooltip('season:N', title='Season'),
                alt.Tooltip('mean(tempAvg):Q', title='Avg Temp', format='.1f'),
                alt.Tooltip('count()', title='Days')
            ]
        ).properties(width=400, height=200, title='Season-Level Aggregation')

        st.altair_chart(season_bars, use_container_width=False)

    with col2:
        # Month aggregation
        month_bars = alt.Chart(df).mark_bar().encode(
            x=alt.X('month_id:N', title='Month', axis=alt.Axis(labelAngle=-45)),
            y=alt.Y('mean(tempAvg):Q', title='Avg Temp (°C)'),
            color=alt.condition(select_month | brush, alt.value('green'), alt.value('lightgray')),
            opacity=alt.condition(select_month | brush, alt.value(1.0), alt.value(0.5)),
            tooltip=[
                alt.Tooltip('month_id:N', title='Month'),
                alt.Tooltip('mean(tempAvg):Q', title='Avg Temp', format='.1f'),
                alt.Tooltip('count()', title='Days')
            ]
        ).properties(width=400, height=200, title='Month-Level Aggregation')

        st.altair_chart(month_bars, use_container_width=False)

        # Year aggregation
        year_bars = alt.Chart(df).mark_bar().encode(
            x=alt.X('year:O', title='Year'),
            y=alt.Y('mean(tempAvg):Q', title='Avg Temp (°C)'),
            color=alt.condition(select_year | brush, alt.value('purple'), alt.value('lightgray')),
            opacity=alt.condition(select_year | brush, alt.value(1.0), alt.value(0.5)),
            tooltip=[
                alt.Tooltip('year:O', title='Year'),
                alt.Tooltip('mean(tempAvg):Q', title='Avg Temp', format='.1f'),
                alt.Tooltip('count()', title='Days')
            ]
        ).properties(width=400, height=200, title='Year-Level Aggregation')

        st.altair_chart(year_bars, use_container_width=False)

    # View 3: Scatter Plot
    scatter = alt.Chart(df).mark_circle(size=60).encode(
        x=alt.X('humidity:Q', title='Humidity (0-1)', scale=alt.Scale(domain=[0, 1])),
        y=alt.Y('windSpeed:Q', title='Wind Speed (km/h)', scale=alt.Scale(domain=[0, 26])),
        color=alt.condition(combined_selection,
                          alt.Color('season:N', scale=alt.Scale(
                              domain=['Winter', 'Spring', 'Summer', 'Fall'],
                              range=['#3498db', '#2ecc71', '#f39c12', '#e74c3c']
                          ), title='Season'),
                          alt.value('lightgray')),
        opacity=alt.condition(combined_selection, alt.value(0.8), alt.value(0.1)),
        size=alt.condition(combined_selection, alt.value(100), alt.value(20)),
        tooltip=[
            alt.Tooltip('day:T', title='Date', format='%Y-%m-%d'),
            alt.Tooltip('humidity:Q', title='Humidity', format='.2f'),
            alt.Tooltip('windSpeed:Q', title='Wind Speed', format='.1f'),
            alt.Tooltip('season:N', title='Season')
        ]
    ).properties(width=800, height=300, title='Humidity vs Wind Speed - Updates Based on Selection')

    # Display main chart
    st.altair_chart(time_series, use_container_width=False)
    st.altair_chart(scatter, use_container_width=False)

    if st.button("💾 Export to Altair Viewer"):
        # Combine all for export
        aggregation_row = (week_bars | month_bars) & (season_bars | year_bars)
        final_chart = alt.vconcat(time_series, aggregation_row, scatter).configure_view(strokeWidth=0)
        final_chart.save('SystemA/system_a_with_generalization.html')
        st.success("✓ Saved to SystemA/system_a_with_generalization.html")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1rem; color: #6b7280;">
    <p><strong>Glasgow Weather Analytics Dashboard</strong> | Information Visualisation (M) | University of Glasgow | 2024/25</p>
    <p style="font-size: 0.9em;">All visualizations created with Altair 5.5.0 | Interactive features powered by Vega-Lite</p>
</div>
""", unsafe_allow_html=True)
