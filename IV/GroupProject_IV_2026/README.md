# Information Visualisation Group Project
## Multiview Visualisation of Glasgow Weather Data

**Course:** Information Visualisation (M), 2024/25
**Submission Date:** March 20, 2026
**Toolkit:** Python/Altair

---

## 📦 Project Structure

```
GroupProject_IV_2026/
├── README.md                          # This file
├── data/                              # Dataset folder
│   └── Glasgow_weather_data/
│       └── clean_weather_data.csv    # Main dataset (1,795 records, 9 attributes)
├── SystemA/                           # System A implementation (to be developed)
├── SystemB/                           # System B implementation (to be developed)
├── SystemC/                           # System C implementation (to be developed)
├── docs/                              # Documentation (to be created)
└── evaluation_data/                   # User evaluation data (to be collected)
└── archive_happiness_project/         # Archived previous work (happiness data)
```

---

## 📊 Dataset Overview

**Glasgow Weather Data (2015-2019)**

- **Records:** 1,795 daily weather observations
- **Time Period:** January 1, 2015 - November 30, 2019
- **Location:** Glasgow, Scotland
- **Attributes:** 9 columns

### Attributes

| Attribute | Type | Range | Description |
|-----------|------|-------|-------------|
| day | Temporal | 2015-01-01 to 2019-11-30 | Date of observation |
| tempMin | Quantitative | Continuous | Minimum temperature (°C) |
| tempMax | Quantitative | Continuous | Maximum temperature (°C) |
| summary | Categorical | Text | Daily weather summary |
| desc | Categorical | Text | Weather description |
| cloudCover | Quantitative | 0-1 | Cloud cover percentage (normalized) |
| humidity | Quantitative | 0-1 | Humidity level (normalized) |
| windSpeed | Quantitative | Continuous | Wind speed (km/h) |
| visibility | Quantitative | Continuous | Visibility distance (km) |

### Data Quality Notes

- **Missing Values:** 194 total (summary: 7, desc: 184, cloudCover: 3)
- **Temporal Coverage:** Complete daily records except missing values
- **Years:** 2015 (365 days), 2016 (366 days), 2017 (365 days), 2018 (365 days), 2019 (334 days)

---

## 🎯 Project Status

**Current Phase:** Initial Setup

- [x] Archive previous happiness data project
- [x] Set up new folder structure
- [x] Verify weather data availability
- [ ] Define analytical tasks (T1, T2, ..., TN)
- [ ] Design System A (multiview visualization)
- [ ] Design System B (multiview visualization)
- [ ] Design System C (multiview visualization)
- [ ] Implement generalized selection (hierarchical temporal structure)
- [ ] Conduct user evaluation (5+ participants per system)
- [ ] Write project report
- [ ] Create demo video

---

## 🚀 Next Steps

### 1. Data Categorization (Section 1)
Describe and categorize the dataset using IV terminology (Lecture 1a concepts)

### 2. Task Definition (Section 2)
Define N analytical tasks users might want to perform:
- At least one task must involve data subset selection
- Use task taxonomy from Lecture 1b
- Consider temporal analysis, outlier detection, correlation exploration

### 3. System Implementation (Section 3)
Implement three different multiview visualization systems:
- Each system must support ALL defined tasks
- Each system must have at least 2 linked views
- Implement brushing and linking (bidirectional preferred)

### 4. Generalized Selection (Section 4)
Implement hierarchical semantic structure:
- **Proposed hierarchy:** Day → Week → Month → Season → Year
- Example: Select "Jan 8, 2015" → Generalize to "All days in Week 2" → Generalize to "All days in January"
- This is NOT global filtering, but semantic hierarchical abstraction

---

## 🗂️ Hierarchical Structure Proposal

**Temporal Hierarchy for Generalized Selection:**

```
Level 4 (Year)           - e.g., "All of 2015"
    ↑ generalizes
Level 3 (Season)         - e.g., "Winter 2015" (Dec 2014-Feb 2015)
    ↑ generalizes
Level 2 (Month)          - e.g., "January 2015"
    ↑ generalizes
Level 1 (Week)           - e.g., "Week 2 of January 2015"
    ↑ generalizes
Level 0 (Day)            - e.g., "January 8, 2015"
```

**Alternative: Weather Type Hierarchy:**

```
Level 2 (All Weather)
    ↑
Level 1 (Weather Category) - Rain, Clear, Cloudy, etc.
    ↑
Level 0 (Specific Description) - "Light rain", "Heavy rain", etc.
```

---

## 📚 Requirements Reference

See `GroupProj 2026 v1.pdf` for complete assignment specification.

**Key Requirements:**
- **Part A (20%):** Design and Implementation
  1. Data description (2%) - max 400 words
  2. Tasks definition (2%) - max 400 words
  3. Core systems (4%) - 3 systems (A, B, C)
  4. Generalized selection (4%) - max 400 words
  5. Demo video (required) - max 5 minutes
  6. Design comparison (8%) - max 1200 words (6 decisions × 200 words)

- **Part B (10%):** Evaluation
  7. User evaluation (8%) - 5+ participants per system, max 1000 words
  8. Future work (2%) - max 400 words

**Deadline:** 16:30, Friday March 20, 2026

---

## 🔧 Technical Setup

### Prerequisites

- Python 3.7+
- pip package manager

### Installation

```bash
# Install required packages
pip install altair pandas numpy vega_datasets
```

### Running Visualizations

```bash
# System A (to be implemented)
cd SystemA
python system_a.py

# System B (to be implemented)
cd SystemB
python system_b.py

# System C (to be implemented)
cd SystemC
python system_c.py
```

---

## 📧 Team Information

**Group:** [Insert Group Number]
**Team Members:** [Insert Names]

---

## 📝 Notes

**Previous Work:** The happiness data project has been archived in `archive_happiness_project/` folder. This new project focuses on Glasgow weather data visualization.

**Data Source:** Glasgow weather data (2015-2019)

---

**Last Updated:** February 23, 2026
