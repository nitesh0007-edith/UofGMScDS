# Glasgow Weather Visualization Project
## Multi-view Interactive Analysis with Altair Viewer

**Course:** Information Visualisation (M), 2024/25
**Submission Date:** March 20, 2026
**Technology:** Python/Altair + Streamlit

---

## 🚀 Quick Start

### Option 1: Streamlit Landing Page (Recommended)

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

Then navigate to the "🚀 Launch Systems" page and click the buttons to launch visualizations in **Altair Viewer**.

### Option 2: Run Systems Directly

```bash
# System A
python SystemA/system_a.py

# System B
python SystemB/system_b.py

# System C
python SystemC/system_c.py

# Generalized Selection
python SystemA/system_a_with_generalization.py
```

Each command will:
1. Save HTML and JSON files (backup)
2. Open the visualization in **Altair Viewer** (interactive window)

---

## 📦 What's Implemented

### ✅ All 3 Core Visualization Systems

**System A - Temporal Analysis:**
- Time series line chart (temperature trends)
- Scatter plot with regression (humidity vs visibility)
- Seasonal bar chart
- Wind speed histogram
- **Bidirectional brushing and linking** ✓

**System B - Statistical Focus:**
- Month × Year temperature heatmap
- Box plots with outliers by season
- Scatter with dynamic polynomial regression
- Weather type distribution bars
- **Click and brush selection** ✓

**System C - Small Multiples:**
- Faceted time series (5 years side-by-side)
- Strip plot for outlier identification
- Multi-dimensional bubble chart (4D encoding)
- Temperature histogram by weather type
- **Dropdown and slider filtering** ✓

**System A + Generalized Selection:**
- 5-level temporal hierarchy (Day → Week → Month → Season → Year)
- Radio buttons for hierarchy traversal
- Aggregation views at all levels
- **True semantic abstraction** ✓

---

## 🎨 Interactive Features

### All Systems Support:

✅ **Brushing:** Drag to select date ranges or value ranges
✅ **Clicking:** Click on marks to select specific items
✅ **Linking:** Selection propagates across all views
✅ **Tooltips:** Hover for detailed information
✅ **Filtering:** Interactive controls (dropdowns, sliders)
✅ **Regression:** Dynamic regression lines appear on selection

### How to Interact:

**System A:**
1. **Brush** on time series → Drag to select date range
2. **Brush** on scatter plot → Drag to select patterns
3. **Click** on bar chart → Click season to filter
4. Watch red regression line update dynamically

**System B:**
1. **Click** on heatmap cells → Select specific month-year
2. **Click** on box plot → Select by season
3. **Brush** on scatter → Drag to select patterns
4. See polynomial regression curve appear

**System C:**
1. **Use dropdown** → Filter by year (2015-2019 or All)
2. **Brush** on faceted charts → Select patterns
3. Watch all views update together
4. **Hover** on bubble chart → See 4D data

**Generalized Selection:**
1. **Select "Day" level** with radio button
2. **Click or brush** on time series
3. **Switch to "Week" level** → Selection expands!
4. Try Month, Season, Year → Watch hierarchy generalize

---

## 📊 Dataset Information

**Glasgow Daily Weather Observations (2015-2019)**

- **Records:** 1,795 daily observations
- **Time Period:** January 1, 2015 - November 30, 2019
- **Location:** Glasgow, Scotland
- **Source:** Dark Sky API historical weather data

**Attributes (9):**
- `day`: Date of observation
- `tempMin`, `tempMax`: Temperature range (°C)
- `cloudCover`: Cloud coverage [0-1]
- `humidity`: Humidity level [0-1]
- `windSpeed`: Wind speed (km/h)
- `visibility`: Visibility distance (km)
- `desc`: Weather type (rain, clear, cloudy, fog)
- `summary`: Detailed description

**Derived Features:**
- `tempAvg`: Average daily temperature
- `year`, `month`, `season`: Temporal groupings
- `week_id`, `month_id`, `season_id`: Hierarchical IDs

---

## 🎯 Analytical Tasks Supported

All systems support these 5 tasks:

**T1: Compare Seasonal Patterns**
- Compare mean temperatures across seasons
- Identify seasonal variations

**T2: Identify Extreme Weather Events**
- Find outlier days (extreme temp, wind, etc.)
- Detect anomalies

**T3: Explore Correlations**
- Discover relationships between weather factors
- Understand atmospheric interactions

**T4: Analyze Temporal Trends**
- Track year-over-year changes (2015-2019)
- Identify warming/cooling patterns

**T5: Filter and Subset Data**
- Focus on specific time periods
- Filter by weather conditions
- Interactive exploration

---

## 🛠️ Technical Details

### Dependencies:

```
Python 3.7+
altair==5.5.0
pandas==2.2.0
numpy==1.26.0
vega_datasets==0.9.0
streamlit>=1.28.0
```

### Installation:

```bash
# Install all dependencies
pip install -r requirements.txt

# Or install individually
pip install altair pandas numpy vega_datasets streamlit
```

### Altair Viewer:

All visualizations now use **Altair Viewer** for interactive display:
- Automatically opens in a new window
- Full interactivity preserved
- Responsive to screen size
- Works offline

### Backup Files:

Each system also saves:
- **HTML files:** `system_*_visualization.html` (can open in browser)
- **JSON files:** `system_*_spec.json` (Vega-Lite specification)

---

## 📁 Project Structure

```
GroupProject_IV_2026/
│
├── app.py                              ← Streamlit landing page (RUN THIS!)
├── requirements.txt                     ← Python dependencies
├── README_UPDATED.md                    ← This file
│
├── data/
│   └── Glasgow_weather_data/
│       ├── clean_weather_data.csv      (original)
│       └── weather_data_enriched.csv   (with temporal features)
│
├── SystemA/
│   ├── system_a.py                     ← Run for System A
│   ├── system_a_with_generalization.py ← Run for generalized selection
│   ├── system_a_visualization.html     (backup)
│   └── system_a_spec.json              (backup)
│
├── SystemB/
│   ├── system_b.py                     ← Run for System B
│   ├── system_b_visualization.html     (backup)
│   └── system_b_spec.json              (backup)
│
├── SystemC/
│   ├── system_c.py                     ← Run for System C
│   ├── system_c_visualization.html     (backup)
│   └── system_c_spec.json              (backup)
│
└── docs/
    ├── SECTION_1_DATA_DESCRIPTION.md
    ├── SECTION_2_TASKS_DEFINITION.md
    └── SECTION_4_GENERALIZED_SELECTION.md
```

---

## 🧪 Testing the Visualizations

### Test System A:
```bash
python SystemA/system_a.py
```
**Expected:** Altair Viewer opens with 4 linked views
**Test:**
- Brush on time series → All views update
- Click on bar chart season → Selection propagates
- Regression line appears in red

### Test System B:
```bash
python SystemB/system_b.py
```
**Expected:** Altair Viewer opens with heatmap, box plots, scatter
**Test:**
- Click heatmap cells → Views highlight
- Click box plot → Filter by season
- Brush scatter → Polynomial regression appears

### Test System C:
```bash
python SystemC/system_c.py
```
**Expected:** Altair Viewer opens with faceted views
**Test:**
- Use year dropdown → All views filter
- Brush on facets → Selection propagates
- Hover on bubbles → 4D tooltips appear

### Test Generalized Selection:
```bash
python SystemA/system_a_with_generalization.py
```
**Expected:** Altair Viewer opens with hierarchy controls
**Test:**
- Select "Day" level, click on a day
- Switch to "Week" → Selection expands to whole week
- Switch to "Month" → Selection expands to whole month
- Observe aggregation bars at all levels

---

## 🎓 Learning Outcomes Demonstrated

✓ Multi-view coordinated visualization
✓ Brushing and linking (uni and bidirectional)
✓ Hierarchical data structures and semantic abstraction
✓ Generalized selection vs. global filtering
✓ Task-driven design (Brehmer & Munzner taxonomy)
✓ Data categorization (Munzner framework)
✓ Design comparison and justification
✓ Alternative design approaches for same dataset
✓ Small multiples and faceting
✓ Statistical visualizations (box plots, heatmaps)
✓ Interactive filtering controls

---

## 📝 Documentation Sections Complete

- [x] Section 1: Data Description (398 words)
- [x] Section 2: Tasks Definition (395 words)
- [x] Section 3: System A (implemented)
- [x] Section 3: System B (implemented)
- [x] Section 3: System C (implemented)
- [x] Section 4: Generalized Selection (398 words + implementation)
- [ ] Section 5: Demo Video (5 minutes, YouTube)
- [ ] Section 6: Design Comparison (1200 words)
- [ ] Section 7: User Evaluation (1000 words)
- [ ] Section 8: Future Work (400 words)

---

## 🚨 Troubleshooting

**If Altair Viewer doesn't open:**
```bash
# Try installing/updating altair
pip install --upgrade altair

# Or open HTML files directly in browser
open SystemA/system_a_visualization.html
```

**If Streamlit doesn't start:**
```bash
# Check installation
pip install --upgrade streamlit

# Run with verbose output
streamlit run app.py --logger.level=debug
```

**If filters don't work:**
- Make sure you're using the latest version of Altair (5.5.0)
- Check that all dependencies are installed
- Try restarting the visualization

---

## 🎯 Next Steps

### Immediate (Week 1):
- Write Section 6: Design Comparison (1200 words)
- Test all filters and interactions thoroughly

### Week 2:
- Recruit 5 participants per system (15 total)
- Conduct user evaluation for all 5 tasks
- Collect timing, accuracy, and feedback data

### Week 3:
- Analyze evaluation data (statistical tests)
- Write Section 7: User Evaluation (1000 words)
- Write Section 8: Future Work (400 words)

### Week 4:
- Record demo video (5 minutes)
- Upload to YouTube
- Compile final PDF report
- Prepare zip folders for submission

**Deadline:** March 20, 2026 (25 days remaining)

---

## 📧 Support

For questions or issues:
1. Check this README
2. Review `IMPLEMENTATION_COMPLETE.md` for details
3. Check `PROJECT_CHECKLIST.md` for requirements

---

**Last Updated:** February 23, 2026
**Status:** Implementation Phase Complete ✅
**All visualizations working in Altair Viewer** ✅
**Streamlit landing page functional** ✅
