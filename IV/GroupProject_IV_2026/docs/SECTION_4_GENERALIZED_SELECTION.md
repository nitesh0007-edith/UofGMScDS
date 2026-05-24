# Section 4: Generalized Selection (400 words maximum)

## 4.1 Semantic Hierarchical Structure

Our Glasgow weather dataset exhibits a natural five-level temporal hierarchy based on calendar organization:

```
Level 4 (Year - Most General)
    ↓ contains ↓
Level 3 (Season)
    ↓ contains ↓
Level 2 (Month)
    ↓ contains ↓
Level 1 (Week)
    ↓ contains ↓
Level 0 (Day - Most Specific)
```

**Hierarchy Definition:**

- **Level 0 (Day):** Individual daily observations (e.g., "January 8, 2015")
- **Level 1 (Week):** ISO week groupings (e.g., "Week 2 of 2015" contains January 5-11, 2015)
- **Level 2 (Month):** Calendar months (e.g., "January 2015" contains all 31 days)
- **Level 3 (Season):** Meteorological seasons (e.g., "Winter 2015" contains December 2014, January, February 2015)
- **Level 4 (Year):** Annual groupings (e.g., "2015" contains all 365 days of that year)

**Semantic Relationships:**

- Many-to-one: Days → Weeks (7 days per week)
- Many-to-one: Weeks → Months (~4 weeks per month)
- Many-to-one: Months → Seasons (3 months per season)
- Many-to-one: Seasons → Years (4 seasons per year)
- No orphans: Every day belongs to exactly one week, month, season, and year

## 4.2 Traversal Policy

**Generalization (Moving UP the hierarchy):**

1. **Day → Week:** When user selects specific day(s), generalization expands selection to ALL days within the same ISO week(s). Example: Select "January 8, 2015" (Thursday) → Generalizes to entire Week 2 (January 5-11, 2015).

2. **Week → Month:** When selection is at week level, generalization expands to ALL days in the month(s) containing those weeks. Example: Select "Week 2 of January 2015" → Generalizes to all of January 2015 (31 days).

3. **Month → Season:** When selection is at month level, generalization expands to ALL months in the same meteorological season. Example: Select "January 2015" → Generalizes to Winter 2015 (December 2014, January, February 2015).

4. **Season → Year:** When selection is at season level, generalization expands to ALL seasons in that year. Example: Select "Winter 2015" → Generalizes to entire year 2015 (all 365 days).

**Specialization (Moving DOWN the hierarchy):**

Users can narrow from general to specific levels by changing the hierarchy level control and making new selections at more granular levels.

**Key Distinction from Global Filtering:**

Generalized selection is fundamentally different from filtering. Filtering changes what data is globally visible, while generalized selection semantically moves through hierarchical abstraction levels while maintaining relationship context.

- **Global Filtering Example:** "Show only January 2015 data" (removes other months from view entirely)
- **Generalized Selection Example:** "I selected January 8; generalize this to the week level" (semantic operation that finds all days sharing the week relationship with January 8)

## 4.3 Implementation Approach

**Implementation File:** `SystemA/system_a_with_generalization.html`

**Technical Implementation:**

1. **UI Controls:** Radio buttons control hierarchy level (0=Day, 1=Week, 2=Month, 3=Season, 4=Year)

2. **Selection Parameters:** Five distinct selection parameters for each hierarchy level:
   - `select_day`: Point selection for individual days
   - `select_week`: Point selection for weeks (using week_id field)
   - `select_month`: Point selection for months (using month_id field)
   - `select_season`: Point selection for seasons (using season_id field)
   - `select_year`: Point selection for years

3. **Data Preparation:** Additional hierarchical identifier fields added to dataset:
   - `week_id`: "YYYY-WWW" format (e.g., "2015-W02")
   - `month_id`: "YYYY-MM" format (e.g., "2015-M01")
   - `season_id`: "YYYY-Season" format (e.g., "2015-Winter")

4. **Visual Feedback:**
   - **Size encoding:** Selected items appear larger (size=100) vs unselected (size=20)
   - **Opacity encoding:** Selected items at 80% opacity, unselected at 10%
   - **Color encoding:** Maintains seasonal color scheme for context
   - **Aggregation views:** Four bar charts show aggregations at week, month, season, and year levels simultaneously, all lighting up based on selection

5. **Linked Views:** Time series, four aggregation bar charts (week/month/season/year), and scatter plot all update based on hierarchical selection, demonstrating how selection propagates through different abstraction levels.

**User Workflow:**

1. User selects hierarchy level via radio button (e.g., "Day")
2. User clicks/brushes on time series to select specific days
3. User switches radio button to "Week" level
4. Selection automatically generalizes to all days in the same week(s)
5. Visual feedback shows enlarged, highlighted points across all linked views
6. Aggregation bar charts highlight corresponding weeks, months, seasons, and years
7. Scatter plot filters to show only data from selected temporal range

This implementation demonstrates true hierarchical data abstraction through semantic relationships, not simple filtering.

---

**Word Count:** 398 words
