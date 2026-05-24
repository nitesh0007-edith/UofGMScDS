# Section 2: The Tasks (400 words maximum)

## 2.1 Task Taxonomy

We define five analytical tasks for exploring Glasgow weather data, categorized using the Brehmer & Munzner (2013) task taxonomy:

---

### **T1: COMPARE Seasonal Temperature Patterns**

- **Why:** Discover seasonal differences and trends
- **How:** Compare mean temperatures across four seasons (Winter, Spring, Summer, Fall)
- **What:** Derived attributes (aggregate statistics: mean tempMin, mean tempMax per season)
- **User Goal:** Understand which season has highest/lowest temperatures and identify seasonal temperature ranges
- **Example:** "Which season has the widest daily temperature variation? Is summer truly warmer than fall?"

---

### **T2: IDENTIFY Extreme Weather Events**

- **Why:** Identify anomalies and outliers
- **How:** Lookup days with unusual values (extreme temperatures, high wind speed, low visibility)
- **What:** Individual data items (specific days) with exceptional quantitative values
- **User Goal:** Find days with record temperatures, storms, or unusual weather conditions
- **Example:** "Which day had the highest wind speed in 2015? When did visibility drop below 1 km?"

---

### **T3: EXPLORE Correlation Between Humidity and Visibility**

- **Why:** Discover relationships between weather factors
- **How:** Browse using scatter plots showing humidity vs. visibility with regression trends
- **What:** Relationships between quantitative attributes (humidity, visibility, cloudCover, temperature)
- **User Goal:** Understand how atmospheric conditions relate to each other (e.g., does high humidity reduce visibility?)
- **Example:** "How does cloud cover affect temperature? Is there a relationship between wind speed and rainfall?"

---

### **T4: ANALYZE Temporal Trends Across Years**

- **Why:** Discover changes and patterns over time
- **How:** Browse temporal patterns using time-series visualizations from 2015-2019
- **What:** Trends in temperature, precipitation patterns, and seasonal weather evolution
- **User Goal:** Identify year-over-year changes, warming/cooling trends, or shifting seasonal patterns
- **Example:** "Has average summer temperature increased from 2015 to 2019? Are winters getting wetter?"

---

### **T5: FILTER and SUBSET Data by Time Period and Weather Type** *(Required for Generalized Selection)*

- **Why:** Present relevant subsets for focused analysis
- **How:** Select/filter based on temporal criteria (year, season, month, date range) and weather conditions (weather type, temperature threshold)
- **What:** Subsets of daily observations meeting specific criteria
- **User Goal:** Focus analysis on specific time periods or weather conditions of interest
- **Example:** "Show only rainy days in summer 2017" or "Display all days with temperature above 20°C"

---

## 2.2 Task Implementation Strategy

All three visualization systems (A, B, C) will support these five tasks through:

- **Linked brushing and selection**: Enables T5 (filtering/subsetting) across multiple views
- **Temporal views**: Line charts and heatmaps support T4 (trend analysis)
- **Statistical encodings**: Box plots and histograms support T1 (seasonal comparison)
- **Scatter plots with tooltips**: Support T2 (outlier identification) and T3 (correlation exploration)
- **Aggregations**: Bar charts show seasonal means (T1), time series show annual trends (T4)
- **Interactive highlighting**: Color/opacity changes emphasize selected subsets (T2, T5)

The tasks progress from overview (T1: seasonal patterns) to identification (T2: extremes), exploration (T3: correlations), temporal analysis (T4: trends), and interactive filtering (T5: subsetting), aligning with Shneiderman's Visual Information-Seeking Mantra: "Overview first, zoom and filter, then details on demand."

The hierarchical temporal structure (Day → Week → Month → Season → Year) naturally supports generalized selection for T5, enabling users to select a specific day and generalize upward to broader temporal contexts.

---

**Word Count:** 395 words
