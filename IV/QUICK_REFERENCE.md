# Quick Reference Guide - Altair & Vega-Lite

Fast reference for common visualization patterns in both Python/Altair and JavaScript/Vega-Lite.

## 📊 Basic Chart Structure

### Python/Altair
```python
import altair as alt

chart = alt.Chart(data).mark_point().encode(
    x='field1',
    y='field2'
)
```

### JavaScript/Vega-Lite
```javascript
const spec = {
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": {"url": "data.json"},
  "mark": "point",
  "encoding": {
    "x": {"field": "field1", "type": "quantitative"},
    "y": {"field": "field2", "type": "quantitative"}
  }
};
```

## 📈 Common Mark Types

| Visualization | Python | JavaScript |
|---------------|--------|------------|
| Scatter plot | `.mark_point()` | `"mark": "point"` |
| Bar chart | `.mark_bar()` | `"mark": "bar"` |
| Line chart | `.mark_line()` | `"mark": "line"` |
| Area chart | `.mark_area()` | `"mark": "area"` |
| Heatmap | `.mark_rect()` | `"mark": "rect"` |
| Text labels | `.mark_text()` | `"mark": "text"` |

## 🎨 Encoding Channels

### Python/Altair
```python
.encode(
    x='field',                    # Position
    y='field',
    color='field',                # Color
    size='field',                 # Size
    shape='field',                # Shape
    opacity='field',              # Opacity
    tooltip=['field1', 'field2']  # Tooltip
)
```

### JavaScript/Vega-Lite
```javascript
"encoding": {
  "x": {"field": "field", "type": "quantitative"},
  "y": {"field": "field", "type": "quantitative"},
  "color": {"field": "field", "type": "nominal"},
  "size": {"field": "field", "type": "quantitative"},
  "shape": {"field": "field", "type": "nominal"},
  "opacity": {"field": "field", "type": "quantitative"},
  "tooltip": [
    {"field": "field1"},
    {"field": "field2"}
  ]
}
```

## 🔤 Data Types

| Type | Description | Python | JavaScript |
|------|-------------|--------|------------|
| Quantitative | Continuous numbers | `:Q` or `type='quantitative'` | `"type": "quantitative"` |
| Nominal | Unordered categories | `:N` or `type='nominal'` | `"type": "nominal"` |
| Ordinal | Ordered categories | `:O` or `type='ordinal'` | `"type": "ordinal"` |
| Temporal | Dates/times | `:T` or `type='temporal'` | `"type": "temporal"` |

### Python Shorthand
```python
x='Horsepower:Q'      # Quantitative
color='Origin:N'      # Nominal
y='Cylinders:O'       # Ordinal
x='Year:T'            # Temporal
```

## 📊 Aggregation

### Python/Altair
```python
# In encoding
y='mean(Miles_per_Gallon)'
y='count()'
y='sum(Sales)'
y='median(Price)'

# Or using alt.X/Y
y=alt.Y('Miles_per_Gallon', aggregate='mean')
```

### JavaScript/Vega-Lite
```javascript
"y": {
  "aggregate": "mean",  // count, sum, median, min, max
  "field": "Miles_per_Gallon",
  "type": "quantitative"
}
```

## 🔧 Data Transformation

### Filtering

**Python:**
```python
.transform_filter(
    alt.datum.Miles_per_Gallon > 30
)
```

**JavaScript:**
```javascript
"transform": [
  {"filter": "datum.Miles_per_Gallon > 30"}
]
```

### Calculate New Fields

**Python:**
```python
.transform_calculate(
    hp_per_cyl='datum.Horsepower / datum.Cylinders'
)
```

**JavaScript:**
```javascript
"transform": [
  {
    "calculate": "datum.Horsepower / datum.Cylinders",
    "as": "hp_per_cyl"
  }
]
```

### Binning

**Python:**
```python
x=alt.X('Horsepower', bin=alt.Bin(maxbins=20))
```

**JavaScript:**
```javascript
"x": {
  "bin": {"maxbins": 20},
  "field": "Horsepower"
}
```

## 🎨 Customizing Scales

### Color Scale

**Python:**
```python
color=alt.Color('Origin',
    scale=alt.Scale(
        domain=['USA', 'Europe', 'Japan'],
        range=['red', 'blue', 'green']
    )
)
```

**JavaScript:**
```javascript
"color": {
  "field": "Origin",
  "scale": {
    "domain": ["USA", "Europe", "Japan"],
    "range": ["red", "blue", "green"]
  }
}
```

### Scale Types

**Python:**
```python
x=alt.X('field', scale=alt.Scale(type='log'))
```

**JavaScript:**
```javascript
"x": {
  "field": "field",
  "scale": {"type": "log"}  // linear, log, sqrt, time, etc.
}
```

## 📏 Customizing Axes

### Python/Altair
```python
x=alt.X('Horsepower',
    axis=alt.Axis(
        title='Horsepower (HP)',
        titleFontSize=14,
        grid=True,
        format='.2f'
    )
)
```

### JavaScript/Vega-Lite
```javascript
"x": {
  "field": "Horsepower",
  "axis": {
    "title": "Horsepower (HP)",
    "titleFontSize": 14,
    "grid": true,
    "format": ".2f"
  }
}
```

## 🎭 Customizing Legends

### Python/Altair
```python
color=alt.Color('Origin',
    legend=alt.Legend(
        title='Country',
        orient='right',
        titleFontSize=14
    )
)
```

### JavaScript/Vega-Lite
```javascript
"color": {
  "field": "Origin",
  "legend": {
    "title": "Country",
    "orient": "right",
    "titleFontSize": 14
  }
}
```

## 📐 Chart Properties

### Python/Altair
```python
.properties(
    width=600,
    height=400,
    title='My Chart'
)
```

### JavaScript/Vega-Lite
```javascript
"width": 600,
"height": 400,
"title": "My Chart"
```

## 🔄 Multi-view Composition

### Horizontal Concatenation (Side by Side)

**Python:**
```python
chart1 | chart2
# or
alt.hconcat(chart1, chart2)
```

**JavaScript:**
```javascript
{
  "hconcat": [spec1, spec2]
}
```

### Vertical Concatenation (Stacked)

**Python:**
```python
chart1 & chart2
# or
alt.vconcat(chart1, chart2)
```

**JavaScript:**
```javascript
{
  "vconcat": [spec1, spec2]
}
```

### Layering (Overlay)

**Python:**
```python
chart1 + chart2
# or
alt.layer(chart1, chart2)
```

**JavaScript:**
```javascript
{
  "layer": [spec1, spec2]
}
```

### Faceting (Small Multiples)

**Python:**
```python
.facet(column='Origin')
# or
.facet(row='Year', column='Origin')
```

**JavaScript:**
```javascript
"facet": {"column": {"field": "Origin"}}
// or
"facet": {
  "row": {"field": "Year"},
  "column": {"field": "Origin"}
}
```

## 🖱️ Interaction

### Selection (Click)

**Python:**
```python
selection = alt.selection_point(fields=['Origin'])

chart = alt.Chart(data).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color=alt.condition(selection, 'Origin', alt.value('lightgray'))
).add_params(selection)
```

**JavaScript:**
```javascript
{
  "params": [{
    "name": "selection",
    "select": {"type": "point", "fields": ["Origin"]}
  }],
  "mark": "point",
  "encoding": {
    "color": {
      "condition": {"param": "selection", "field": "Origin"},
      "value": "lightgray"
    }
  }
}
```

### Brush Selection (Drag)

**Python:**
```python
brush = alt.selection_interval()

chart = alt.Chart(data).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color=alt.condition(brush, 'Origin', alt.value('lightgray'))
).add_params(brush)
```

**JavaScript:**
```javascript
{
  "params": [{
    "name": "brush",
    "select": {"type": "interval"}
  }],
  "mark": "point",
  "encoding": {
    "color": {
      "condition": {"param": "brush", "field": "Origin"},
      "value": "lightgray"
    }
  }
}
```

### Dropdown Binding

**Python:**
```python
dropdown = alt.binding_select(
    options=[None, 'USA', 'Europe', 'Japan'],
    name='Origin: '
)
selection = alt.selection_point(
    fields=['Origin'],
    bind=dropdown
)
```

**JavaScript:**
```javascript
{
  "params": [{
    "name": "selection",
    "select": {"type": "point", "fields": ["Origin"]},
    "bind": {
      "input": "select",
      "options": [null, "USA", "Europe", "Japan"],
      "name": "Origin: "
    }
  }]
}
```

### Slider Binding

**Python:**
```python
slider = alt.binding_range(min=1970, max=1982, step=1, name='Year: ')
selection = alt.param(value=1970, bind=slider)

chart.add_params(selection).transform_filter(
    alt.datum.Year >= selection
)
```

**JavaScript:**
```javascript
{
  "params": [{
    "name": "year_slider",
    "value": 1970,
    "bind": {
      "input": "range",
      "min": 1970,
      "max": 1982,
      "step": 1,
      "name": "Year: "
    }
  }],
  "transform": [
    {"filter": "datum.Year >= year_slider"}
  ]
}
```

## 💾 Data Loading

### Python/Altair
```python
# From pandas DataFrame
chart = alt.Chart(df)

# From URL
chart = alt.Chart('https://example.com/data.json')

# From file
chart = alt.Chart('data.csv')

# From vega_datasets
from vega_datasets import data
cars = data.cars()
chart = alt.Chart(cars)
```

### JavaScript/Vega-Lite
```javascript
// From URL
"data": {"url": "https://example.com/data.json"}

// From file (relative path)
"data": {"url": "./data.json"}

// Inline data
"data": {
  "values": [
    {"x": 1, "y": 28},
    {"x": 2, "y": 55}
  ]
}
```

## 💡 Common Patterns

### Histogram

**Python:**
```python
alt.Chart(data).mark_bar().encode(
    x=alt.X('field', bin=alt.Bin(maxbins=20)),
    y='count()'
)
```

**JavaScript:**
```javascript
{
  "mark": "bar",
  "encoding": {
    "x": {"bin": {"maxbins": 20}, "field": "field"},
    "y": {"aggregate": "count"}
  }
}
```

### Scatter Plot with Regression

**Python:**
```python
points = alt.Chart(data).mark_point().encode(x='x', y='y')
line = alt.Chart(data).mark_line(color='red').encode(
    x='x', y='y'
).transform_regression('x', 'y')

points + line
```

**JavaScript:**
```javascript
{
  "layer": [
    {
      "mark": "point",
      "encoding": {"x": {"field": "x"}, "y": {"field": "y"}}
    },
    {
      "mark": {"type": "line", "color": "red"},
      "transform": [{"regression": "y", "on": "x"}],
      "encoding": {"x": {"field": "x"}, "y": {"field": "y"}}
    }
  ]
}
```

### Grouped Bar Chart

**Python:**
```python
alt.Chart(data).mark_bar().encode(
    x='category',
    y='value',
    color='group',
    xOffset='group'  # Dodge bars
)
```

**JavaScript:**
```javascript
{
  "mark": "bar",
  "encoding": {
    "x": {"field": "category"},
    "y": {"field": "value"},
    "color": {"field": "group"},
    "xOffset": {"field": "group"}
  }
}
```

## 🎯 Quick Tips

### Python/Altair
- Use `.interactive()` to enable pan and zoom
- Chain methods: `.mark_point().encode().properties()`
- Use `alt.X()` and `alt.Y()` for detailed control
- Save charts: `chart.save('output.html')`

### JavaScript/Vega-Lite
- Validate JSON syntax (use JSONLint)
- Test in Vega Editor online first
- Use `vegaEmbed('#id', spec)` to render
- Check browser console for errors

## 🐛 Common Issues

### Python
```python
# Issue: Charts not showing
alt.renderers.enable('default')

# Issue: Row limit exceeded
alt.data_transformers.disable_max_rows()

# Issue: Wrong data type
x='field:Q'  # Explicitly specify type
```

### JavaScript
```javascript
// Issue: Missing comma
{
  "x": {"field": "x"},  // ← Don't forget this comma
  "y": {"field": "y"}
}

// Issue: Wrong quotes
"field": "Horsepower"  // Use double quotes, not single

// Issue: Undefined field
// Check field names match your data exactly
```

## 📚 Where to Learn More

- **Altair:** https://altair-viz.github.io/
- **Vega-Lite:** https://vega.github.io/vega-lite/
- **Examples:** https://vega.github.io/vega-lite/examples/
- **Editor:** https://vega.github.io/editor/
- **UW Curriculum:** https://github.com/uwdata/visualization-curriculum

---

**Keep this reference handy while working on your visualizations!** 📊✨
