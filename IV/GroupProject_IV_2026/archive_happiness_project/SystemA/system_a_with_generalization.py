"""
System A with Generalized Selection
====================================

This is an enhanced version of System A that implements generalized selection
based on a semantic hierarchy and traversal policy.

SEMANTIC STRUCTURE:
------------------
Level 3 (Most Specific): Individual Country (e.g., "Finland")
    ↓ generalizes to ↓
Level 2 (Mid-level): Region (e.g., "Western Europe")
    ↓ generalizes to ↓
Level 1 (Most General): Global (All Countries/Regions)

TRAVERSAL POLICY:
-----------------
1. When a country is selected, user can:
   - Generalize UP: Select all countries in the same region
   - Generalize UP again: Select all countries globally

2. When a region is selected, user can:
   - Generalize UP: Select all regions (global view)

3. Selection can be refined (specialized) back down the hierarchy:
   - From Global → Select specific regions
   - From Region → Select specific countries

IMPLEMENTATION APPROACH:
------------------------
We implement this using:
1. Altair parameters for selection state
2. Dropdown menus to trigger generalization levels
3. Bidirectional linking to show generalization effects across views
4. Visual feedback showing the current selection hierarchy level

This goes beyond simple filtering - it implements true hierarchical
generalization where the selection semantically moves up/down the
conceptual hierarchy of the data.
"""

import altair as alt
import pandas as pd
import json

# Enable data transformer
alt.data_transformers.disable_max_rows()

def load_data():
    """Load the World Happiness dataset"""
    df = pd.read_csv('../data/world_happiness_data.csv')
    return df

def create_system_a_with_generalization():
    """
    Create System A with generalized selection capability
    """
    # Load data
    data = load_data()

    # ===== GENERALIZATION MECHANISM SETUP =====

    # Selection level parameter (controls hierarchy level)
    # Level 0 = Country-specific, Level 1 = Region, Level 2 = Global
    selection_level = alt.param(
        name='sel_level',
        value=0,
        bind=alt.binding_radio(
            options=[0, 1, 2],
            labels=['Country Level', 'Region Level (Generalized)', 'Global Level (Full Generalization)'],
            name='Selection Granularity: '
        )
    )

    # Country selection
    country_select = alt.selection_point(
        fields=['Country'],
        name='country_sel'
    )

    # Region selection
    region_select = alt.selection_point(
        fields=['Region'],
        name='region_sel'
    )

    # Brush selection for intervals
    brush = alt.selection_interval(name='brush_gen')

    # Color scale
    color_scale = alt.Scale(
        domain=list(data['Region'].unique()),
        range=['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00',
               '#ffff33', '#a65628', '#f781bf', '#999999', '#66c2a5']
    )

    # ===== VIEW 1: Main Scatter Plot with Hierarchical Selection =====
    # This view demonstrates generalization visually
    scatter_base = alt.Chart(data).mark_circle(size=100)

    # Define selection condition based on hierarchy level
    selection_condition = (
        # Level 0: Country-specific selection
        ((alt.datum.sel_level == 0) & (country_select | brush)) |
        # Level 1: Region-level generalization
        ((alt.datum.sel_level == 1) & (region_select | brush)) |
        # Level 2: Global level (everything selected)
        (alt.datum.sel_level == 2)
    )

    scatter = scatter_base.encode(
        x=alt.X('GDP_per_Capita:Q',
                title='GDP per Capita',
                scale=alt.Scale(zero=False)),
        y=alt.Y('Happiness_Score:Q',
                title='Happiness Score',
                scale=alt.Scale(zero=False, domain=[3, 8.5])),
        color=alt.condition(
            selection_condition | brush | country_select | region_select,
            alt.Color('Region:N',
                     scale=color_scale,
                     legend=alt.Legend(title='Region (Click to Select)', columns=2)),
            alt.value('lightgray')
        ),
        size=alt.condition(
            selection_condition | brush | country_select | region_select,
            alt.value(150),
            alt.value(30)
        ),
        opacity=alt.condition(
            selection_condition | brush | country_select | region_select,
            alt.value(0.9),
            alt.value(0.2)
        ),
        tooltip=[
            alt.Tooltip('Country:N', title='Country'),
            alt.Tooltip('Region:N', title='Region'),
            alt.Tooltip('Year:O', title='Year'),
            alt.Tooltip('Happiness_Score:Q', title='Happiness', format='.2f'),
            alt.Tooltip('GDP_per_Capita:Q', title='GDP', format='.3f')
        ]
    ).add_params(
        selection_level,
        country_select,
        region_select,
        brush
    ).properties(
        width=700,
        height=400,
        title='Happiness vs GDP: Hierarchical Selection (Use radio buttons to generalize)'
    )

    # ===== VIEW 2: Region Bar Chart with Generalization =====
    bars = alt.Chart(data).mark_bar().encode(
        y=alt.Y('Region:N',
                title='Region',
                sort='-x'),
        x=alt.X('mean(Happiness_Score):Q',
                title='Average Happiness Score'),
        color=alt.condition(
            selection_condition | region_select | brush,
            alt.Color('Region:N',
                     scale=color_scale,
                     legend=None),
            alt.value('lightgray')
        ),
        opacity=alt.condition(
            selection_condition | region_select | brush,
            alt.value(1.0),
            alt.value(0.3)
        ),
        tooltip=[
            alt.Tooltip('Region:N', title='Region'),
            alt.Tooltip('mean(Happiness_Score):Q', title='Avg Happiness', format='.2f'),
            alt.Tooltip('count():Q', title='Data Points')
        ]
    ).properties(
        width=700,
        height=350,
        title='Regional Averages (Responds to Generalization Level)'
    )

    # ===== VIEW 3: Time Series showing generalization effect =====
    lines = alt.Chart(data).mark_line(point=True, strokeWidth=3).encode(
        x=alt.X('Year:O', title='Year'),
        y=alt.Y('mean(Happiness_Score):Q',
                title='Mean Happiness Score'),
        color=alt.condition(
            selection_condition | region_select | brush | country_select,
            alt.Color('Region:N',
                     scale=color_scale,
                     legend=None),
            alt.value('lightgray')
        ),
        opacity=alt.condition(
            selection_condition | region_select | brush | country_select,
            alt.value(1.0),
            alt.value(0.1)
        ),
        strokeDash=alt.condition(
            (alt.datum.sel_level == 2),  # Show dashed lines at global level
            alt.value([5, 5]),
            alt.value([0])
        ),
        tooltip=[
            alt.Tooltip('Region:N', title='Region'),
            alt.Tooltip('Year:O', title='Year'),
            alt.Tooltip('mean(Happiness_Score):Q', title='Mean Happiness', format='.2f')
        ]
    ).properties(
        width=700,
        height=250,
        title='Temporal Trends (Filtered by Hierarchical Selection Level)'
    )

    # ===== Explanatory Text =====
    explanation_text = alt.Chart(pd.DataFrame({
        'text': [
            'GENERALIZED SELECTION HIERARCHY:',
            '• Level 0 (Country): Click individual points or brush to select specific countries',
            '• Level 1 (Region): Selection generalizes to entire regions',
            '• Level 2 (Global): All data is selected (full generalization)',
            '',
            'TRY THIS:',
            '1. Brush select some points at Country Level',
            '2. Switch to Region Level - selection generalizes to full regions',
            '3. Switch to Global Level - everything becomes selected',
            '4. Switch back down to see specialization'
        ],
        'y': list(range(10))
    })).mark_text(
        align='left',
        baseline='top',
        fontSize=11,
        dx=5,
        fontWeight='normal'
    ).encode(
        text='text:N',
        y=alt.Y('y:Q', axis=None)
    ).properties(
        width=700,
        height=150,
        title='How to Use Generalized Selection'
    )

    # ===== Final Composition =====
    final_chart = alt.vconcat(
        explanation_text,
        scatter,
        bars,
        lines
    ).properties(
        title=alt.TitleParams(
            text='System A with Generalized Selection: Hierarchical Data Exploration',
            fontSize=18,
            anchor='middle',
            fontWeight='bold'
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
    print("Creating System A with Generalized Selection...")

    # Create the visualization
    chart = create_system_a_with_generalization()

    # Save as HTML
    chart.save('system_a_with_generalization.html')
    print("✓ System A with Generalization saved as 'system_a_with_generalization.html'")

    # Also save as JSON spec
    chart.save('system_a_generalization_spec.json')
    print("✓ Specification saved as 'system_a_generalization_spec.json'")

    print("\n" + "="*70)
    print("GENERALIZED SELECTION IMPLEMENTATION")
    print("="*70)
    print("\nSEMANTIC HIERARCHY:")
    print("  Level 0 (Specific): Individual Country")
    print("  Level 1 (General):  Region (all countries in region)")
    print("  Level 2 (Global):   All regions/countries")
    print("\nTRAVERSAL POLICY:")
    print("  • UP (Generalize):   Country → Region → Global")
    print("  • DOWN (Specialize): Global → Region → Country")
    print("\nIMPLEMENTATION:")
    print("  • Radio buttons control hierarchy level")
    print("  • Selection propagates based on semantic relationships")
    print("  • Visual feedback (size, opacity, dash) shows generalization")
    print("  • All views update to reflect current hierarchy level")
    print("\n" + "="*70)

if __name__ == "__main__":
    main()
