# 🚀 PowerBI-Style Dashboard - How to Run

## ✅ **NEW: Embedded Altair Visualizations**

All visualizations now work **directly in the browser** with full interactivity!

---

## 🎯 Features

### ✅ **PowerBI-Style Layout**
- Professional dashboard interface
- Grid-based layout with colored cards
- Statistics overview
- Clean, modern design

### ✅ **All Filters & Interactions Working**
- ✅ Radio buttons work
- ✅ Dropdowns work
- ✅ Brushing works
- ✅ Clicking works
- ✅ All selections propagate correctly
- ✅ Dynamic regression lines appear

### ✅ **Three Visualization Systems + Generalized Selection**
- System A: Temporal Analysis (4 linked views)
- System B: Statistical Distribution (4 linked views)
- System C: Small Multiples (4 linked views)
- Generalized Selection: Hierarchical temporal abstraction

### ✅ **Export to Altair Viewer**
- Each system has an "Export" button
- Saves HTML file for standalone viewing
- Can be opened in Altair Viewer separately

---

## 🚀 How to Run

### Step 1: Start the Dashboard

```bash
cd /Users/niteshranjansingh/IV/GroupProject_IV_2026
streamlit run dashboard.py
```

### Step 2: Navigate

The dashboard will open in your browser at `http://localhost:8501`

**Sidebar Navigation:**
- 🏠 Home - Overview and statistics
- 📈 System A - Temporal Analysis
- 📊 System B - Statistical Distribution
- 📉 System C - Small Multiples
- 🔄 Generalized Selection - Hierarchical abstraction

---

## 🎨 System A: Temporal Analysis

### Views:
1. **Time Series** - Temperature over time
2. **Scatter Plot** - Humidity vs Visibility with regression line
3. **Bar Chart** - Temperature by season
4. **Histogram** - Wind speed distribution

### Interactions:
- 🖱️ **Brush on time series** (click and drag horizontally)
  - All 4 views update instantly

- 🖱️ **Brush on scatter plot** (click and drag to select area)
  - Other views highlight selected data
  - Red regression line appears for selection

- 🖱️ **Click on season bar**
  - Filters all views to that season

- 🔄 **All views linked bidirectionally**

### Export:
Click "💾 Export to Altair Viewer" button to save as HTML

---

## 📊 System B: Statistical Distribution

### Views:
1. **Heatmap** - Monthly temperature matrix (year × month)
2. **Box Plots** - Temperature distribution by season with outliers
3. **Scatter Plot** - Cloud cover vs humidity with polynomial regression
4. **Bar Chart** - Weather type distribution by season

### Interactions:
- 🖱️ **Click heatmap cells**
  - Select specific month-year combination
  - Cell gets black border when selected

- 🖱️ **Click box plot seasons**
  - Filter by season
  - See outliers highlighted

- 🖱️ **Brush scatter plot**
  - Select cloud cover patterns
  - Red polynomial regression line appears

- 🔗 **All selections linked**

### Export:
Click "💾 Export to Altair Viewer" button to save as HTML

---

## 📉 System C: Small Multiples & Faceting

### Views:
1. **Faceted Time Series** - 5 separate charts (one per year)
2. **Strip Plot** - Daily temperature points by season
3. **Bubble Chart** - Multi-dimensional (temp, wind, humidity, cloud)
4. **Histogram** - Temperature distribution by weather type

### Interactions:
- 📅 **Dropdown filter** (top of page)
  - Select specific year or "All Years"
  - Affects all views immediately

- 🖱️ **Brush on faceted charts**
  - Select across any of the 5 year charts
  - All other views update

- 🎯 **Strip plot reveals outliers**
  - Each tick is one day
  - Easy to spot extreme values

- 🫧 **Bubble chart**
  - Size = humidity
  - Color = cloud cover
  - Hover for details

### Export:
Click "💾 Export to Altair Viewer" button to save as HTML

---

## 🔄 Generalized Selection: Hierarchical Temporal Abstraction

### **This is NOT Global Filtering!**

Generalized selection implements true semantic hierarchical abstraction based on temporal relationships.

### Hierarchy Levels:
```
Level 4: Year    (e.g., "All of 2015")
    ↑ generalizes
Level 3: Season  (e.g., "Winter 2015")
    ↑ generalizes
Level 2: Month   (e.g., "January 2015")
    ↑ generalizes
Level 1: Week    (e.g., "Week 2 of January 2015")
    ↑ generalizes
Level 0: Day     (e.g., "January 8, 2015")
```

### How to Use:

1. **Select hierarchy level** using radio buttons (top left)

2. **Click or brush** on the time series chart

3. **Watch the magic happen!**
   - All aggregation bars light up at their respective levels
   - Week bars show selected weeks
   - Month bars show selected months
   - Season bars show selected seasons
   - Year bars show selected years
   - Scatter plot updates to show selected temporal range

4. **Change hierarchy level** to see selection expand/contract

### Example Workflow:

**Scenario:** Select January 8, 2015 at Day level, then generalize up

1. Set radio button to "Day (Level 0)"
2. Click on January 8, 2015 in time series
3. → Only that one day is highlighted (red line)
4. → Week bar shows Week 2 is partially selected
5. → Month bar shows January 2015 is partially selected

**Now generalize to Week:**

1. Change radio to "Week (Level 1)"
2. → Selection expands to entire Week 2
3. → All 7 days in that week turn red
4. → Week bar for Week 2 lights up fully

**Generalize to Month:**

1. Change radio to "Month (Level 2)"
2. → Selection expands to all of January 2015
3. → All 31 days turn red
4. → Month bar for January 2015 lights up fully

**And so on...**

This demonstrates TRUE hierarchical semantic abstraction!

### Views:
1. **Time Series** - With hierarchical selection overlay (red)
2. **Week Aggregation Bars** - Shows week-level selection
3. **Month Aggregation Bars** - Shows month-level selection
4. **Season Aggregation Bars** - Shows season-level selection
5. **Year Aggregation Bars** - Shows year-level selection
6. **Scatter Plot** - Updates based on temporal selection

### Export:
Click "💾 Export to Altair Viewer" button to save complete hierarchy visualization

---

## 💾 Export Feature

Each system page has an "Export to Altair Viewer" button at the bottom.

**When you click it:**
1. Saves the current visualization as HTML file
2. Saves to appropriate folder:
   - SystemA/system_a_visualization.html
   - SystemB/system_b_visualization.html
   - SystemC/system_c_visualization.html
   - SystemA/system_a_with_generalization.html

**To open in Altair Viewer:**
```bash
# Option 1: Open HTML in browser
open SystemA/system_a_visualization.html

# Option 2: Use Altair Viewer directly
python3 -c "import altair as alt; chart = alt.Chart.from_json(open('SystemA/system_a_spec.json').read()); chart.show()"
```

---

## 🎯 Key Differences from Previous Version

### ✅ BEFORE (app.py):
- ❌ Opened visualizations in separate windows
- ❌ Subprocess launching
- ❌ Browser-based but not embedded
- ❌ Filters might not work properly

### ✅ NOW (dashboard.py):
- ✅ Everything embedded in ONE dashboard
- ✅ All filters work natively in Streamlit
- ✅ Radio buttons work perfectly
- ✅ PowerBI-style grid layout
- ✅ Professional design
- ✅ Instant interactions
- ✅ Can still export to Altair Viewer
- ✅ All Altair features work correctly

---

## 🛠️ Technical Details

### How It Works:

1. **Streamlit renders Altair charts natively**
   - Uses `st.altair_chart()`
   - Vega-Lite specs rendered in browser
   - All interactions work via Vega-Lite

2. **Selection parameters propagate correctly**
   - `alt.selection_interval()` for brushing
   - `alt.selection_point()` for clicking
   - Combined with `|` operator for multi-selection
   - `alt.condition()` for visual feedback

3. **Layout uses Streamlit columns**
   - `st.columns()` creates grid layout
   - `st.altair_chart()` displays charts
   - Wide layout mode for more space

4. **Filters use Streamlit widgets**
   - `st.radio()` for radio buttons (Generalized Selection)
   - `st.selectbox()` for dropdowns (System C)
   - State managed by Streamlit automatically

---

## ✅ Verification

### Test All Features:

**System A:**
- [ ] Brush time series → other views update
- [ ] Brush scatter → other views update
- [ ] Click season bar → all views filter
- [ ] Red regression line appears when data selected

**System B:**
- [ ] Click heatmap cell → gets black border
- [ ] Click box plot season → filters data
- [ ] Brush scatter → red polynomial line appears
- [ ] All views update together

**System C:**
- [ ] Dropdown changes year → all views update
- [ ] Faceted charts show 5 years side-by-side
- [ ] Brush on facets → other views update
- [ ] Bubble size changes with selection

**Generalized Selection:**
- [ ] Radio buttons change level
- [ ] Click time series → red highlight appears
- [ ] Aggregation bars light up at all levels
- [ ] Scatter plot updates with temporal selection

**Export:**
- [ ] Export button creates HTML file
- [ ] HTML file can be opened independently
- [ ] Interactions work in exported HTML

---

## 📝 Summary

**Run Command:**
```bash
streamlit run dashboard.py
```

**What You Get:**
- ✅ PowerBI-style dashboard
- ✅ All visualizations embedded
- ✅ All filters & interactions working
- ✅ Radio buttons working
- ✅ Dropdown filters working
- ✅ Brushing & linking working
- ✅ Export to Altair Viewer available
- ✅ Professional, clean design
- ✅ Fast, responsive interface

**This meets your requirements:**
- ✅ Altair-based (uses Altair 5.5.0)
- ✅ Dashboard landing page
- ✅ Visualizations in squares/grid
- ✅ All filters working
- ✅ Radio buttons working
- ✅ Can export to Altair Viewer
- ✅ PowerBI-style layout

---

**Ready to Use!** 🎉

Run `streamlit run dashboard.py` and explore the interactive dashboard!
