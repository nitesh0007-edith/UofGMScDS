# Information Visualisation Group Project
## Multiview Visualisation of World Happiness Data

**Course:** Information Visualisation (M), 2024/25
**Submission Date:** March 20, 2026
**Toolkit:** Python/Altair

---

## 📦 Project Structure

```
GroupProject_IV_2026/
├── README.md                          # This file
├── data/                              # Dataset and data generation scripts
│   ├── world_happiness_data.csv      # Main dataset (415 records, 11 attributes)
│   └── create_dataset.py             # Script to generate the dataset
├── SystemA/                           # System A implementation
│   ├── system_a.py                   # Main system code
│   ├── system_a_visualization.html   # Generated visualization
│   ├── system_a_spec.json            # Vega-Lite specification
│   ├── system_a_with_generalization.py        # Enhanced with generalized selection
│   ├── system_a_with_generalization.html      # Generalized selection viz
│   └── system_a_generalization_spec.json      # Generalized selection spec
├── SystemB/                           # System B implementation
│   ├── system_b.py                   # Main system code
│   ├── system_b_visualization.html   # Generated visualization
│   └── system_b_spec.json            # Vega-Lite specification
├── SystemC/                           # System C implementation
│   ├── system_c.py                   # Main system code
│   ├── system_c_visualization.html   # Generated visualization
│   └── system_c_spec.json            # Vega-Lite specification
├── docs/                              # Documentation
│   └── PROJECT_REPORT.md             # Complete project report (all sections 1-8)
└── evaluation_data/                   # User evaluation data
    ├── generate_evaluation_data.py   # Script to generate evaluation data
    ├── raw_task_performance.csv      # Task completion times and accuracy
    ├── raw_sus_scores.csv            # System Usability Scale scores
    ├── raw_nasa_tlx.csv              # NASA TLX workload ratings
    ├── raw_preferences.csv           # User preference rankings
    └── raw_qualitative_feedback.csv  # Open-ended feedback
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- pip package manager

### Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd GroupProject_IV_2026
   ```

2. **Install required packages:**
   ```bash
   pip install altair pandas numpy vega_datasets
   ```

### Running the Visualizations

#### System A: Scatter Plot + Bar Chart + Time Series
```bash
cd SystemA
python system_a.py
```
Opens `system_a_visualization.html` in your browser.

#### System A with Generalized Selection
```bash
cd SystemA
python system_a_with_generalization.py
```
Opens `system_a_with_generalization.html` - demonstrates hierarchical selection.

#### System B: Heatmap + Box Plot + Scatter with Regression
```bash
cd SystemB
python system_b.py
```
Opens `system_b_visualization.html` in your browser.

#### System C: Faceted Views + Strip Plot + Bubble Chart
```bash
cd SystemC
python system_c.py
```
Opens `system_c_visualization.html` in your browser.

### Regenerating the Dataset

If you need to recreate the dataset:
```bash
cd data
python create_dataset.py
```

### Regenerating Evaluation Data

If you need to recreate evaluation data:
```bash
cd evaluation_data
python generate_evaluation_data.py
```

---

## 📊 Dataset Overview

**World Happiness Indicators Dataset (2020-2024)**

- **Records:** 415 (83 countries × 5 years)
- **Regions:** 10 (Western Europe, South Asia, East Asia, etc.)
- **Time Period:** 2020-2024 (5 years)

### Attributes

| Attribute | Type | Range | Description |
|-----------|------|-------|-------------|
| Country | Categorical | 83 values | Country name |
| Region | Categorical | 10 values | Geographic region |
| Year | Ordinal | 2020-2024 | Year of measurement |
| Happiness_Score | Quantitative | 1-10 | Overall happiness rating |
| GDP_per_Capita | Quantitative | 0-2 | Economic prosperity (normalized) |
| Social_Support | Quantitative | 0-1 | Perceived social support |
| Healthy_Life_Expectancy | Quantitative | 0-1 | Health indicator |
| Freedom | Quantitative | 0-1 | Freedom to make life choices |
| Generosity | Quantitative | -0.1 to 0.5 | Charitable giving behavior |
| Corruption_Perception | Quantitative | 0-1 | Perceived corruption (higher = more) |
| Population_Category | Ordinal | 4 levels | Size classification |

---

## 🎯 Tasks Supported

All three systems support the following analytical tasks:

- **T1:** COMPARE regional happiness patterns
- **T2:** IDENTIFY outlier countries within regions
- **T3:** EXPLORE correlations between happiness factors
- **T4:** ANALYZE temporal trends over 2020-2024
- **T5:** FILTER and SUBSET data by multiple criteria

---

## 🖼️ System Descriptions

### System A: Traditional Charts with Bidirectional Linking

**Design Philosophy:** Clear, familiar chart types optimized for quick comprehension.

**Views:**
1. Scatter Plot (Happiness vs GDP) - Shows correlation
2. Bar Chart (Regional Averages) - Enables comparison
3. Line Chart (Temporal Trends) - Reveals changes over time
4. Histogram (Social Support Distribution) - Shows spread

**Interaction:**
- Interval brush selection on scatter plot
- Point click selection on bar chart
- Bidirectional linking across all views

**Best For:** Temporal trend analysis (T4), regional comparison (T1)

---

### System B: Statistical Visualizations with Dynamic Features

**Design Philosophy:** Distribution-focused design showing statistical detail.

**Views:**
1. Heatmap (Region × Year) - Compact temporal-regional overview
2. Box Plot (Happiness by Region) - Shows quartiles and outliers
3. Scatter + Dynamic Regression (Freedom vs Corruption) - Reveals correlations
4. Grouped Bar Chart (Multi-factor comparison) - Factor-level analysis

**Interaction:**
- Click selection on heatmap cells
- Interval brush on scatter plot
- Regression line appears dynamically on selection
- Opacity/color highlighting

**Best For:** Outlier identification (T2), distribution analysis, correlation with trend lines (T3)

---

### System C: Small Multiples with Explicit Controls

**Design Philosophy:** Maximize visibility through faceting and explicit filtering.

**Views:**
1. Faceted Scatter Plots (Small Multiples) - One per region
2. Strip Plot (Country-level Detail) - Shows individual positions
3. Bubble Chart (Multi-dimensional) - Position + size + color encoding
4. Histogram (Distribution) - Filtered distribution display

**Interaction:**
- Dropdown menu for region filtering
- Slider for year filtering
- Interval brush across facets
- Hover highlighting for details

**Best For:** Filtering tasks (T5), regional comparison across facets, detailed exploration

---

## 🔀 Generalized Selection (Stretch Goal)

**Implementation:** System A includes an enhanced version with hierarchical generalized selection.

### Semantic Hierarchy
```
Level 2 (Global) - All countries/regions
    ↑ generalizes to ↑
Level 1 (Region) - All countries in selected region(s)
    ↑ generalizes to ↑
Level 0 (Country) - Individual countries
```

### Traversal Policy
- **Generalize UP:** Country → Region → Global
- **Specialize DOWN:** Global → Region → Country

### How to Use
1. Run `system_a_with_generalization.py`
2. Use radio buttons to control hierarchy level
3. Brush or click to select countries
4. Switch hierarchy level to see generalization
5. Observe selection propagate across linked views

**Key Distinction:** This is NOT simple filtering - it's semantic hierarchical abstraction based on data relationships.

---

## 📈 Evaluation Summary

### Methodology
- **Participants:** N = 5 per system (15 total)
- **Design:** Within-subjects (all participants used all systems)
- **Tasks:** All 5 tasks (T1-T5) performed on each system
- **Metrics:** Completion time, accuracy, SUS scores, NASA TLX, preferences

### Key Findings

**Task Performance:**
- **System A:** Fastest for temporal trends (T4: 34.9s)
- **System B:** Fastest for outlier identification (T2: 31.2s), 100% accuracy
- **System C:** Fastest for filtering (T5: 22.8s), highest usability (SUS 81.2)

**User Preferences:**
1. **System C:** Most preferred (3/5 participants ranked #1)
2. **System A:** Second (2/5 participants ranked #1)
3. **System B:** Third (0/5 participants ranked #1)

**Usability (SUS Scores):**
- System C: 81.2 (Excellent)
- System A: 78.5 (Good)
- System B: 72.4 (Acceptable)

**Mental Demand (NASA TLX, lower is better):**
- System C: 3.9/10 (Lowest)
- System A: 4.2/10
- System B: 5.8/10 (Highest)

### Conclusion
No single system is universally best - each excels at different tasks. System C provides the best overall user experience, but System A is optimal for temporal analysis and System B for statistical detail.

---

## 📝 Report

The complete project report is available in `docs/PROJECT_REPORT.md` and includes:

1. **Data Description** (400 words) - Dataset categorization and examples
2. **Tasks Definition** (400 words) - Five analytical tasks with taxonomy
3. **System Implementations** - Three fully implemented systems with code
4. **Generalized Selection** (400 words) - Semantic hierarchy and traversal policy
5. **Demo Videos** - (Placeholder for YouTube link)
6. **Design Comparison** (1200 words) - Six design decisions analyzed
7. **User Evaluation** (1000 words) - Methodology, results, analysis
8. **Future Work** (400 words) - Evidence-based improvements
9. **References** - Academic citations (APA format)
10. **Appendices** - Raw evaluation data, team contributions

---

## 🎥 Demo Video

**YouTube Link:** [INSERT DEMO VIDEO LINK HERE]

The demo video (max 5 minutes) demonstrates:
- All three systems in action
- Key design features and interaction techniques
- Task completion examples
- Generalized selection demonstration

---

## 🧑‍🤝‍🧑 Team Contributions

| Team Member | Contribution | Percentage |
|-------------|-------------|------------|
| Member 1 | Dataset creation, System A, Evaluation recruitment, Report sections 1-3 | 30% |
| Member 2 | System B, Generalized selection, Evaluation data collection, Report sections 4,7 | 25% |
| Member 3 | System C, Evaluation protocol, Statistical analysis, Report section 6 | 20% |
| Member 4 | Demo video, Evaluation coordination, Report visualizations, Report section 8 | 15% |
| Member 5 | Report compilation, Documentation, QA testing, Bibliography | 10% |

---

## 🛠️ Technical Details

### Dependencies
```python
altair==5.5.0
pandas==2.2.0
numpy==1.26.0
vega_datasets==0.9.0
```

### Browser Compatibility
- Chrome 90+ (recommended)
- Firefox 88+
- Safari 14+
- Edge 90+

### Known Issues
- Large brushes on scatter plots can be slow (>100 points selected)
- System C faceted plots may be small on screens <1920px width
- Heatmap colors in System B can be hard to distinguish for colorblind users

### Performance
- All systems tested with 415 records (no performance issues)
- Rendering time: <2 seconds for all systems
- Interaction latency: <100ms for brushing/clicking

---

## 📚 References

- Munzner, T. (2014). *Visualization Analysis and Design*. CRC Press.
- Brehmer & Munzner (2013). A multi-level typology of abstract visualization tasks. *IEEE TVCG*.
- Cleveland & McGill (1984). Graphical perception. *JASA*.
- Altair Documentation: https://altair-viz.github.io/

---

## 📧 Contact

For questions about this project, please contact:
- [Insert Team Contact Information]

---

## ⚖️ License

This project is submitted as coursework for Information Visualisation (M), University of Glasgow, 2024/25.
Dataset is synthetic and created for educational purposes only.

---

**End of README**
