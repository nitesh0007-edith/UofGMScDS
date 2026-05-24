# IDSS 2020-2021 Examination Solutions

## Files in this Directory

1. **idss_m_2020_2021_main.pdf** - Original exam question paper with official model solutions
2. **IDSS_2020-2021_Solutions.md** - Complete solutions in Markdown format (enhanced)
3. **IDSS_2020-2021_Solutions.html** - Complete solutions in HTML format (styled and ready for viewing)

## How to Create PDF from HTML

Open `IDSS_2020-2021_Solutions.html` in your web browser and use "Print → Save as PDF"

### Quick Method:
1. Double-click `IDSS_2020-2021_Solutions.html` to open in browser
2. Press `Cmd+P` (Mac) or `Ctrl+P` (Windows)
3. Select "Save as PDF"
4. Enable "Background graphics" for better appearance
5. Save the PDF

## Examination Details

**Date:** Monday 26 April 2021
**Time:** Available from 14:00 BST
**Expected Duration:** 2 hours
**Time Allowed:** 4 hours (timed exam within 24 hours)
**Course:** Introduction to Data Science and Systems (M)
**Total Marks:** 60 marks
**Type:** Open book, online assessment
**Questions:** Answer all 3 questions

## Solution Coverage

### Question 1: Computational Linear Algebra and Optimization (20 marks)

- **(a) Music Track Identification (6 marks)**
  - (i) Data normalization for similarity search - why different scales matter
  - (ii) Simple search routine design - scalability issues with 101,750 tracks

- **(b) Track-to-Popularity Mapping (3 marks)**
  - (i) Matrix and vector dimensions for linear regression
  - (ii) Pseudo-inverse method for solving least-squares

- **(c) PCA for Visualization (7 marks)**
  - (i) 3D projection procedure preserving variance - complete steps with dimensions
  - (ii) Eigenspectrum analysis - low-rank covariance, 2D vs 3D interface justification

- **(d) Music Generation via Optimization (4 marks)**
  - Optimization problem formulation for genre-based track generation
  - Gradient descent vs stochastic methods
  - Convergence conditions and assumptions

**Topics:** Data normalization, Euclidean distance, similarity search, linear regression, pseudo-inverse, PCA, eigendecomposition, dimensionality reduction, non-linear optimization, gradient descent

---

### Question 2: Probabilities and Bayes Rule (20 marks)

- **(a) Disease Testing Analysis (11 marks)**
  - (i) Bayes formula for p(D|T) and p(D|T̄) from trial data (4 marks)
  - (ii) Test appropriateness for vulnerable populations, severe treatment, population screening (3 marks)
  - (iii) Prevalence estimation accounting for false positives/negatives (4 marks)

- **(b) Vaccine Efficacy Study (9 marks)**
  - (i) Accounting for test limitations in vaccine/placebo groups (5 marks)
  - (ii) Vaccine efficacy calculation and impact of lower test accuracy (4 marks)

**Topics:** Bayes' theorem, conditional probability, sensitivity, specificity, positive/negative predictive value, false positives/negatives, prevalence estimation, vaccine efficacy, test reliability

---

### Question 3: Database Systems (20 marks)

- **(a) Blocking Factors and Storage (2 marks)**
  - Student relation: 50-byte records, 10 records/block, 100 blocks
  - Marks relation: 20-byte records, 25 records/block, 4,000 blocks

- **(b) Query Optimization with Nested-Loop Joins (18 marks)**
  - Student as outer relation: 3,300 block accesses
  - Marks as outer relation: 4,812 block accesses
  - Analysis of heap vs sequential file organizations
  - Binary search optimization for sorted files
  - Block nested-loop join algorithms

**Topics:** Physical database design, blocking factors, heap files, sequential files, nested-loop joins, binary search, query cost estimation, join optimization

---

## Solution Quality

Each solution includes:
- **Problem restatement** with complete context and given data
- **Step-by-step methodology** with detailed explanations
- **All formulas** with mathematical derivations
- **Worked examples** with complete calculations
- **Python code** implementations for practical understanding
- **Verification** of answers where applicable
- **Visual aids, tables, and comparisons**
- **Decision-making frameworks** and analysis
- **Final answers** clearly highlighted

## Key Features

**Comprehensive Coverage:**
- All 3 questions fully solved (60 marks total)
- Multiple solution methods where applicable
- Both theoretical explanations and practical code implementations

**Practical Focus:**
- Python implementations for music similarity search
- NumPy/SciPy for linear algebra and optimization
- Statistical analysis with detailed probability calculations
- Database query cost analysis and simulations

**Real-World Applications:**
- Music streaming service design
- Pandemic modeling and testing strategies
- Vaccine efficacy evaluation
- Database performance tuning

## Topics Covered

**Linear Algebra & Vector Spaces:**
- Data normalization and standardization
- Euclidean distance and similarity metrics
- Covariance matrices and eigendecomposition
- Principal Component Analysis (PCA)
- Dimensionality reduction
- Low-rank matrix approximation

**Optimization:**
- Linear least-squares (pseudo-inverse)
- Non-linear optimization problems
- Gradient descent
- Stochastic hill-climbing
- Convergence conditions
- Lipschitz continuity

**Probability & Statistics:**
- Bayes' theorem and conditional probability
- Sensitivity and specificity
- Positive/negative predictive values
- False positive/negative rates
- Prevalence estimation
- Law of total probability
- Vaccine efficacy calculations

**Machine Learning:**
- Feature normalization
- Distance-based similarity
- Linear regression
- Model evaluation
- Scalability issues

**Database Systems:**
- Physical storage design
- Blocking factors and record organization
- File organizations (heap, sequential)
- Nested-loop join algorithms
- Block nested-loop joins
- Binary search on sorted files
- Query cost estimation
- Join optimization strategies

## Additional Resources

For more information on topics covered:
- **Music Information Retrieval:** Audio features, similarity search, scalable nearest neighbor search (FAISS, Annoy)
- **Linear Algebra:** Pseudo-inverse, Moore-Penrose inverse, SVD applications
- **PCA:** Eigenspectrum analysis, scree plots, variance explained, whitening
- **Optimization:** Gradient-based methods, zero-order methods, Bayesian optimization
- **Probability:** Bayes' theorem applications, diagnostic testing, epidemiology
- **Databases:** Index structures, B+ trees, query execution plans, join algorithms

## Note

The original PDF contains both questions AND official model solutions (marked "SOLUTIONS" on cover page). Our enhanced version provides:
- Extended explanations and mathematical intuitions
- Python code implementations for all computational problems
- Visual aids, tables, and comprehensive examples
- Practical applications and real-world context
- Alternative solution methods and approaches
- Detailed cost-benefit analyses

---

*Solutions prepared with detailed explanations for IDSS 2020-2021 examination (April 2021)*
