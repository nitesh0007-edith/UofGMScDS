# CLAUDE.md — IV Group Project: Multiview Visualisation

## Role

You are building a Python + Altair multiview weather visualisation project for a university Information Visualisation course. The final output is a multi-page website: a landing page (index.html) linking to three separate system pages (System_A.html, System_B.html, System_C.html). Each system page is a self-contained, richly interactive dashboard with multiple linked Vega-Lite/Altair charts, dropdowns, sliders, instructions, and task descriptions — all in one HTML file.

Follow every instruction in this file precisely. When asked to work on this project, reference this file as the source of truth.

---

## Project Context

- **Course:** Information Visualisation (IV), University of Glasgow
- **Deadline:** 16:30, Friday 20th March 2026
- **Weight:** 30% of IV course mark
- **Stack:** Python 3.10+, Altair 5.x, Pandas. NO other visualisation libraries (no matplotlib, plotly, seaborn, etc.)
- **Output format:** Each system saves as a standalone `.html` file viewable in any browser. The landing page is `index.html`.
- **Dataset:** `data/clean_weather_data.csv` (1,795 rows, 2015-01-01 to 2019-11-30)

---

## Project Structure

Always maintain this exact structure:

```
iv-group-project/
├── CLAUDE.md                  # This file — project instructions
├── data/
│   └── clean_weather_data.csv # Source dataset (DO NOT modify)
├── src/
│   ├── data_prep.py           # Shared data loading & preprocessing
│   ├── index_page.py          # Generates index.html landing page
│   ├── system_a.py            # Generates System_A.html
│   ├── system_b.py            # Generates System_B.html
│   └── system_c.py            # Generates System_C.html
├── output/
│   ├── index.html             # Landing page with 3 buttons
│   ├── System_A.html          # System A full dashboard
│   ├── System_B.html          # System B full dashboard
│   └── System_C.html          # System C full dashboard
├── evaluation/
│   ├── eval_template.csv      # Blank evaluation collection form
│   └── results.csv            # Raw evaluation data (filled after user study)
├── report/
│   └── report_sections.md     # Draft text for all 8 report sections
├── requirements.txt           # Python dependencies
└── README.md                  # How to install and run
```

---

## Commands

```bash
# Setup
pip install -r requirements.txt

# Generate all pages
python src/index_page.py       # → output/index.html
python src/system_a.py         # → output/System_A.html
python src/system_b.py         # → output/System_B.html
python src/system_c.py         # → output/System_C.html

# Generate everything at once
python src/index_page.py && python src/system_a.py && python src/system_b.py && python src/system_c.py

# Lint
ruff check src/
```

---

## requirements.txt contents

```
altair>=5.0,<6.0
pandas>=2.0
vl-convert-python>=1.0
```

---

## Dataset Specification

The CSV has these columns — use these exact names everywhere:

| Column | Pandas dtype | Notes |
|---|---|---|
| `day` | `datetime64` | Parse with `pd.to_datetime()` |
| `tempMin` | `float64` | Min temperature °C |
| `tempMax` | `float64` | Max temperature °C |
| `summary` | `str` | Free text, 7 nulls → fill with `"No description"` |
| `desc` | `str` | Weather category, 184 blanks → fill with `"unknown"` |
| `cloudCover` | `float64` | 0–1 ratio, 3 nulls → fill with median |
| `humidity` | `float64` | 0–1 ratio |
| `windSpeed` | `float64` | km/h |
| `visibility` | `float64` | km |

### Derived columns (compute in `data_prep.py`)

- `tempRange` = `tempMax - tempMin`
- `month` = integer month (1–12)
- `year` = integer year (2015–2019)
- `season` = mapped from month: Dec/Jan/Feb → Winter, Mar/Apr/May → Spring, Jun/Jul/Aug → Summer, Sep/Oct/Nov → Autumn
- `monthName` = abbreviated month name (Jan, Feb, etc.)
- `dayOfYear` = integer day of year (1–366)
- `avgTemp` = (`tempMax + tempMin`) / 2

---

## Shared Data Prep Module (`src/data_prep.py`)

Implement a single function `load_and_prepare(filepath)` that:
1. Reads the CSV
2. Parses `day` as datetime
3. Fills nulls as specified above
4. Computes all derived columns
5. Returns the cleaned DataFrame

Every system file imports from this module. Never duplicate preprocessing logic.

---

## Landing Page (`index.html`)

### Visual Design
- Full-viewport centred card with a gradient background (light gray-blue gradient, like the reference)
- Frosted-glass card container in the centre
- Large bold title: **MULTIVIEW VISUALISATION** (uppercase, white text)
- Three stacked buttons: **System A**, **System B**, **System C**
- Buttons are dark (dark teal/navy), rounded corners, wide, stacked vertically with spacing
- Each button links to the corresponding `System_X.html` file (same directory)

### Implementation (`src/index_page.py`)
- Generate a pure HTML/CSS file — no Altair needed
- Save to `output/index.html`
- Use inline CSS, no external dependencies
- The gradient background should span the full viewport
- The card should be semi-transparent with a subtle shadow/blur effect

---

## Task Definitions

All three systems must support ALL five tasks:

| ID | Task Description |
|---|---|
| **T1** | Identify the season or month with the highest average temperature range |
| **T2** | Find the top 3 weather types (desc) by frequency across the dataset |
| **T3** | Determine which year had the highest average wind speed |
| **T4** | Find weather type with the highest average visibility, filtered by a minimum humidity threshold |
| **T5** | Identify months with wind speed above a user-set threshold AND humidity above a user-set threshold. Find the top 3 seasons with the highest average cloud cover. |

---

## HTML Page Structure (applies to ALL three system pages)

Every System_X.html page MUST follow this exact layout structure, matching the reference design:

### 1. Page Header
- Large centred title: **SYSTEM A** (or B/C), bold, dark red/maroon colour
- Horizontal rule below the title (dark red/maroon line, full width)

### 2. "How to Use" Section
- Section heading: **How to Use** (bold, left-aligned)
- Light gray background box containing bullet points explaining every interaction:
  - Which elements can be used as filters
  - How brushing/clicking works between charts
  - What dropdowns and sliders control
  - How to reset (refresh the page)
- Each bullet point is clear and specific to that system's charts

### 3. "Tasks" Section
- Section heading: **Tasks** (bold, left-aligned)
- Light gray background box containing numbered task list (T1–T5)
- Tasks that involve thresholds should bold the threshold values
- Example: "Find a weather type with **humidity > 0.85** and determine its average visibility."

### 4. Charts Section
- Charts arranged in a grid: typically 2 charts per row
- Row 1: Two charts side by side (e.g., bar chart + secondary chart)
- Row 2: Two more charts side by side
- Row 3 (if needed): Additional charts
- All charts are Vega-Lite specs embedded via `vegaEmbed()`
- Charts must have clear titles, axis labels with units, and tooltips

### 5. Controls Section (at the bottom, below charts)
- Dropdowns for selecting metrics (e.g., "Select Variable:", "Rank by:")
- Sliders for setting thresholds (e.g., "Minimum humidity:", "Wind speed greater than:")
- Sliders show their current value next to them
- Controls are rendered using Altair's `alt.binding_select()`, `alt.binding_range()`, and `alt.param()` bound to the chart specs

### 6. Page Styling
- White/light background
- Clean, professional typography (system fonts are fine)
- Charts should have NO unnecessary borders — clean and flat
- Section backgrounds in light gray (#f5f5f5 or similar) with subtle padding
- Consistent spacing between all sections

---

## System Specifications

### CRITICAL REQUIREMENTS (apply to ALL systems)

- Each system is a **multi-view composition** of at least 4 charts (2x2 grid or more)
- Each system must implement **brushing and linking** between charts
- **Bidirectional linking** where possible (both views filter/highlight each other)
- Use `alt.selection_interval()` and/or `alt.selection_point()` for all interactions
- Every chart must have: a descriptive title, axis labels with units, and tooltip encoding
- Each system must include **at least 1 dropdown** and **at least 2 sliders** as bound parameters
- Save output with the full page HTML template (not just Altair's default `.save()`)
- Use a consistent colour scale for `desc` across all systems:

```python
WEATHER_COLORS = alt.Scale(
    domain=['rain', 'clear-day', 'partly-cloudy-day', 'cloudy', 'fog', 'unknown'],
    range=['#4c78a8', '#f58518', '#e45756', '#72b7b2', '#54a24b', '#bab0ac']
)
```

### How to Build Each System Page

Since Altair's `.save()` produces a minimal HTML wrapper, you need to build the full page HTML yourself:

1. Build each Altair chart as a separate `alt.Chart` object
2. Combine them using `alt.vconcat()`, `alt.hconcat()`, or `alt.layer()` into a single compound chart
3. Get the Vega-Lite JSON spec using `chart.to_dict()`
4. Embed the spec into a custom HTML template that includes the header, How to Use, Tasks, and styling
5. Write the final HTML string to `output/System_X.html`

```python
import json

def save_system_page(chart, system_name, how_to_use_html, tasks_html, output_path):
    spec_json = json.dumps(chart.to_dict(), indent=2)
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{system_name}</title>
    <script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
    <script src="https://cdn.jsdelivr.net/npm/vega-lite@5.20.1"></script>
    <script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>
    <style>
        body {{ font-family: Georgia, 'Times New Roman', serif; margin: 0; padding: 20px; background: #fff; }}
        h1 {{ text-align: center; color: #8b0000; font-size: 2.5em; margin-bottom: 5px; }}
        hr {{ border: 2px solid #8b0000; margin-bottom: 30px; }}
        h2 {{ font-size: 1.3em; margin-top: 30px; }}
        .info-box {{ background: #f5f5f5; padding: 15px 25px; border-radius: 4px; margin: 10px 0 25px; }}
        .info-box ul {{ margin: 8px 0; padding-left: 20px; }}
        .info-box li {{ margin: 6px 0; line-height: 1.5; }}
        .info-box ol {{ margin: 8px 0; padding-left: 20px; }}
        .info-box ol li {{ margin: 8px 0; line-height: 1.5; }}
        #vis {{ display: flex; justify-content: center; margin: 20px 0; }}
    </style>
</head>
<body>
    <h1>{system_name}</h1>
    <hr>
    <h2>How to Use</h2>
    <div class="info-box">{how_to_use_html}</div>
    <h2>Tasks</h2>
    <div class="info-box">{tasks_html}</div>
    <div id="vis"></div>
    <script>
        var spec = {spec_json};
        vegaEmbed('#vis', spec, {{mode: 'vega-lite', actions: {{export: true, source: false, compiled: false, editor: false}}}})
            .catch(console.error);
    </script>
</body>
</html>"""
    with open(output_path, 'w') as f:
        f.write(html)
```

---

### System A — Category + Attribute Overview (4 charts, orange/salmon colours)

**Design philosophy:** Overview of weather patterns across categories, with metric selection dropdown and threshold sliders. Uses warm colour palette (oranges, salmons).

**Charts (2x2 grid via `hconcat` inside `vconcat`):**

1. **Top-left: Horizontal Bar Chart** — "Top Weather Types (Available Metrics: Avg Temp | Wind Speed | Humidity | Count)"
   - Mark: `mark_bar()`
   - X: aggregate of selected metric via dropdown
   - Y: `desc:N` (weather type), sorted descending by value
   - Color: orange/salmon sequential or `desc:N` with warm palette
   - Clickable bars → filter all other charts to that weather type
   - Metric controlled by **"Rank by" dropdown**

2. **Top-right: Bar Chart** — "Number of Days by Month"
   - Mark: `mark_bar()` (pink/salmon colour)
   - X: `monthName:O` sorted Jan–Dec
   - Y: `count():Q`
   - Linked: clicking a weather type in chart 1 filters this to show monthly distribution for that type only
   - Has Vega-Embed action menu (...) in top-right corner

3. **Bottom-left: Scatter Plot** — "Day vs Wind Speed"
   - Mark: `mark_circle()`
   - X: `day:T` (temporal)
   - Y: `windSpeed:Q`
   - Color: `desc:N` with blue-teal palette (different from chart 1)
   - Interval brush → highlights points in chart 4
   - Filtered by sliders

4. **Bottom-right: Scatter Plot** — "Humidity vs Visibility"
   - Mark: `mark_circle()`
   - X: `humidity:Q`
   - Y: `visibility:Q`
   - Color: `desc:N` with green-teal palette
   - Linked to brush from chart 3
   - Filtered by sliders

**Bound parameters (appear below charts):**
- **Dropdown:** "Rank by:" — options: `['tempMax', 'windSpeed', 'humidity', 'visibility']` with labels `['Avg Max Temp', 'Avg Wind Speed', 'Avg Humidity', 'Avg Visibility']`
- **Slider 1:** "Minimum humidity:" — range 0 to 1, step 0.01, default 0
- **Slider 2:** "Wind speed greater than:" — range 0 to 30, step 0.5, default 0
- **Slider 3:** "Cloud cover less than:" — range 0 to 1, step 0.01, default 1

---

### System B — Temporal Decomposition + Heatmap (4 charts, blue/green/yellow)

**Design philosophy:** Temporal focus — how weather varies across months, seasons, years. Uses a calendar heatmap to provide a spatial-like overview (replacing the map from the reference). Green/yellow/blue colour treatment.

**Charts (2x2 grid):**

1. **Top-left: Horizontal Bar Chart** — "Top Months/Seasons by [Metric]"
   - Mark: `mark_bar()` (blue tones)
   - X: aggregate of selected metric
   - Y: `monthName:O` or `season:N`, sorted
   - Clickable → filters other charts to that month/season

2. **Top-right: Calendar Heatmap** — "Daily Weather by Month × Year"
   - Mark: `mark_rect()`
   - X: `monthName:O` (sorted Jan–Dec)
   - Y: `year:O`
   - Color: mean of selected variable (sequential blue/green scheme)
   - Replaces the geographic map from the reference project
   - Click a cell → filters scatter and line charts below
   - Has Vega-Embed action menu (...) in corner

3. **Bottom-left: Grouped Bar Chart** — "Season: Wind Speed vs Humidity"
   - Mark: `mark_bar()` layered or grouped
   - X: `season:N`
   - Y: `mean(windSpeed):Q` (green bars) and `mean(humidity):Q` (yellow/orange bars) — use `alt.layer()` with two bar marks and separate Y axes or `fold` transform
   - Shows dual metrics side by side per season

4. **Bottom-right: Line Chart** — "Number of [Weather Type] Days (Resolution: Yearly/Monthly)"
   - Mark: `mark_line()` + `mark_point()`
   - X: `year:O` or `yearmonth(day):T`
   - Y: `count():Q` or aggregate
   - Color: by `desc:N` (multiple lines, one per weather type) — the top/thickest line is the total or dominant type
   - Click on yearly aggregate point → shows monthly breakdown (generalised selection)

**Bound parameters:**
- **Dropdown:** "Metric:" — same options as System A
- **Slider 1:** "Wind speed greater than:" — range 0–30
- **Slider 2:** "Humidity greater than:" — range 0–1

---

### System C — Full Exploration with Legend Filtering (4+ charts, multi-hue)

**Design philosophy:** Maximum exploration flexibility. Uses colour for weather type, shape for season, clickable legends for both. Largest scatter plot is the centrepiece. Colourful, multi-hue palette.

**Charts (bar on left, large scatter in centre, legend panel on right, summary below):**

1. **Left: Horizontal Bar Chart** — "Top Weather Types (Available Metrics)"
   - Same metric-switching bar chart as other systems
   - But uses a gradient or rainbow colour scheme for the bars (different from A and B)
   - Each weather type has a distinct vivid colour

2. **Centre: Large Scatter Plot** — "Day vs [Selected Metric]"
   - Mark: `mark_point()` (not circle — using different shapes)
   - X: `day:T` (full temporal range 2015–2019)
   - Y: selected metric via dropdown
   - Color: `desc:N` — each weather type gets a unique colour
   - Shape: `season:N` — circle=Winter, diamond=Spring, square=Summer, triangle=Autumn
   - Brushable interval selection
   - This is the main exploration chart — should be the widest chart

3. **Right: Legend Panel**
   - The colour legend for `desc` (weather type) is clickable — implemented via `alt.selection_point(fields=['desc'], bind='legend')`
   - The shape legend for `season` is also clickable — via `alt.selection_point(fields=['season'], bind='legend')`
   - Clicking a legend item filters ALL charts

4. **Bottom: Heatmap or Map-equivalent** — "Monthly Weather Composition"
   - Mark: `mark_rect()` or `mark_area()`
   - Shows year × month or season × year breakdown
   - Linked to scatter brush above
   - Provides summary context

**Bound parameters:**
- **Dropdown:** "Metric:" — select Y-axis variable for scatter and bar ranking
- **Slider 1:** "Minimum humidity:" — range 0–1
- **Slider 2:** "Wind speed greater than:" — range 0–30
- **Slider 3:** "Cloud cover less than:" — range 0–1

---

## Generalised Selection (Part 4)

Implement in **System B** using the temporal hierarchy:

```
Level 0: Individual Day      → e.g., 2017-07-15
Level 1: Month               → e.g., July 2017
Level 2: Season              → e.g., Summer 2017
Level 3: Year                → e.g., 2017
Level 4: Entire Dataset      → 2015–2019
```

The line chart in System B implements this: clicking a yearly aggregate point shows monthly breakdown for that year. This is generalised selection — going from a general view (yearly) to specific (monthly) with a single interaction.

---

## Chart Layout Pattern

Use this Altair composition for the 2x2 grid:

```python
row1 = alt.hconcat(chart1, chart2)
row2 = alt.hconcat(chart3, chart4)
full_dashboard = alt.vconcat(row1, row2).resolve_scale(color='independent')
```

For System C with side legend panel:
```python
row1 = alt.hconcat(bar_chart, scatter_chart)
row2 = alt.hconcat(bottom_chart)
full_dashboard = alt.vconcat(row1, row2).resolve_scale(color='shared')
```

---

## Slider and Dropdown Implementation Pattern

```python
# Dropdown for metric selection
metric_dropdown = alt.binding_select(
    options=['tempMax', 'windSpeed', 'humidity', 'visibility'],
    labels=['Avg Max Temp', 'Avg Wind Speed', 'Avg Humidity', 'Avg Visibility'],
    name='Rank by: '
)
metric_param = alt.param(name='selected_metric', bind=metric_dropdown, value='tempMax')

# Slider for threshold filtering
humidity_slider = alt.binding_range(min=0, max=1, step=0.01, name='Minimum humidity: ')
humidity_param = alt.param(name='min_humidity', bind=humidity_slider, value=0)

wind_slider = alt.binding_range(min=0, max=30, step=0.5, name='Wind speed greater than: ')
wind_param = alt.param(name='min_wind', bind=wind_slider, value=0)

# Apply to chart with transform_filter
chart = alt.Chart(df).mark_circle().encode(
    ...
).transform_filter(
    'datum.humidity >= min_humidity'
).transform_filter(
    'datum.windSpeed >= min_wind'
).add_params(metric_param, humidity_param, wind_param)
```

For **dynamic field selection** (dropdown changes which field the bar chart ranks by):

```python
chart = alt.Chart(df).transform_calculate(
    selected_value='datum[selected_metric]'
).mark_bar().encode(
    x=alt.X('mean(selected_value):Q', title='Metric Value'),
    y=alt.Y('desc:N', sort='-x', title='Weather Type'),
    color=alt.Color('desc:N', scale=WEATHER_COLORS)
).add_params(metric_param)
```

---

## Report Sections (for `report/report_sections.md`)

When asked to draft report text, follow these constraints:

| Section | Max Words | Content |
|---|---|---|
| Part 1: The Data | 400 | Title, description, categorise using Lecture 1a IV terminology |
| Part 2: The Tasks | 400 | T1–T5 with Lecture 1b task taxonomy (action + target) |
| Part 3: The Systems | — | Code only (3 zipped folders) |
| Part 4: Generalised Selection | 400 | Semantic structure, traversal policy, implementation |
| Part 5: Demo Video | — | YouTube link (max 5 min) |
| Part 6: Design Comparison | 1200 (200 each x 6) | 6 design decisions with per-system justification |
| Part 7: User Evaluation | 1000 | Methodology, data, analysis |
| Part 8: Future Work | 400 | Changes justified by evaluation data |

### Writing rules
- ACM reference style
- Stay within word limits
- Use IV terminology (mark, channel, idiom, effectiveness principle, expressiveness principle, Gestalt principles)
- Cite: Munzner (2014), Mackinlay (1986), Shneiderman (1996)

---

## Evaluation Design

### Methodology

- **Within-subjects:** Same 5+ participants use all 3 systems
- **Counterbalanced order:** Latin square (ABC, BCA, CAB)
- **Per (participant x system x task), collect:**
  - `time_seconds` — task completion time
  - `accuracy` — 0 (wrong), 1 (partial), 2 (correct)
  - `likert` — 1–5 ease-of-use rating
- **Post-study:** Rank systems 1–3 overall preference

### eval_template.csv format

```csv
participant_id,system,task,time_seconds,accuracy,likert,notes
P1,A,T1,,,,
P1,A,T2,,,,
...
```

Generate 75 rows (5 participants x 3 systems x 5 tasks).

---

## Code Style Rules

- Python 3.10+ syntax
- Type hints on function signatures
- Docstrings on every function
- No wildcard imports
- Import order: stdlib → third-party → local
- Variable names: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- Max line length: 100 chars
- Every `.py` file has `if __name__ == "__main__":` guard

---

## Common Mistakes to Avoid

- DO NOT use `matplotlib`, `plotly`, `seaborn`, or any non-Altair library for charts
- DO NOT exceed 5,000 rows without `alt.data_transformers.disable_max_rows()` — 1,795 rows is fine
- DO NOT hardcode file paths — use relative paths from project root
- DO NOT make systems look identical — each must have visually distinct chart types, layout, and colour treatment
- DO NOT implement generalised selection as a simple dropdown — it must respond to a SELECTED item and expand through the hierarchy
- DO NOT forget "How to Use" and "Tasks" sections in EVERY system page
- DO NOT use Altair's default `.save()` without wrapping in the full page template
- DO NOT put all charts in a single `vconcat` stack — use `hconcat` within `vconcat` for 2x2 grid
- DO NOT forget bound parameters (dropdowns + sliders) — every system needs at least 1 dropdown and 2 sliders
- DO NOT use `mark_geoshape` — this dataset has no geographic coordinates
- DO NOT forget tooltips on every chart
- DO NOT forget to sort bar charts by value descending

---

## Checklist (verify before final submission)

- [ ] `data_prep.py` handles all nulls and derived columns
- [ ] `index.html` has centred card with gradient background and 3 nav buttons
- [ ] `System_A.html` has header, How to Use, Tasks, 4+ charts, dropdown, sliders
- [ ] `System_B.html` has header, How to Use, Tasks, 4+ charts, dropdown, sliders, generalised selection
- [ ] `System_C.html` has header, How to Use, Tasks, 4+ charts, legend filtering, dropdown, sliders
- [ ] All charts have titles, axis labels, tooltips
- [ ] Brushing and linking works bidirectionally in each system
- [ ] Sliders filter data reactively across charts
- [ ] Dropdown changes the metric displayed in charts
- [ ] All 3 pages follow same HTML structure (header → How to Use → Tasks → Charts → Controls)
- [ ] Each system looks visually distinct (different chart types, colours, layouts)
- [ ] Report covers all 8 parts with correct numbering
- [ ] Word counts within limits
- [ ] YouTube link at TOP of PDF
- [ ] ACM reference style
- [ ] Raw evaluation data in appendix
- [ ] Team contribution log in appendix
- [ ] Three zipped folders (A, B, C) with code + data files
- [ ] Demo video ≤ 5 minutes
