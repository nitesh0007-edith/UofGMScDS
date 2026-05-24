# Python Altair Tutorials for Information Visualization

Welcome to the Python/Altair tutorial series! This tutorial covers all 6 essential topics required for your Information Visualization project at the University of Glasgow.

## 📚 What's Covered

This tutorial series covers:

1. **Introduction to Altair** - Basic chart structure and syntax
2. **Marks and Encoding** - Visual elements and data mapping
3. **Data Transformation** - Filtering, calculating, aggregating data
4. **Scales, Axes, and Legends** - Customizing visual mappings
5. **Multi-view Composition** - Combining multiple charts into dashboards
6. **Interaction** - Creating dynamic, explorable visualizations

Based on the [UW Data Visualization Curriculum](https://github.com/uwdata/visualization-curriculum)

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Visual Studio Code (VS Code)
- Basic Python knowledge

### Step 1: Install Python (if needed)

Check if Python is installed:
```bash
python --version
# or
python3 --version
```

If not installed, download from [python.org](https://www.python.org/downloads/)

### Step 2: Set Up VS Code for Python

1. **Install VS Code** from [code.visualstudio.com](https://code.visualstudio.com/)

2. **Install Python Extension:**
   - Open VS Code
   - Go to Extensions (⌘+Shift+X on Mac, Ctrl+Shift+X on Windows)
   - Search for "Python" by Microsoft
   - Click Install

3. **Install Jupyter Extension:**
   - In Extensions, search for "Jupyter"
   - Install the Jupyter extension by Microsoft

### Step 3: Create a Virtual Environment (Recommended)

Open Terminal in VS Code (Terminal → New Terminal) and run:

```bash
# Navigate to the python_altair_tutorials folder
cd python_altair_tutorials

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Mac/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

You should see `(venv)` in your terminal prompt.

### Step 4: Install Required Packages

With the virtual environment activated, install the required packages:

```bash
pip install --upgrade pip
pip install altair pandas vega_datasets numpy jupyter notebook
```

Verify installation:
```bash
pip list | grep altair
```

You should see altair and related packages listed.

### Step 5: Open the Tutorial Notebook

1. In VS Code, open the `altair_complete_tutorial.ipynb` file
2. VS Code will prompt you to select a kernel - choose the Python environment you just created (`venv`)
3. You're ready to go! Run cells using Shift+Enter

## 📖 How to Use This Tutorial

### Running Code Cells

- **Run a single cell:** Click the ▶️ button or press `Shift+Enter`
- **Run all cells:** Click "Run All" at the top of the notebook
- **Clear outputs:** Right-click and select "Clear All Outputs"

### Learning Approach

1. **Read the explanations** in markdown cells
2. **Run each code cell** to see the output
3. **Experiment:** Modify the code and see what changes
4. **Practice:** Try creating your own variations

### Tips for Success

- Work through the notebook sequentially
- Don't skip the early examples - they build foundational knowledge
- Read all comments in the code
- Experiment with different parameters
- Save your experiments in a separate notebook

## 📁 File Structure

```
python_altair_tutorials/
├── README.md                          # This file
├── altair_complete_tutorial.ipynb     # Main tutorial notebook
└── venv/                              # Virtual environment (after setup)
```

## 🎯 Learning Objectives

By the end of this tutorial, you will be able to:

- Create basic and advanced visualizations using Altair
- Map data to visual properties (marks and encoding)
- Transform data within visualizations
- Customize scales, axes, and legends
- Combine multiple views into dashboards
- Add interactive elements to your visualizations
- Apply these skills to your own datasets

## 🔧 Troubleshooting

### Charts Not Displaying

If charts don't display:

```python
import altair as alt
alt.renderers.enable('default')
```

### "Data exceeds 5000 rows" Error

Altair has a default row limit for safety:

```python
alt.data_transformers.disable_max_rows()
```

### Kernel Not Found

1. Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows)
2. Type "Python: Select Interpreter"
3. Choose the venv interpreter

### Package Import Errors

Reinstall packages:
```bash
pip install --force-reinstall altair pandas vega_datasets
```

## 📚 Additional Resources

### Official Documentation
- [Altair Documentation](https://altair-viz.github.io/)
- [Altair Example Gallery](https://altair-viz.github.io/gallery/index.html)
- [Vega-Lite Documentation](https://vega.github.io/vega-lite/)

### UW Data Curriculum
- [GitHub Repository](https://github.com/uwdata/visualization-curriculum)
- [Introduction Tutorial](https://uwdata.github.io/visualization-curriculum/altair_introduction.html)
- [Marks and Encoding](https://uwdata.github.io/visualization-curriculum/altair_marks_encoding.html)
- [Data Transformation](https://uwdata.github.io/visualization-curriculum/altair_data_transformation.html)
- [Scales, Axes, Legends](https://uwdata.github.io/visualization-curriculum/altair_scales_axes_legends.html)
- [Multi-view Composition](https://uwdata.github.io/visualization-curriculum/altair_view_composition.html)
- [Interaction](https://uwdata.github.io/visualization-curriculum/altair_interaction.html)

### Learning Python
- [LearnPython.org](https://www.learnpython.org/)
- [W3Schools Python](https://www.w3schools.com/python/)
- [Python for Everybody](http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf)

### Sample Datasets
- [Vega Datasets](https://github.com/vega/vega-datasets)
- Your notebook includes the cars dataset, but many others are available

## 💡 Tips for Your IV Project

### Design Considerations
1. **Start Simple:** Begin with basic charts, then add complexity
2. **Know Your Audience:** Design for your users' needs
3. **Tell a Story:** Use visualizations to communicate insights
4. **Iterate:** Test and refine your designs

### Technical Best Practices
1. **Document Your Code:** Add comments explaining your choices
2. **Use Version Control:** Commit your work regularly with git
3. **Test Interactions:** Make sure all interactive elements work
4. **Export Options:** Save visualizations as HTML for your report

### Saving Your Work

Save charts as HTML:
```python
chart.save('my_chart.html')
```

Save as JSON spec:
```python
chart.save('my_chart_spec.json')
```

Save as PNG (requires additional setup):
```python
# Install: pip install altair_saver selenium
chart.save('my_chart.png')
```

## 🎓 Next Steps

After completing this tutorial:

1. ✅ Work through all examples in the notebook
2. ✅ Experiment with your own data
3. ✅ Try combining techniques from different sections
4. ✅ Explore the JavaScript/Vega-Lite tutorial for comparison
5. ✅ Start planning your project visualizations

## 📝 Assessment Note

Remember: While the lab work itself is not assessed, the tutorials cover material that:
- Is essential for your group project implementation
- May appear in exams (at a basic level)
- Will help you justify and evaluate your designs in the project report

The focus is on your **written report** (justification and evaluation), but you must implement **working code**.

## 🤝 Getting Help

### Lab Sessions
- Drop-in sessions available (check Moodle for schedule)
- Lab assistants can provide technical guidance
- Prof. Chalmers available for theoretical questions

### Remember
- Lab assistants are there to **guide** you, not write code for you
- Learn by doing - experiment and make mistakes!
- Ask questions when stuck

## ✨ Good Luck!

Information Visualization is a powerful tool for understanding and communicating data. Have fun exploring and creating!

---

**Course:** Information Visualisation (M), 2024/25
**Institution:** University of Glasgow
**Based on:** UW Data Visualization Curriculum
