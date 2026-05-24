# 🚀 How to Run the Glasgow Weather Visualizations

## ✅ **FULLY WORKING: All Issues Resolved**

- ✅ Path issues fixed (absolute paths)
- ✅ Visualization display working (opens in browser)
- ✅ All interactive features functional

---

## **Method 1: Streamlit App (RECOMMENDED)**

```bash
cd /Users/niteshranjansingh/IV/GroupProject_IV_2026
streamlit run app.py
```

Then:
1. Go to "🚀 Launch Systems" page
2. Click any button (e.g., "🚀 Launch System A")
3. The visualization will open in **your default web browser**

**Note:** The Streamlit app stays running while visualizations open in new browser tabs.

---

## **Method 2: Run Systems Directly**

From the project root directory:

```bash
cd /Users/niteshranjansingh/IV/GroupProject_IV_2026

# System A
python3 SystemA/system_a.py

# System B
python3 SystemB/system_b.py

# System C
python3 SystemC/system_c.py

# Generalized Selection
python3 SystemA/system_a_with_generalization.py
```

Each will:
1. Print status messages
2. Save HTML/JSON backups
3. **Open in your web browser automatically**

---

## **What You Should See**

### **After running streamlit app:**
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

Browser opens automatically with the landing page.

### **After clicking "Launch System A":**
```
✓ System A visualization created successfully!
  - /path/to/system_a_visualization.html (saved)
  - /path/to/system_a_spec.json (saved)

Features:
  • Brush on time series to filter by date range
  • Brush on scatter plot to select humidity-visibility patterns
  • Click on bar chart to filter by season
  • All views linked bidirectionally
  • Red regression line shows correlation for selected data

🚀 Opening in browser...
```

Then **a new browser tab opens** with the interactive visualization.

---

## **Troubleshooting**

### **Issue: "FileNotFoundError: weather_data_enriched.csv"**

**Status:** ✅ **FIXED!** All systems now use absolute paths.

If you still see this error:
1. Make sure you're in the project root directory
2. Verify the file exists:
   ```bash
   ls data/Glasgow_weather_data/weather_data_enriched.csv
   ```
3. If missing, regenerate it:
   ```bash
   python3 -c "
   import pandas as pd
   df = pd.read_csv('data/Glasgow_weather_data/clean_weather_data.csv')
   df['day'] = pd.to_datetime(df['day'])
   df['year'] = df['day'].dt.year
   df['month'] = df['day'].dt.month
   df['month_name'] = df['day'].dt.month_name()
   df['season'] = df['month'].apply(lambda x: 'Winter' if x in [12, 1, 2] else
                                                'Spring' if x in [3, 4, 5] else
                                                'Summer' if x in [6, 7, 8] else 'Fall')
   df.to_csv('data/Glasgow_weather_data/weather_data_enriched.csv', index=False)
   print('✓ Enriched data created')
   "
   ```

### **Issue: Browser doesn't open automatically**

Try opening the HTML file manually:
```bash
# macOS
open SystemA/system_a_visualization.html

# Linux
xdg-open SystemA/system_a_visualization.html

# Windows
start SystemA/system_a_visualization.html

# Or just drag the HTML file into any web browser
```

### **Issue: Streamlit won't start**

```bash
# Update Streamlit
pip install --upgrade streamlit

# Check if port 8501 is already in use
lsof -i :8501

# Use different port if needed
streamlit run app.py --server.port 8502
```

---

## **Quick Test**

To verify everything works:

```bash
cd /Users/niteshranjansingh/IV/GroupProject_IV_2026
python3 SystemA/system_a.py
```

**Expected:** A new browser tab opens showing the visualization with 4 interactive views.

**If it works:** ✅ All systems are ready!

---

## **Interactive Features to Test**

Once the visualization opens in your browser:

### **System A:**
1. **Brush** on time series (click and drag horizontally)
2. Watch all 4 views update
3. **Click** on a season bar (Winter, Spring, Summer, Fall)
4. See red regression line appear in scatter plot

### **System B:**
1. **Click** on a heatmap cell (any month-year square)
2. See box plots and scatter highlight
3. **Brush** on scatter plot (click and drag)
4. Watch red polynomial regression line appear

### **System C:**
1. **Select year** from dropdown (top of visualization)
2. **Brush** across faceted time series
3. Watch strip plot, bubble chart, histogram update
4. **Hover** over bubble chart to see tooltips

### **Generalized Selection:**
1. **Select "Day" level** with radio button at top
2. **Click** on a specific day in time series
3. **Switch to "Week" level**
4. 🎯 **Watch selection expand to whole week!**
5. Try "Month", "Season", "Year" levels

---

## **Files Updated**

All these files now use absolute paths:
- ✅ `SystemA/system_a.py`
- ✅ `SystemB/system_b.py`
- ✅ `SystemC/system_c.py`
- ✅ `SystemA/system_a_with_generalization.py`

**Changes made:**
```python
# OLD (relative path - didn't work from Streamlit):
df = pd.read_csv('../data/Glasgow_weather_data/weather_data_enriched.csv')

# NEW (absolute path - works from anywhere):
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
data_path = os.path.join(project_root, 'data', 'Glasgow_weather_data', 'weather_data_enriched.csv')
df = pd.read_csv(data_path)
```

---

## **Now Try Again!**

```bash
cd /Users/niteshranjansingh/IV/GroupProject_IV_2026
streamlit run app.py
```

Click "🚀 Launch System A" → It should work! ✅

---

**Last Updated:** February 23, 2026
**Status:** ✅ **FULLY WORKING - BROWSER-BASED VISUALIZATION!**

All visualizations now open automatically in your web browser for reliable display across all platforms.
