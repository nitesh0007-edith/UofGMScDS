# IDSS 2022-2023 Examination Solutions

## Files in this Directory

1. **IDSS_2022-23_main.pdf** - Original exam question paper
2. **IDSS_2022-2023_Solutions.md** - Complete solutions in Markdown format
3. **IDSS_2022-2023_Solutions.html** - Complete solutions in HTML format (styled and ready for viewing)

## How to Create PDF from HTML

Open `IDSS_2022-2023_Solutions.html` in your web browser and use "Print → Save as PDF"

### Quick Method:
1. Double-click `IDSS_2022-2023_Solutions.html` to open in browser
2. Press `Cmd+P` (Mac) or `Ctrl+P` (Windows)
3. Select "Save as PDF"
4. Enable "Background graphics" for better appearance
5. Save the PDF

## Examination Details

**Course:** Introduction to Data Science and Systems (COMPSCI 5089)
**Duration:** 2 hours + 30 minutes additional time
**Total Marks:** 60 marks
**Type:** Open book, online assessment
**Questions:** Answer all 4 questions

## Solution Coverage

### Question 1: KNN Classification, PCA, and SVD (15 marks)
- (a) KNN for T-shirt size prediction
  - (i) Euclidean distance calculations
  - (ii) Prediction with k=3
- (b) Covariance matrix and PCA using NumPy
  - (i) Covariance matrix calculation
  - (ii) Eigenvalues and eigenvectors
  - (iii) Dimensionality reduction to principal component
- (c) Singular Value Decomposition
  - (i) SVD calculation for 3×2 matrix with full working
  - (ii) Relations between determinant, inversion, and non-singular matrices

**Topics:** KNN, distance metrics, covariance, eigendecomposition, PCA, SVD, matrix properties

### Question 2: Tennis Serve Statistical Analysis (15 marks)
- (a) Empirical distribution estimation for serve locations
- (b) Normal distribution modeling
  - (i) Parameters and Maximum Likelihood Estimation
  - (ii) Problems with normal distribution for bounded data
- (c) Gaussian Mixture Model parameterization and EM algorithm

**Topics:** Non-parametric estimation, Gaussian distributions, MLE, GMM, EM algorithm, model selection

### Question 3: Radio Programming Optimization (15 marks)
- (a) Linear least squares formulation
  - (i) Variables, dimensions, and interpretation
  - (ii) Model limitations and validation methods
- (b) Non-linear bell curve model
  - (i) Parameter counting and roles (14 parameters)
  - (ii) Gradient descent optimization approach
- (c) Constrained optimization with equality and inequality constraints

**Topics:** Linear regression, non-linear optimization, gradient descent, Lagrange multipliers, constrained optimization

### Question 4: Database Systems (15 marks)
- (a) Weather relation analysis
  - (i) Blocking factor and block count calculations
  - (ii) File organization for frequent inserts (heap file recommendation)
- (b) Three-way join optimization
  - (i) Join strategy selection and cost analysis (10,202 block accesses)
  - (ii) Naive vs Index-based nested loop join comparison

**Topics:** Physical database design, blocking factors, file organizations, join algorithms, query optimization, index structures

## Solution Quality

Each solution includes:
- **Problem restatement** with given information clearly listed
- **Step-by-step methodology** with detailed explanations
- **All formulas** with mathematical derivations
- **Worked examples** with complete calculations
- **Python code** implementations for practical understanding
- **Verification** of answers where applicable
- **Visual aids** and tables for clarity
- **Alternative approaches** discussed
- **Final answers** clearly highlighted

## Key Features

**Comprehensive Coverage:**
- All 4 questions fully solved (60 marks total)
- Multiple solution methods where applicable
- Both theoretical explanations and practical implementations

**Practical Focus:**
- Python code for KNN classification
- NumPy implementations for linear algebra
- Scikit-learn examples for GMM
- SciPy optimization for non-linear problems
- Database query cost analysis

**Real-World Applications:**
- Machine learning classification (T-shirt sizing)
- Sports analytics (tennis serve analysis)
- Media programming optimization
- Database performance tuning

## Topics Covered

**Machine Learning:**
- K-Nearest Neighbors (KNN)
- Principal Component Analysis (PCA)
- Dimensionality reduction
- Model validation and cross-validation

**Statistics:**
- Empirical distributions
- Normal distributions and MLE
- Gaussian Mixture Models
- EM algorithm
- Statistical inference

**Optimization:**
- Linear least squares
- Non-linear optimization
- Gradient descent
- Constrained optimization
- Lagrange multipliers

**Linear Algebra:**
- Covariance matrices
- Eigendecomposition
- Singular Value Decomposition (SVD)
- Matrix properties and inverses

**Database Systems:**
- Physical storage design
- Blocking factors
- File organizations (heap, sequential, hash)
- Join algorithms (nested loop, index-based)
- Query optimization and cost estimation

## Additional Resources

For more information on topics covered:
- **KNN:** Curse of dimensionality, distance metrics, weighted voting
- **PCA:** Whitening, kernel PCA, applications in ML
- **GMM:** Model selection (BIC/AIC), initialization strategies
- **Optimization:** Second-order methods (Newton, L-BFGS), convergence criteria
- **Databases:** B+ trees, hash indexes, query plan optimization

---

*Solutions prepared with detailed explanations for IDSS 2022-2023 examination*
