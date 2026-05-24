"""
System B: Heatmap + Box Plot + Stacked Area with Bidirectional Linking
========================================================================

Design: This system uses heatmaps and box plots to explore distributions
and patterns across regions and time.

Views:
- View 1: Heatmap showing average happiness score by Region × Year
- View 2: Box plot showing distribution of happiness factors by region
- View 3: Stacked area chart showing contribution of happiness factors over time
- View 4: Scatter plot matrix (mini) for multivariate relationships

Interaction: Bidirectional brushing and linking with interval and point selections
Tasks Supported: T1-T5 (see project report for task definitions)
"""

import altair as alt
import pandas as pd

# Enable data transformer to handle larger datasets
alt.data_transformers.disable_max_rows()

def load_data():
    """Load the World Happiness dataset"""
    df = pd.read_csv('../data/world_happiness_data.csv')
    return df

def create_system_b():
    """
    Create System B with multiple linked views
    """
    # Load data
    data = load_data()

    # Create shared selections
    brush = alt.selection_interval(name='brush_b')
    click = alt.selection_point(fields=['Region'], name='click_region_b')

    # Color scale for regions
    color_scale = alt.Scale(
        domain=list(data['Region'].unique()),
        range=['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3',
               '#fdb462', '#b3de69', '#fccde5', '#d9d9d9', '#bc80bd']
    )

    # ===== VIEW 1: Heatmap (Region × Year) =====
    heatmap = alt.Chart(data).mark_rect().encode(
        x=alt.X('Year:O', title='Year'),
        y=alt.Y('Region:N', title='Region', sort='-color'),
        color=alt.condition(
            brush | click,
            alt.Color('mean(Happiness_Score):Q',
                     scale=alt.Scale(scheme='viridis', domain=[4, 7.5]),
                     legend=alt.Legend(title='Avg Happiness')),
            alt.value('lightgray')
        ),
        opacity=alt.condition(brush | click, alt.value(1.0), alt.value(0.3)),
        tooltip=[
            alt.Tooltip('Region:N', title='Region'),
            alt.Tooltip('Year:O', title='Year'),
            alt.Tooltip('mean(Happiness_Score):Q', title='Avg Happiness', format='.2f'),
            alt.Tooltip('count():Q', title='Countries')
        ]
    ).add_params(
        click
    ).properties(
        width=400,
        height=350,
        title='Happiness Score Heatmap: Region × Year (Click Region to Filter)'
    )

    # ===== VIEW 2: Box Plot (Happiness Distribution by Region) =====
    boxplot = alt.Chart(data).mark_boxplot(size=30).encode(
        x=alt.X('Happiness_Score:Q',
                title='Happiness Score',
                scale=alt.Scale(domain=[3, 8.5])),
        y=alt.Y('Region:N',
                title='Region',
                sort='-x'),
        color=alt.condition(
            click | brush,
            alt.Color('Region:N',
                     scale=color_scale,
                     legend=None),
            alt.value('lightgray')
        ),
        opacity=alt.condition(click | brush, alt.value(0.9), alt.value(0.2)),
        tooltip=[
            alt.Tooltip('Region:N', title='Region'),
            alt.Tooltip('min(Happiness_Score):Q', title='Min', format='.2f'),
            alt.Tooltip('q1(Happiness_Score):Q', title='Q1', format='.2f'),
            alt.Tooltip('median(Happiness_Score):Q', title='Median', format='.2f'),
            alt.Tooltip('q3(Happiness_Score):Q', title='Q3', format='.2f'),
            alt.Tooltip('max(Happiness_Score):Q', title='Max', format='.2f')
        ]
    ).properties(
        width=450,
        height=350,
        title='Distribution of Happiness Scores by Region'
    )

    # ===== VIEW 3: Scatter Plot with Regression (Freedom vs Corruption) =====
    # Create base scatter
    scatter_fc = alt.Chart(data).mark_circle(size=60).encode(
        x=alt.X('Corruption_Perception:Q',
                title='Corruption Perception (higher = more corrupt)',
                scale=alt.Scale(zero=False)),
        y=alt.Y('Freedom:Q',
                title='Freedom to Make Life Choices',
                scale=alt.Scale(zero=False)),
        color=alt.condition(
            brush | click,
            alt.Color('Region:N',
                     scale=color_scale,
                     legend=None),
            alt.value('lightgray')
        ),
        opacity=alt.condition(brush | click, alt.value(0.7), alt.value(0.1)),
        tooltip=[
            alt.Tooltip('Country:N', title='Country'),
            alt.Tooltip('Region:N', title='Region'),
            alt.Tooltip('Freedom:Q', title='Freedom', format='.3f'),
            alt.Tooltip('Corruption_Perception:Q', title='Corruption', format='.3f')
        ]
    ).add_params(
        brush
    )

    # Add regression line
    regression = alt.Chart(data).mark_line(color='red', size=2).encode(
        x='Corruption_Perception:Q',
        y='Freedom:Q',
        opacity=alt.condition(brush | click, alt.value(0.8), alt.value(0))
    ).transform_filter(
        brush | click
    ).transform_regression(
        'Corruption_Perception', 'Freedom'
    )

    scatter_with_reg = (scatter_fc + regression).properties(
        width=450,
        height=300,
        title='Freedom vs Corruption (Brush to Select, Shows Trend Line)'
    )

    # ===== VIEW 4: Grouped Bar Chart (Factors Comparison) =====
    # Prepare data for factors comparison
    # We'll create a transformed view showing selected factors
    factors_chart = alt.Chart(data).transform_fold(
        ['GDP_per_Capita', 'Social_Support', 'Healthy_Life_Expectancy', 'Freedom'],
        as_=['Factor', 'Value']
    ).mark_bar().encode(
        x=alt.X('mean(Value):Q',
                title='Average Value (normalized)',
                scale=alt.Scale(domain=[0, 1])),
        y=alt.Y('Factor:N',
                title='Happiness Factor',
                sort='-x'),
        color=alt.condition(
            brush | click,
            alt.Color('Factor:N',
                     scale=alt.Scale(scheme='category20'),
                     legend=alt.Legend(title='Factor')),
            alt.value('lightgray')
        ),
        opacity=alt.condition(brush | click, alt.value(0.9), alt.value(0.2)),
        tooltip=[
            alt.Tooltip('Factor:N', title='Factor'),
            alt.Tooltip('mean(Value):Q', title='Average Value', format='.3f')
        ]
    ).properties(
        width=450,
        height=300,
        title='Average Happiness Factors (Filtered by Selection)'
    )

    # ===== Combine all views =====
    # Top row: heatmap and boxplot side by side
    top_row = heatmap | boxplot

    # Bottom row: scatter and factors bar
    bottom_row = scatter_with_reg | factors_chart

    # Final composition
    final_chart = alt.vconcat(
        top_row,
        bottom_row
    ).properties(
        title=alt.TitleParams(
            text='System B: Multi-View Distribution and Pattern Analysis',
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
    print("Creating System B...")

    # Create the visualization
    chart = create_system_b()

    # Save as HTML
    chart.save('system_b_visualization.html')
    print("✓ System B visualization saved as 'system_b_visualization.html'")

    # Also save as JSON spec
    chart.save('system_b_spec.json')
    print("✓ System B specification saved as 'system_b_spec.json'")

    print("\nSystem B Features:")
    print("- Heatmap showing temporal patterns across regions")
    print("- Box plots for distribution analysis")
    print("- Scatter plot with dynamic regression line")
    print("- Grouped bar chart showing multiple factors")
    print("- Bidirectional brushing and linking across all views")
    print("- Point selection (click) + Interval selection (brush)")

if __name__ == "__main__":
    main()
