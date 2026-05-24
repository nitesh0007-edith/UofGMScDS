"""
Glasgow Weather Visualization Project - Streamlit Landing Page
Information Visualisation (M) | University of Glasgow | 2024/25

This app provides an interactive interface to launch all visualization systems.
"""

import streamlit as st
import subprocess
import os
import sys

# Page configuration
st.set_page_config(
    page_title="Glasgow Weather Visualization",
    page_icon="🌦️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .system-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #3498db;
        margin-bottom: 1rem;
    }
    .stat-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🌦️ Glasgow Weather Visualization</h1>
    <p>Multi-view Interactive Analysis of Daily Weather Data (2015-2019)</p>
    <p style="font-size: 0.9em; opacity: 0.9;">Information Visualisation Group Project | University of Glasgow | 2024/25</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("📊 Navigation")
    st.markdown("---")

    page = st.radio(
        "Select View:",
        ["🏠 Home", "🚀 Launch Systems", "📖 Documentation", "ℹ️ About"]
    )

    st.markdown("---")
    st.markdown("### 📈 Dataset Info")
    st.info("""
    **Records:** 1,795 days
    **Time Period:** 2015-2019
    **Attributes:** 9 weather metrics
    **Location:** Glasgow, Scotland
    """)

# Main content
if page == "🏠 Home":
    st.header("Welcome to Glasgow Weather Visualization Project")

    st.markdown("""
    This project presents **three distinct visualization systems** for analyzing 1,795 days of Glasgow weather data.
    Each system uses different design approaches to support five analytical tasks:

    1. **T1:** Compare seasonal patterns
    2. **T2:** Identify extreme weather events
    3. **T3:** Explore correlations between weather factors
    4. **T4:** Analyze temporal trends (2015-2019)
    5. **T5:** Filter and subset data interactively
    """)

    # Statistics
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
        <div class="stat-box">
            <h2>5 Years</h2>
            <p>Time Period</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="stat-box">
            <h2>9</h2>
            <p>Weather Attributes</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="stat-box">
            <h2>3</h2>
            <p>Visualization Systems</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Quick preview
    st.subheader("🎨 Visualization Systems Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### System A")
        st.info("**Temporal Analysis & Correlation**")
        st.markdown("""
        - Time series line chart
        - Scatter plot with regression
        - Seasonal bar chart
        - Wind speed histogram
        - **Bidirectional brushing & linking**
        """)

    with col2:
        st.markdown("### System B")
        st.warning("**Statistical Distribution Focus**")
        st.markdown("""
        - Monthly temperature heatmap
        - Box plots with outliers
        - Dynamic regression scatter
        - Weather type distribution
        - **Click & brush selection**
        """)

    with col3:
        st.markdown("### System C")
        st.success("**Small Multiples & Faceting**")
        st.markdown("""
        - Faceted time series (5 years)
        - Strip plot for outliers
        - Multi-dimensional bubble chart
        - Temperature histogram
        - **Dropdown & slider controls**
        """)

elif page == "🚀 Launch Systems":
    st.header("Launch Visualization Systems")

    st.markdown("""
    Click the buttons below to launch each visualization system in **your web browser**.
    All visualizations are fully interactive with brushing, linking, and filtering capabilities.
    Each visualization opens in a new browser tab.
    """)

    st.markdown("---")

    # System A
    st.subheader("🔵 System A: Temporal Analysis & Correlation")
    st.markdown("""
    **Features:**
    - Brush on time series to filter by date range
    - Brush on scatter plot to select humidity-visibility patterns
    - Click on bar chart to filter by season
    - All views linked bidirectionally
    - Red regression line shows correlation for selected data
    """)

    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("🚀 Launch System A", key="system_a", type="primary"):
            with st.spinner("Launching System A in browser..."):
                try:
                    subprocess.Popen([sys.executable, "SystemA/system_a.py"])
                    st.success("✓ System A launched! Check your browser for a new tab.")
                except Exception as e:
                    st.error(f"Error launching System A: {e}")

    st.markdown("---")

    # System B
    st.subheader("🔴 System B: Statistical Distribution Focus")
    st.markdown("""
    **Features:**
    - Click on heatmap cells to filter by month-year
    - Click on box plot to filter by season
    - Brush on scatter plot to select cloud cover patterns
    - All views linked with coordinated highlighting
    - Red regression curve shows correlation for selected data
    - Box plots explicitly show outliers and quartiles
    """)

    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("🚀 Launch System B", key="system_b", type="primary"):
            with st.spinner("Launching System B in browser..."):
                try:
                    subprocess.Popen([sys.executable, "SystemB/system_b.py"])
                    st.success("✓ System B launched! Check your browser for a new tab.")
                except Exception as e:
                    st.error(f"Error launching System B: {e}")

    st.markdown("---")

    # System C
    st.subheader("🟢 System C: Small Multiples & Faceting")
    st.markdown("""
    **Features:**
    - Faceted time series shows patterns for each year side-by-side
    - Dropdown to filter by year (affects strip plot, bubble, histogram)
    - Strip plot shows individual days - reveals outliers clearly
    - Brush on faceted view propagates to other views
    - Bubble chart encodes 4 dimensions: temp, wind, humidity (size), cloud (color)
    - Histogram shows temperature distribution by weather type
    """)

    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("🚀 Launch System C", key="system_c", type="primary"):
            with st.spinner("Launching System C in browser..."):
                try:
                    subprocess.Popen([sys.executable, "SystemC/system_c.py"])
                    st.success("✓ System C launched! Check your browser for a new tab.")
                except Exception as e:
                    st.error(f"Error launching System C: {e}")

    st.markdown("---")

    # Generalized Selection
    st.subheader("🟡 System A + Generalized Selection (Advanced)")
    st.markdown("""
    **Hierarchical Temporal Selection:**
    - 5-level temporal hierarchy: Day → Week → Month → Season → Year
    - Interactive hierarchy traversal with radio buttons
    - Aggregation views at all levels (week/month/season/year)
    - Visual feedback on selection generalization
    - **This is TRUE semantic abstraction, NOT global filtering**
    """)

    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("🚀 Launch Generalized Selection", key="system_gen", type="primary"):
            with st.spinner("Launching Generalized Selection in browser..."):
                try:
                    subprocess.Popen([sys.executable, "SystemA/system_a_with_generalization.py"])
                    st.success("✓ Generalized Selection launched! Check your browser for a new tab.")
                except Exception as e:
                    st.error(f"Error launching Generalized Selection: {e}")

    st.markdown("---")
    st.info("""
    **💡 Tip:** After clicking a button, the visualization will open in a new browser tab.
    All interactive features (brushing, linking, filtering) work directly in the browser.
    Keep this Streamlit page open to launch other systems!
    """)

elif page == "📖 Documentation":
    st.header("Project Documentation")

    tab1, tab2, tab3, tab4 = st.tabs(["📊 Data", "🎯 Tasks", "🔧 Systems", "🔄 Generalized Selection"])

    with tab1:
        st.subheader("Section 1: The Data")
        st.markdown("""
        **Glasgow Daily Weather Observations (2015-2019)**

        This dataset contains comprehensive meteorological measurements for Glasgow, Scotland,
        spanning 1,795 daily observations from January 1, 2015, to November 30, 2019.

        **Data Categorization (Munzner, 2014):**

        **Quantitative Attributes (6):**
        - `tempMin`: Minimum daily temperature in °C
        - `tempMax`: Maximum daily temperature in °C
        - `cloudCover`: Cloud coverage percentage [0-1]
        - `humidity`: Atmospheric humidity level [0-1]
        - `windSpeed`: Wind speed in km/h
        - `visibility`: Visibility distance in km

        **Categorical Attributes (2):**
        - `desc`: Weather condition type (rain, partly-cloudy-day, clear-day, cloudy, fog)
        - `summary`: Detailed weather description text

        **Temporal Attribute (1):**
        - `day`: Date of observation [2015-01-01 to 2019-11-30]

        **Hierarchical Structure:**
        - Day → Week → Month → Season → Year
        """)

    with tab2:
        st.subheader("Section 2: The Tasks")
        st.markdown("""
        Five analytical tasks defined using Brehmer & Munzner (2013) taxonomy:

        **T1: COMPARE Seasonal Temperature Patterns**
        - Compare mean temperatures across four seasons
        - Understand seasonal temperature ranges and variations

        **T2: IDENTIFY Extreme Weather Events**
        - Find days with unusual values (extreme temperatures, high wind, low visibility)
        - Identify outliers and anomalies

        **T3: EXPLORE Correlation Between Humidity and Visibility**
        - Discover relationships between weather factors
        - Understand how atmospheric conditions relate to each other

        **T4: ANALYZE Temporal Trends Across Years**
        - Identify year-over-year changes and patterns
        - Detect warming/cooling trends or shifting seasonal patterns

        **T5: FILTER and SUBSET Data by Time Period and Weather Type**
        - Focus analysis on specific time periods or weather conditions
        - Enable interactive exploration through selection and filtering
        """)

    with tab3:
        st.subheader("Section 3: The Core Systems")
        st.markdown("""
        **System A: Temporal Analysis & Correlation**
        - 4 views: Time series, Scatter plot, Bar chart, Histogram
        - Bidirectional brushing and linking
        - Best for: Temporal trend analysis (T4), Regional comparison (T1)

        **System B: Statistical Distribution Focus**
        - 4 views: Heatmap, Box plots, Scatter with regression, Bar chart
        - Click and brush selection
        - Best for: Outlier identification (T2), Statistical detail (T3)

        **System C: Small Multiples & Faceting**
        - 4 views: Faceted time series, Strip plot, Bubble chart, Histogram
        - Dropdown and slider controls
        - Best for: Filtering tasks (T5), Year-by-year comparison
        """)

    with tab4:
        st.subheader("Section 4: Generalized Selection")
        st.markdown("""
        **Hierarchical Temporal Structure:**
        ```
        Level 4 (Year)    → 2015, 2016, 2017, 2018, 2019
              ↑ generalizes
        Level 3 (Season)  → Winter, Spring, Summer, Fall
              ↑ generalizes
        Level 2 (Month)   → January-December
              ↑ generalizes
        Level 1 (Week)    → ~260 weeks
              ↑ generalizes
        Level 0 (Day)     → 1,795 individual days
        ```

        **Traversal Policy:**
        - **Generalize UP:** Move from specific (Day) to general (Year)
        - **Specialize DOWN:** Move from general (Year) to specific (Day)

        **Key Distinction:** This is NOT global filtering. It's true semantic hierarchical
        abstraction based on temporal relationships.

        **Example:**
        1. Select "January 8, 2015" (specific day)
        2. Generalize to "Week" level → Selects ALL days in Week 2
        3. Generalize to "Month" level → Selects ALL days in January 2015
        4. Generalize to "Season" level → Selects ALL Winter 2015 days
        5. Generalize to "Year" level → Selects ALL 2015 days
        """)

else:  # About page
    st.header("About This Project")

    st.markdown("""
    ### 🎓 Course Information
    - **Course:** Information Visualisation (M)
    - **Institution:** University of Glasgow
    - **Academic Year:** 2024/25
    - **Deadline:** March 20, 2026

    ### 📊 Project Overview
    This project implements a comprehensive multi-view visualization system for exploring Glasgow weather data.
    It demonstrates advanced information visualization techniques including:

    - Multi-view coordinated visualization
    - Brushing and linking (uni and bidirectional)
    - Hierarchical data structures
    - Generalized selection vs. global filtering
    - Task-driven design
    - Alternative design approaches

    ### 🛠️ Technology Stack
    - **Python 3.7+**
    - **Altair 5.5.0** (Declarative visualization library)
    - **Pandas 2.2.0** (Data manipulation)
    - **Streamlit** (Interactive web app framework)
    - **Vega-Lite** (Underlying JSON specification)

    ### 📈 Dataset
    - **Source:** Dark Sky API historical weather data
    - **Location:** Glasgow, Scotland
    - **Time Period:** January 1, 2015 - November 30, 2019
    - **Records:** 1,795 daily observations
    - **Attributes:** 9 weather metrics

    ### ✅ Implementation Status
    - ✓ All 3 core visualization systems
    - ✓ Generalized selection implementation
    - ✓ Data categorization and task definitions
    - ✓ Interactive Streamlit landing page
    - ✓ Browser-based visualization display
    - ✓ All filters and interactions working

    ### 📝 Remaining Work
    - Design comparison (Section 6)
    - User evaluation (Section 7)
    - Future work (Section 8)
    - Demo video (Section 5)
    - Final report compilation

    ### 🚀 How to Run
    ```bash
    # Start Streamlit app
    streamlit run app.py

    # Or run systems directly
    python SystemA/system_a.py
    python SystemB/system_b.py
    python SystemC/system_c.py
    python SystemA/system_a_with_generalization.py
    ```

    ### 📚 Learning Outcomes Demonstrated
    ✓ Multi-view coordinated visualization
    ✓ Brushing and linking
    ✓ Hierarchical data structures
    ✓ Semantic abstraction
    ✓ Task-driven design
    ✓ Data categorization
    ✓ Design comparison
    ✓ Alternative approaches
    """)

    st.markdown("---")
    st.info("**Contact:** [Insert Team Contact Information]")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1rem; color: #7f8c8d;">
    <p><strong>Glasgow Weather Visualization Project</strong></p>
    <p>Information Visualisation (M) | University of Glasgow | 2024/25</p>
</div>
""", unsafe_allow_html=True)
