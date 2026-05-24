# JavaScript Vega-Lite Tutorials for Information Visualization

Welcome to the JavaScript/Vega-Lite tutorial series! This tutorial covers all 6 essential topics required for your Information Visualization project at the University of Glasgow.

## 📚 What's Covered

This tutorial series covers:

1. **Introduction to Vega-Lite** - Basic chart structure and JSON syntax
2. **Marks and Encoding** - Visual elements and data mapping
3. **Data Transformation** - Filtering, calculating, aggregating data
4. **Scales, Axes, and Legends** - Customizing visual mappings
5. **Multi-view Composition** - Combining multiple charts into dashboards
6. **Interaction** - Creating dynamic, explorable visualizations

Based on the [UW Data Visualization Curriculum](https://github.com/uwdata/visualization-curriculum)

## 🚀 Getting Started

### Prerequisites

- A modern web browser (Chrome, Firefox, Safari, or Edge)
- Visual Studio Code (VS Code)
- No prior JavaScript experience required!

### Step 1: Install VS Code

Download and install VS Code from [code.visualstudio.com](https://code.visualstudio.com/)

### Step 2: Install Live Server Extension

The Live Server extension lets you run HTML files with live reload:

1. Open VS Code
2. Go to Extensions (⌘+Shift+X on Mac, Ctrl+Shift+X on Windows)
3. Search for "Live Server" by Ritwick Dey
4. Click Install

### Step 3: Open the Tutorial

1. In VS Code, open the `javascript_vegalite_tutorials` folder
2. Open the file `vegalite_complete_tutorial.html`

### Step 4: Run the Tutorial

**Method 1: Using Live Server (Recommended)**
1. Right-click anywhere in the HTML file
2. Select "Open with Live Server"
3. Your browser will open with the tutorial
4. Any changes you make will automatically refresh!

**Method 2: Direct Browser Open**
1. In VS Code, right-click the `vegalite_complete_tutorial.html` file
2. Select "Reveal in Finder" (Mac) or "Reveal in File Explorer" (Windows)
3. Double-click the file to open in your default browser

## 📖 How to Use This Tutorial

### Navigation

- Scroll through the tutorial sequentially
- Use the Table of Contents to jump to specific sections
- All visualizations are interactive - try clicking and dragging!

### Learning Approach

1. **Read the explanations** for each topic
2. **View the visualizations** - they're live and interactive
3. **Examine the code** shown in the gray boxes
4. **Experiment:** Modify the code and reload the page
5. **Practice:** Create your own variations

### Editing and Experimenting

The tutorial is a single HTML file containing:
- **HTML structure** - The page layout
- **JavaScript specifications** - The visualization code
- **CSS styling** - The visual appearance

To experiment:
1. Find the `<script>` section at the bottom of the file
2. Locate the visualization spec you want to modify (e.g., `spec1_1`, `spec2_1`)
3. Change parameters like:
   - Field names: `"field": "Horsepower"`
   - Colors: `"color": "#e74c3c"`
   - Chart types: `"mark": "point"` → `"mark": "bar"`
   - Width/height: `"width": 600`
4. Save the file (⌘+S or Ctrl+S)
5. If using Live Server, changes appear instantly!

## 🎨 Understanding Vega-Lite Specifications

Vega-Lite uses JSON (JavaScript Object Notation) to describe visualizations:

```javascript
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",  // Version
  "data": {"url": "path/to/data.json"},                           // Data source
  "mark": "point",                                                // Visual mark type
  "encoding": {                                                   // Map data to visuals
    "x": {"field": "Horsepower", "type": "quantitative"},
    "y": {"field": "Miles_per_Gallon", "type": "quantitative"}
  }
}
```

### Key Concepts

**Marks:** Visual elements
- `point`, `bar`, `line`, `area`, `rect`, `text`

**Encoding Channels:** Visual properties
- `x`, `y` - Position
- `color` - Color
- `size` - Size
- `shape` - Shape
- `opacity` - Transparency

**Data Types:**
- `quantitative` - Continuous numbers
- `nominal` - Unordered categories
- `ordinal` - Ordered categories
- `temporal` - Dates/times

## 📁 File Structure

```
javascript_vegalite_tutorials/
├── README.md                            # This file
└── vegalite_complete_tutorial.html      # All-in-one tutorial file
```

## 🎯 Learning Objectives

By the end of this tutorial, you will be able to:

- Create visualizations using Vega-Lite JSON specifications
- Understand the declarative grammar of graphics
- Map data to visual properties
- Transform data within visualizations
- Customize scales, axes, and legends
- Combine multiple views into dashboards
- Add interactive elements to visualizations
- Apply these skills to your own datasets

## 🔧 Creating Your Own Visualizations

### Using Your Own Data

Replace the data URL with your own:

```javascript
"data": {
  "url": "path/to/your/data.json"
  // or
  "values": [
    {"category": "A", "value": 28},
    {"category": "B", "value": 55},
    {"category": "C", "value": 43}
  ]
}
```

### Data Format

Vega-Lite expects data in JSON format:

```json
[
  {"name": "Item A", "value": 100, "category": "X"},
  {"name": "Item B", "value": 200, "category": "Y"},
  {"name": "Item C", "value": 150, "category": "X"}
]
```

### Creating a New Visualization

1. Copy an existing specification
2. Add a new div in the HTML:
   ```html
   <div id="my_viz"></div>
   ```
3. Create your spec:
   ```javascript
   const mySpec = { /* your spec here */ };
   ```
4. Embed it:
   ```javascript
   vegaEmbed('#my_viz', mySpec);
   ```

## 🌐 Online Tools

### Vega Editor
Try the [Vega Editor](https://vega.github.io/editor/) to:
- Experiment with specs online
- See changes in real-time
- Access example gallery
- Export visualizations

### Observable
[Observable](https://observablehq.com/@uwdata) offers:
- Interactive notebooks (like Jupyter for JavaScript)
- Live coding environment
- Community examples
- UW Data Lab notebooks

## 📚 Additional Resources

### Official Documentation
- [Vega-Lite Documentation](https://vega.github.io/vega-lite/)
- [Vega-Lite Examples](https://vega.github.io/vega-lite/examples/)
- [Vega-Lite Tutorials](https://vega.github.io/vega-lite/tutorials/getting_started.html)

### UW Data Curriculum (Observable)
- [Introduction to Vega-Lite](https://observablehq.com/@uwdata/introduction-to-vega-lite)
- [Data Types & Marks](https://observablehq.com/@uwdata/data-types-graphical-marks-and-visual-encoding-channels)
- [Data Transformation](https://observablehq.com/@uwdata/data-transformation)
- [Scales, Axes, Legends](https://observablehq.com/@uwdata/scales-axes-and-legends)
- [Multi-view Composition](https://observablehq.com/@uwdata/multi-view-composition)
- [Interaction](https://observablehq.com/@uwdata/interaction)

### Learning JavaScript
- [JavaScript.info](https://javascript.info/)
- [W3Schools JavaScript](https://www.w3schools.com/js/)
- [Codecademy JavaScript](https://www.codecademy.com/learn/introduction-to-javascript)

**Note:** You don't need extensive JavaScript knowledge for this tutorial! The focus is on Vega-Lite's JSON specifications.

## 🔧 Troubleshooting

### Visualizations Not Showing

1. **Check the browser console:**
   - Open Developer Tools (F12 or Cmd+Option+I)
   - Look for error messages in the Console tab

2. **Common issues:**
   - Missing comma in JSON
   - Mismatched brackets `{}` or `[]`
   - Typo in field names

3. **Validate JSON:**
   - Use [JSONLint](https://jsonlint.com/) to check syntax

### Live Server Not Working

1. Ensure Live Server extension is installed
2. Right-click directly on the HTML file
3. Or use the "Go Live" button in the bottom right of VS Code

### Data Loading Issues

If using local data files:
- Ensure data file is in the same folder
- Use relative paths: `"url": "./mydata.json"`
- For external data, ensure URL is accessible

## 💡 Tips for Your IV Project

### Why Consider JavaScript/Vega-Lite?

**Advantages:**
- **Web Integration:** Easy to embed in websites
- **Sharing:** Just send an HTML file
- **Interactive:** Built-in interaction support
- **Declarative:** Concise specifications
- **Cross-platform:** Works anywhere with a browser

**When to Use:**
- Advanced interaction requirements
- Web-based deployment
- Sharing with non-technical users
- Creating standalone visualizations

### Design Considerations

1. **Start Simple:** Begin with basic charts
2. **Iterate:** Add complexity gradually
3. **Test Interactions:** Ensure all interactions work smoothly
4. **Mobile Responsive:** Consider different screen sizes
5. **Accessibility:** Add proper titles and labels

### Combining with Python

You can use both!
- Use **Python/Altair** for data analysis and exploration
- Use **JavaScript/Vega-Lite** for final interactive visualizations
- Altair generates Vega-Lite JSON, so you can transfer specs between them!

### Exporting from Altair to Vega-Lite

```python
import altair as alt

chart = alt.Chart(data).mark_point()...
chart.save('chart_spec.json')  # Save as Vega-Lite JSON
```

Then use that JSON in your HTML file!

## 🎓 Next Steps

After completing this tutorial:

1. ✅ Work through all examples in the tutorial
2. ✅ Experiment by modifying specifications
3. ✅ Try the [Vega Editor](https://vega.github.io/editor/) online
4. ✅ Explore [Observable notebooks](https://observablehq.com/@uwdata)
5. ✅ Create visualizations with your own data
6. ✅ Compare with Python/Altair tutorial
7. ✅ Start planning your project visualizations

## 🆚 Python vs JavaScript: Quick Comparison

| Aspect | Python/Altair | JavaScript/Vega-Lite |
|--------|---------------|----------------------|
| **Syntax** | Python code | JSON specifications |
| **Environment** | Jupyter notebooks | Browser/HTML |
| **Data Analysis** | Excellent (pandas) | Limited (use Python first) |
| **Web Deployment** | Requires export | Native |
| **Learning Curve** | Familiar to Python users | Easier for beginners |
| **Sharing** | Export to HTML | Just send HTML file |

**Recommendation:** Learn both! They complement each other well.

## 📝 Assessment Note

While the lab work itself is not assessed:
- The tutorial covers material **essential for your project**
- Material **may appear in exams** (basic level)
- You must implement **working code** for your project
- Focus on **written report** (justification and evaluation)

## 🤝 Getting Help

### Lab Sessions
- Drop-in sessions available (check Moodle for schedule)
- Lab assistants can provide technical guidance
- Lecturers available for theoretical questions

### Remember
- Lab assistants **guide** you, not write code for you
- **Experiment** and make mistakes - that's how you learn!
- **Ask questions** when stuck

### Community Resources
- [Vega-Lite Google Group](https://groups.google.com/g/vega-js)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/vega-lite)
- [GitHub Issues](https://github.com/vega/vega-lite/issues)

## ✨ Why Vega-Lite is Awesome

> "Vega-Lite provides a concise JSON syntax for rapidly generating visualizations to support analysis."

Benefits:
- **Concise:** Less code, more visualization
- **Declarative:** Say what you want, not how to do it
- **Automatic:** Smart defaults handle details
- **Interactive:** Built-in interaction support
- **Composable:** Build complex views from simple parts

## 🎉 Have Fun!

Information Visualization is about telling stories with data. Vega-Lite makes it easy to explore, experiment, and create beautiful interactive visualizations. Enjoy the journey!

---

**Course:** Information Visualisation (M), 2024/25
**Institution:** University of Glasgow
**Based on:** UW Data Visualization Curriculum
