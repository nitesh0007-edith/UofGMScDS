# 🎯 QUICK START GUIDE

## Run the Dashboard

```bash
cd /Users/niteshranjansingh/IV/GroupProject_IV_2026
streamlit run dashboard.py
```

## What You'll See

### 🏠 Home Page (Landing)
- Statistics cards with key metrics
- 3 system cards in a grid
- Generalized selection card (highlighted)
- Professional PowerBI-style design

### 📈 System A
- Time series (brush to select date range)
- Scatter plot (brush to select patterns)
- Season bars (click to filter)
- Histogram
- **All views linked bidirectionally**
- Red regression line on selection

### 📊 System B
- Heatmap (click cells to select month-year)
- Box plots (click seasons)
- Scatter with polynomial regression
- Weather distribution bars
- **All views update together**

### 📉 System C
- **Dropdown at top:** Filter by year
- Faceted time series (5 charts side-by-side)
- Strip plot (reveals outliers)
- Bubble chart (multi-dimensional)
- Histogram by weather type

### 🔄 Generalized Selection
- **Radio buttons at top:** Select hierarchy level (Day/Week/Month/Season/Year)
- Time series with hierarchical selection
- 4 aggregation bar charts (week/month/season/year)
- Scatter plot
- **Watch selection propagate across all levels!**

## ✅ All Interactions Work

- ✅ Radio buttons
- ✅ Dropdowns
- ✅ Brushing (click and drag)
- ✅ Clicking
- ✅ Linked views
- ✅ Dynamic regression lines
- ✅ Hierarchical selection
- ✅ Filtering

## 💾 Export Feature

Each system has "Export to Altair Viewer" button that saves HTML file for standalone viewing.

## 🎯 Key Features

1. **PowerBI-Style Dashboard** - Professional grid layout
2. **All Embedded** - No separate windows
3. **Native Altair** - Uses Altair 5.5.0 with st.altair_chart()
4. **All Filters Working** - Radio, dropdown, brush, click
5. **Fast & Responsive** - Instant updates
6. **Export Ready** - Save to Altair Viewer HTML

---

**That's it! Enjoy your interactive dashboard!** 🎉
