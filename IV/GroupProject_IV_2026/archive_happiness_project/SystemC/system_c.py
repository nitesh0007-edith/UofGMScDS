"""
System C: Faceted Views + Strip Plot + Parallel Coordinates with Linking
==========================================================================

Design: This system uses faceting and alternative mark types to explore
patterns across multiple dimensions simultaneously.

Views:
- View 1: Faceted scatter plots (small multiples by region)
- View 2: Strip plot showing individual country rankings
- View 3: Bubble chart with multiple encodings
- View 4: Histogram grid showing distributions

Interaction: Bidirectional brushing and linking with dropdown filters
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

def create_system_c():
    """
    Create System C with multiple linked views
    """
    # Load data
    data = load_data()

    # Filter to most recent year for some views to reduce complexity
    data_recent = data[data['Year'] == data['Year'].max()].copy()

    # Create shared selections
    brush = alt.selection_interval(name='brush_c')
    hover = alt.selection_point(on='mouseover', fields=['Country'], name='hover')

    # Create dropdown selections for interactivity
    region_dropdown = alt.binding_select(
        options=[None] + sorted(data['Region'].unique().tolist()),
        name='Filter by Region: '
    )
    region_select = alt.selection_point(
        fields=['Region'],
        bind=region_dropdown,
        name='region_dropdown'
    )

    year_slider = alt.binding_range(
        min=int(data['Year'].min()),
        max=int(data['Year'].max()),
        step=1,
        name='Year: '
    )
    year_select = alt.param(
        name='year_slider',
        value=int(data['Year'].max()),
        bind=year_slider
    )

    # Color scale
    color_scale = alt.Scale(
        domain=list(data['Region'].unique()),
        range=['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00',
               '#ffff33', '#a65628', '#f781bf', '#999999', '#66c2a5']
    )

    # ===== VIEW 1: Faceted Scatter Plots (GDP vs Life Expectancy by Region) =====
    faceted = alt.Chart(data).mark_circle(size=60).encode(
        x=alt.X('GDP_per_Capita:Q',
                title='GDP per Capita',
                scale=alt.Scale(zero=False)),
        y=alt.Y('Healthy_Life_Expectancy:Q',
                title='Life Expectancy',
                scale=alt.Scale(zero=False)),
        color=alt.condition(
            brush | hover | region_select,
            alt.Color('Region:N',
                     scale=color_scale,
                     legend=None),
            alt.value('lightgray')
        ),
        opacity=alt.condition(
            brush | hover | region_select,
            alt.value(0.8),
            alt.value(0.2)
        ),
        tooltip=[
            alt.Tooltip('Country:N', title='Country'),
            alt.Tooltip('Year:O', title='Year'),
            alt.Tooltip('Happiness_Score:Q', title='Happiness', format='.2f'),
            alt.Tooltip('GDP_per_Capita:Q', title='GDP', format='.3f'),
            alt.Tooltip('Healthy_Life_Expectancy:Q', title='Life Exp', format='.3f')
        ]
    ).add_params(
        brush,
        hover,
        region_select,
        year_select
    ).transform_filter(
        alt.datum.Year >= year_select
    ).properties(
        width=200,
        height=150,
        title='GDP vs Life Expectancy'
    ).facet(
        column=alt.Column('Region:N',
                         title='Region',
                         header=alt.Header(labelAngle=-45, labelAlign='right')),
        columns=5
    )

    # ===== VIEW 2: Strip Plot (Country Rankings) =====
    strip = alt.Chart(data_recent).mark_tick(thickness=3).encode(
        x=alt.X('Happiness_Score:Q',
                title='Happiness Score',
                scale=alt.Scale(domain=[3, 8.5])),
        y=alt.Y('Region:N',
                title='Region',
                sort='-x'),
        color=alt.condition(
            brush | region_select | hover,
            alt.Color('Region:N',
                     scale=color_scale,
                     legend=alt.Legend(title='Region', columns=2)),
            alt.value('lightgray')
        ),
        opacity=alt.condition(
            brush | region_select | hover,
            alt.value(0.9),
            alt.value(0.2)
        ),
        tooltip=[
            alt.Tooltip('Country:N', title='Country'),
            alt.Tooltip('Region:N', title='Region'),
            alt.Tooltip('Happiness_Score:Q', title='Happiness', format='.2f'),
            alt.Tooltip('GDP_per_Capita:Q', title='GDP', format='.3f')
        ]
    ).properties(
        width=850,
        height=300,
        title=f'Country-Level Happiness Distribution by Region (Year {data["Year"].max()})'
    )

    # ===== VIEW 3: Bubble Chart (Multiple Dimensions) =====
    bubble = alt.Chart(data).mark_circle().encode(
        x=alt.X('Social_Support:Q',
                title='Social Support',
                scale=alt.Scale(zero=False)),
        y=alt.Y('Freedom:Q',
                title='Freedom',
                scale=alt.Scale(zero=False)),
        size=alt.Size('Happiness_Score:Q',
                     scale=alt.Scale(range=[50, 500]),
                     legend=alt.Legend(title='Happiness Score')),
        color=alt.condition(
            brush | region_select | hover,
            alt.Color('Region:N',
                     scale=color_scale,
                     legend=None),
            alt.value('lightgray')
        ),
        opacity=alt.condition(
            brush | region_select | hover,
            alt.value(0.6),
            alt.value(0.1)
        ),
        tooltip=[
            alt.Tooltip('Country:N', title='Country'),
            alt.Tooltip('Region:N', title='Region'),
            alt.Tooltip('Year:O', title='Year'),
            alt.Tooltip('Happiness_Score:Q', title='Happiness', format='.2f'),
            alt.Tooltip('Social_Support:Q', title='Social Support', format='.3f'),
            alt.Tooltip('Freedom:Q', title='Freedom', format='.3f')
        ]
    ).transform_filter(
        alt.datum.Year >= year_select
    ).properties(
        width=400,
        height=300,
        title='Social Support vs Freedom (Size = Happiness)'
    )

    # ===== VIEW 4: Histogram Grid =====
    histogram = alt.Chart(data).mark_bar().encode(
        x=alt.X('Happiness_Score:Q',
                bin=alt.Bin(maxbins=20),
                title='Happiness Score'),
        y=alt.Y('count():Q',
                title='Count'),
        color=alt.condition(
            brush | region_select,
            alt.value('steelblue'),
            alt.value('lightgray')
        ),
        opacity=alt.condition(
            brush | region_select,
            alt.value(0.8),
            alt.value(0.2)
        ),
        tooltip=[
            alt.Tooltip('count():Q', title='Count'),
            alt.Tooltip('Happiness_Score:Q', bin=True, title='Happiness Range')
        ]
    ).transform_filter(
        alt.datum.Year >= year_select
    ).properties(
        width=400,
        height=300,
        title='Distribution of Happiness Scores'
    )

    # ===== Combine all views =====
    # Top: faceted scatter plots
    top = faceted

    # Middle: strip plot (full width)
    middle = strip

    # Bottom: bubble and histogram side by side
    bottom = bubble | histogram

    # Final composition
    final_chart = alt.vconcat(
        top,
        middle,
        bottom
    ).properties(
        title=alt.TitleParams(
            text='System C: Multi-Faceted Exploration with Interactive Filters',
            fontSize=18,
            anchor='middle'
        )
    ).configure_axis(
        labelFontSize=10,
        titleFontSize=11
    ).configure_title(
        fontSize=13,
        anchor='start'
    ).configure_legend(
        titleFontSize=11,
        labelFontSize=10
    ).configure_header(
        labelFontSize=9
    )

    return final_chart

def main():
    """Main function to create and save the visualization"""
    print("Creating System C...")

    # Create the visualization
    chart = create_system_c()

    # Save as HTML
    chart.save('system_c_visualization.html')
    print("✓ System C visualization saved as 'system_c_visualization.html'")

    # Also save as JSON spec
    chart.save('system_c_spec.json')
    print("✓ System C specification saved as 'system_c_spec.json'")

    print("\nSystem C Features:")
    print("- Faceted small multiples showing patterns by region")
    print("- Strip plots for detailed country-level analysis")
    print("- Bubble chart with multiple visual encodings")
    print("- Histogram showing distributions")
    print("- Dropdown filter for region selection")
    print("- Slider for year filtering")
    print("- Bidirectional brushing and linking")
    print("- Hover interactions for detailed exploration")

if __name__ == "__main__":
    main()
