# IDSS 2023-2024 Examination Solutions

**University of Glasgow**
**Introduction to Data Science and Systems**
**COMPSCI 5089**
**Date: December 2023**
**Total Marks: 80**

---

## Question 1: Linear Algebra (20 marks)

### Part (a): Whitening a dataset [6 marks]

**Given:**
- Data matrix M: 100 rows × 10 columns
- Each row = one subject
- Each column = one observation/feature

**Goal:** Whiten the dataset

**What is Whitening?**

Whitening (also called sphering) transforms data so that:
1. Mean is zero (centered)
2. Covariance is identity matrix (uncorrelated, unit variance)

---

**Step-by-Step Whitening Process:**

**Step 1: Center the Data**

Subtract the mean from each column to center the data at origin.

**Formula:**
```
M_centered = M - μ
```

where μ is the mean vector (1 × 10).

**Calculation:**
```python
# Compute mean of each column
mu = (1/N) * Σᵢ₌₁ᴺ M[i, :]  # Shape: (10,)

# Or in numpy:
mu = np.mean(M, axis=0)  # Shape: (10,)

# Center the data
M_centered = M - mu  # Broadcasting: (100, 10) - (10,) → (100, 10)
```

**Dimensions:**
- M: (100, 10)
- μ: (10,) or (1, 10)
- M_centered: (100, 10)

---

**Step 2: Compute Covariance Matrix**

Calculate the covariance matrix of the centered data.

**Formula:**
```
C = (1/(N-1)) * M_centeredᵀ * M_centered
```

**Calculation:**
```python
# Covariance matrix
C = (1/(N-1)) * M_centered.T @ M_centered

# Or using numpy:
C = np.cov(M.T)  # Shape: (10, 10)
```

**Dimensions:**
- M_centeredᵀ: (10, 100)
- M_centered: (100, 10)
- C: (10, 10) - symmetric positive semi-definite matrix

**Properties of C:**
- Diagonal elements: variances of each feature
- Off-diagonal elements: covariances between features

---

**Step 3: Eigen-decomposition of Covariance Matrix**

Decompose the covariance matrix into eigenvalues and eigenvectors.

**Formula:**
```
C = VΛVᵀ
```

where:
- V: matrix of eigenvectors (10 × 10)
- Λ: diagonal matrix of eigenvalues (10 × 10)

**Calculation:**
```python
# Eigenvalue decomposition
eigenvalues, eigenvectors = np.linalg.eig(C)
# eigenvalues: (10,) array
# eigenvectors: (10, 10) matrix, columns are eigenvectors

# Create diagonal matrix
Lambda = np.diag(eigenvalues)  # Shape: (10, 10)
V = eigenvectors  # Shape: (10, 10)
```

**Dimensions:**
- Λ: (10, 10) diagonal matrix
- V: (10, 10) orthonormal matrix (VᵀV = I)

**Note:** Eigenvalues λᵢ represent variance along principal component i

---

**Step 4: Compute Whitening Matrix**

The whitening transformation matrix scales each principal component by 1/√λᵢ.

**Formula:**
```
W = Λ^(-1/2) * Vᵀ
```

where Λ^(-1/2) is diagonal matrix with elements 1/√λᵢ

**Calculation:**
```python
# Compute Λ^(-1/2)
Lambda_inv_sqrt = np.diag(1.0 / np.sqrt(eigenvalues))  # Shape: (10, 10)

# Whitening matrix
W = Lambda_inv_sqrt @ V.T  # Shape: (10, 10)
```

**Dimensions:**
- Λ^(-1/2): (10, 10)
- Vᵀ: (10, 10)
- W: (10, 10)

---

**Step 5: Apply Whitening Transform**

Transform the centered data using the whitening matrix.

**Formula:**
```
M_whitened = M_centered * Wᵀ
```

Or equivalently:
```
M_whitened = M_centered * V * Λ^(-1/2)
```

**Calculation:**
```python
# Apply whitening
M_whitened = M_centered @ W.T  # Shape: (100, 10)

# Equivalent form:
M_whitened = M_centered @ V @ Lambda_inv_sqrt  # Shape: (100, 10)
```

**Dimensions:**
- M_centered: (100, 10)
- W: (10, 10)
- Wᵀ: (10, 10)
- M_whitened: (100, 10)

---

**Verification:**

Check that the whitened data has desired properties:

```python
# 1. Check mean is zero
mean_whitened = np.mean(M_whitened, axis=0)
# Should be ≈ [0, 0, ..., 0]

# 2. Check covariance is identity
C_whitened = np.cov(M_whitened.T)
# Should be ≈ I (10×10 identity matrix)

# 3. Verify
print(np.allclose(C_whitened, np.eye(10)))  # Should print True
```

---

**Summary of Dimensions:**

| Matrix/Vector | Dimension | Description |
|---------------|-----------|-------------|
| M | (100, 10) | Original data |
| μ | (10,) | Mean vector |
| M_centered | (100, 10) | Centered data |
| C | (10, 10) | Covariance matrix |
| Λ | (10, 10) | Eigenvalues (diagonal) |
| V | (10, 10) | Eigenvectors |
| Λ^(-1/2) | (10, 10) | Inverse sqrt eigenvalues |
| W | (10, 10) | Whitening matrix |
| M_whitened | (100, 10) | Whitened data |

---

**Complete Python Implementation:**

```python
import numpy as np

# Step 1: Center the data
mu = np.mean(M, axis=0)  # (10,)
M_centered = M - mu  # (100, 10)

# Step 2: Compute covariance
C = np.cov(M.T)  # (10, 10)

# Step 3: Eigendecomposition
eigenvalues, V = np.linalg.eig(C)
# eigenvalues: (10,)
# V: (10, 10)

# Step 4: Whitening matrix
Lambda_inv_sqrt = np.diag(1.0 / np.sqrt(eigenvalues))  # (10, 10)
W = Lambda_inv_sqrt @ V.T  # (10, 10)

# Step 5: Whiten the data
M_whitened = M_centered @ W.T  # (100, 10)

# Verify
C_whitened = np.cov(M_whitened.T)
print("Covariance is identity:", np.allclose(C_whitened, np.eye(10)))
```

---

### Part (b): Effect of whitening on height and weight [4 marks]

**Given Variables:**
- H: Height (in meters)
- W: Weight (in pounds)

**Issue:** Different units and scales
- Height: typically 1.5 - 2.0 meters
- Weight: typically 100 - 250 pounds

---

**Effect of Whitening:**

**1. Standardization:**

Whitening will:
- Center each variable to zero mean
- Scale each to unit variance
- Remove correlation between H and W

**Before whitening:**
```
H_original: mean ≈ 1.7m, std ≈ 0.1m
W_original: mean ≈ 150lbs, std ≈ 30lbs
Correlation: ρ(H,W) ≈ 0.7 (typically positive)
```

**After whitening:**
```
H_whitened: mean = 0, std = 1
W_whitened: mean = 0, std = 1
Correlation: ρ(H_whitened, W_whitened) = 0 (uncorrelated)
```

---

**2. Unit Removal:**

Whitened variables are **dimensionless** (no units):
- Original: H in meters, W in pounds
- Whitened: Both are unitless standardized values

**Interpretation:**
- H_whitened = 1.5 means "1.5 standard deviations above mean height"
- W_whitened = -0.5 means "0.5 standard deviations below mean weight"

---

**3. Equal Weighting:**

Variables with different scales now contribute equally.

**Before whitening:**
- Weight dominates (larger numerical values)
- Distance: √((H₁-H₂)² + (W₁-W₂)²) ≈ √((0.1)² + (50)²) ≈ 50
- Weight change dominates distance calculation

**After whitening:**
- Both variables equally weighted
- Distance: √((H₁'-H₂')² + (W₁'-W₂')²)
- Height and weight changes contribute equally

---

**Why Desirable?**

**1. Machine Learning Algorithms:**

Many ML algorithms assume:
- Features on similar scales
- No multicollinearity

**Algorithms that benefit:**
- K-means clustering (distance-based)
- PCA (variance-based)
- Neural networks (gradient descent)
- SVM with RBF kernel
- K-nearest neighbors

**Without whitening:**
- Weight (larger scale) dominates
- Algorithm focuses on weight, ignores height
- Biased predictions

---

**2. Distance Metrics:**

For Euclidean distance:

**Before whitening:**
```
Person A: H=1.7m, W=150lbs
Person B: H=1.8m, W=160lbs
Person C: H=1.7m, W=200lbs

d(A,B) = √((1.7-1.8)² + (150-160)²) = √(0.01 + 100) ≈ 10.0
d(A,C) = √((1.7-1.7)² + (150-200)²) = √(0 + 2500) = 50.0
```

Height difference barely affects distance!

**After whitening:**
```
Assume: mean_H=1.7, std_H=0.1, mean_W=150, std_W=30

Person A: H'=0, W'=0
Person B: H'=1, W'=0.33
Person C: H'=0, W'=1.67

d(A,B) = √(1² + 0.33²) ≈ 1.05
d(A,C) = √(0² + 1.67²) ≈ 1.67
```

Now both features contribute meaningfully!

---

**Example Application: Health Clustering**

**Task:** Cluster people into health risk groups based on H and W.

**Without whitening:**
- Clusters mainly determined by weight
- People with same weight but different heights grouped together
- Unhealthy: ignores BMI relationship

**With whitening:**
- Both height and weight considered
- Naturally identifies BMI patterns
- Better health risk assessment

**BMI context:**
```
BMI = W / H²

Two people:
1. H=1.5m, W=150lbs → BMI high (overweight)
2. H=2.0m, W=150lbs → BMI low (underweight)
```

Whitening allows algorithm to distinguish these cases!

---

**When Desirable?**

**Whitening is desirable when:**

1. **Different scales:** Variables measured in different units
2. **Distance-based methods:** K-means, KNN, PCA
3. **Gradient-based optimization:** Neural networks
4. **Fair feature importance:** All features should contribute equally
5. **Removing correlations:** When independence assumption required

**Whitening NOT desirable when:**

1. **Interpretability needed:** Original units more meaningful
2. **Domain knowledge:** Some features should naturally dominate
3. **Sparse data:** Whitening can destroy sparsity
4. **Ordinal/categorical:** Not applicable to non-numerical data

---

**Practical Example:**

```python
# Before whitening
H = np.array([1.65, 1.70, 1.75, 1.80, 1.85])  # meters
W = np.array([140, 150, 160, 170, 180])  # pounds

# Stack into matrix
data = np.column_stack([H, W])  # (5, 2)

# Whiten
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data_whitened = scaler.fit_transform(data)

print("Original data:")
print(data)
print("\nWhitened data:")
print(data_whitened)
print("\nMean:", data_whitened.mean(axis=0))  # [0, 0]
print("Std:", data_whitened.std(axis=0))  # [1, 1]
```

---

### Part (c)(i): Calculate matrix M from two point correspondences [7 marks]

**Given:**
- P → P': One point correspondence
- Q → Q': Another point correspondence
- M: 2×2 transformation matrix
- P' = MP and Q' = MQ

**From figure:** (approximate coordinates)
- P ≈ (4, 5)
- P' ≈ (5, 1)
- Q ≈ (2, 4)
- Q' ≈ (1, 3)

---

**Problem Setup:**

We have a linear transformation:
```
P' = MP
Q' = MQ
```

Let M be a 2×2 matrix:
```
M = [m₁₁  m₁₂]
    [m₂₁  m₂₂]
```

We need to find the 4 unknowns: m₁₁, m₁₂, m₂₁, m₂₂

---

**Step 1: Write Out the Equations**

**For point P → P':**
```
[p'ₓ] = [m₁₁  m₁₂] [pₓ]
[p'ᵧ]   [m₂₁  m₂₂] [pᵧ]
```

Expanding:
```
p'ₓ = m₁₁·pₓ + m₁₂·pᵧ  ... (1)
p'ᵧ = m₂₁·pₓ + m₂₂·pᵧ  ... (2)
```

**For point Q → Q':**
```
q'ₓ = m₁₁·qₓ + m₁₂·qᵧ  ... (3)
q'ᵧ = m₂₁·qₓ + m₂₂·qᵧ  ... (4)
```

---

**Step 2: Organize as Linear System**

We have 4 equations and 4 unknowns. Rewrite in matrix form:

**Rearrange as Ax = b:**

Let x = [m₁₁, m₁₂, m₂₁, m₂₂]ᵀ (the unknowns)

From equations (1) and (3) (x-coordinates):
```
pₓ·m₁₁ + pᵧ·m₁₂ = p'ₓ
qₓ·m₁₁ + qᵧ·m₁₂ = q'ₓ
```

From equations (2) and (4) (y-coordinates):
```
pₓ·m₂₁ + pᵧ·m₂₂ = p'ᵧ
qₓ·m₂₁ + qᵧ·m₂₂ = q'ᵧ
```

---

**Step 3: Matrix Formulation**

**Method 1: Separate systems for each row of M**

**For first row [m₁₁, m₁₂]:**
```
[pₓ  pᵧ] [m₁₁]   [p'ₓ]
[qₓ  qᵧ] [m₁₂] = [q'ₓ]
```

**For second row [m₂₁, m₂₂]:**
```
[pₓ  pᵧ] [m₂₁]   [p'ᵧ]
[qₓ  qᵧ] [m₂₂] = [q'ᵧ]
```

---

**Method 2: Stack points as matrices**

Define:
```
P_matrix = [P, Q] = [pₓ  qₓ]  (2×2)
                    [pᵧ  qᵧ]

P'_matrix = [P', Q'] = [p'ₓ  q'ₓ]  (2×2)
                       [p'ᵧ  q'ᵧ]
```

Then:
```
P'_matrix = M · P_matrix
```

Therefore:
```
M = P'_matrix · P_matrix⁻¹
```

---

**Step 4: Solve for M**

**Using Method 2 (most elegant):**

```python
# Define point coordinates
P = np.array([4, 5])  # pₓ, pᵧ
P_prime = np.array([5, 1])  # p'ₓ, p'ᵧ
Q = np.array([2, 4])  # qₓ, qᵧ
Q_prime = np.array([1, 3])  # q'ₓ, q'ᵧ

# Stack into matrices (points as columns)
P_matrix = np.column_stack([P, Q])  # [[4, 2],
                                     #  [5, 4]]

P_prime_matrix = np.column_stack([P_prime, Q_prime])  # [[5, 1],
                                                       #  [1, 3]]

# Solve: M = P'_matrix · P_matrix⁻¹
P_matrix_inv = np.linalg.inv(P_matrix)
M = P_prime_matrix @ P_matrix_inv

print("Transformation matrix M:")
print(M)
```

---

**Step 5: Verification**

```python
# Verify P' = M·P
P_calc = M @ P
print("Calculated P':", P_calc)
print("Actual P':", P_prime)
print("Match:", np.allclose(P_calc, P_prime))

# Verify Q' = M·Q
Q_calc = M @ Q
print("Calculated Q':", Q_calc)
print("Actual Q':", Q_prime)
print("Match:", np.allclose(Q_calc, Q_prime))
```

---

**Alternative: Using least squares (more numerically stable)**

```python
# For x-coordinates: solve for [m₁₁, m₁₂]
A_x = np.array([[pₓ, pᵧ],
                [qₓ, qᵧ]])
b_x = np.array([p'ₓ, q'ₓ])
row1 = np.linalg.solve(A_x, b_x)  # [m₁₁, m₁₂]

# For y-coordinates: solve for [m₂₁, m₂₂]
b_y = np.array([p'ᵧ, q'ᵧ])
row2 = np.linalg.solve(A_x, b_y)  # [m₂₁, m₂₂]

# Construct M
M = np.array([row1, row2])
```

---

**Summary of Method:**

1. **Set up equations:** P' = MP, Q' = MQ
2. **Stack points:** P_matrix = [P | Q], P'_matrix = [P' | Q']
3. **Matrix equation:** P'_matrix = M · P_matrix
4. **Solve:** M = P'_matrix · P_matrix⁻¹
5. **Verify:** Check MP = P' and MQ = Q'

**Requirements:**
- P and Q must be linearly independent (not collinear)
- P_matrix must be invertible (det(P_matrix) ≠ 0)

---

### Part (c)(ii): Using three point correspondences [3 marks]

**Question:** With third point R → R', can we use same approach?

**Answer: No, we cannot use the same approach directly.**

---

**Why Not?**

**Overdetermined System:**

With 2 points: 4 equations, 4 unknowns → **exactly determined** ✓
With 3 points: 6 equations, 4 unknowns → **overdetermined** ✗

**The system:**
```
R'ₓ = m₁₁·rₓ + m₁₂·rᵧ  ... (5)
R'ᵧ = m₂₁·rₓ + m₂₂·rᵧ  ... (6)
```

Adding to previous 4 equations gives 6 equations total.

**Problem:**
- More equations than unknowns
- System may be inconsistent (no exact solution)
- Cannot invert a non-square matrix

---

**When Can We Use Same Approach?**

Only if R' = MR where M is the **same** matrix from P and Q.

**This requires:** All three points are related by the **same linear transformation**.

**If true:** R → R' is redundant, doesn't add new information.

---

**How to Find M with 3 Points?**

**Method 1: Least Squares Solution**

Use overdetermined system and minimize error:

```python
# Stack all three points
P_matrix = np.column_stack([P, Q, R])  # (2×3)
P_prime_matrix = np.column_stack([P_prime, Q_prime, R_prime])  # (2×3)

# Solve: M = P'_matrix · P_matrix^+
# where P_matrix^+ is pseudo-inverse
P_matrix_pinv = np.linalg.pinv(P_matrix)
M = P_prime_matrix @ P_matrix_pinv

# This minimizes: ||M·P_matrix - P'_matrix||²
```

**Properties:**
- Minimizes squared error across all three points
- Handles noise in measurements
- More robust than 2-point solution

---

**Method 2: Use Only 2 Points, Verify with 3rd**

```python
# Calculate M using P and Q only (as before)
M = calculate_M_from_PQ(P, P_prime, Q, Q_prime)

# Verify with R
R_calc = M @ R
error = np.linalg.norm(R_calc - R_prime)

if error < tolerance:
    print("R is consistent with same transformation")
else:
    print("Points not related by single linear transformation")
    print("Use least squares instead")
```

---

**Method 3: Weighted Least Squares**

If some correspondences are more reliable:

```python
from scipy.optimize import least_squares

def residuals(m_flat, points, points_prime, weights):
    M = m_flat.reshape(2, 2)
    errors = []
    for i, (p, p_prime, w) in enumerate(zip(points, points_prime, weights)):
        predicted = M @ p
        error = w * (predicted - p_prime)
        errors.extend(error)
    return errors

# Initial guess
m0 = np.eye(2).flatten()

# Points and weights
points = [P, Q, R]
points_prime = [P_prime, Q_prime, R_prime]
weights = [1.0, 1.0, 0.5]  # R less reliable

# Solve
result = least_squares(residuals, m0, args=(points, points_prime, weights))
M = result.x.reshape(2, 2)
```

---

**Comparison:**

| Method | Pros | Cons | When to use |
|--------|------|------|-------------|
| Exact (2 points) | Simple, exact solution | Requires exactly 2 points | Clean data, exact correspondences |
| Least squares (3+ points) | Handles noise, more robust | Approximate solution | Noisy measurements, redundant data |
| Weighted LS | Accounts for reliability | More complex | Some measurements more reliable |

---

**Practical Note:**

In computer vision/robotics, having **more** correspondences is always better:
- Provides redundancy
- Handles outliers
- More robust to noise
- Use RANSAC for outlier rejection

**Recommended:** Use least squares with 3+ points for real applications!

---

## Question 2: Optimization (20 marks)

### Part (a): Characterize loss function at specific points [6 marks]

Looking at the contour plot, we need to analyze three points:

---

**Point (-1, -1):**

**Location:** Upper left region of the plot

**Loss Function Characterization:**
- **Type:** Local minimum (valley bottom on left side)
- **Value:** Approximately 0.25 (from contour lines)

**Gradient Analysis:**

**Direction:** Zero vector (∇f = 0)
- At a local minimum, gradient vanishes
- All partial derivatives are zero
- No direction of decrease exists

**Magnitude:** ||∇f|| = 0

**Why?**
- Point is at the bottom of a local valley
- Moving in any direction increases loss
- First-order optimality condition satisfied: ∇f = 0

**Mathematical:**
```
∂f/∂x₁ |₍₋₁,₋₁₎ = 0
∂f/∂x₂ |₍₋₁,₋₁₎ = 0
```

**Hessian:** Positive definite (eigenvalues > 0)
- Confirms this is a minimum, not saddle point or maximum

---

**Point (-1, 1):**

**Location:** Upper middle region, between two minima

**Loss Function Characterization:**
- **Type:** Saddle point
- **Value:** Approximately 1.0-1.5

**Gradient Analysis:**

**Direction:** Cannot be zero (not an extremum)
- Looking at contours, gradient points away from saddle
- Two main components:
  - Positive x-direction (towards right minimum)
  - Or negative x-direction (towards left minimum)
  - Depending on exact location relative to saddle

**Best estimate:** Gradient points in x-direction (horizontally)

**Magnitude:** Moderate ||∇f|| ≈ 0.5-1.0

**Why?**
- Contour lines moderately spaced
- Not a stationary point (gradient ≠ 0)
- On a ridge between two valleys
- Moving right or left decreases loss

**Note:** If (-1, 1) is exactly at the saddle point:
- Gradient = 0
- Hessian has both positive and negative eigenvalues
- Unstable equilibrium

---

**Point (-2, 1.5):**

**Location:** Far upper left, steep region

**Loss Function Characterization:**
- **Type:** Steep region (not an extremum)
- **Value:** High, approximately 2.0-3.0

**Gradient Analysis:**

**Direction:**
Looking at contour lines, gradient points:
- **Primary:** Towards right and down (southeast direction)
- Perpendicular to contours
- Pointing towards nearest minimum (left valley)

**Approximate direction:** ≈ (1, -1) normalized: (0.707, -0.707)

**Magnitude:** Large ||∇f|| ≈ 2.0-3.0

**Why?**
- Contour lines very close together → steep gradient
- Far from any minimum
- Strong direction of decrease exists
- Moving towards (-1, -1) minimum

**Mathematical estimate:**
```
∇f|₍₋₂,₁.₅₎ ≈ [2.0, -2.0]ᵀ  (pointing southeast)
||∇f|| ≈ 2.83
```

---

**Summary Table:**

| Point | Type | Loss Value | Gradient Direction | Gradient Magnitude |
|-------|------|------------|-------------------|-------------------|
| (-1, -1) | Local minimum | ~0.25 | Zero (none) | 0 |
| (-1, 1) | Saddle/ridge | ~1.0-1.5 | Horizontal (±x) | Moderate (~0.5) |
| (-2, 1.5) | Steep region | ~2.0-3.0 | Southeast (↘) | Large (~2-3) |

**Key Observations:**
1. Gradient magnitude indicates steepness
2. Gradient direction perpendicular to contour lines
3. At minima, gradient vanishes
4. Far from minima, gradients are large

---

### Part (b): Identify optimization algorithms from trajectories [6 marks]

Looking at the four trajectories (A=red, B=green, C=blue, D=black):

---

**Which is Gradient Descent? → Trajectory C (blue)**

**Characteristics of trajectory C:**
- Starts at approximately (1.5, 0)
- Takes many small steps
- Follows path perpendicular to contours
- Converges slowly to minimum
- Smooth, consistent trajectory
- Zig-zag pattern typical of gradient descent

**Why gradient descent?**

1. **Small steps:** Learning rate α is conservative
2. **Perpendicular to contours:** Follows negative gradient direction
3. **Slow convergence:** Many iterations needed
4. **Characteristic zig-zagging:** Especially in elongated valleys

**Update rule:**
```
xₖ₊₁ = xₖ - α∇f(xₖ)
```

**Behavior:**
- Each step goes in steepest descent direction
- Step size constant (α fixed)
- Inefficient in narrow valleys (oscillation)

---

**Which is Hill-Climbing? → Trajectory A (red)**

**Characteristics of trajectory A:**
- Starts at approximately (-1, 1)
- Moves horizontally rightward
- Eventually gets stuck at right-side minimum
- Relatively direct path
- Medium step sizes

**Why hill-climbing?**

Hill-climbing maximizes an objective, equivalent to minimizing -f(x).

But looking more carefully, trajectory A shows:
- **Escapes the left minimum** (passes over saddle)
- Moves towards better (lower) region
- This suggests **simulated annealing** or **stochastic search**

**Alternative interpretation:**
If we interpret "hill-climbing" as any gradient-free method:
- Random search component
- Can escape local minima
- Not strictly following gradient

Actually, trajectory A most resembles:
- **Simulated annealing** (can move uphill early on)
- **Momentum-based method** (overshoots saddle)

**Best answer: A is likely a stochastic/hill-climbing variant**

---

**Which is Newton's Method? → Trajectory B (green)**

**Characteristics of trajectory B:**
- Starts near (0, 0.5)
- Takes very few steps (2-4 iterations)
- Large, intelligent steps
- Converges rapidly to right minimum
- Nearly straight path to optimum

**Why Newton's method?**

1. **Very fast convergence:** Quadratic convergence rate
2. **Few iterations:** Typical of Newton methods
3. **Optimal step direction:** Uses curvature information
4. **Direct path:** Not following contours, using Hessian

**Update rule:**
```
xₖ₊₁ = xₖ - H⁻¹∇f(xₖ)
```

where H is the Hessian matrix (second derivatives).

**Advantages:**
- Accounts for curvature (not just gradient)
- Adapts step size automatically
- Optimal for quadratic functions

**Why so few steps?**
- For quadratic functions, Newton converges in 1 step
- This loss looks locally quadratic near minimum
- Each step accounts for valley shape

---

**What about Trajectory D (black)?**

**Characteristics:**
- Starts at (-2.5, 0.5)
- Moves towards left minimum
- Converges steadily but not as fast as B
- More steps than Newton, fewer than basic GD

**Likely candidate:**
- **Conjugate Gradient**
- **Quasi-Newton (BFGS)**
- **Gradient Descent with momentum**

These methods are between GD and Newton in performance.

---

**Summary:**

| Trajectory | Algorithm | Reasoning |
|------------|-----------|-----------|
| **A (red)** | Hill-climbing / Simulated annealing | Can escape local minimum, random component |
| **B (green)** | **Newton's method** | Very fast (2-4 steps), uses curvature |
| **C (blue)** | **Gradient descent** | Many small steps, zig-zagging, slow |
| **D (black)** | Quasi-Newton / Conjugate gradient | Faster than GD, slower than Newton |

---

**Detailed Comparison:**

**Gradient Descent (C):**
- Pros: Simple, guaranteed descent
- Cons: Slow, sensitive to learning rate
- Steps: 20-50 iterations
- Path: Perpendicular to contours

**Newton's Method (B):**
- Pros: Very fast, optimal for quadratics
- Cons: Expensive (requires Hessian)
- Steps: 2-5 iterations
- Path: Nearly straight line

**Hill-Climbing (A):**
- Pros: Can escape local minima
- Cons: No convergence guarantee
- Steps: Variable
- Path: Random/stochastic component

---

### Part (c): Issues with iterative algorithms and solutions [5 marks]

**Issue: Multiple Local Minima**

**Problem Identified:**

From the contour plot, there are **at least two local minima:**
1. Left minimum: around (-1, -1)
2. Right minimum: around (1.5, -1)

**Why is this an issue?**

---

**1. Initial Point Dependence:**

The solution found depends on where the algorithm starts:

```
Start at x₀ = (-2, 1)  →  Converges to left minimum
Start at x₀ = (2, 0)   →  Converges to right minimum
```

**Consequence:**
- No guarantee of finding global minimum
- Different runs give different results
- Solution is random/unpredictable

---

**2. Convergence to Suboptimal Solution:**

**If left minimum is higher than right:**
- Algorithm may get stuck in left valley
- Misses the better (lower) right minimum
- Suboptimal solution

**Example values from plot:**
```
Left minimum: f ≈ 0.25
Right minimum: f ≈ 0.10 (appears lower)
```

If right is global optimum, converging to left is suboptimal!

---

**3. Saddle Point Problem:**

Between the two minima is a **saddle point/ridge** around (-1, 1).

**Issue:**
- Gradient near saddle is very small
- Algorithm slows down dramatically
- May take very long to choose direction
- Numerical precision issues

---

**Solutions to Mitigate:**

**Solution 1: Multiple Random Restarts**

Run optimization many times from different random starting points:

```python
best_solution = None
best_loss = float('inf')

for trial in range(N_trials):  # e.g., N=50
    # Random initialization
    x0 = np.random.uniform(-3, 3, size=2)

    # Run optimization
    result = minimize(loss_func, x0, method='BFGS')

    # Keep best
    if result.fun < best_loss:
        best_loss = result.fun
        best_solution = result.x

return best_solution
```

**Benefits:**
- Explores different regions
- Likely to find global minimum (with enough trials)
- Simple to implement

**Drawback:**
- Computationally expensive (N× cost)

---

**Solution 2: Simulated Annealing**

Allow algorithm to occasionally move uphill (accept worse solutions):

```python
def simulated_annealing(loss_func, x0, T_initial, cooling_rate):
    x = x0
    T = T_initial

    for iteration in range(max_iter):
        # Propose new point (random neighbor)
        x_new = x + np.random.randn(2) * step_size

        # Compute energy difference
        delta_E = loss_func(x_new) - loss_func(x)

        # Accept if better, or with probability exp(-ΔE/T)
        if delta_E < 0 or np.random.rand() < np.exp(-delta_E / T):
            x = x_new

        # Cool down
        T *= cooling_rate

    return x
```

**Benefits:**
- Can escape local minima early on (high T)
- Settles into global minimum later (low T)
- No need for multiple restarts

---

**Solution 3: Basin-Hopping**

Combine local optimization with random jumps:

```python
from scipy.optimize import basinhopping

# Callback to track progress
def print_fun(x, f, accepted):
    print(f"Current minimum: {f:.4f}")

result = basinhopping(
    loss_func,
    x0,
    niter=100,  # Number of basin-hopping iterations
    T=1.0,  # Temperature for acceptance
    stepsize=0.5,  # Size of random jumps
    minimizer_kwargs={'method': 'BFGS'},
    callback=print_fun
)
```

**How it works:**
1. Perform local minimization from x₀
2. Make a random jump
3. Perform local minimization from new point
4. Accept if improves global best
5. Repeat

---

**Solution 4: Global Optimization Methods**

**Differential Evolution:**
```python
from scipy.optimize import differential_evolution

bounds = [(-3, 3), (-3, 3)]  # Search space
result = differential_evolution(loss_func, bounds)
```

**Particle Swarm Optimization:**
```python
from pyswarm import pso

lb = [-3, -3]  # Lower bounds
ub = [3, 3]    # Upper bounds
xopt, fopt = pso(loss_func, lb, ub)
```

---

**Solution 5: Gradient Descent with Momentum**

Add momentum to help escape shallow local minima:

```python
def gd_with_momentum(loss_func, grad_func, x0, alpha=0.01, beta=0.9):
    x = x0
    v = np.zeros_like(x)  # Velocity

    for iteration in range(max_iter):
        # Compute gradient
        g = grad_func(x)

        # Update velocity
        v = beta * v + alpha * g

        # Update position
        x = x - v

    return x
```

**Benefit:** Momentum carries through small barriers

---

**Looking at the Graph - Is this likely a problem?**

**Analysis:**

1. **Two clear minima:** Yes, definitely multiple local minima

2. **Separation:** Minima are well-separated
   - Left: (-1, -1)
   - Right: (1.5, -1)
   - Distance ≈ 2.5 units apart

3. **Barrier height:**
   - Barrier at saddle ≈ 1.0
   - Minima at ≈ 0.1-0.25
   - **Barrier height ≈ 0.75-0.9**

4. **Starting point matters greatly**

**Verdict: YES, this IS a problem for this application!**

**Why:**
- Significant barrier between minima
- Standard GD will definitely get stuck
- Need one of the solutions above

**Recommended approach:**
- Use multiple random restarts (10-20 runs)
- Or use basin-hopping
- For production: Differential evolution

---

### Part (d): Avoid finding bottom-right minimum [3 marks]

**Goal:** Optimize to find left minimum, avoid right minimum

**Challenge:** Right minimum appears to be the global optimum (lowest point)!

---

**Solution: Constrained Optimization**

**Method 1: Add Constraint to Stay Left**

Add constraint: x₁ < 0 (stay in left half-plane)

```python
from scipy.optimize import minimize

# Define constraint
def constraint(x):
    return -x[0]  # Requires x[0] < 0

con = {'type': 'ineq', 'fun': constraint}

# Optimize with constraint
result = minimize(
    loss_func,
    x0=[-2, 1],  # Start on left
    method='SLSQP',  # Sequential Least Squares
    constraints=con
)
```

**Explanation:**
- Inequality constraint: x₁ ≤ 0
- Forces solution to left side
- SLSQP can handle constraints
- Will find left minimum

---

**Method 2: Add Penalty to Right Region**

Modify loss function to penalize right side:

```python
def penalized_loss(x):
    loss = original_loss(x)

    # Add penalty if x[0] > 0
    if x[0] > 0:
        penalty = 1000 * x[0]**2  # Large penalty
        loss += penalty

    return loss

# Optimize penalized loss
result = minimize(penalized_loss, x0, method='BFGS')
```

**How it works:**
- Original loss for x₁ < 0
- Huge penalty for x₁ > 0
- Algorithm stays on left side

---

**Method 3: Box Constraints (Bounded Optimization)**

Restrict search space:

```python
from scipy.optimize import minimize

# Bounds: x₁ ∈ [-3, 0], x₂ ∈ [-3, 3]
bounds = [(-3, 0), (-3, 3)]

result = minimize(
    loss_func,
    x0=[-2, 1],
    method='L-BFGS-B',  # Bounded L-BFGS
    bounds=bounds
)
```

**Benefits:**
- Simple to implement
- Computationally efficient
- Guaranteed to satisfy bounds

---

**Method 4: Barrier Function**

Add logarithmic barrier:

```python
def barrier_loss(x, mu=0.01):
    loss = original_loss(x)

    # Barrier: -μ log(-x[0]) enforces x[0] < 0
    if x[0] >= 0:
        return float('inf')  # Infeasible

    barrier = -mu * np.log(-x[0])
    return loss + barrier

# Optimize
result = minimize(barrier_loss, x0=[-2, 1], args=(mu,))
```

**As μ → 0:** Solution approaches constrained optimum

---

**Method 5: Projection Method**

After each gradient step, project back to feasible region:

```python
def projected_gradient_descent(loss_func, grad_func, x0, alpha=0.01):
    x = x0

    for iteration in range(max_iter):
        # Gradient step
        g = grad_func(x)
        x_new = x - alpha * g

        # Project: if x_new[0] > 0, set to 0
        x_new[0] = min(x_new[0], 0)

        x = x_new

    return x
```

**Ensures:** x₁ ≤ 0 at every iteration

---

**Method 6: Careful Initialization**

Start from left side and use small learning rate:

```python
# Start deep in left region
x0 = [-2.5, 1.0]

# Use small learning rate
result = minimize(
    loss_func,
    x0,
    method='BFGS',
    options={'gtol': 1e-6, 'maxiter': 50}
)

# Stop early if approaching right side
if result.x[0] > -0.5:
    print("Getting too close to right minimum, stopping")
```

**Not recommended:** Unreliable, depends on hyperparameters

---

**Summary of Methods:**

| Method | Pros | Cons | Reliability |
|--------|------|------|-------------|
| **Box constraints** | Simple, efficient | Hard bounds only | ✓✓✓ Best |
| Add penalty | Flexible | Needs tuning | ✓✓ Good |
| Barrier function | Theoretical guarantees | Numerical issues | ✓✓ Good |
| Projection | Simple implementation | May be slow | ✓ Okay |
| Careful init | Easy | Unreliable | ✗ Poor |

**Recommended: Use box constraints with L-BFGS-B**

---

**Complete Solution:**

```python
from scipy.optimize import minimize

def optimize_left_minimum():
    """Find left minimum, avoiding right minimum."""

    # Box constraints: x₁ ≤ 0
    bounds = [(-3, 0), (-3, 3)]

    # Start in left region
    x0 = np.array([-2.0, 1.0])

    # Optimize with constraints
    result = minimize(
        loss_func,
        x0,
        method='L-BFGS-B',
        bounds=bounds,
        options={'ftol': 1e-9, 'maxiter': 1000}
    )

    print(f"Found minimum at: {result.x}")
    print(f"Loss value: {result.fun:.6f}")
    print(f"x₁ = {result.x[0]:.4f} (should be < 0)")

    return result.x

optimal_x = optimize_left_minimum()
```

**This guarantees:** Solution is left minimum, never reaches right side!

---

## Question 3: Probability and Statistics (20 marks)

### Part (a): Calculate expectations [6 marks]

**Given data:**

| Index | age | exam | coursework | group |
|-------|-----|------|------------|-------|
| 0 | 21 | 9 | 7 | A |
| 1 | 18 | 3 | 7 | A |
| 2 | 18 | 5 | 6 | A |
| 3 | 19 | 6 | 8 | B |
| 4 | 18 | 4 | 5 | B |

---

**Step 1: Calculate E[exam]**

**Formula:**
```
E[X] = (1/N) Σᵢ₌₁ᴺ xᵢ
```

**Calculation:**
```
E[exam] = (1/5) × (9 + 3 + 5 + 6 + 4)
        = (1/5) × 27
        = 5.4
```

**Answer: E[exam] = 5.4**

---

**Step 2: Calculate E[coursework]**

```
E[coursework] = (1/5) × (7 + 7 + 6 + 8 + 5)
              = (1/5) × 33
              = 6.6
```

**Answer: E[coursework] = 6.6**

---

**Step 3: Calculate E[final mark]**

**Final mark formula:**
```
Final = 0.6 × exam + 0.4 × coursework
```

**Method 1: Using linearity of expectation**

```
E[Final] = E[0.6×exam + 0.4×coursework]
         = 0.6×E[exam] + 0.4×E[coursework]
         = 0.6×5.4 + 0.4×6.6
         = 3.24 + 2.64
         = 5.88
```

**Answer: E[final] = 5.88**

---

**Method 2: Calculate each final mark first**

```python
import pandas as pd

data = {
    'age': [21, 18, 18, 19, 18],
    'exam': [9, 3, 5, 6, 4],
    'coursework': [7, 7, 6, 8, 5],
    'group': ['A', 'A', 'A', 'B', 'B']
}
df = pd.DataFrame(data)

# Calculate final marks
df['final'] = 0.6 * df['exam'] + 0.4 * df['coursework']

print("Final marks:")
print(df['final'])
```

**Individual final marks:**
```
Student 0: 0.6×9 + 0.4×7 = 5.4 + 2.8 = 8.2
Student 1: 0.6×3 + 0.4×7 = 1.8 + 2.8 = 4.6
Student 2: 0.6×5 + 0.4×6 = 3.0 + 2.4 = 5.4
Student 3: 0.6×6 + 0.4×8 = 3.6 + 3.2 = 6.8
Student 4: 0.6×4 + 0.4×5 = 2.4 + 2.0 = 4.4
```

**Expectation:**
```
E[final] = (1/5) × (8.2 + 4.6 + 5.4 + 6.8 + 4.4)
         = (1/5) × 29.4
         = 5.88
```

**Verification: Both methods give same answer ✓**

---

**Summary:**

| Metric | Expectation |
|--------|-------------|
| E[exam] | 5.4 |
| E[coursework] | 6.6 |
| E[final] | 5.88 |

**Observations:**
- Coursework scores higher on average
- Final mark: 5.88/10 = 58.8%
- Just above typical pass mark (50%)

---

**Python Code:**

```python
import numpy as np

# Data
exam = np.array([9, 3, 5, 6, 4])
coursework = np.array([7, 7, 6, 8, 5])

# Expectations
E_exam = np.mean(exam)
E_coursework = np.mean(coursework)
E_final = 0.6 * E_exam + 0.4 * E_coursework

print(f"E[exam] = {E_exam:.2f}")
print(f"E[coursework] = {E_coursework:.2f}")
print(f"E[final] = {E_final:.2f}")
```

**Output:**
```
E[exam] = 5.40
E[coursework] = 6.60
E[final] = 5.88
```

---

### Part (b): Probability of passing and by group [7 marks]

**Pass mark: 5.0 out of 10**

**Student final marks (calculated above):**
```
Student 0 (A): 8.2 → PASS
Student 1 (A): 4.6 → FAIL
Student 2 (A): 5.4 → PASS
Student 3 (B): 6.8 → PASS
Student 4 (B): 4.4 → FAIL
```

---

**Question 1: Probability of passing (overall)**

**Count:**
- Passing: 3 students (0, 2, 3)
- Failing: 2 students (1, 4)
- Total: 5 students

**Probability:**
```
P(pass) = (Number passing) / (Total students)
        = 3 / 5
        = 0.6
        = 60%
```

**Answer: P(pass) = 0.6 or 60%**

---

**Question 2: Probability by group**

**Group A:**
- Students: 0, 1, 2 (3 total)
- Passing: 0, 2 (2 students)
- Failing: 1 (1 student)

```
P(pass | Group A) = 2/3 ≈ 0.667 = 66.7%
```

**Group B:**
- Students: 3, 4 (2 total)
- Passing: 3 (1 student)
- Failing: 4 (1 student)

```
P(pass | Group B) = 1/2 = 0.5 = 50%
```

---

**Summary Table:**

| Group | Total Students | Passing | Failing | P(pass \| group) |
|-------|---------------|---------|---------|------------------|
| A | 3 | 2 | 1 | 66.7% |
| B | 2 | 1 | 1 | 50.0% |
| **Overall** | **5** | **3** | **2** | **60.0%** |

---

**Question 3: What can you conclude?**

**Conclusion 1: Group A performs better**

```
P(pass | A) = 66.7% > P(pass | B) = 50.0%
```

Group A students have higher pass rate (+16.7 percentage points).

**Possible interpretations:**
- Group A students better prepared
- Group A has better teaching/resources
- Group A self-selected (better students chose A)
- Random variation (sample size very small!)

---

**Conclusion 2: Small sample size - results not statistically significant**

With only 5 students:
- 3 in group A, 2 in group B
- Very small sample!
- High variance in estimates
- Cannot draw strong conclusions

**Statistical test needed:**

```python
from scipy.stats import fisher_exact

# Contingency table
#           Pass  Fail
# Group A:   2     1
# Group B:   1     1

table = [[2, 1],
         [1, 1]]

odds_ratio, p_value = fisher_exact(table)
print(f"p-value: {p_value:.3f}")
```

**Result:** p-value ≈ 1.0 (not significant)

**Interpretation:** No statistical evidence of difference between groups.

---

**Conclusion 3: Overall pass rate concerning**

```
Overall pass rate: 60%
```

If target pass rate is 80%:
- Current: 60% (below target)
- Need to improve by +20 percentage points
- May need to adjust weightings or grading

---

**Conclusion 4: High variance in performance**

**Exam scores:** 3, 4, 5, 6, 9 (range: 6)
**Coursework scores:** 5, 6, 7, 7, 8 (range: 3)

**Observations:**
- Exam has wider spread
- Student 0: Excellent (8.2)
- Students 1, 4: Struggling (4.6, 4.4)
- Large performance gap suggests:
  - Diverse student abilities
  - Or exam particularly challenging

---

**Conclusion 5: Coursework vs Exam**

**Average scores:**
- Exam: 5.4/10 = 54%
- Coursework: 6.6/10 = 66%

**Students score 12% higher on coursework**

**Possible reasons:**
- Coursework allows more time
- Coursework allows collaboration
- Exam has time pressure
- Different skill assessment

**Implication for weighting:**
- Current: 60% exam, 40% coursework
- If coursework weighted more, pass rate would increase

---

**Complete Python Analysis:**

```python
import pandas as pd
import numpy as np

# Data
data = {
    'age': [21, 18, 18, 19, 18],
    'exam': [9, 3, 5, 6, 4],
    'coursework': [7, 7, 6, 8, 5],
    'group': ['A', 'A', 'A', 'B', 'B']
}
df = pd.DataFrame(data)

# Calculate final marks
df['final'] = 0.6 * df['exam'] + 0.4 * df['coursework']

# Pass/fail
df['pass'] = df['final'] >= 5.0

print("Student data:")
print(df)

# Overall pass rate
overall_pass_rate = df['pass'].mean()
print(f"\nOverall pass rate: {overall_pass_rate:.1%}")

# Pass rate by group
group_pass_rates = df.groupby('group')['pass'].agg(['sum', 'count', 'mean'])
group_pass_rates.columns = ['Passing', 'Total', 'Pass Rate']
print("\nPass rates by group:")
print(group_pass_rates)

# Conclusion
print("\nConclusions:")
print(f"1. Group A pass rate ({group_pass_rates.loc['A', 'Pass Rate']:.1%}) > Group B ({group_pass_rates.loc['B', 'Pass Rate']:.1%})")
print("2. Small sample size (N=5) - results not statistically significant")
print(f"3. Overall pass rate (60%) below typical target (80%)")
print("4. High variance in exam performance suggests diverse abilities")
print("5. Students perform better on coursework (+12%) than exam")
```

---

### Part (c): Approach to set weightings for 80% pass rate [7 marks]

**Problem:**
- Have 3 coursework scores and 1 exam score per student
- Large historical dataset (multiple years)
- Want to find weights w₁, w₂, w₃, w₄ such that:
  - Final = w₁×CW1 + w₂×CW2 + w₃×CW3 + w₄×Exam
  - Pass rate ≈ 80%

**Constraints:**
- w₁ + w₂ + w₃ + w₄ = 1 (weights sum to 1)
- wᵢ ≥ 0 (non-negative weights)
- 0 ≤ wᵢ ≤ 1 (realistic bounds)

---

**Approach:**

**Step 1: Data Preparation**

Load historical data:

```python
import pandas as pd

# Load data
df = pd.read_csv('student_data.csv')
# Columns: student_id, year, cw1, cw2, cw3, exam

print(f"Total students: {len(df)}")
print(f"Years covered: {df['year'].nunique()}")
```

**Ensure data quality:**
- Remove missing values
- Check for outliers
- Normalize if scores on different scales

```python
# Clean data
df = df.dropna()  # Remove missing
df = df[(df[['cw1', 'cw2', 'cw3', 'exam']] >= 0).all(axis=1)]  # Valid range
df = df[(df[['cw1', 'cw2', 'cw3', 'exam']] <= 10).all(axis=1)]
```

---

**Step 2: Define Optimization Problem**

**Objective:** Find weights that achieve 80% pass rate

**Formulation:**

```python
def calculate_pass_rate(weights, data, pass_threshold=5.0):
    """
    Calculate pass rate for given weights.

    Args:
        weights: [w1, w2, w3, w4] for [cw1, cw2, cw3, exam]
        data: DataFrame with columns [cw1, cw2, cw3, exam]
        pass_threshold: Minimum passing score

    Returns:
        Pass rate (fraction between 0 and 1)
    """
    w1, w2, w3, w4 = weights

    # Calculate final marks
    final_marks = (w1 * data['cw1'] +
                   w2 * data['cw2'] +
                   w3 * data['cw3'] +
                   w4 * data['exam'])

    # Calculate pass rate
    pass_rate = (final_marks >= pass_threshold).mean()

    return pass_rate
```

---

**Step 3: Formulate as Optimization**

**Method 1: Minimize squared error from target**

```python
from scipy.optimize import minimize

def objective(weights, data, target_pass_rate=0.80):
    """Minimize (actual_pass_rate - target)^2"""
    actual_pass_rate = calculate_pass_rate(weights, data)
    error = (actual_pass_rate - target_pass_rate)**2
    return error

# Constraints
constraints = [
    {'type': 'eq', 'fun': lambda w: sum(w) - 1}  # Sum to 1
]

# Bounds
bounds = [(0, 1), (0, 1), (0, 1), (0, 1)]  # Each weight in [0, 1]

# Initial guess
w0 = [0.15, 0.15, 0.15, 0.55]  # Start with reasonable values

# Optimize
result = minimize(
    objective,
    w0,
    args=(df,),
    method='SLSQP',
    bounds=bounds,
    constraints=constraints
)

optimal_weights = result.x
print(f"Optimal weights: {optimal_weights}")
print(f"Pass rate: {calculate_pass_rate(optimal_weights, df):.1%}")
```

---

**Method 2: Grid Search**

```python
import numpy as np

def grid_search_weights(data, target_rate=0.80, resolution=0.05):
    """
    Exhaustive search over weight space.

    Args:
        data: Student data
        target_rate: Target pass rate
        resolution: Grid spacing

    Returns:
        Best weights and resulting pass rate
    """
    best_weights = None
    best_error = float('inf')

    # Generate grid (constrained to sum to 1)
    for w4 in np.arange(0, 1 + resolution, resolution):  # Exam weight
        for w3 in np.arange(0, 1 - w4 + resolution, resolution):  # CW3
            for w2 in np.arange(0, 1 - w4 - w3 + resolution, resolution):  # CW2
                w1 = 1 - w4 - w3 - w2  # CW1 (determined by others)

                if w1 < 0 or w1 > 1:
                    continue

                weights = [w1, w2, w3, w4]
                pass_rate = calculate_pass_rate(weights, data)
                error = abs(pass_rate - target_rate)

                if error < best_error:
                    best_error = error
                    best_weights = weights

    return best_weights, calculate_pass_rate(best_weights, data)

optimal_weights, actual_rate = grid_search_weights(df)
print(f"Optimal weights: {optimal_weights}")
print(f"Achieved pass rate: {actual_rate:.1%}")
```

---

**Step 4: Cross-Validation**

Validate that weights generalize across years:

```python
from sklearn.model_selection import KFold

def cross_validate_weights(data, n_folds=5):
    """
    Validate weights across different subsets.

    Args:
        data: Full dataset
        n_folds: Number of cross-validation folds

    Returns:
        Average pass rate across folds
    """
    kf = KFold(n_splits=n_folds, shuffle=True, random_state=42)
    pass_rates = []

    for train_idx, val_idx in kf.split(data):
        # Split data
        train_data = data.iloc[train_idx]
        val_data = data.iloc[val_idx]

        # Find weights on training data
        weights = find_optimal_weights(train_data, target_rate=0.80)

        # Evaluate on validation data
        val_pass_rate = calculate_pass_rate(weights, val_data)
        pass_rates.append(val_pass_rate)

        print(f"Fold pass rate: {val_pass_rate:.1%}")

    avg_pass_rate = np.mean(pass_rates)
    std_pass_rate = np.std(pass_rates)

    print(f"\nAverage pass rate: {avg_pass_rate:.1%} ± {std_pass_rate:.1%}")

    return avg_pass_rate, std_pass_rate

# Run cross-validation
avg_rate, std_rate = cross_validate_weights(df)
```

---

**Step 5: Sensitivity Analysis**

Check how sensitive pass rate is to weight changes:

```python
def sensitivity_analysis(weights, data):
    """
    Analyze sensitivity of pass rate to weight perturbations.

    Args:
        weights: Baseline weights
        data: Student data

    Returns:
        Sensitivity for each weight
    """
    baseline_rate = calculate_pass_rate(weights, data)
    sensitivities = []

    delta = 0.01  # 1% change

    for i in range(len(weights)):
        # Perturb weight i
        perturbed = weights.copy()
        perturbed[i] += delta

        # Renormalize
        perturbed = perturbed / perturbed.sum()

        # Calculate new pass rate
        new_rate = calculate_pass_rate(perturbed, data)

        # Sensitivity: change in rate per unit change in weight
        sensitivity = (new_rate - baseline_rate) / delta
        sensitivities.append(sensitivity)

    return sensitivities

sensitivities = sensitivity_analysis(optimal_weights, df)
weight_names = ['CW1', 'CW2', 'CW3', 'Exam']

for name, sens in zip(weight_names, sensitivities):
    print(f"{name}: {sens:+.2f}% pass rate per 1% weight increase")
```

---

**Step 6: Apply Additional Constraints**

**Policy constraints:**
- Minimum exam weight (e.g., ≥ 40%)
- Maximum coursework weight per piece (e.g., ≤ 25%)

```python
# Extended constraints
constraints = [
    {'type': 'eq', 'fun': lambda w: sum(w) - 1},  # Sum to 1
    {'type': 'ineq', 'fun': lambda w: w[3] - 0.40},  # Exam ≥ 40%
    {'type': 'ineq', 'fun': lambda w: 0.25 - w[0]},  # CW1 ≤ 25%
    {'type': 'ineq', 'fun': lambda w: 0.25 - w[1]},  # CW2 ≤ 25%
    {'type': 'ineq', 'fun': lambda w: 0.25 - w[2]},  # CW3 ≤ 25%
]

result = minimize(
    objective,
    w0,
    args=(df,),
    method='SLSQP',
    bounds=bounds,
    constraints=constraints
)
```

---

**Step 7: Analyze Results**

```python
def analyze_results(weights, data):
    """
    Comprehensive analysis of chosen weights.

    Args:
        weights: Chosen weights
        data: Student data

    Returns:
        dict: Analysis results
    """
    # Calculate final marks
    final = (weights[0] * data['cw1'] +
             weights[1] * data['cw2'] +
             weights[2] * data['cw3'] +
             weights[3] * data['exam'])

    # Pass/fail
    passing = final >= 5.0

    # Statistics
    stats = {
        'pass_rate': passing.mean(),
        'mean_mark': final.mean(),
        'std_mark': final.std(),
        'min_mark': final.min(),
        'max_mark': final.max(),
        'median_mark': final.median()
    }

    # Grade distribution
    grades = pd.cut(final,
                    bins=[0, 4, 5, 6, 7, 10],
                    labels=['Fail', 'D', 'C', 'B', 'A'])
    stats['grade_dist'] = grades.value_counts().to_dict()

    return stats

results = analyze_results(optimal_weights, df)
print(f"Pass rate: {results['pass_rate']:.1%}")
print(f"Mean mark: {results['mean_mark']:.2f}")
print(f"Std: {results['std_mark']:.2f}")
print(f"\nGrade distribution:")
for grade, count in results['grade_dist'].items():
    print(f"  {grade}: {count}")
```

---

**Step 8: Validate with Recent Data**

Test on most recent year (held out):

```python
# Split by year
recent_year = df['year'].max()
recent_data = df[df['year'] == recent_year]
historical_data = df[df['year'] < recent_year]

# Find weights on historical data
weights = find_optimal_weights(historical_data, target_rate=0.80)

# Test on recent data
recent_pass_rate = calculate_pass_rate(weights, recent_data)
print(f"Pass rate on recent data: {recent_pass_rate:.1%}")

if abs(recent_pass_rate - 0.80) < 0.05:
    print("✓ Weights generalize well")
else:
    print("✗ Weights may not generalize")
```

---

**Summary of Approach:**

1. **Data Preparation:** Clean and validate historical data
2. **Define Objective:** Minimize |pass_rate - 0.80|²
3. **Optimize:** Use constrained optimization (SLSQP)
4. **Cross-Validate:** Ensure generalization across years
5. **Sensitivity Analysis:** Check robustness
6. **Apply Constraints:** Enforce policy requirements
7. **Analyze Results:** Grade distribution, statistics
8. **Validate:** Test on held-out recent data

**Result:** Optimal weights that achieve ~80% pass rate while respecting constraints!

---

## Question 4: Database Systems (20 marks)

### Part (a): Calculate blocking factors [4 marks]

**Given:**

**Course (C):**
- Id: 32-bit integer = 4 bytes
- Description: 195 bytes
- Credits: 8-bit integer = 1 byte
- Total: r_C = 32 records

**Transcript (T):**
- StudentId: 4 bytes
- CourseId: 4 bytes
- Mark: 8 bytes (double)
- Total: r_T = 51,200 records

**Block size:** Default database block = 4096 bytes (typical)

---

**Step 1: Calculate Record Sizes**

**Course record size:**
```
R_C = sizeof(Id) + sizeof(Description) + sizeof(Credits)
    = 4 + 195 + 1
    = 200 bytes per record
```

**Transcript record size:**
```
R_T = sizeof(StudentId) + sizeof(CourseId) + sizeof(Mark)
    = 4 + 4 + 8
    = 16 bytes per record
```

---

**Step 2: Calculate Blocking Factors**

**Blocking factor:** Number of records that fit in one block

**For Course:**
```
bfr_C = floor(Block_size / R_C)
      = floor(4096 / 200)
      = floor(20.48)
      = 20 records per block
```

**For Transcript:**
```
bfr_T = floor(Block_size / R_T)
      = floor(4096 / 16)
      = floor(256)
      = 256 records per block
```

---

**Answer:**
- **Blocking factor for Course: bfr_C = 20 records/block**
- **Blocking factor for Transcript: bfr_T = 256 records/block**

---

**Python Verification:**

```python
# Given
block_size = 4096

# Course
R_C = 4 + 195 + 1  # 200 bytes
bfr_C = block_size // R_C
print(f"Course blocking factor: {bfr_C}")

# Transcript
R_T = 4 + 4 + 8  # 16 bytes
bfr_T = block_size // R_T
print(f"Transcript blocking factor: {bfr_T}")
```

**Output:**
```
Course blocking factor: 20
Transcript blocking factor: 256
```

---

### Part (b): Number of blocks required [6 marks]

**Step 1: Calculate Blocks for Course**

**Formula:**
```
n_C = ceil(r_C / bfr_C)
```

**Calculation:**
```
n_C = ceil(32 / 20)
    = ceil(1.6)
    = 2 blocks
```

**Verification:**
- Block 1: 20 records
- Block 2: 12 records (32 - 20 = 12)
- Total: 2 blocks ✓

**Answer: Course requires 2 blocks**

---

**Step 2: Calculate Blocks for Transcript**

**Formula:**
```
n_T = ceil(r_T / bfr_T)
```

**Calculation:**
```
n_T = ceil(51200 / 256)
    = ceil(200)
    = 200 blocks
```

**Verification:**
- 200 blocks × 256 records/block = 51,200 records ✓
- Exactly fills 200 blocks with no wasted space!

**Answer: Transcript requires 200 blocks**

---

**Summary:**

| Relation | Records | Record Size | Blocking Factor | Blocks |
|----------|---------|-------------|-----------------|--------|
| Course (C) | 32 | 200 bytes | 20 | 2 |
| Transcript (T) | 51,200 | 16 bytes | 256 | 200 |

---

**Python Code:**

```python
import math

# Course
r_C = 32
bfr_C = 20
n_C = math.ceil(r_C / bfr_C)
print(f"Course blocks: {n_C}")

# Transcript
r_T = 51200
bfr_T = 256
n_T = math.ceil(r_T / bfr_T)
print(f"Transcript blocks: {n_T}")

# Total storage
total_blocks = n_C + n_T
total_size_KB = (total_blocks * 4096) / 1024
print(f"\nTotal blocks: {total_blocks}")
print(f"Total storage: {total_size_KB:.1f} KB")
```

**Output:**
```
Course blocks: 2
Transcript blocks: 200

Total blocks: 202
Total storage: 808.0 KB
```

---

### Part (c): Nested loop join cost analysis [6 marks]

**Given:**
- n_C = 2 blocks
- n_T = 200 blocks
- Memory buffer: n_B = 23 blocks
- Can use (n_B - 2) = 21 blocks for outer relation

**Query:**
```sql
SELECT * FROM Course C JOIN Transcript T ON C.Id = T.CourseId
```

---

**Block Nested-Loop Join Algorithm:**

```
For each chunk of (n_B - 2) blocks of outer relation:
    Load chunk into memory
    For each block of inner relation:
        Load block into memory
        Join records in memory
        Write results
```

**Memory allocation:**
- (n_B - 2) blocks: outer relation
- 1 block: inner relation
- 1 block: output buffer

---

**Strategy 1: Course (C) as Outer, Transcript (T) as Inner**

**Number of outer chunks:**
```
chunks_C = ceil(n_C / (n_B - 2))
         = ceil(2 / 21)
         = ceil(0.095)
         = 1 chunk
```

**Cost formula:**
```
Cost = n_C + (chunks_C × n_T)
     = 2 + (1 × 200)
     = 2 + 200
     = 202 block accesses
```

**Breakdown:**
- Read C once: 2 blocks
- For 1 chunk of C, read all of T: 1 × 200 = 200 blocks
- Total: 202 blocks

---

**Strategy 2: Transcript (T) as Outer, Course (C) as Inner**

**Number of outer chunks:**
```
chunks_T = ceil(n_T / (n_B - 2))
         = ceil(200 / 21)
         = ceil(9.52)
         = 10 chunks
```

**Cost formula:**
```
Cost = n_T + (chunks_T × n_C)
     = 200 + (10 × 2)
     = 200 + 20
     = 220 block accesses
```

**Breakdown:**
- Read T once: 200 blocks
- For 10 chunks of T, read all of C: 10 × 2 = 20 blocks
- Total: 220 blocks

---

**Comparison:**

| Strategy | Outer | Inner | Cost Formula | Cost (blocks) |
|----------|-------|-------|-------------|---------------|
| **1** | **C** | **T** | **n_C + ⌈n_C/(n_B-2)⌉ × n_T** | **202** ✓ Best |
| 2 | T | C | n_T + ⌈n_T/(n_B-2)⌉ × n_C | 220 |

**Winner: Strategy 1 (Course as outer) is more efficient**

**Savings: 220 - 202 = 18 block accesses (8.2% reduction)**

---

**Why is Strategy 1 better?**

**General principle:** Choose **smaller relation as outer**

**Reason:**
- Outer relation read once: favors smaller
- Inner relation read multiple times: number of reads = ⌈n_outer/(n_B-2)⌉
- Minimizing ⌈n_outer/(n_B-2)⌉ minimizes total cost

**For our case:**
- C is much smaller (2 blocks << 200 blocks)
- Fits entirely in buffer (2 < 21)
- Only need to read T once

---

**Mathematical Analysis:**

**Cost formula (general):**
```
Cost(outer, inner) = n_outer + ⌈n_outer/(n_B-2)⌉ × n_inner
```

**Optimal strategy:**
```
Choose outer = argmin(n + ⌈n/(n_B-2)⌉ × n_other)
```

**For us:**
```
Cost(C outer) = 2 + ⌈2/21⌉ × 200 = 2 + 1×200 = 202
Cost(T outer) = 200 + ⌈200/21⌉ × 2 = 200 + 10×2 = 220
```

**C is optimal!**

---

**Special case optimization:**

Since n_C = 2 ≤ (n_B - 2) = 21, **all of C fits in memory!**

**One-pass algorithm possible:**
1. Load all of C into memory (2 blocks)
2. Scan T once (200 blocks)
3. For each T record, probe C in memory

**Cost = 2 + 200 = 202 blocks** (same as block nested-loop)

This is the **best possible** for nested-loop joins!

---

**Python Simulation:**

```python
import math

# Given
n_C = 2
n_T = 200
n_B = 23

# Strategy 1: C outer, T inner
chunks_C = math.ceil(n_C / (n_B - 2))
cost_1 = n_C + chunks_C * n_T
print(f"Strategy 1 (C outer): {cost_1} blocks")
print(f"  Read C: {n_C}")
print(f"  Chunks of C: {chunks_C}")
print(f"  Read T {chunks_C} times: {chunks_C * n_T}")

# Strategy 2: T outer, C inner
chunks_T = math.ceil(n_T / (n_B - 2))
cost_2 = n_T + chunks_T * n_C
print(f"\nStrategy 2 (T outer): {cost_2} blocks")
print(f"  Read T: {n_T}")
print(f"  Chunks of T: {chunks_T}")
print(f"  Read C {chunks_T} times: {chunks_T * n_C}")

# Winner
print(f"\n{'='*50}")
print(f"Best strategy: {'Strategy 1 (C outer)' if cost_1 < cost_2 else 'Strategy 2 (T outer)'}")
print(f"Cost: {min(cost_1, cost_2)} blocks")
print(f"Savings: {abs(cost_1 - cost_2)} blocks")
```

**Output:**
```
Strategy 1 (C outer): 202 blocks
  Read C: 2
  Chunks of C: 1
  Read T 1 times: 200

Strategy 2 (T outer): 220 blocks
  Read T: 200
  Chunks of T: 10
  Read C 10 times: 20

==================================================
Best strategy: Strategy 1 (C outer)
Cost: 202 blocks
Savings: 18 blocks
```

---

### Part (d): Selection Cardinality and Query Optimization [4 marks]

**Definition:**

**Selection Cardinality** (or **result cardinality**) is the **number of tuples** returned by a query or operation.

**Formula:**
```
Selection Cardinality = |result set| = number of output tuples
```

---

**For Selections (WHERE clauses):**

```sql
SELECT * FROM Employee WHERE salary > 50000
```

**Selection cardinality:**
```
|σ_salary>50000(Employee)| = number of employees with salary > 50000
```

**Estimated using selectivity:**
```
Cardinality ≈ Selectivity × |Employee|
```

where selectivity = fraction of tuples satisfying condition.

---

**For Joins:**

```sql
SELECT * FROM Course C JOIN Transcript T ON C.Id = T.CourseId
```

**Join cardinality:**
```
|C ⋈ T| = number of joined tuples
```

**For our database:**
- Each Transcript record joins with exactly one Course
- Join cardinality = |T| = 51,200 tuples

---

**Significance in Query Optimization:**

**1. Cost Estimation:**

Query optimizer uses cardinality to estimate costs:

```
Cost(operation) = f(input_cardinality, selectivity, ...)
```

**Example:**
```sql
SELECT * FROM T WHERE Mark > 8
```

If selectivity = 0.1:
- Input: 51,200 tuples
- **Estimated cardinality: 0.1 × 51,200 = 5,120 tuples**
- Affects downstream operation costs

---

**2. Join Order Selection:**

**Problem:** Choose optimal order for multi-way joins

```sql
SELECT * FROM A, B, C WHERE A.id = B.id AND B.id = C.id
```

**Options:**
- (A ⋈ B) ⋈ C
- (A ⋈ C) ⋈ B
- (B ⋈ C) ⋈ A

**Decision based on intermediate cardinalities:**

If |A ⋈ B| = 1000 and |A ⋈ C| = 100,000:
- Prefer (A ⋈ C) ⋈ B (smaller intermediate)
- Minimizes total cost

**Rule:** Perform most selective joins first

---

**3. Access Method Selection:**

**Cardinality determines index usage:**

```sql
SELECT * FROM Employee WHERE department = 'CS'
```

**Low cardinality** (few results):
- Use index scan
- Cost: O(log n + k) where k = result size
- Example: k = 10 → index fast

**High cardinality** (many results):
- Use table scan
- Cost: O(n)
- Example: k = 10,000 → table scan faster (avoid index overhead)

**Threshold:** Typically switch at 5-15% selectivity

---

**4. Memory Allocation:**

**Buffer sizing based on cardinality:**

```sql
SELECT * FROM Course C JOIN Transcript T ...
```

If join cardinality = 51,200:
- Allocate buffer for ~50K tuples
- May need temporary disk storage
- Affects hash table size for hash joins

**Low cardinality:** Use in-memory algorithms
**High cardinality:** Use disk-based algorithms

---

**5. Parallel Query Processing:**

**Cardinality affects parallelization decisions:**

**High cardinality:**
- Partition data across multiple CPUs
- Parallel processing beneficial
- Example: |result| = 1M → use 10 threads

**Low cardinality:**
- Sequential processing sufficient
- Avoid parallelization overhead
- Example: |result| = 100 → use 1 thread

---

**6. Materialization vs Pipelining:**

**Decision:** Should intermediate results be materialized?

**High cardinality:**
- Cost of materialization high
- Prefer pipelining (stream results)

**Low cardinality:**
- Materialize intermediate results
- Enable better optimization of subsequent operations

---

**Example: Our Join Query**

```sql
SELECT * FROM Course C JOIN Transcript T ON C.Id = T.CourseId
WHERE T.Mark > 8
```

**Without cardinality info:**
- Join all (51,200 tuples)
- Then filter by Mark > 8

**With cardinality info:**
- Estimate: 10% have Mark > 8 → 5,120 tuples
- Filter T first, then join
- Input to join: 5,120 instead of 51,200
- **10× fewer tuples to join!**

---

**Cardinality Estimation Techniques:**

**1. Histograms:**
```
Store distribution of values
Example: Mark distribution
  0-2: 10%
  2-4: 20%
  4-6: 30%
  6-8: 25%
  8-10: 15%

Estimate P(Mark > 8) ≈ 15%
```

**2. Sampling:**
```python
# Sample 1% of data
sample = T.sample(frac=0.01)
selectivity = (sample['Mark'] > 8).mean()
estimated_cardinality = selectivity * len(T)
```

**3. Maintained Statistics:**
```sql
-- Database maintains stats
ANALYZE TABLE Transcript;

-- Stats stored:
-- - Total rows
-- - Value distributions
-- - Index cardinalities
```

---

**Summary:**

**Selection Cardinality** = number of result tuples

**Significance:**
1. **Cost estimation:** Predict query execution cost
2. **Join ordering:** Choose optimal join sequence
3. **Access method:** Index vs table scan decision
4. **Memory allocation:** Buffer sizing
5. **Parallelization:** Parallel vs sequential
6. **Materialization:** Pipeline vs materialize

**Impact:** Can make difference between seconds and hours for large queries!

---

## End of Solutions

**Summary:**
- **Question 1 (20 marks):** Linear Algebra - whitening, matrix transformations
- **Question 2 (20 marks):** Optimization - contour analysis, algorithms, local minima
- **Question 3 (20 marks):** Probability - expectations, conditional probability, weight optimization
- **Question 4 (20 marks):** Databases - blocking factors, join strategies, cardinality

**Total: 80 marks**

---

**Prepared by: AI Assistant**
**Date: November 25, 2025**
**For: IDSS 2023-2024 Examination (December 2023)**
