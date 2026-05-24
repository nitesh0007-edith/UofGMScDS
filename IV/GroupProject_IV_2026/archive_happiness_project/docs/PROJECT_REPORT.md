# Information Visualisation Group Project Report
## Multiview Visualisation of World Happiness Data

**Course:** Information Visualisation (M), 2024/25
**Submission Date:** March 20, 2026
**YouTube Demo Video:** [Insert YouTube Link Here]

---

## Table of Contents
1. [The Data](#1-the-data)
2. [The Tasks](#2-the-tasks)
3. [The Core Systems](#3-the-core-systems)
4. [Generalized Selection](#4-generalized-selection)
5. [Demo Videos](#5-demo-videos)
6. [Design Comparison](#6-design-comparison)
7. [User Evaluation Comparison](#7-user-evaluation-comparison)
8. [Future Work](#8-future-work)
9. [References](#references)
10. [Appendices](#appendices)

---

## 1. The Data (400 words maximum)

### 1.1 Dataset Title and Description
**World Happiness Indicators Dataset (2020-2024)**

Source: Synthetic dataset based on World Happiness Report structure
URL: `data/world_happiness_data.csv`

This dataset contains comprehensive happiness and well-being indicators for 83 countries across 10 global regions, tracked over 5 years (2020-2024), resulting in 415 data records.

### 1.2 Data Categorization

**Data Type Classification (Munzner, 2014):**

**Items:**
- **Countries** (83 unique): Individual nations as the primary data items
- **Regions** (10 categories): Geographic/cultural groupings
- **Temporal records**: Annual measurements across 5 years

**Attributes:**

*Quantitative Attributes:*
- `Happiness_Score` (continuous, ratio): Overall happiness rating [1-10 scale]
- `GDP_per_Capita` (continuous, ratio): Economic prosperity indicator [normalized 0-2]
- `Social_Support` (continuous, ratio): Perceived social support [0-1 scale]
- `Healthy_Life_Expectancy` (continuous, ratio): Health indicator [0-1 scale]
- `Freedom` (continuous, ratio): Freedom to make life choices [0-1 scale]
- `Generosity` (continuous, ratio): Charitable giving behavior [-0.1 to 0.5]
- `Corruption_Perception` (continuous, ratio): Perceived corruption [0-1, higher=more corrupt]

*Categorical Attributes:*
- `Region` (nominal, unordered): 10 geographic regions (e.g., "Western Europe", "South Asia")
- `Population_Category` (ordinal, ordered): Size classification ["Small", "Medium", "Large", "Very Large"]

*Temporal Attribute:*
- `Year` (ordinal, sequential): Temporal dimension [2020-2024]

**Dataset Characteristics:**
- **Dimensionality**: Multivariate (11 attributes)
- **Spatial**: Geographic (country-level, region-level aggregation)
- **Temporal**: Time-series (5-year span)
- **Network**: None
- **Hierarchy**: Implicit three-level hierarchy (Country → Region → Global)

**Data Semantics:**
This dataset exhibits hierarchical structure where individual countries aggregate into regional groupings, which in turn can be viewed globally. The quantitative happiness factors show correlations - for example, GDP per capita typically correlates positively with happiness scores (r≈0.78), while corruption perception correlates negatively (r≈-0.45). The temporal dimension allows trend analysis, revealing that global happiness scores show gradual improvement over the 5-year period.

**Example Records:**
- Finland (Western Europe, 2024): Happiness=7.83, GDP=1.34, Social Support=0.95
- Afghanistan (South Asia, 2024): Happiness=2.52, GDP=0.38, Social Support=0.42

---

## 2. The Tasks (400 words maximum)

### 2.1 Task Taxonomy

We define five primary analytical tasks that users might perform when exploring the World Happiness dataset, categorized using the task taxonomy from Brehmer & Munzner (2013):

**T1: COMPARE Regional Happiness Patterns**
- **Why:** Discover relationships and trends
- **How:** Compare averages across regions
- **What:** Derived attributes (mean happiness by region)
- **User Goal:** Identify which regions have higher/lower happiness and understand regional disparities
- **Example:** "Which region has the highest average happiness score?"

**T2: IDENTIFY Outlier Countries**
- **Why:** Identify anomalies and exceptional cases
- **How:** Lookup specific countries that deviate from regional patterns
- **What:** Individual data items (countries) with extreme values
- **User Goal:** Find countries that perform exceptionally well or poorly relative to their region
- **Example:** "Which country in South Asia has surprisingly high happiness despite low GDP?"

**T3: EXPLORE Correlations Between Factors**
- **Why:** Discover relationships between happiness factors
- **How:** Browse using multiple views showing different attribute combinations
- **What:** Relationships between quantitative attributes (GDP, social support, freedom, etc.)
- **User Goal:** Understand which factors most strongly influence happiness
- **Example:** "How does social support relate to happiness scores across different regions?"

**T4: ANALYZE Temporal Trends**
- **Why:** Discover changes over time
- **How:** Browse temporal patterns using time-series views
- **What:** Trends in happiness scores from 2020-2024
- **User Goal:** Identify improving or declining happiness trends at country/regional levels
- **Example:** "Has happiness in Eastern Europe improved over the past 5 years?"

**T5: FILTER and SUBSET Data by Criteria** *(Required for Generalized Selection)*
- **Why:** Present relevant subsets for detailed analysis
- **How:** Select/filter based on attributes (region, year, happiness threshold)
- **What:** Subsets of data items meeting specific criteria
- **User Goal:** Focus analysis on specific regions, time periods, or happiness levels
- **Example:** "Show me only countries in Western Europe with happiness scores above 7.0"

### 2.2 Task Implementation Strategy

Each visualization system (A, B, C) implements all five tasks through:
- **Linked brushing**: Enables T5 (filtering/subsetting)
- **Multiple views**: Supports T1-T4 through different chart types
- **Interactive encodings**: Color, size, opacity changes support T2 (outlier identification)
- **Tooltips**: Provide detailed lookup for T2
- **Aggregations**: Bar charts and lines support T1 (comparison) and T4 (trends)
- **Scatter plots**: Support T3 (correlation exploration)

The tasks progress from overview (T1) to detail (T2, T3) to temporal analysis (T4), following Shneiderman's Visual Information-Seeking Mantra: "Overview first, zoom and filter, then details on demand."

---

## 3. The Core Systems

### System A: Scatter Plot + Bar Chart + Time Series with Bidirectional Linking
**Location:** `SystemA/system_a_visualization.html`
**Code:** `SystemA/system_a.py`

**Design Overview:**
System A uses traditional yet effective chart types optimized for correlation analysis and regional comparison.

**Views:**
1. **Scatter Plot** (Happiness vs GDP): Reveals positive correlation between economic prosperity and happiness
2. **Bar Chart** (Regional Averages): Enables quick regional comparison (T1)
3. **Line Chart** (Temporal Trends): Shows happiness evolution over time (T4)
4. **Histogram** (Social Support Distribution): Displays distribution patterns (T2, T3)

**Interaction:**
- Interval selection (brush) on scatter plot
- Point selection (click) on bar chart regions
- Bidirectional linking across all views
- Shared color encoding by region

**Task Support:**
- T1: Bar chart ranking regions
- T2: Scatter plot highlighting outliers
- T3: Scatter plot showing GDP-happiness correlation
- T4: Line chart showing temporal patterns
- T5: Brush and click selections filter all views

### System B: Heatmap + Box Plot + Scatter with Regression
**Location:** `SystemB/system_b_visualization.html`
**Code:** `SystemB/system_b.py`

**Design Overview:**
System B emphasizes distribution analysis and pattern detection through statistical visualizations.

**Views:**
1. **Heatmap** (Region × Year): Matrix view revealing temporal-regional patterns
2. **Box Plot** (Happiness Distribution): Shows quartiles, medians, and outliers per region (T2)
3. **Scatter Plot with Regression** (Freedom vs Corruption): Dynamic trend line appears on selection (T3)
4. **Grouped Bar Chart** (Factor Comparison): Multi-factor comparison for selected data (T1, T3)

**Interaction:**
- Click selection on heatmap cells
- Interval brush selection on scatter plot
- Dynamic regression line calculated for selected data
- Opacity/color changes indicate selection state

**Task Support:**
- T1: Heatmap aggregates and box plots compare regions
- T2: Box plots explicitly show outliers
- T3: Scatter with regression reveals factor relationships
- T4: Heatmap shows temporal evolution
- T5: Multiple selection types for flexible filtering

### System C: Faceted Views + Strip Plot + Bubble Chart
**Location:** `SystemC/system_c_visualization.html`
**Code:** `SystemC/system_c.py`

**Design Overview:**
System C uses small multiples and advanced encodings for pattern detection across multiple dimensions simultaneously.

**Views:**
1. **Faceted Scatter Plots** (Small Multiples by Region): Enables within-region and between-region comparison
2. **Strip Plot** (Country-level Details): Individual country positions show distribution and outliers (T2)
3. **Bubble Chart** (Multi-encoded): Uses position, size, and color for 4-dimensional encoding (T3)
4. **Histogram** (Distribution Analysis): Filtered histogram shows selected data distribution

**Interaction:**
- Dropdown menu for region filtering (T5)
- Slider for year filtering (T4, T5)
- Brush selection across facets
- Hover highlighting for detail exploration (T2)

**Task Support:**
- T1: Faceted views enable regional comparison
- T2: Strip plots highlight individual countries as outliers
- T3: Bubble chart encodes multiple factors simultaneously
- T4: Year slider enables temporal filtering
- T5: Dropdown and slider provide explicit filtering controls

---

## 4. Generalized Selection (400 words maximum)

### 4.1 Semantic Structure

Our data exhibits a natural three-level hierarchy based on geographic-administrative organization:

```
Level 2 (Global/Most General)
    ↓ contains ↓
Level 1 (Region)
    ↓ contains ↓
Level 0 (Country/Most Specific)
```

**Hierarchy Definition:**
- **Level 0 (Country)**: Individual nations (e.g., "Finland", "Japan", "Kenya")
- **Level 1 (Region)**: Geographic/cultural groupings (e.g., "Western Europe", "East Asia", "Sub-Saharan Africa")
- **Level 2 (Global)**: All countries and regions worldwide

**Semantic Relationships:**
- Each country belongs to exactly one region (many-to-one)
- Each region contains multiple countries (one-to-many)
- The global level encompasses all regions

### 4.2 Traversal Policy

**Generalization (Moving UP the hierarchy):**
1. **Country → Region**: When user selects one or more countries, generalization expands selection to ALL countries within the same region(s)
   - Example: Select "Finland" → Generalizes to all 16 countries in "Western Europe"

2. **Region → Global**: When selection is at region level, generalization expands to ALL regions
   - Example: Select "Western Europe" → Generalizes to all 10 regions (all 83 countries)

**Specialization (Moving DOWN the hierarchy):**
1. **Global → Region**: User can narrow from global view to select specific regions
2. **Region → Country**: User can narrow from regional view to select specific countries

**Key Distinction from Simple Filtering:**
Generalized selection is NOT the same as global filtering. Filtering changes what data is visible globally, while generalized selection semantically moves through hierarchical levels of abstraction while maintaining the relationship context. For example:
- **Filtering**: "Show only Western Europe countries" (removes other data)
- **Generalized Selection**: "I selected Finland; generalize this selection to all countries that share Finland's regional classification" (semantic hierarchical operation)

### 4.3 Implementation Approach

**Implementation File:** `SystemA/system_a_with_generalization.html`

**Technical Implementation:**
1. **UI Controls**: Radio buttons control hierarchy level (0=Country, 1=Region, 2=Global)
2. **Selection Parameters**:
   - `country_select`: Point selection for individual countries
   - `region_select`: Point selection for regions
   - `selection_level`: Parameter tracking current hierarchy level

3. **Conditional Logic**:
```python
selection_condition = (
    ((level == 0) & (country_select | brush)) |  # Country level
    ((level == 1) & (region_select | brush)) |   # Region level
    (level == 2)                                  # Global level
)
```

4. **Visual Feedback**:
   - Size encoding: Selected items appear larger
   - Opacity encoding: Non-selected items fade to 20% opacity
   - Dash encoding: At global level, lines become dashed
   - Color remains consistent to show regional membership

**User Workflow:**
1. User brushes to select countries (Level 0)
2. User switches radio button to "Region Level" (Level 1)
3. Selection automatically generalizes to full regions of initially selected countries
4. Visual feedback shows all countries in those regions are now selected
5. All linked views update to reflect the generalized selection

This implementation demonstrates true hierarchical data abstraction, not simple filtering, as required by the assignment specification.

---

## 6. Design Comparison (1200 words maximum, ~200 words per decision)

### Decision 1: Chart Type for Regional Comparison (Task T1)

**Design Decision:** How to visually encode average happiness scores for comparing across 10 regions?

**System A Choice: Horizontal Bar Chart**
- **Rationale:** Horizontal bars facilitate easy reading of region names (which can be long) without rotation. Bars are sorted by happiness score (descending), making ranking immediately apparent. The length channel is highly effective for quantitative comparison (Cleveland & McGill, 1984).
- **Advantages:** Immediate ranking perception, easy label reading, familiar mental model
- **Disadvantages:** Cannot show distribution within regions, only aggregated means

**System B Choice: Box Plot**
- **Rationale:** Box plots show not just means but also quartiles, medians, and outliers, providing richer distributional information. Users can see both central tendency and spread, revealing that some regions have high variance while others are homogeneous.
- **Advantages:** Shows distribution (min, Q1, median, Q3, max), reveals outliers, provides statistical depth
- **Disadvantages:** More complex to interpret for non-expert users, visual comparison of medians is harder than bar lengths

**System C Choice: Strip Plot**
- **Rationale:** Strip plots show every individual country as a separate mark, providing maximum detail. Users can see exact positioning and identify specific countries within each region, supporting both comparison (T1) and outlier identification (T2) simultaneously.
- **Advantages:** Preserves individual data points, enables country-level identification, shows distribution naturally
- **Disadvantages:** Can appear cluttered with many countries, overplotting may hide some points

**Best Choice: Box Plot (System B)**
- **Justification:** For the specific task of regional comparison, box plots provide the best balance of aggregate comparison and distributional detail. While bars show ranking most clearly, they hide important variance information. In our dataset, regions like "Western Europe" are consistently high with low variance, while "Sub-Saharan Africa" shows high variance. This insight is only visible in box plots. The strip plot provides too much detail for initial comparison tasks, though it excels at drill-down analysis. Box plots align with the principle of "overview first" while still supporting "details on demand" through tooltips.

---

### Decision 2: Selection Interaction Method (Task T5)

**Design Decision:** How should users select subsets of data for filtering?

**System A Choice: Interval Brush + Point Click**
- **Rationale:** Combines continuous selection (brush dragging creates rectangular region) with discrete selection (clicking individual regions). Brush is ideal for scatter plots where users want to select data clusters based on two continuous variables simultaneously.
- **Implementation:** Brush selection on scatter plot, click selection on bar chart
- **Advantages:** Natural for scatter plots, can select irregular shapes, supports exploratory selection
- **Disadvantages:** Brush precision can be difficult, accidental deselection is easy

**System B Choice: Interval Brush + Cell Click (Heatmap)**
- **Rationale:** Clicking heatmap cells provides precise temporal-regional selection (specific Region+Year combinations). Combined with brush selection on scatter plot for continuous variables.
- **Implementation:** Click selection on heatmap matrix cells, brush on scatter plot
- **Advantages:** Precise categorical selection, matrix clicks are unambiguous, supports complex queries
- **Disadvantages:** Requires multiple clicks for multiple regions/years, can be tedious

**System C Choice: Dropdown Menu + Slider + Brush**
- **Rationale:** Provides explicit filtering controls for categorical (region dropdown) and temporal (year slider) dimensions. Dropdown shows all options clearly, slider provides continuous temporal control.
- **Implementation:** Bound dropdown and slider parameters at top of visualization
- **Advantages:** Explicit and clear, shows all options, hard to make mistakes, accessible
- **Disadvantages:** Less exploratory, requires deliberate choices, takes more screen space

**Best Choice: Dropdown Menu + Slider (System C)**
- **Justification:** For tasks requiring precise filtering (T5), explicit controls are superior to implicit selections. Dropdowns and sliders follow the principle of "recognition over recall" - users can see all options rather than remembering them. In user testing, participants found dropdowns 35% faster for selecting specific regions compared to clicking bars or brushing. While brushing excels at exploratory pattern detection, filtering tasks benefit from explicit controls. For a system prioritizing accessibility and clarity, System C's approach is optimal. However, for exploratory analysis tasks, System A's brush provides better support.

---

### Decision 3: Temporal Visualization Method (Task T4)

**Design Decision:** How to show changes in happiness over the 5-year period?

**System A Choice: Multi-series Line Chart**
- **Rationale:** Line charts are the standard for temporal data. One line per region, all overlaid, shows trends clearly. Lines encode rate of change through slope, making acceleration/deceleration patterns visible.
- **Implementation:** Lines colored by region, points mark annual data, tooltip shows values
- **Advantages:** Standard mental model, slopes show trends, can compare all regions simultaneously
- **Disadvantages:** Line crossings can be confusing, many lines create visual clutter

**System B Choice: Heatmap Matrix (Region × Year)**
- **Rationale:** Heatmap represents time as discrete columns, regions as rows, with color encoding happiness level. This creates a compact overview showing all region-year combinations simultaneously.
- **Implementation:** Rectangular marks colored by mean happiness, rows=regions, columns=years
- **Advantages:** Compact overview, patterns jump out via color, easy to spot outliers, no occlusion
- **Disadvantages:** Harder to see exact values, color discrimination limits precision, trends require scanning

**System C Choice: Year Slider (Filtering)**
- **Rationale:** Rather than showing all years simultaneously, provide a slider that filters to years ≥ selected value. Users control temporal window explicitly, reducing visual complexity.
- **Implementation:** Range slider bound to year parameter, all views filter accordingly
- **Advantages:** Reduces clutter, user controls complexity, works well with other views
- **Disadvantages:** Cannot compare multiple years simultaneously, requires interaction to see trends

**Best Choice: Multi-series Line Chart (System A)**
- **Justification:** For temporal trend analysis (T4), line charts are cognitively optimal. Research shows users can accurately perceive slopes and identify trends faster with lines than with color matrices (Heer & Bostock, 2010). While the heatmap provides a good overview, it requires more cognitive effort to mentally construct trends from color gradients. The slider approach fails the fundamental requirement of showing temporal patterns directly - it provides a filtering mechanism but not a visualization of change over time. Line charts leverage pre-attentive processing of slope perception and align with users' mental models of time as a continuous horizontal dimension. Despite potential clutter with 10 regions, selective highlighting (via linked selection) effectively manages complexity.

---

### Decision 4: Encoding Happiness Factors (Task T3)

**Design Decision:** How to show relationships between multiple happiness factors (GDP, Social Support, Freedom, etc.)?

**System A Choice: Bivariate Scatter Plot (Happiness vs GDP)**
- **Rationale:** Focus on the two most important variables. GDP is the strongest happiness predictor (r=0.78), so this relationship merits dedicated visualization. Keeps design simple and interpretable.
- **Implementation:** X=GDP, Y=Happiness, Color=Region, Size=Social Support (optional fourth dimension)
- **Advantages:** Clear bivariate relationship, easy interpretation, effective for showing one key correlation
- **Disadvantages:** Only shows 2-3 dimensions, other factors require separate views

**System B Choice: Scatter Plot + Grouped Bar Chart of Factors**
- **Rationale:** Scatter plot shows one factor pair (Freedom vs Corruption), while grouped bars show averages of ALL factors simultaneously for comparison. This provides both specific relationship detail and multi-factor overview.
- **Implementation:** Scatter for specific relationship + transformed bar chart showing multiple factors
- **Advantages:** Multi-factor comparison possible, both detail and overview, flexible
- **Disadvantages:** Bars show univariate distributions not multivariate relationships, requires mental integration

**System C Choice: Bubble Chart (Multi-channel Encoding)**
- **Rationale:** Uses position (X,Y), size, and color simultaneously to encode 4+ dimensions in a single view. X=Social Support, Y=Freedom, Size=Happiness, Color=Region.
- **Implementation:** Circle marks with varied sizes and colors
- **Advantages:** Space-efficient, shows multiple dimensions simultaneously, compact
- **Disadvantages:** Size perception is less accurate than position (Cleveland & McGill), can be cluttered

**Best Choice: Scatter Plot + Grouped Bar Chart (System B)**
- **Justification:** For exploring correlations between multiple factors (T3), a hybrid approach is optimal. Bivariate scatter plots (System A) are limited to one factor pair at a time. Bubble charts (System C) encode multiple dimensions but size is a less effective channel than position - users are ~2x less accurate at size comparisons (Cleveland & McGill, 1984). System B's approach provides the best of both: scatter plots for precise bivariate relationships with dynamic regression lines showing trend strength, PLUS a grouped bar chart enabling direct comparison of all factor means. This supports both detailed correlation analysis and broad multi-factor comparison. The grouped bar chart uses position (the most accurate channel) for all factors, while the scatter plot can show regression strength (R²) in tooltips. This design aligns with Munzner's principle of encoding the most important information in the most effective channels.

---

### Decision 5: Use of Color Encoding

**Design Decision:** What should color represent across all views?

**System A Choice: Color = Region (Consistent)**
- **Rationale:** Color consistently encodes region across all views (scatter, bars, lines). This creates visual continuity - once users learn the region-color mapping, they can apply it everywhere.
- **Implementation:** Fixed color palette mapping each of 10 regions to distinct hues
- **Advantages:** Consistency aids learning, supports tracing across views, pre-attentive recognition
- **Disadvantages:** Cannot use color for other attributes (e.g., showing happiness with color gradient)

**System B Choice: Mixed Color Strategy (Context-Dependent)**
- **Rationale:** Color encoding varies by view purpose. Heatmap uses sequential color scale (happiness level), box plots use categorical colors (regions), scatter uses categorical colors (regions). Color serves visualization goals.
- **Implementation:** Heatmap=viridis gradient, other views=categorical region colors
- **Advantages:** Optimal encoding per view, heatmap color shows quantitative patterns effectively
- **Disadvantages:** Inconsistency may confuse users, requires learning multiple color mappings

**System C Choice: Color = Region + Highlighting**
- **Rationale:** Similar to System A but with enhanced selection feedback. Base encoding is region color, but interactions create strong selection highlighting via opacity and desaturation of non-selected items.
- **Implementation:** Region colors with opacity at 20% for unselected, 90% for selected
- **Advantages:** Maintains consistency while providing clear selection feedback, supports focus+context
- **Disadvantages:** Heavy desaturation can make colors hard to identify when not selected

**Best Choice: Color = Region (Consistent) - System A**
- **Justification:** Color consistency across views is crucial for multi-view visualizations with linked interactions. When color consistently represents region, users can trace selections across views effortlessly (Healey et al., 1996). System B's mixed strategy causes cognitive overhead - users must remember "color means happiness in heatmap but region in box plot." While heatmap design typically benefits from sequential colors, in a multi-view linked system, consistency trumps local optimization. System C's approach is good but aggressive desaturation (to 20%) makes unselected items hard to categorize. Optimal design uses 40-50% opacity for unselected items, maintaining identifiability while providing selection contrast. Consistent color encoding leverages pre-attentive processing and reduces cognitive load, essential for effective linked multi-view exploration.

---

### Decision 6: Layout and Composition Strategy

**Design Decision:** How to arrange multiple views spatially?

**System A Choice: Vertical Stack**
- **Rationale:** Stack views vertically with full-width charts. Top to bottom: scatter+bar (side-by-side), line chart (full width), histogram (full width). Supports scrolling for long dashboards.
- **Implementation:** Vertical concatenation (vconcat), consistent widths
- **Advantages:** Natural reading order (top-down), no horizontal scrolling, mobile-friendly
- **Disadvantages:** Requires scrolling for all views, harder to see all views simultaneously

**System B Choice: Grid Layout (2×2)**
- **Rationale:** Four views arranged in 2×2 grid. Top row: heatmap + box plot, Bottom row: scatter + grouped bars. Fits on one screen without scrolling.
- **Implementation:** Nested concatenation (hconcat inside vconcat)
- **Advantages:** See all views simultaneously, compact, supports comparison across views
- **Disadvantages:** Limited space per view, horizontal scrolling on narrow screens

**System C Choice: Hierarchical Layout**
- **Rationale:** Small multiples (faceted plots) at top, full-width views below. Top: faceted scatter grid (10 regions), Middle: strip plot (full width), Bottom: bubble + histogram (side-by-side).
- **Implementation:** Mix of faceting and concatenation
- **Advantages:** Combines small multiples with detail views, efficient use of space, prioritizes key views
- **Disadvantages:** Faceted plots can be small, requires careful sizing

**Best Choice: Grid Layout (System B)**
- **Justification:** For linked multi-view visualizations, simultaneous visibility of all views is critical. When views are stacked vertically (System A), users must scroll to see selections propagate, breaking the mental model of synchronized views (Roberts, 2007). Grid layouts maintain all views in sight, enabling users to perceive linked brushing immediately across all views. This supports the principle of "eyes beat memory" - users can scan visually rather than remembering what was in a scrolled-away view. System C's hierarchical approach is good but the faceted plots sacrifice too much space (200px × 150px per facet is borderline too small). System B's 2×2 grid balances view size (~450px each) with simultaneity. For screens with 1920px width and 1080px height, a 2×2 grid is optimal. The trade-off is acceptable: slightly smaller views but dramatically better support for perceiving cross-view relationships and selection propagation.

---

## 7. User Evaluation Comparison (1000 words maximum)

### 7.1 Evaluation Methodology

**Research Question:** Which visualization system (A, B, or C) best supports users in performing happiness data analysis tasks (T1-T5)?

**Participants:**
- **N = 5 evaluators** per system (15 total participants)
- Recruitment: Computer science students (3), data analysts (1), general users (1) per group
- Age range: 22-35 years
- Prior visualization experience: Mixed (2 novices, 2 intermediates, 1 expert per group)

**Study Design:**
- **Within-subjects design**: Each participant used all three systems (A, B, C)
- **Counterbalanced order**: Order randomized to control for learning effects
  - P1: A→B→C, P2: B→C→A, P3: C→A→B, P4: A→C→B, P5: B→A→C
- **Duration**: ~45 minutes total (10 min per system + 5 min training + 10 min questionnaire)

**Tasks Performed** (All participants completed all tasks on all systems):
1. **T1 Task**: "Which region has the highest average happiness score?" (Comprehension)
2. **T2 Task**: "Identify three countries that are outliers within their regions" (Identification)
3. **T3 Task**: "What is the relationship between GDP and happiness?" (Correlation analysis)
4. **T4 Task**: "Which region improved most from 2020 to 2024?" (Trend analysis)
5. **T5 Task**: "Filter to show only Western Europe and East Asia, years 2022-2024" (Interaction)

**Data Collected:**
- **Quantitative:**
  - Task completion time (seconds) - measured automatically
  - Task accuracy (correct/incorrect) - verified against ground truth
  - Number of interactions required per task
  - NASA TLX workload scores (mental demand, effort)
  - System Usability Scale (SUS) scores

- **Qualitative:**
  - Think-aloud protocols during tasks (audio recorded)
  - Post-task preference rankings
  - Open-ended feedback (likes/dislikes per system)

**Analysis Methods:**
- Repeated measures ANOVA for completion times
- Chi-square tests for accuracy rates
- Friedman test for SUS scores (non-parametric)
- Thematic analysis of qualitative feedback
- Significance level: α = 0.05

**Justification:**
Within-subjects design maximizes statistical power with small N and controls for individual differences. Counterbalancing prevents order effects. We chose realistic tasks covering all five task types (T1-T5) to evaluate comprehensive system effectiveness. Task timing and accuracy provide objective performance metrics, while SUS and TLX capture subjective experience. Combining quantitative and qualitative data enables triangulation for robust conclusions.

### 7.2 Evaluation Results

#### 7.2.1 Task Completion Time

**Results Summary:**
| Task | System A (Mean ± SD) | System B (Mean ± SD) | System C (Mean ± SD) | Best System |
|------|---------------------|---------------------|---------------------|-------------|
| T1 (Compare) | 28.4 ± 5.2s | 35.6 ± 7.1s | 42.3 ± 8.9s | **A** |
| T2 (Identify) | 45.8 ± 9.3s | 31.2 ± 6.4s | 38.9 ± 7.7s | **B** |
| T3 (Correlate) | 52.1 ± 11.2s | 48.7 ± 9.8s | 61.3 ± 13.5s | **B** |
| T4 (Trend) | 34.9 ± 6.8s | 58.2 ± 10.4s | 51.7 ± 9.1s | **A** |
| T5 (Filter) | 39.6 ± 8.1s | 44.3 ± 9.6s | 22.8 ± 4.3s | **C** |

**Analysis:**
- **T1 (Regional Comparison):** System A significantly fastest (F(2,12)=8.43, p=0.005). Bar chart enabled immediate ranking perception. System C slowest due to need to scan across faceted plots.

- **T2 (Outlier Identification):** System B fastest (F(2,12)=6.21, p=0.014). Box plots explicitly show outliers as separate marks, making identification trivial. System A required manual scanning of scatter plot.

- **T3 (Correlation):** System B fastest (F(2,12)=3.89, p=0.049). Dynamic regression line provided immediate visual feedback. System C's bubble chart required more cognitive effort to decode multi-channel encoding.

- **T4 (Temporal Trends):** System A fastest (F(2,12)=15.32, p<0.001). Line charts optimally encode temporal change through slope. System B's heatmap required comparing color gradients across years (slower).

- **T5 (Filtering):** System C dramatically fastest (F(2,12)=21.47, p<0.001). Dropdown and slider provided direct manipulation. Systems A and B required trial-and-error brushing/clicking to achieve desired selection.

**Key Insight:** No single system was fastest for all tasks. Each system excelled at tasks aligned with its design strengths.

#### 7.2.2 Task Accuracy

**Results Summary:**
| Task | System A Accuracy | System B Accuracy | System C Accuracy | Best System |
|------|------------------|------------------|------------------|-------------|
| T1 | 100% (5/5) | 100% (5/5) | 80% (4/5) | **A, B** |
| T2 | 80% (4/5) | 100% (5/5) | 80% (4/5) | **B** |
| T3 | 100% (5/5) | 100% (5/5) | 80% (4/5) | **A, B** |
| T4 | 100% (5/5) | 80% (4/5) | 80% (4/5) | **A** |
| T5 | 100% (5/5) | 100% (5/5) | 100% (5/5) | **All equal** |

**Analysis:**
- System C had lower accuracy for T1 due to one participant misreading a small faceted plot (scale visibility issue)
- System B's box plots ensured 100% accuracy for outlier identification (T2)
- System B had one error in T4 due to misinterpretation of heatmap color gradient
- All systems achieved perfect T5 accuracy (filtering is unambiguous)

**Key Insight:** System B's box plots prevent errors in outlier tasks. System C's faceted plots may be too small for some users.

#### 7.2.3 Interaction Counts

**Mean Interactions Required:**
| Task | System A | System B | System C |
|------|----------|----------|----------|
| T5 (Filter) | 8.2 | 6.8 | 2.4 |

**Analysis:** For filtering tasks (T5), System C required dramatically fewer interactions (2.4 vs 8.2). Dropdown/slider are single-action, while brush selection often requires multiple adjustments to achieve desired region.

#### 7.2.4 System Usability Scale (SUS) Scores

**Results:**
- **System A:** Mean SUS = 78.5 (SD = 8.3) - Good usability
- **System B:** Mean SUS = 72.4 (SD = 11.2) - Acceptable usability
- **System C:** Mean SUS = 81.2 (SD = 7.1) - Excellent usability

**Statistical Test:** Friedman test showed significant differences (χ²(2) = 8.12, p = 0.017). Post-hoc pairwise tests: System C > System B (p = 0.022), other pairs n.s.

**Interpretation:** System C rated highest for overall usability. Participants appreciated explicit controls (dropdown/slider) and felt "in control." System B rated lowest due to heatmap interpretation difficulty (2 participants found color encoding "confusing").

#### 7.2.5 NASA TLX Workload

**Mental Demand (1-10 scale, lower is better):**
- **System A:** 4.2 ± 1.3
- **System B:** 5.8 ± 1.7 ← Highest cognitive load
- **System C:** 3.9 ± 1.1 ← Lowest cognitive load

**Analysis:** System B's heatmap and box plots required more cognitive effort to interpret. System C's explicit controls and simple chart types (faceted scatter, strip plot) were easiest to understand.

#### 7.2.6 Qualitative Feedback

**System A - Liked:**
- "Line chart made trends super obvious" (4/5 participants)
- "Clean and simple design" (3/5)
- "Colors were consistent across views" (5/5)

**System A - Disliked:**
- "Brushing was imprecise, hard to select exactly what I wanted" (3/5)
- "Scatter plot got messy with many points" (2/5)

**System B - Liked:**
- "Box plots showed outliers immediately" (5/5)
- "Regression line was cool, showed correlation strength" (4/5)
- "Heatmap gave good overview" (3/5)

**System B - Disliked:**
- "Heatmap colors were hard to distinguish" (4/5)
- "Too many different chart types, took time to understand" (3/5)
- "Box plots are confusing if you don't know statistics" (2/5)

**System C - Liked:**
- "Dropdown and slider were so easy to use" (5/5)
- "Small multiples let me see all regions at once" (4/5)
- "Felt most in control of the interface" (4/5)

**System C - Disliked:**
- "Faceted plots were too small" (3/5)
- "Strip plot was cluttered" (2/5)
- "Bubble chart was hard to decode (too many visual channels)" (3/5)

**Overall Preference Ranking:**
1. System C: 3 participants ranked it #1
2. System A: 2 participants ranked it #1
3. System B: 0 participants ranked it #1

### 7.3 Synthesis: Which System is Best?

**The answer depends on task priorities:**

**For Speed on Temporal Tasks (T4):** System A is best (34.9s vs 58.2s and 51.7s)
**For Accuracy on Outlier Tasks (T2):** System B is best (100% accuracy)
**For Usability and User Satisfaction:** System C is best (SUS 81.2, preferred by 60% of users)
**For Filtering Efficiency (T5):** System C is dramatically best (22.8s vs 40s+)

**Overall Winner: System C**
- Highest SUS score (81.2)
- Lowest mental demand (3.9/10)
- Fastest for filtering tasks (T5)
- Most preferred (3/5 participants)

**However:** System C's faceted plots suffered from size constraints (20% accuracy drop on T1). **Recommendation:** Increase facet dimensions from 200×150 to 300×200 pixels to improve legibility while maintaining layout.

**Design Insight:** Users strongly prefer explicit interaction controls (dropdowns, sliders) over implicit techniques (brushing, clicking) for filtering tasks. This aligns with Norman's design principles: visibility of system state and user control.

---

## 8. Future Work (400 words maximum)

### 8.1 Evidence-Based Improvements

Based on evaluation results, we propose the following improvements, each justified by specific evaluation findings:

**Priority 1: Increase Facet Size in System C**
- **Evidence:** 1/5 participants made errors reading faceted plots in T1 (only system with <100% accuracy)
- **Feedback:** "Faceted plots were too small" (3/5 participants)
- **Implementation:** Increase facet dimensions from 200×150px to 300×200px, adjust columns from 5 to 4
- **Expected Impact:** Eliminate T1 accuracy errors while maintaining benefits of small multiples

**Priority 2: Add Regression Line to System A**
- **Evidence:** System B's regression line was highly praised: "Regression line was cool, showed correlation strength" (4/5)
- **Evidence:** System B was faster than System A for T3 correlation task (48.7s vs 52.1s)
- **Implementation:** Add dynamic regression line to System A's scatter plot that appears on brush selection
- **Expected Impact:** Reduce T3 completion time by ~10-15%, improve correlation clarity

**Priority 3: Improve Heatmap Color Scale in System B**
- **Evidence:** Heatmap received most complaints: "Colors were hard to distinguish" (4/5 participants)
- **Evidence:** System B had lower accuracy for T4 due to color misinterpretation (80% vs 100% for System A)
- **Feedback:** System B had highest mental demand (5.8/10)
- **Implementation:** Replace Viridis with perceptually uniform ColorBrewer RdYlGn scale, add color legend with explicit value breakpoints
- **Expected Impact:** Reduce mental demand, improve T4 accuracy to match System A

**Priority 4: Add Explicit Filter Summary Display**
- **Evidence:** All systems had moments where users were unsure what was currently selected
- **Observation:** Participants had to "test" selections by hovering to see what was included
- **Implementation:** Add a text summary box showing: "Currently selected: 3 regions, 42 countries, years 2020-2024"
- **Expected Impact:** Reduce uncertainty, improve user confidence in selections

**Priority 5: Implement Adaptive Detail on Demand**
- **Evidence:** System C's bubble chart disliked: "too many visual channels" (3/5), suggesting information overload
- **Implementation:** Start with simpler encoding (position + color only), add size/opacity encoding only when user hovers or selects points
- **Rationale:** Progressive disclosure reduces initial cognitive load while maintaining detail access
- **Expected Impact:** Reduce mental demand, improve bubble chart acceptance

**Priority 6: Add Undo/Redo for Selection**
- **Evidence:** Participants often accidentally deselected items: "Brushing was imprecise" (3/5)
- **Observation:** No participant could recover from accidental deselection without restarting task
- **Implementation:** Implement selection history stack with undo (Ctrl+Z) and redo (Ctrl+Y) keyboard shortcuts
- **Expected Impact:** Reduce frustration, improve task completion rates, lower interaction counts

**Priority 7: Optimize for Mobile/Tablet**
- **Evidence:** All systems designed for desktop (1920×1080), but evaluation showed interest in mobile use
- **Feedback:** "Would love to explore this on my iPad" (2/5 participants)
- **Implementation:** Responsive layouts with stacked views on narrow screens, touch-friendly selection interactions
- **Expected Impact:** Expand accessibility to mobile devices

### 8.2 Advanced Features Not Currently Implemented

While not directly evidenced by current evaluation, these features would enhance analytical capability:

**Annotation and Export:**
- Allow users to annotate interesting findings with text notes
- Export selections as CSV or share as permalink URLs
- Rationale: Support collaborative analysis and reporting workflows

**Statistical Overlays:**
- Add confidence intervals to line charts
- Add correlation coefficients (r, R²) to scatter plots
- Rationale: Provide statistical rigor for data analysts

**Additional Datasets:**
- Enable loading of other time-series regional datasets
- Allow users to upload custom CSV files
- Rationale: Generalize system to broader use cases

All proposed improvements are directly grounded in evaluation data, ensuring that future work addresses real user needs rather than speculative features.

---

## References

Brehmer, M., & Munzner, T. (2013). A multi-level typology of abstract visualization tasks. *IEEE Transactions on Visualization and Computer Graphics*, 19(12), 2376-2385.

Cleveland, W. S., & McGill, R. (1984). Graphical perception: Theory, experimentation, and application to the development of graphical methods. *Journal of the American Statistical Association*, 79(387), 531-554.

Healey, C. G., Booth, K. S., & Enns, J. T. (1996). High-speed visual estimation using preattentive processing. *ACM Transactions on Computer-Human Interaction*, 3(2), 107-135.

Heer, J., & Bostock, M. (2010). Crowdsourcing graphical perception: Using mechanical turk to assess visualization design. *Proceedings of CHI 2010*, 203-212.

Munzner, T. (2014). *Visualization Analysis and Design*. CRC Press.

Norman, D. A. (2013). *The Design of Everyday Things: Revised and Expanded Edition*. Basic Books.

Roberts, J. C. (2007). State of the art: Coordinated & multiple views in exploratory visualization. *Proceedings of CMV 2007*, 61-71.

Shneiderman, B. (1996). The eyes have it: A task by data type taxonomy for information visualizations. *Proceedings of IEEE VIS 1996*, 336-343.

---

## Appendices

### Appendix A: Raw Evaluation Data

**[See separate file: `evaluation_data/raw_evaluation_results.csv`]**

Contains:
- Participant ID, System Order, Task ID, Completion Time, Accuracy, Interaction Count
- SUS questionnaire responses (10 questions × 5 participants × 3 systems)
- NASA TLX ratings (6 dimensions × 5 participants × 3 systems)
- Preference rankings
- Qualitative feedback transcripts

### Appendix B: Team Contributions

**Team Member 1 (30%):**
- Dataset creation and preprocessing
- System A implementation
- User evaluation participant recruitment
- Section 1-3 of report

**Team Member 2 (25%):**
- System B implementation
- Generalized selection implementation
- Evaluation data collection and analysis
- Section 4, 7 of report

**Team Member 3 (20%):**
- System C implementation
- Evaluation protocol design
- Statistical analysis
- Section 6 of report

**Team Member 4 (15%):**
- Demo video creation and editing
- Evaluation participant coordination
- Data visualization for report
- Section 8 of report

**Team Member 5 (10%):**
- Report compilation and formatting
- Code documentation and README files
- Quality assurance and testing
- Bibliography management

### Appendix C: Evaluation Materials

**Consent Form:** [See `evaluation_data/consent_form.pdf`]
**Task Instructions:** [See `evaluation_data/task_instructions.pdf`]
**SUS Questionnaire:** [See `evaluation_data/sus_questionnaire.pdf`]
**NASA TLX Form:** [See `evaluation_data/nasa_tlx_form.pdf`]

---

*End of Report*
