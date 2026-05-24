# IDSS 2021-2022 Examination Solutions

## Files in this Directory

1. **idss_m_2021_2022_main.pdf** - Original exam question paper with solutions
2. **IDSS_2021-2022_Solutions.md** - Complete solutions in Markdown format
3. **IDSS_2021-2022_Solutions.html** - Complete solutions in HTML format (styled and ready for viewing)

## How to Create PDF from HTML

Open `IDSS_2021-2022_Solutions.html` in your web browser and use "Print → Save as PDF"

### Quick Method:
1. Double-click `IDSS_2021-2022_Solutions.html` to open in browser
2. Press `Cmd+P` (Mac) or `Ctrl+P` (Windows)
3. Select "Save as PDF"
4. Enable "Background graphics" for better appearance
5. Save the PDF

## Examination Details

**Date:** Wednesday 15th December 2021
**Time:** 9:00 am - 11:30 am
**Course:** Introduction to Data Science and Systems (M) (COMPSCI5089)
**Duration:** 2 hours + 30 minutes additional time
**Total Marks:** 60 marks
**Type:** Open book, online assessment
**Questions:** Answer all 3 questions

## Solution Coverage

### Question 1: Computational Linear Algebra and Optimization (20 marks)

- **(a) Document Similarity (7 marks)**
  - (i) Vector representation of documents (dimension = vocabulary size)
  - (ii) L0 norm interpretation (number of unique terms)
  - (iii) Lp distance definition and formulas
  - (iv) Cosine similarity for length-independent comparison

- **(b) Gaussian Distributions and PCA (4 marks)**
  - (i) Contour plots for 4 different 2D Gaussians with various covariance matrices
  - (ii) PCA dimensionality reduction visual analysis

- **(c) Linear Regression (9 marks)**
  - (i) Stochastic gradient descent derivation with squared loss
  - (ii) Polynomial regression extension, overfitting, and regularization
  - (iii) Learning rate schedules (decreasing vs increasing)

**Topics:** Document vectors, TF-IDF, distance metrics, cosine similarity, Gaussian distributions, PCA, linear regression, SGD, polynomial features, overfitting, regularization

### Question 2: Probabilities and Bayes Rule (20 marks)

- **(a) Basic Probabilities (5 marks)**
  - Drawing from a 32-card deck
  - Probabilities for Ace, red cards, diamonds, royalty, specific cards

- **(b) Conditional Probabilities (4 marks)**
  - Given hand: {10, J, Q}
  - Probability of pairs, two pairs, three of a kind, sequences

- **(c) Expected Value and Decision Making (11 marks)**
  - (i) Expected payout calculation
  - (ii) Decision: draw or fold with cost analysis
  - (iii) Sequential decisions after drawing first card (3 scenarios)

**Topics:** Basic probability, conditional probability, expected value, decision theory, game strategy

### Question 3: Database Systems (20 marks)

- **(a) Storage Calculations (2 marks)**
  - Blocking factors for Seller and Product relations
  - Number of blocks required

- **(b) Query Optimization (18 marks)**
  - (i) Nested loop join with Seller as outer relation (cost: 3,725 blocks)
  - (ii) Nested loop join with Product as outer relation (cost: 7,263 blocks)
  - Analysis of heap vs sequential file organizations
  - Binary search optimization for sorted files

**Topics:** Physical database design, blocking factors, file organizations (heap, sequential), nested-loop joins, query cost analysis, join optimization

## Solution Quality

Each solution includes:
- **Problem restatement** with complete context
- **Step-by-step methodology** with detailed explanations
- **All formulas** with mathematical derivations
- **Worked examples** with complete calculations
- **Python code** implementations for practical understanding
- **Verification** of answers where applicable
- **Visual aids, tables, and comparisons**
- **Decision-making frameworks**
- **Final answers** clearly highlighted

## Key Features

**Comprehensive Coverage:**
- All 3 questions fully solved (60 marks total)
- Multiple solution methods where applicable
- Both theoretical explanations and practical code

**Practical Focus:**
- Python implementations for document similarity (sklearn)
- Gaussian visualization with matplotlib/scipy
- SGD and polynomial regression examples
- Database cost analysis simulations

**Real-World Applications:**
- Information retrieval and document search
- Machine learning model training
- Statistical decision making in games
- Database query optimization

## Topics Covered

**Linear Algebra & Vector Spaces:**
- Document vectorization (bag-of-words, TF-IDF)
- Lp norms and distance metrics
- Cosine similarity
- Gaussian distributions and covariance matrices
- PCA for dimensionality reduction

**Optimization:**
- Stochastic Gradient Descent (SGD)
- Learning rate schedules
- Convergence analysis
- Regularization (L1/L2)

**Probability & Statistics:**
- Basic and conditional probability
- Expected value calculations
- Decision theory
- Game strategy optimization

**Machine Learning:**
- Linear regression
- Polynomial regression
- Overfitting and underfitting
- Cross-validation
- Feature engineering

**Database Systems:**
- Physical storage design
- Blocking factors and record organization
- File organizations (heap, sequential)
- Nested-loop join algorithms
- Query cost estimation
- Join optimization strategies

## Additional Resources

For more information on topics covered:
- **Information Retrieval:** Vector space models, TF-IDF weighting, similarity measures
- **Linear Regression:** Gradient descent variants (batch, mini-batch, SGD), regularization techniques
- **PCA:** Eigendecomposition, variance explained, scree plots
- **Probability:** Bayes' theorem, conditional probability, decision trees
- **Databases:** B+ trees, hash indexes, sort-merge joins, query execution plans

## Note

This PDF contains both questions AND official model solutions. The provided solutions include detailed working, step-by-step derivations, and marking schemes. Our enhanced version adds:
- Extended explanations and intuitions
- Python code implementations
- Visual aids and examples
- Practical applications
- Alternative solution methods

---

*Solutions prepared with detailed explanations for IDSS 2021-2022 examination (December 2021)*
