"""
System A: Scatter Plot + Bar Chart with Bidirectional Linking
=============================================================

Design: This system uses scatter plots and bar charts to explore relationships
between happiness indicators and regional patterns.

Views:
- View 1: Scatter plot (Happiness Score vs GDP per Capita) with color by region
- View 2: Bar chart showing average happiness score by region
- View 3: Time series line chart showing happiness trends over years

Interaction: Bidirectional brushing and linking across all views
Tasks Supported: T1-T5 (see project report for task definitions)
"""

import altair as alt
import pandas as pd
import sys

# Enable data transformer to handle larger datasets
alt.data_transformers.disable_max_rows()

def load_data():
    """Load the World Happiness dataset"""
    df = pd.read_csv('../data/world_happiness_data.csv')
    return df

def create_system_a():
    """
    Create System A with multiple linked views
    """
    # Load data
    data = load_data()

    # Create a selection that will be shared across charts
    brush = alt.selection_interval(
        encodings=['x', 'y'],
        name='brush'
    )

    click_region = alt.selection_point(
        fields=['Region'],
        name='region_select'
    )

    # Color scale for regions
    color_scale = alt.Scale(
        domain=list(data['Region'].unique()),
        range=['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00',
               '#ffff33', '#a65628', '#f781bf', '#999999', '#66c2a5']
    )

    # ===== VIEW 1: Scatter Plot (Happiness vs GDP) =====
    scatter = alt.Chart(data).mark_circle(size=100).encode(
        x=alt.X('GDP_per_Capita:Q',
                title='GDP per Capita (normalized)',
                scale=alt.Scale(zero=False)),
        y=alt.Y('Happiness_Score:Q',
                title='Happiness Score',
                scale=alt.Scale(zero=False, domain=[3, 8.5])),
        color=alt.condition(
            brush | click_region,
            alt.Color('Region:N',
                     scale=color_scale,
                     legend=alt.Legend(title='Region', columns=2)),
            alt.value('lightgray')
        ),
        opacity=alt.condition(brush | click_region, alt.value(0.9), alt.value(0.2)),
        tooltip=[
            alt.Tooltip('Country:N', title='Country'),
            alt.Tooltip('Region:N', title='Region'),
            alt.Tooltip('Year:O', title='Year'),
            alt.Tooltip('Happiness_Score:Q', title='Happiness Score', format='.2f'),
            alt.Tooltip('GDP_per_Capita:Q', title='GDP per Capita', format='.3f'),
            alt.Tooltip('Social_Support:Q', title='Social Support', format='.3f')
        ]
    ).add_params(
        brush
    ).properties(
        width=450,
        height=350,
        title='Happiness Score vs GDP per Capita (Brush to Select)'
    )

    # ===== VIEW 2: Bar Chart (Average Happiness by Region) =====
    bars = alt.Chart(data).mark_bar().encode(
        y=alt.Y('Region:N',
                title='Region',
                sort='-x'),
        x=alt.X('mean(Happiness_Score):Q',
                title='Average Happiness Score',
                scale=alt.Scale(domain=[4, 8])),
        color=alt.condition(
            click_region | brush,
            alt.Color('Region:N',
                     scale=color_scale,
                     legend=None),
            alt.value('lightgray')
        ),
        opacity=alt.condition(click_region | brush, alt.value(1.0), alt.value(0.3)),
        tooltip=[
            alt.Tooltip('Region:N', title='Region'),
            alt.Tooltip('mean(Happiness_Score):Q', title='Avg Happiness', format='.2f'),
            alt.Tooltip('count():Q', title='Number of Records')
        ]
    ).add_params(
        click_region
    ).properties(
        width=450,
        height=350,
        title='Average Happiness Score by Region (Click to Select)'
    )

    # ===== VIEW 3: Line Chart (Happiness Trend Over Time) =====
    lines = alt.Chart(data).mark_line(point=True, strokeWidth=2).encode(
        x=alt.X('Year:O', title='Year'),
        y=alt.Y('mean(Happiness_Score):Q',
                title='Average Happiness Score',
                scale=alt.Scale(domain=[4, 8])),
        color=alt.condition(
            brush | click_region,
            alt.Color('Region:N',
                     scale=color_scale,
                     legend=None),
            alt.value('lightgray')
        ),
        opacity=alt.condition(brush | click_region, alt.value(1.0), alt.value(0.1)),
        tooltip=[
            alt.Tooltip('Region:N', title='Region'),
            alt.Tooltip('Year:O', title='Year'),
            alt.Tooltip('mean(Happiness_Score):Q', title='Avg Happiness', format='.2f')
        ]
    ).properties(
        width=920,
        height=250,
        title='Happiness Score Trends Over Time'
    )

    # ===== VIEW 4: Histogram (Distribution of Social Support) =====
    histogram = alt.Chart(data).mark_bar().encode(
        x=alt.X('Social_Support:Q',
                bin=alt.Bin(maxbins=30),
                title='Social Support'),
        y=alt.Y('count():Q',
                title='Number of Countries'),
        color=alt.condition(
            brush | click_region,
            alt.value('steelblue'),
            alt.value('lightgray')
        ),
        opacity=alt.condition(brush | click_region, alt.value(0.8), alt.value(0.2)),
        tooltip=[
            alt.Tooltip('count():Q', title='Count'),
            alt.Tooltip('Social_Support:Q', bin=True, title='Social Support Range')
        ]
    ).properties(
        width=450,
        height=250,
        title='Distribution of Social Support (Filtered by Selection)'
    )

    # ===== Combine all views =====
    # Top row: scatter and bars side by side
    top_row = scatter | bars

    # Bottom left: lines
    bottom_left = lines

    # Final composition: stack vertically
    final_chart = alt.vconcat(
        top_row,
        bottom_left
    ).properties(
        title=alt.TitleParams(
            text='System A: Multi-View Happiness Analysis with Linked Brushing',
            fontSize=18,
            anchor='middle'
        )
    ).configure_axis(
        labelFontSize=11,
        titleFontSize=12
    ).configure_title(
        fontSize=14,
        anchor='start'
    ).configure_legend(
        titleFontSize=12,
        labelFontSize=11
    )

    return final_chart

def main():
    """Main function to create and save the visualization"""
    print("Creating System A...")

    # Create the visualization
    chart = create_system_a()

    # Save as HTML
    chart.save('system_a_visualization.html')
    print("✓ System A visualization saved as 'system_a_visualization.html'")

    # Also save as JSON spec
    chart.save('system_a_spec.json')
    print("✓ System A specification saved as 'system_a_spec.json'")

    print("\nSystem A Features:")
    print("- Bidirectional brushing and linking across multiple views")
    print("- Scatter plot: Happiness vs GDP with region coloring")
    print("- Bar chart: Average happiness by region (click to filter)")
    print("- Line chart: Temporal trends filtered by selection")
    print("- Interactive tooltips with detailed information")

if __name__ == "__main__":
    main()
