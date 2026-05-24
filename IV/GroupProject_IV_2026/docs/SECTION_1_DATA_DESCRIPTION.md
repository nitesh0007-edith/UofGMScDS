# Section 1: The Data (400 words maximum)

## 1.1 Dataset Title and Description

**Glasgow Daily Weather Observations (2015-2019)**

This dataset contains comprehensive meteorological measurements for Glasgow, Scotland, spanning 1,795 daily observations from January 1, 2015, to November 30, 2019. Source: Dark Sky API historical weather data (https://darksky.net/dev).

## 1.2 Data Categorization

### Data Type Classification (Munzner, 2014)

**Items:**
- **Daily observations** (1,795 unique): Individual days as the primary data items
- **Temporal records**: Daily measurements across 4.9 years (1,795 days)

**Attributes:**

*Quantitative Attributes (6):*
- `tempMin` (continuous, ratio): Minimum daily temperature in Celsius [-8.67°C to 18.03°C]
- `tempMax` (continuous, ratio): Maximum daily temperature in Celsius [-1.39°C to 30.36°C]
- `cloudCover` (continuous, ratio): Cloud coverage percentage [0-1 normalized scale]
- `humidity` (continuous, ratio): Atmospheric humidity level [0-1 normalized scale]
- `windSpeed` (continuous, ratio): Wind speed in km/h [0.14 to 24.84 km/h]
- `visibility` (continuous, ratio): Visibility distance in km [0.19 to 10.0 km]

*Categorical Attributes (2):*
- `desc` (nominal, unordered): Weather condition type with 5 categories ("rain", "partly-cloudy-day", "clear-day", "cloudy", "fog")
- `summary` (nominal, unordered): Detailed weather description text (e.g., "Light rain throughout the day")

*Temporal Attribute (1):*
- `day` (ordinal, sequential): Date of observation [2015-01-01 to 2019-11-30]

### Dataset Characteristics

**Dimensionality**: Multivariate (9 original attributes + derived temporal features)

**Spatial**: Single geographic location (Glasgow, Scotland) - no spatial hierarchy

**Temporal**: Time-series (1,795 consecutive daily observations with natural temporal hierarchy: Day → Week → Month → Season → Year)

**Network**: None

**Hierarchy**: Implicit multi-level temporal hierarchy:
- Level 4 (Year): 5 years (2015-2019)
- Level 3 (Season): 4 seasons (Winter, Spring, Summer, Fall)
- Level 2 (Month): 12 months (January-December)
- Level 1 (Week): ~260 weeks
- Level 0 (Day): 1,795 individual days

### Data Semantics

This dataset exhibits strong temporal structure suitable for trend analysis and seasonal pattern detection. The quantitative weather attributes show meaningful correlations: minimum and maximum temperatures correlate positively (r=0.80, as expected), while humidity and visibility correlate negatively (r=-0.43, indicating that high humidity reduces visibility). Cloud cover positively correlates with humidity (r=0.58), suggesting rainy/cloudy conditions co-occur with high moisture content.

Temporal patterns reveal balanced seasonal coverage (Winter: 420 days, Spring: 460 days, Summer: 460 days, Fall: 455 days), enabling robust seasonal comparisons. The dominant weather type is "rain" (763 days, 42.5%), followed by "partly-cloudy-day" (566 days, 31.5%), reflecting Glasgow's maritime climate.

### Example Records

**Summer Day (2018-07-15):**
- tempMin: 13.5°C, tempMax: 22.1°C, cloudCover: 0.35, humidity: 0.62, windSpeed: 8.2 km/h, visibility: 8.5 km, desc: "partly-cloudy-day"

**Winter Day (2016-01-10):**
- tempMin: -2.1°C, tempMax: 3.8°C, cloudCover: 0.88, humidity: 0.91, windSpeed: 18.5 km/h, visibility: 3.2 km, desc: "rain"

---

**Word Count:** 398 words
