# DATASET REQUIREMENTS SPECIFICATION
## World Happiness Data - Complete Requirements

**Project:** Information Visualisation Group Project
**Course:** Information Visualisation (M), 2024/25
**Date:** February 9, 2026

---

## 📋 EXECUTIVE SUMMARY

The dataset must contain **multivariate time-series data** about world happiness indicators with the following specifications:

| Requirement | Specification |
|-------------|---------------|
| **Total Records** | 415 (83 countries × 5 years) |
| **Countries** | 83 unique nations |
| **Regions** | 10 geographic-cultural groupings |
| **Time Period** | 5 years (2020-2024) |
| **Attributes** | 11 columns total |
| **Data Type** | Table (multivariate) |
| **Structure** | Hierarchical (Country → Region → Global) |
| **Quality** | Zero missing values |
| **Format** | CSV file |

---

## 🎯 1. RECORD COUNT REQUIREMENTS

### REQ-1.1: Total Records
**Requirement:** Exactly **415 records**
**Calculation:** 83 countries × 5 years = 415
**Rationale:** Complete time-series coverage for all countries

### REQ-1.2: Temporal Coverage
**Requirement:** Every country must have **exactly 5 records** (one per year)
**Years:** 2020, 2021, 2022, 2023, 2024
**No Gaps:** All countries must have data for all 5 years

### REQ-1.3: Complete Coverage
**Requirement:** No missing years, no missing countries
**Validation:** `country_count * year_count = total_records`

---

## 🌍 2. GEOGRAPHIC REQUIREMENTS

### REQ-2.1: Countries (Items)
**Requirement:** Exactly **83 unique countries**
**Type:** Primary data items
**Examples Required:**
- Finland, Denmark, Norway (Western Europe)
- India, Pakistan, Afghanistan (South Asia)
- Nigeria, Ghana, Ethiopia (Sub-Saharan Africa)
- China, Japan, South Korea (East Asia)
- USA, Canada, Mexico (North America)

### REQ-2.2: Regions (Categories)
**Requirement:** Exactly **10 geographic-cultural regions**

**Required Regions:**
1. **Western Europe** (≈16 countries)
   - Examples: Finland, Denmark, Norway, Sweden, Germany, UK, France, etc.

2. **North America** (≈5 countries)
   - Examples: USA, Canada, Mexico, Costa Rica, Panama

3. **Australia and New Zealand** (2 countries)
   - Examples: Australia, New Zealand

4. **Middle East and North Africa** (≈9 countries)
   - Examples: Israel, UAE, Saudi Arabia, Egypt, etc.

5. **Latin America and Caribbean** (≈10 countries)
   - Examples: Chile, Brazil, Argentina, Colombia, etc.

6. **Eastern Europe** (≈10 countries)
   - Examples: Czech Republic, Poland, Russia, Ukraine, etc.

7. **Southeast Asia** (≈9 countries)
   - Examples: Singapore, Thailand, Philippines, Indonesia, Vietnam, etc.

8. **East Asia** (≈6 countries)
   - Examples: Taiwan, Japan, South Korea, China, Hong Kong, Mongolia

9. **South Asia** (≈6 countries)
   - Examples: India, Pakistan, Bangladesh, Sri Lanka, Nepal, Afghanistan

10. **Sub-Saharan Africa** (≈10 countries)
    - Examples: Nigeria, South Africa, Kenya, Ghana, Ethiopia, etc.

**Total:** Must sum to 83 countries

### REQ-2.3: Regional Distribution
**Requirement:** Countries must be distributed across regions
**Constraint:** Each country belongs to **exactly ONE region**
**No Overlap:** No country appears in multiple regions
**Coverage:** All 10 regions must have at least 2 countries

---

## 📊 3. ATTRIBUTE REQUIREMENTS

### REQ-3.1: Total Attributes
**Requirement:** Exactly **11 columns/attributes**
**Breakdown:**
- 3 Categorical attributes
- 7 Quantitative attributes
- 1 Temporal attribute

### REQ-3.2: Categorical Attributes (3)

#### Attribute 1: Country
- **Name:** `Country`
- **Type:** Categorical (Nominal, unordered)
- **Values:** 83 unique country names
- **Examples:** "Finland", "Denmark", "Afghanistan"
- **Data Type:** String/Text

#### Attribute 2: Region
- **Name:** `Region`
- **Type:** Categorical (Nominal, unordered)
- **Values:** 10 unique region names (see REQ-2.2)
- **Examples:** "Western Europe", "South Asia"
- **Data Type:** String/Text

#### Attribute 3: Population_Category
- **Name:** `Population_Category`
- **Type:** Categorical (Ordinal, ordered)
- **Values:** 4 levels in order:
  1. "Small"
  2. "Medium"
  3. "Large"
  4. "Very Large"
- **Data Type:** String/Text
- **Ordering:** Small < Medium < Large < Very Large

### REQ-3.3: Temporal Attribute (1)

#### Attribute 4: Year
- **Name:** `Year`
- **Type:** Temporal (Ordinal, sequential)
- **Values:** 5 distinct years: 2020, 2021, 2022, 2023, 2024
- **Data Type:** Integer
- **Range:** 2020 ≤ Year ≤ 2024

### REQ-3.4: Quantitative Attributes (7)

#### Attribute 5: Happiness_Score
- **Name:** `Happiness_Score`
- **Type:** Quantitative (Continuous, Ratio scale)
- **Description:** Overall happiness rating
- **Scale:** 1-10 (continuous)
- **Expected Range:** ~2.5 to ~8.5
- **Data Type:** Float
- **Example Values:** 7.83 (Finland), 2.52 (Afghanistan)

#### Attribute 6: GDP_per_Capita
- **Name:** `GDP_per_Capita`
- **Type:** Quantitative (Continuous, Ratio scale)
- **Description:** Economic prosperity indicator (normalized)
- **Scale:** 0-2 range (normalized values)
- **Expected Range:** ~0.3 to ~1.5
- **Data Type:** Float
- **Example Values:** 1.34 (Finland), 0.38 (Afghanistan)

#### Attribute 7: Social_Support
- **Name:** `Social_Support`
- **Type:** Quantitative (Continuous, Ratio scale)
- **Description:** Perceived social support network strength
- **Scale:** 0-1 (normalized)
- **Expected Range:** 0.3 to 1.0
- **Data Type:** Float
- **Example Values:** 0.95 (Finland), 0.42 (Afghanistan)

#### Attribute 8: Healthy_Life_Expectancy
- **Name:** `Healthy_Life_Expectancy`
- **Type:** Quantitative (Continuous, Ratio scale)
- **Description:** Population health indicator (normalized)
- **Scale:** 0-1 (normalized)
- **Expected Range:** 0.2 to 0.7
- **Data Type:** Float

#### Attribute 9: Freedom
- **Name:** `Freedom`
- **Type:** Quantitative (Continuous, Ratio scale)
- **Description:** Freedom to make life choices
- **Scale:** 0-1 (normalized)
- **Expected Range:** 0.2 to 0.8
- **Data Type:** Float

#### Attribute 10: Generosity
- **Name:** `Generosity`
- **Type:** Quantitative (Continuous, Ratio scale)
- **Description:** Charitable giving behavior
- **Scale:** -0.1 to 0.5 range
- **Expected Range:** -0.05 to 0.4 (can be negative!)
- **Data Type:** Float
- **Note:** Negative values allowed (indicates low generosity)

#### Attribute 11: Corruption_Perception
- **Name:** `Corruption_Perception`
- **Type:** Quantitative (Continuous, Ratio scale)
- **Description:** Perceived corruption level
- **Scale:** 0-1 (normalized)
- **Expected Range:** 0.3 to 0.85
- **Data Type:** Float
- **Note:** **Higher value = MORE corrupt**

---

## 🏗️ 4. STRUCTURAL REQUIREMENTS

### REQ-4.1: Dataset Type
**Requirement:** Table structure (rows = records, columns = attributes)
**Format:** Multivariate data with items (countries) and attributes (indicators)

### REQ-4.2: Hierarchical Structure
**Requirement:** Three-level implicit hierarchy

**Level 0 (Most Specific):** Country
- 83 individual countries
- Each country has 5 records (one per year)

**Level 1 (Mid-level):** Region
- 10 geographic-cultural groupings
- Each region contains 2-16 countries

**Level 2 (Most General):** Global
- All data (415 records)
- Encompasses all regions

**Hierarchy Relationships:**
- Many-to-one: Countries → Regions
- Many-to-one: Regions → Global
- No orphans (all countries must belong to a region)

### REQ-4.3: Dimensionality
**Requirement:** Multivariate with 11 dimensions
**Nature:**
- **Spatial:** Geographic (country-level with regional aggregation)
- **Temporal:** Time-series (5-year longitudinal)
- **Hierarchical:** Three levels of aggregation

---

## 🔗 5. DATA SEMANTICS & RELATIONSHIPS

### REQ-5.1: Required Correlations
**Requirement:** Dataset must exhibit meaningful relationships

#### Correlation 1: GDP ↔ Happiness (POSITIVE)
- **Requirement:** Strong positive correlation (r ≈ 0.75 to 0.85)
- **Rationale:** High GDP countries generally happier
- **Example:**
  - Finland: High GDP (1.34) → High Happiness (7.83)
  - Afghanistan: Low GDP (0.38) → Low Happiness (2.52)

#### Correlation 2: Corruption ↔ Happiness (NEGATIVE)
- **Requirement:** Moderate negative correlation (r ≈ -0.40 to -0.50)
- **Rationale:** More corruption → Lower happiness
- **Example:**
  - Low corruption countries → Higher happiness
  - High corruption countries → Lower happiness

#### Correlation 3: Social Support ↔ Happiness (POSITIVE)
- **Requirement:** Positive correlation
- **Rationale:** Better social support → Higher happiness

### REQ-5.2: Regional Patterns
**Requirement:** Regions should show distinct happiness levels

**Expected Regional Rankings (approximate):**
1. Australia and New Zealand (highest ~7.4)
2. Western Europe (~7.2)
3. North America (~7.0)
4. East Asia (~6.4)
5. Latin America (~6.3)
6. Southeast Asia (~6.0)
7. Middle East (~6.0)
8. Eastern Europe (~5.9)
9. South Asia (~4.7)
10. Sub-Saharan Africa (lowest ~4.2)

### REQ-5.3: Temporal Trends
**Requirement:** Data should show realistic temporal variation
- Not strictly monotonic (some ups and downs)
- Overall slight upward trend (~0.02 per year)
- Individual country variation realistic

---

## ✅ 6. DATA QUALITY REQUIREMENTS

### REQ-6.1: Completeness
**Requirement:** Zero missing values
**Validation:** All 415 records × 11 attributes = 4,565 values must be present
**No nulls, no NaN, no empty strings**

### REQ-6.2: Consistency
**Requirement:** All values within specified ranges
**Validation Checks:**
- Happiness_Score: 1 ≤ value ≤ 10
- GDP_per_Capita: 0 ≤ value ≤ 2
- Social_Support: 0 ≤ value ≤ 1
- Healthy_Life_Expectancy: 0 ≤ value ≤ 1
- Freedom: 0 ≤ value ≤ 1
- Generosity: -0.1 ≤ value ≤ 0.5
- Corruption_Perception: 0 ≤ value ≤ 1
- Year: {2020, 2021, 2022, 2023, 2024}
- Region: One of 10 specified regions
- Population_Category: {Small, Medium, Large, Very Large}

### REQ-6.3: Uniqueness
**Requirement:** No duplicate records
**Validation:** Each (Country, Year) combination appears exactly once
**Total Unique:** 415 unique (Country, Year) pairs

### REQ-6.4: Data Types
**Requirement:** Correct data types for each attribute

| Attribute | Required Type |
|-----------|---------------|
| Country | String/Text |
| Region | String/Text |
| Year | Integer |
| Happiness_Score | Float |
| GDP_per_Capita | Float |
| Social_Support | Float |
| Healthy_Life_Expectancy | Float |
| Freedom | Float |
| Generosity | Float |
| Corruption_Perception | Float |
| Population_Category | String/Text |

---

## 📁 7. FILE FORMAT REQUIREMENTS

### REQ-7.1: File Format
**Requirement:** CSV (Comma-Separated Values)
**File Name:** `world_happiness_data.csv`
**Encoding:** UTF-8
**Line Endings:** Unix (LF) or Windows (CRLF)

### REQ-7.2: File Structure
**Requirement:**
- **Header Row:** Required (contains column names)
- **Data Rows:** 415 rows
- **Total Lines:** 416 (1 header + 415 data)

**Example Structure:**
```csv
Country,Region,Year,Happiness_Score,GDP_per_Capita,Social_Support,Healthy_Life_Expectancy,Freedom,Generosity,Corruption_Perception,Population_Category
Finland,Western Europe,2020,7.448,1.1103,0.9197,0.6416,0.8000,0.1313,0.4673,Very Large
Denmark,Western Europe,2020,7.584,1.1141,0.9317,0.5928,0.8000,0.1694,0.3168,Very Large
...
```

### REQ-7.3: File Size
**Expected:** ~35-50 KB (depending on precision)
**Acceptable Range:** 30-100 KB

### REQ-7.4: CSV Standards
**Requirement:** Follow standard CSV conventions
- Comma delimiter
- No trailing commas
- No extra whitespace
- Proper escaping if needed
- Consistent number of columns per row

---

## 🎯 8. FUNCTIONAL REQUIREMENTS (TASK SUPPORT)

The dataset must support all 5 analytical tasks:

### REQ-8.1: Support Task T1 (Regional Comparison)
**Requirement:** Enable comparison of mean happiness across 10 regions
**Validation:** Can calculate `GROUP BY Region, AVG(Happiness_Score)`
**Example Query:** "Which region has highest average happiness?"

### REQ-8.2: Support Task T2 (Outlier Identification)
**Requirement:** Enable identification of outliers within regions
**Validation:** Can detect countries with unusual values relative to regional mean
**Example Query:** "Which countries are outliers in South Asia?"

### REQ-8.3: Support Task T3 (Correlation Exploration)
**Requirement:** Enable exploration of relationships between variables
**Validation:** Can create scatter plots of any two quantitative attributes
**Example Query:** "What's the correlation between GDP and Happiness?"

### REQ-8.4: Support Task T4 (Temporal Trends)
**Requirement:** Enable analysis of changes over time (2020→2024)
**Validation:** Can track any attribute over 5 years for any country/region
**Example Query:** "How has Eastern Europe's happiness changed over time?"

### REQ-8.5: Support Task T5 (Filtering)
**Requirement:** Enable filtering by multiple criteria
**Validation:** Can filter by Region, Year, Population_Category
**Example Query:** "Show only Western Europe data for 2022-2024"

---

## 📊 9. STATISTICAL REQUIREMENTS

### REQ-9.1: Distribution Requirements
**Requirement:** Realistic statistical distributions

**For Happiness_Score:**
- Mean: ~5.5-6.0 (global average)
- Standard Deviation: ~1.5-2.0
- Range: ~2.5 to ~8.5
- Distribution: Approximately normal with slight left skew

**For each Quantitative Attribute:**
- No extreme outliers (within 3 standard deviations)
- Realistic variance within groups
- Natural variation over time

### REQ-9.2: Variance Requirements
**Requirement:** Sufficient variance for interesting analysis
- Between-region variance > within-region variance
- Temporal variance present but not excessive
- Individual countries show realistic year-to-year changes

---

## 🔍 10. VALIDATION CHECKLIST

Use this checklist to verify dataset meets all requirements:

### Basic Requirements
- [ ] Total records = 415
- [ ] Unique countries = 83
- [ ] Unique regions = 10
- [ ] Years = {2020, 2021, 2022, 2023, 2024}
- [ ] Total attributes = 11

### Attribute Requirements
- [ ] All 11 columns present with correct names
- [ ] Country: 83 unique values
- [ ] Region: 10 unique values
- [ ] Year: 5 values (2020-2024)
- [ ] All quantitative attributes in correct ranges
- [ ] Population_Category: 4 levels

### Quality Requirements
- [ ] Zero missing values (no nulls, no NaN)
- [ ] No duplicate (Country, Year) combinations
- [ ] All values within specified ranges
- [ ] Correct data types for all columns

### Structure Requirements
- [ ] Hierarchical structure: Country → Region → Global
- [ ] Each country in exactly one region
- [ ] Each country has exactly 5 records (one per year)

### Relationship Requirements
- [ ] GDP-Happiness correlation positive (r ≈ 0.75-0.85)
- [ ] Corruption-Happiness correlation negative (r ≈ -0.4 to -0.5)
- [ ] Regional means show expected pattern
- [ ] Temporal trends realistic (not strictly monotonic)

### File Requirements
- [ ] CSV format, UTF-8 encoding
- [ ] Header row present
- [ ] 416 total lines (1 header + 415 data)
- [ ] File size: 30-100 KB
- [ ] Valid CSV syntax (no formatting errors)

### Task Support Requirements
- [ ] Can aggregate by region (T1)
- [ ] Can identify outliers (T2)
- [ ] Can explore correlations (T3)
- [ ] Can analyze temporal trends (T4)
- [ ] Can filter by multiple criteria (T5)

---

## 📚 11. REFERENCE EXAMPLES

### Example Record 1 (High Happiness)
```
Country: Finland
Region: Western Europe
Year: 2024
Happiness_Score: 7.83
GDP_per_Capita: 1.34
Social_Support: 0.95
Healthy_Life_Expectancy: 0.63
Freedom: 0.66
Generosity: 0.12
Corruption_Perception: 0.47
Population_Category: Very Large
```

### Example Record 2 (Low Happiness)
```
Country: Afghanistan
Region: South Asia
Year: 2024
Happiness_Score: 2.52
GDP_per_Capita: 0.38
Social_Support: 0.42
Healthy_Life_Expectancy: 0.20
Freedom: 0.09
Generosity: -0.01
Corruption_Perception: 0.82
Population_Category: Large
```

### Example Temporal Series (Finland 2020-2024)
```
2020: Happiness=7.45, GDP=1.11
2021: Happiness=7.01, GDP=1.08
2022: Happiness=6.55, GDP=0.89
2023: Happiness=7.84, GDP=1.12
2024: Happiness=7.28, GDP=1.11
```

---

## ✅ COMPLIANCE STATEMENT

A dataset that meets ALL the above requirements will:
- ✅ Support all three visualization systems (A, B, C)
- ✅ Enable all five analytical tasks (T1-T5)
- ✅ Provide realistic patterns for evaluation
- ✅ Be suitable for academic demonstration
- ✅ Load correctly in pandas, Excel, R, and other tools

---

## 📎 APPENDIX: QUICK REFERENCE

### Core Numbers
- **415 records** (83 countries × 5 years)
- **11 attributes** (3 categorical, 7 quantitative, 1 temporal)
- **10 regions** (geographic-cultural groupings)
- **5 years** (2020-2024)
- **0 missing values**

### File
- **Name:** `world_happiness_data.csv`
- **Format:** CSV (UTF-8)
- **Size:** ~36-50 KB
- **Location:** `data/world_happiness_data.csv`

### Key Correlations
- GDP → Happiness: **POSITIVE** (r ≈ 0.78)
- Corruption → Happiness: **NEGATIVE** (r ≈ -0.45)
- Social Support → Happiness: **POSITIVE**

---

**Document Version:** 1.0
**Date:** February 9, 2026
**Status:** ✅ **COMPLETE SPECIFICATION**

---

*This specification document defines all requirements for the World Happiness dataset used in the Information Visualisation Group Project.*
