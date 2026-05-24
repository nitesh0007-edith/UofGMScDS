# Glasgow Weather Data - IV Project Checklist

**Deadline:** 16:30, Friday March 20, 2026
**Days Remaining:** ~25 days

---

## 📋 Submission Checklist

### Part A: Design and Implementation (20%)

#### 1. The Data (2% - max 400 words)
- [ ] Write one-sentence title and description
- [ ] Provide link to data source
- [ ] Categorize dataset using Lecture 1a terminology:
  - [ ] Define Items (1,795 daily observations)
  - [ ] Define Attributes (9 attributes: temporal, quantitative, categorical)
  - [ ] Describe data type (Table/Multivariate)
  - [ ] Describe dataset characteristics (Spatial, Temporal, Network, Hierarchy)
- [ ] Use specific examples from the data
- [ ] Keep under 400 words

#### 2. The Tasks (2% - max 400 words)
- [ ] Define Task T1 using Lecture 1b taxonomy
- [ ] Define Task T2 using Lecture 1b taxonomy
- [ ] Define Task T3 using Lecture 1b taxonomy
- [ ] Define Task T4 using Lecture 1b taxonomy
- [ ] Define Task T5 using Lecture 1b taxonomy
- [ ] **REQUIRED:** At least one task must involve data subset selection
- [ ] For each task specify: Why, How, What (Brehmer & Munzner taxonomy)
- [ ] Use clear examples
- [ ] Keep under 400 words

#### 3. The Core Systems (4%)
- [ ] **System A:** Implement multiview visualization
  - [ ] At least 2 linked views
  - [ ] Supports ALL tasks (T1-T5)
  - [ ] Implements brushing and linking
  - [ ] Create system_a.py
  - [ ] Generate system_a_visualization.html
  - [ ] Export system_a_spec.json
- [ ] **System B:** Implement multiview visualization
  - [ ] At least 2 linked views
  - [ ] Supports ALL tasks (T1-T5)
  - [ ] Implements brushing and linking
  - [ ] Create system_b.py
  - [ ] Generate system_b_visualization.html
  - [ ] Export system_b_spec.json
- [ ] **System C:** Implement multiview visualization
  - [ ] At least 2 linked views
  - [ ] Supports ALL tasks (T1-T5)
  - [ ] Implements brushing and linking
  - [ ] Create system_c.py
  - [ ] Generate system_c_visualization.html
  - [ ] Export system_c_spec.json
- [ ] Zip folders A, B, C with code + data files

#### 4. Generalized Selection (4% - max 400 words)
- [ ] Determine semantic hierarchical structure
  - [ ] Example: Day → Week → Month → Season → Year
  - [ ] OR: Specific description → Weather type → All weather
- [ ] Define traversal policy
  - [ ] Generalize: Move UP hierarchy (day→week→month)
  - [ ] Specialize: Move DOWN hierarchy (month→week→day)
- [ ] Implement in at least one system
  - [ ] UI control for hierarchy navigation
  - [ ] Selection propagates correctly
  - [ ] Visual feedback on generalization
- [ ] **NOT global filtering** - must be hierarchical semantic abstraction
- [ ] Write description (max 400 words)
- [ ] Replace code in system folder

#### 5. Demo Videos (Required - max 5 minutes)
- [ ] Record video demonstrating all three systems
- [ ] Explain design and implementation basics
- [ ] Show how systems match specifications
- [ ] Upload to YouTube
- [ ] Add YouTube link to top of report
- [ ] Keep under 5 minutes

#### 6. Design Comparison (8% - max 1200 words)
- [ ] **Decision 1:** Choose design decision (200 words max)
  - [ ] State the decision clearly
  - [ ] Explain choice for System A (and why)
  - [ ] Explain choice for System B (and why)
  - [ ] Explain choice for System C (and why)
  - [ ] State which choice is best (and why)
  - [ ] Add diagrams/screenshots
- [ ] **Decision 2:** (200 words max)
  - [ ] Repeat above structure
- [ ] **Decision 3:** (200 words max)
  - [ ] Repeat above structure
- [ ] **Decision 4:** (200 words max)
  - [ ] Repeat above structure
- [ ] **Decision 5:** (200 words max)
  - [ ] Repeat above structure
- [ ] **Decision 6:** (200 words max)
  - [ ] Repeat above structure

---

### Part B: Evaluation (10%)

#### 7. User Evaluation Comparison (8% - max 1000 words)
- [ ] Recruit at least 5 participants per system (15 total)
- [ ] Design evaluation methodology
  - [ ] Within-subjects or between-subjects design
  - [ ] Counterbalance order to avoid learning effects
- [ ] Each participant does ALL tasks on ALL systems
  - [ ] Participant completes T1 three times (A, B, C)
  - [ ] Participant completes T2 three times (A, B, C)
  - [ ] And so on for all tasks...
- [ ] Collect data:
  - [ ] Task completion times
  - [ ] Error rates/accuracy
  - [ ] SUS usability scores (optional but recommended)
  - [ ] Qualitative feedback
- [ ] Analyze data
  - [ ] Statistical tests (ANOVA, t-tests, etc.)
  - [ ] Identify which system is best for which tasks
- [ ] Write evaluation report (max 1000 words)
  - [ ] Describe and justify methodology
  - [ ] Describe data collection process
  - [ ] Explain analysis methods
  - [ ] Present results clearly
  - [ ] Identify which aspects of each system are best
- [ ] Include ALL raw evaluation data in Appendix

#### 8. Future Work (2% - max 400 words)
- [ ] Use evaluation results to justify changes
- [ ] Provide specific, evidence-based improvements
- [ ] Avoid speculative features
- [ ] Reference actual evaluation data
- [ ] Keep under 400 words
- [ ] **DO NOT** actually implement these changes

---

## 📄 Document Structure

### Main PDF Report (Parts 1-8)
- [ ] Include YouTube link at TOP of document
- [ ] Section 1: The Data (max 400 words)
- [ ] Section 2: The Tasks (max 400 words)
- [ ] Section 3: The Core Systems (implementation in folders)
- [ ] Section 4: Generalized Selection (max 400 words)
- [ ] Section 5: Demo Videos (YouTube link)
- [ ] Section 6: Design Comparison (max 1200 words)
- [ ] Section 7: User Evaluation (max 1000 words)
- [ ] Section 8: Future Work (max 400 words)
- [ ] References (ACM style)
- [ ] Appendix A: Raw evaluation data
- [ ] Appendix B: Team member contributions

### Code Submission
- [ ] Zip folder: SystemA/ (with all code + data)
- [ ] Zip folder: SystemB/ (with all code + data)
- [ ] Zip folder: SystemC/ (with all code + data)
- [ ] Ensure code runs without errors
- [ ] Test on fresh environment

---

## ⚠️ Penalties to Avoid

**Two-band penalties applied for:**
- [ ] ❌ Word counts significantly longer than specified
- [ ] ❌ Demo video significantly longer than 5 minutes
- [ ] ❌ Failure to submit demo video
- [ ] ❌ Failure to submit any program code folders
- [ ] ❌ Failure to include appendix with evaluation data
- [ ] ❌ Failure to have 5+ participants per system
- [ ] ❌ Failure to include team contribution log
- [ ] ❌ Document not following numbered structure

**Penalties are cumulative - up to 14 bands can be lost!**

---

## 📊 Weather Data Analysis Tasks (Ideas)

### Potential Tasks to Define:

**T1: COMPARE Seasonal Patterns**
- Why: Discover seasonal weather differences
- How: Compare average temperatures across seasons
- What: Derived attributes (mean temp per season)

**T2: IDENTIFY Extreme Weather Days**
- Why: Identify anomalies
- How: Detect outliers in temperature/wind/precipitation
- What: Individual days with extreme values

**T3: EXPLORE Temperature-Humidity Correlation**
- Why: Discover relationships
- How: Browse using scatter plots
- What: Correlation between quantitative attributes

**T4: ANALYZE Temporal Trends**
- Why: Discover changes over time
- How: Browse time series from 2015-2019
- What: Temperature/precipitation trends

**T5: FILTER by Date Range and Weather Type** ✓ (REQUIRED)
- Why: Focus on relevant subsets
- How: Select/filter by date, season, weather category
- What: Subsets meeting specific criteria

---

## 🎯 Generalized Selection Hierarchy

### Option 1: Temporal Hierarchy
```
Level 4: Year (2015, 2016, 2017, 2018, 2019)
    ↑
Level 3: Season (Winter, Spring, Summer, Fall)
    ↑
Level 2: Month (January, February, ..., December)
    ↑
Level 1: Week (Week 1, Week 2, ...)
    ↑
Level 0: Day (Specific date: 2015-01-08)
```

**User Interaction:**
1. Click on January 8, 2015
2. Press "Generalize" → Selection expands to Week 2 of January
3. Press "Generalize" → Selection expands to all of January 2015
4. Press "Generalize" → Selection expands to Winter 2015
5. Press "Generalize" → Selection expands to entire year 2015

### Option 2: Weather Type Hierarchy
```
Level 2: All Weather
    ↑
Level 1: Weather Category (Rain, Clear, Cloudy, Snow, etc.)
    ↑
Level 0: Specific Description ("Light rain", "Heavy rain", "Drizzle")
```

---

## 🗓️ Timeline Suggestion (25 days)

- **Days 1-3:** Define data categorization and tasks (Sections 1-2)
- **Days 4-8:** Implement System A
- **Days 9-13:** Implement System B
- **Days 14-18:** Implement System C
- **Days 19-20:** Implement generalized selection
- **Days 21-22:** Conduct user evaluation (recruit + test)
- **Days 23-24:** Analyze data, write report, create video
- **Day 25:** Final review and submission

---

**Last Updated:** February 23, 2026
