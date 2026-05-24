# Information Visualization Tutorials

Complete tutorial package for the Information Visualization (M) course at the University of Glasgow, 2024/25.

## 📦 What's Inside

This repository contains comprehensive tutorials for both Python/Altair and JavaScript/Vega-Lite implementations, covering all 6 essential topics required for your Information Visualization group project.

```
IV/
├── README.md                              # This file
├── python_altair_tutorials/               # Python/Altair tutorials
│   ├── README.md                          # Setup guide for Python
│   └── altair_complete_tutorial.ipynb     # Complete Jupyter notebook
└── javascript_vegalite_tutorials/         # JavaScript/Vega-Lite tutorials
    ├── README.md                          # Setup guide for JavaScript
    └── vegalite_complete_tutorial.html    # Complete HTML tutorial
```

## 🎯 Topics Covered

Both tutorial series cover the same 6 essential topics:

1. **Introduction** - Getting started with the visualization toolkit
2. **Marks and Encoding** - Visual elements and data mapping
3. **Data Transformation** - Filtering, calculating, and aggregating data
4. **Scales, Axes, and Legends** - Customizing visual mappings
5. **Multi-view Composition** - Combining charts into dashboards
6. **Interaction** - Creating dynamic, explorable visualizations

Based on the excellent [UW Data Visualization Curriculum](https://github.com/uwdata/visualization-curriculum) by Jeffrey Heer, Dominik Moritz, Jake VanderPlas, and Brock Craft.

## 🚀 Quick Start

### Choose Your Path

You need to implement **at least two visualization systems** for your project. You can choose:

- **Option A:** Both in Python/Altair
- **Option B:** Both in JavaScript/Vega-Lite
- **Option C:** One in Python, one in JavaScript ✨ (Recommended for learning!)

### Getting Started with Python/Altair

```bash
cd python_altair_tutorials
```

Then follow the [Python Tutorial README](python_altair_tutorials/README.md)

**Best for:**
- Data analysis and exploration
- Statistical computing
- Machine learning integration
- Python developers

### Getting Started with JavaScript/Vega-Lite

```bash
cd javascript_vegalite_tutorials
```

Then follow the [JavaScript Tutorial README](javascript_vegalite_tutorials/README.md)

**Best for:**
- Web-based visualizations
- Advanced interactions
- Easy sharing (just HTML file)
- Standalone applications

## 📚 Tutorial Features

### Python/Altair Tutorial

- ✅ **Format:** Jupyter Notebook (.ipynb)
- ✅ **Environment:** VS Code with Python extension
- ✅ **Execution:** Run cells interactively
- ✅ **Learning Style:** Code + outputs + explanations
- ✅ **Beginner-Friendly:** Extensive comments and examples
- ✅ **Dataset:** Cars dataset included (via vega_datasets)

**Technologies:**
- Python 3.7+
- Altair 5.x
- Pandas
- Jupyter

### JavaScript/Vega-Lite Tutorial

- ✅ **Format:** Single HTML file
- ✅ **Environment:** Any modern browser + VS Code
- ✅ **Execution:** Open in browser (with Live Server)
- ✅ **Learning Style:** Visual examples + code specs
- ✅ **Beginner-Friendly:** No JavaScript experience required
- ✅ **Dataset:** Cars dataset loaded from Vega CDN

**Technologies:**
- HTML5
- JavaScript (Vega-Lite JSON specs)
- Vega 5
- Vega-Lite 5
- Vega-Embed 6

## 🎓 Learning Path

### Week 2: Python/Altair (Lab 1)
1. Read the lab instructions (IV Lab 1 information.pdf)
2. Follow the [Python Tutorial README](python_altair_tutorials/README.md)
3. Work through `altair_complete_tutorial.ipynb`
4. Experiment with examples
5. Try with your own data

### Week 3: JavaScript/Vega-Lite (Lab 2)
1. Read the lab instructions (IV Lab 2 information.pdf)
2. Follow the [JavaScript Tutorial README](javascript_vegalite_tutorials/README.md)
3. Open `vegalite_complete_tutorial.html` in browser
4. Experiment with specifications
5. Try the online [Vega Editor](https://vega.github.io/editor/)

### Ongoing: Project Work
1. Choose your implementation toolkit(s)
2. Start with simple visualizations
3. Iterate and add complexity
4. Focus on justification and evaluation for report

## 🔄 Python ↔ JavaScript Interoperability

**Good news:** Altair generates Vega-Lite JSON specifications, so you can:

1. **Prototype in Python:**
   ```python
   import altair as alt
   chart = alt.Chart(data).mark_point()...
   chart.save('spec.json')  # Export Vega-Lite JSON
   ```

2. **Use in JavaScript:**
   ```javascript
   // Load the JSON spec in your HTML
   vegaEmbed('#vis', 'spec.json');
   ```

This means you can:
- Explore data in Python/Jupyter
- Export to Vega-Lite JSON
- Create web visualizations easily

## 📊 Sample Datasets

Both tutorials use the **cars dataset** which includes:
- 406 cars from 1970-1982
- Variables: MPG, Horsepower, Weight, Acceleration, Origin, etc.
- Perfect for learning visualization techniques

**Additional datasets available:**
- Movies: `data.movies()`
- Weather: `data.weather()`
- Stocks: `data.stocks()`
- And many more in vega_datasets package

## 💡 Tips for Success

### Learning
- ✅ Work through tutorials sequentially
- ✅ Run every example
- ✅ Experiment with modifications
- ✅ Try both Python and JavaScript
- ✅ Practice with different datasets

### For Your Project
- ✅ Start simple, add complexity gradually
- ✅ Focus on telling a story with your data
- ✅ Use interaction to enable exploration
- ✅ Test with users and iterate
- ✅ Document design choices for your report

### Assessment Focus
Remember: The assessment focuses on your **written report**, specifically:
- Justification of design choices
- Evaluation of effectiveness
- But you still need **working code**!

## 🛠 VS Code Setup

Both tutorials use VS Code. Here's the recommended setup:

### Required Extensions
1. **Python** (by Microsoft) - For Python tutorials
2. **Jupyter** (by Microsoft) - For .ipynb files
3. **Live Server** (by Ritwick Dey) - For HTML tutorials

### Optional but Helpful
- **Prettier** - Code formatting
- **GitLens** - Git integration
- **Code Spell Checker** - Catch typos

### Installation
1. Open VS Code
2. Go to Extensions (⌘+Shift+X / Ctrl+Shift+X)
3. Search and install each extension

## 📖 Additional Resources

### Official Documentation
- [Altair Documentation](https://altair-viz.github.io/)
- [Vega-Lite Documentation](https://vega.github.io/vega-lite/)
- [Vega Examples](https://vega.github.io/vega-lite/examples/)

### UW Data Curriculum
- [GitHub Repo](https://github.com/uwdata/visualization-curriculum)
- [Altair Tutorials](https://uwdata.github.io/visualization-curriculum/)
- [Observable Notebooks](https://observablehq.com/@uwdata)

### Learning Resources
**Python:**
- [LearnPython.org](https://www.learnpython.org/)
- [Python for Everybody](http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf)

**JavaScript:**
- [JavaScript.info](https://javascript.info/)
- [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

### Online Tools
- [Vega Editor](https://vega.github.io/editor/) - Live editing
- [Observable](https://observablehq.com/) - Interactive notebooks
- [JSONLint](https://jsonlint.com/) - Validate JSON

## 🤝 Getting Help

### Lab Sessions
- **Format:** Drop-in sessions (attendance not required)
- **Purpose:** Technical advice and tutorial work
- **Lab Assistants:** Can guide you (but won't write code for you)
- **Professor Chalmers:** Available for theoretical questions
- **Location:** Boyd Orr lab (1028) or online via Zoom/Moodle

### Course Information
- **Course:** Information Visualisation (M)
- **Year:** 2024/25
- **Institution:** University of Glasgow

### Important Notes
- Lab assistants provide guidance, not solutions
- You learn best by doing and experimenting
- Don't hesitate to ask questions when stuck
- The community is there to help!

## 📝 Project Requirements

For your Information Visualization group project:

### Implementation Requirements
- ✅ Implement **at least 2 visualization systems**
- ✅ Working code is required
- ✅ Can use Python, JavaScript, or both

### Assessment Focus
- ✅ **Primary:** Written report
  - Justification of design choices
  - Evaluation of effectiveness
  - Analysis and insights
- ✅ **Secondary:** Working implementation
  - Must be functional
  - Must demonstrate concepts

### What These Tutorials Provide
- ✅ All technical skills needed
- ✅ Understanding of visualization principles
- ✅ Practical examples to build upon
- ✅ Foundation for project implementation

## 🎯 Learning Objectives

By completing these tutorials, you will be able to:

1. **Create visualizations** using both Altair and Vega-Lite
2. **Map data to visual properties** effectively
3. **Transform data** within visualizations
4. **Customize** scales, axes, and legends appropriately
5. **Compose** multiple views into dashboards
6. **Implement** interactive features
7. **Apply** these techniques to your own datasets
8. **Justify** visualization design choices
9. **Evaluate** visualization effectiveness

## 🌟 Key Takeaways

### Declarative Visualization
Both Altair and Vega-Lite use a **declarative** approach:
- Describe **what** you want, not **how** to draw it
- Framework handles the details
- Concise, readable specifications

### Grammar of Graphics
Both implement the **grammar of graphics**:
- **Data:** What to visualize
- **Marks:** Visual elements (points, bars, lines)
- **Encoding:** Mapping data to visual properties
- **Transforms:** Data manipulation
- **Scales:** Data to visual value mapping
- **Guides:** Axes and legends

### Interactivity
Both support **rich interaction**:
- Selections (click, brush)
- Bindings (dropdowns, sliders)
- Linked views
- Conditional encoding

## 🚦 Next Steps

1. **Choose your starting point:**
   - Familiar with Python? → Start with Altair
   - Want web visualizations? → Start with Vega-Lite
   - Want to learn both? → Start with either, then do the other

2. **Work through the tutorial:**
   - Read the respective README
   - Set up your environment
   - Run all examples
   - Experiment and modify

3. **Practice with your own data:**
   - Load your own datasets
   - Create visualizations
   - Combine techniques

4. **Start planning your project:**
   - Think about your data
   - Sketch visualization ideas
   - Consider user interactions
   - Plan your implementation

## ✨ Final Notes

These tutorials are designed to be:
- **Beginner-friendly** - No prior experience required
- **Comprehensive** - Cover all essential topics
- **Practical** - Hands-on examples you can run
- **Self-paced** - Work at your own speed
- **Extendable** - Foundation to build upon

**Remember:** The goal is not just to learn tools, but to understand **principles of effective visualization** that you can apply in any context.

Good luck with your Information Visualization project! 🎨📊

---

**Course:** Information Visualisation (M), 2024/25
**Institution:** University of Glasgow
**Based on:** [UW Data Visualization Curriculum](https://github.com/uwdata/visualization-curriculum)
**Created:** January 2026
