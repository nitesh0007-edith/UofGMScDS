# IDSS 2024-2025 Examination Solutions

**University of Glasgow**
**Introduction to Data Science and Systems**
**COMPSCI 5089**
**Duration: 2 hours**
**Total Marks: 80**

---

## Question 1: Linear Algebra (20 marks)

### Part (a)(i): Adjacency matrix for the graph [3 marks]

**Given Graph:**
```
    A
   / \
0.3   0.7 (with 1 from A to C)
 /       \
B         C
|         |
1      0.4 (from C to E)
|         |
D ← 0.6 ← E
    (1 from D to E)
```

**Graph Edges:**
- A → B: weight 0.3
- A → C: weight 0.7
- A → C: weight 1 (appears to be same edge, so use 1)
- B → D: weight 1
- C → E: weight 0.4
- C → D: weight 0.6
- E → D: weight 1

**Adjacency Matrix A:**

The adjacency matrix A[i][j] represents the weight of the edge from node i to node j.

Nodes order: A, B, C, D, E (indices 0, 1, 2, 3, 4)

```
       A    B    C    D    E
   A [  0  0.3  1.0   0    0 ]
   B [  0   0    0   1.0   0 ]
A= C [  0   0    0   0.6  0.4]
   D [  0   0    0    0   1.0]
   E [  0   0    0   1.0   0 ]
```

**Answer:**
```python
A = [[0, 0.3, 1.0, 0, 0],
     [0, 0, 0, 1.0, 0],
     [0, 0, 0, 0.6, 0.4],
     [0, 0, 0, 0, 1.0],
     [0, 0, 0, 1.0, 0]]
```

Or in matrix notation:
```
| 0   0.3  1.0  0    0   |
| 0   0    0    1.0  0   |
| 0   0    0    0.6  0.4 |
| 0   0    0    0    1.0 |
| 0   0    0    1.0  0   |
```

---

### Part (a)(ii): Distribution at t = 1 [2 marks]

**Given initial distribution at t = 0:**
- A = 100
- B = 10
- C = 20
- D = 0
- E = 0

**Initial state vector:**
```
x₀ = [100, 10, 20, 0, 0]ᵀ
```

**Distribution at t = 1:**

The distribution at time t = 1 is given by:
```
x₁ = Aᵀx₀
```

Note: We use Aᵀ (transpose) because the adjacency matrix A[i][j] represents edges from i to j, and we want to know what comes INTO each node.

**Calculation:**

```
       | 0   0   0   0   0  |   | 100 |
       | 0.3 0   0   0   0  |   |  10 |
x₁ =   | 1.0 0   0   0   0  | × |  20 |
       | 0   1.0 0.6 0   1.0|   |   0 |
       | 0   0   0.4 1.0 0  |   |   0 |
```

**Computing each component:**

**A (index 0):**
```
x₁[A] = 0×100 + 0×10 + 0×20 + 0×0 + 0×0 = 0
```

**B (index 1):**
```
x₁[B] = 0.3×100 + 0×10 + 0×20 + 0×0 + 0×0 = 30
```

**C (index 2):**
```
x₁[C] = 1.0×100 + 0×10 + 0×20 + 0×0 + 0×0 = 100
```

**D (index 3):**
```
x₁[D] = 0×100 + 1.0×10 + 0.6×20 + 0×0 + 1.0×0 = 10 + 12 = 22
```

**E (index 4):**
```
x₁[E] = 0×100 + 0×10 + 0.4×20 + 1.0×0 + 0×0 = 8
```

**Answer:**
```
Distribution at t = 1:
A = 0, B = 30, C = 100, D = 22, E = 8
```

Or in vector form: **x₁ = [0, 30, 100, 22, 8]ᵀ**

**Verification:** Total parcels = 0 + 30 + 100 + 22 + 8 = 160 ✗

Wait, this doesn't match! Initial total = 100 + 10 + 20 = 130

Let me recalculate. The adjacency matrix represents TRANSITIONS, not flows. Let me reinterpret:

Actually, looking at the graph again more carefully:
- From A: 0.3 to B, 0.7 to C
- From B: 1.0 to D
- From C: 0.6 to D, 0.4 to E
- From D: 1.0 to E
- From E: 1.0 to D

This suggests a **transition matrix** where rows sum to 1 (stochastic matrix).

**Corrected adjacency/transition matrix:**
```
       A    B    C    D    E
   A [  0  0.3  0.7   0    0 ]
   B [  0   0    0   1.0   0 ]
A= C [  0   0    0   0.6  0.4]
   D [  0   0    0    0   1.0]
   E [  0   0    0   1.0   0 ]
```

**Recalculating x₁ = Aᵀx₀:**

```
       | 0   0   0   0   0  |   | 100 |
       | 0.3 0   0   0   0  |   |  10 |
x₁ =   | 0.7 0   0   0   0  | × |  20 |
       | 0   1.0 0.6 0   1.0|   |   0 |
       | 0   0   0.4 1.0 0  |   |   0 |
```

**A:** 0×100 + 0×10 + 0×20 + 0×0 + 0×0 = **0**
**B:** 0.3×100 + 0×10 + 0×20 + 0×0 + 0×0 = **30**
**C:** 0.7×100 + 0×10 + 0×20 + 0×0 + 0×0 = **70**
**D:** 0×100 + 1.0×10 + 0.6×20 + 0×0 + 1.0×0 = **22**
**E:** 0×100 + 0×10 + 0.4×20 + 1.0×0 + 0×0 = **8**

**Final Answer:**
```
x₁ = [A=0, B=30, C=70, D=22, E=8]ᵀ
```

**Verification:** 0 + 30 + 70 + 22 + 8 = 130 ✓

---

### Part (a)(iii): Calculate distribution two days ago (x₍ₜ₌₋₂₎) [2 marks]

**Problem:** Given current distribution x₀, find distribution at t = -2 (two days ago).

**Approach:**

If the forward evolution is given by:
```
xₜ₊₁ = Aᵀxₜ
```

Then to go backwards in time:
```
xₜ = (Aᵀ)⁻¹xₜ₊₁
```

**Method to calculate x₍ₜ₌₋₂₎:**

**Step 1:** From x₀, go back to x₍₋₁₎:
```
x₍₋₁₎ = (Aᵀ)⁻¹x₀
```

**Step 2:** From x₍₋₁₎, go back to x₍₋₂₎:
```
x₍₋₂₎ = (Aᵀ)⁻¹x₍₋₁₎ = (Aᵀ)⁻¹(Aᵀ)⁻¹x₀ = ((Aᵀ)⁻¹)²x₀ = (Aᵀ)⁻²x₀
```

Or equivalently:
```
x₍₋₂₎ = (A²)⁻ᵀx₀
```

**Detailed Steps:**

1. **Compute Aᵀ** (transpose of adjacency matrix)

2. **Compute (Aᵀ)⁻¹** (inverse of transpose)
   - Check if Aᵀ is invertible (det(Aᵀ) ≠ 0)
   - If not invertible, use pseudo-inverse: (Aᵀ)⁺

3. **Compute ((Aᵀ)⁻¹)²** or **(Aᵀ)⁻²**

4. **Multiply:** x₍₋₂₎ = (Aᵀ)⁻²x₀

**Alternative approach using forward evolution:**

Since x₀ = (Aᵀ)²x₍₋₂₎, we need to solve:
```
(Aᵀ)²x₍₋₂₎ = x₀
```

This is a linear system: **Bx₍₋₂₎ = x₀** where **B = (Aᵀ)²**

Can be solved using:
- Direct matrix inversion: x₍₋₂₎ = B⁻¹x₀
- Gaussian elimination
- Least squares if B is not square or singular
- Iterative methods (Jacobi, Gauss-Seidel)

**Important Note:**

Since A is a stochastic matrix (rows sum to 1), it may not be invertible, especially if there are "absorbing" states or the graph is not strongly connected. In such cases, the backward problem may not have a unique solution, and we would need to:
- Use the Moore-Penrose pseudo-inverse
- Add constraints (e.g., non-negativity, total parcels)
- Use least squares approximation

**Summary of approach:**
1. Compute (Aᵀ)⁻² either as ((Aᵀ)⁻¹)² or as ((Aᵀ)²)⁻¹
2. Calculate x₍₋₂₎ = (Aᵀ)⁻²x₀
3. If A is singular, use pseudo-inverse (Aᵀ)⁺

---

### Part (a)(iv): Transform to make graph undirected [2 marks]

**Goal:** Make the graph undirected so paths between any two nodes go both ways.

**Method:**

To make an adjacency matrix symmetric (undirected), we create a new matrix where if there's an edge from i to j OR from j to i, there's an edge in both directions.

**Approach 1: Maximum Weight**
```
A_undirected[i][j] = max(A[i][j], A[j][i])
```

**Approach 2: Average Weight**
```
A_undirected[i][j] = (A[i][j] + A[j][i]) / 2
```

**Approach 3: Symmetrize by addition**
```
A_undirected = (A + Aᵀ) / 2
```

This ensures A_undirected is symmetric: A_undirected[i][j] = A_undirected[j][i]

**Approach 4: Binary (keep if any edge exists)**
```
A_undirected[i][j] = 1 if (A[i][j] > 0 OR A[j][i] > 0) else 0
```

**Recommended Approach:**

For weighted graphs, use:
```
A_undirected = (A + Aᵀ) / 2
```

This creates a symmetric matrix where each edge weight is the average of the forward and backward edge weights.

**Formula:**
```python
A_undirected[i,j] = (A[i,j] + A[j,i]) / 2
```

Or in matrix form:
```
A_undirected = (A + Aᵀ) / 2
```

**Verification:**

For any symmetric matrix S:
- Sᵀ = S
- S[i][j] = S[j][i] for all i, j

**Example calculation for our matrix:**

Original A:
```
| 0   0.3  1.0  0    0   |
| 0   0    0    1.0  0   |
| 0   0    0    0.6  0.4 |
| 0   0    0    0    1.0 |
| 0   0    0    1.0  0   |
```

Aᵀ:
```
| 0    0    0    0    0  |
| 0.3  0    0    0    0  |
| 1.0  0    0    0    0  |
| 0    1.0  0.6  0    1.0|
| 0    0    0.4  1.0  0  |
```

A_undirected = (A + Aᵀ)/2:
```
| 0    0.15  0.5  0    0   |
| 0.15 0     0    0.5  0   |
| 0.5  0     0    0.3  0.2 |
| 0    0.5   0.3  0    1.0 |
| 0    0     0.2  1.0  0   |
```

This matrix is symmetric! ✓

---

### Part (b): Steady state of A [3 marks]

**Definition of Steady State:**

A steady state (or stationary distribution) π is a probability distribution that remains unchanged under the transition matrix A. Mathematically:

```
π = Aᵀπ
```

Or equivalently:
```
Aᵀπ = π
```

This means π is an **eigenvector** of Aᵀ corresponding to **eigenvalue λ = 1**.

**Properties of Steady State:**
- π ≥ 0 (all elements non-negative)
- Σᵢ πᵢ = 1 (sums to 1, probability distribution)
- After sufficient time, the distribution converges to π regardless of initial state

**Physical meaning:** The long-term proportion of parcels at each site, independent of the starting distribution.

---

**Method 1: Eigenvalue/Eigenvector Approach**

**Steps:**

1. **Find eigenvectors of Aᵀ:**
   ```
   (Aᵀ - λI)v = 0
   ```

2. **Find eigenvalue λ = 1:**
   Solve for v where:
   ```
   (Aᵀ - I)v = 0
   ```
   This is equivalent to:
   ```
   Aᵀv = v
   ```

3. **Solve the system:**
   ```
   (Aᵀ - I)π = 0
   ```

   This gives us (n-1) independent equations plus the normalization constraint.

4. **Normalize:**
   ```
   π = v / ||v||₁
   ```
   where ||v||₁ = Σᵢ vᵢ (L1 norm) to ensure Σᵢ πᵢ = 1

**Detailed Calculation:**

For our matrix Aᵀ:
```
| 0    0    0    0    0  |
| 0.3  0    0    0    0  |
| 0.7  0    0    0    0  |
| 0    1.0  0.6  0    1.0|
| 0    0    0.4  1.0  0  |
```

System (Aᵀ - I)π = 0:
```
| -1   0    0    0    0  | | π₁ |   | 0 |
| 0.3 -1    0    0    0  | | π₂ |   | 0 |
| 0.7  0   -1    0    0  | | π₃ | = | 0 |
| 0    1.0  0.6 -1    1.0| | π₄ |   | 0 |
| 0    0    0.4  1.0 -1  | | π₅ |   | 0 |
```

From equation 1: -π₁ = 0 → π₁ = 0
From equation 2: 0.3π₁ - π₂ = 0 → π₂ = 0
From equation 3: 0.7π₁ - π₃ = 0 → π₃ = 0
From equation 4: π₂ + 0.6π₃ - π₄ + π₅ = 0 → -π₄ + π₅ = 0 → π₄ = π₅
From equation 5: 0.4π₃ + π₄ - π₅ = 0 → π₄ = π₅

With normalization π₁ + π₂ + π₃ + π₄ + π₅ = 1:
0 + 0 + 0 + π₄ + π₅ = 1
2π₄ = 1
π₄ = π₅ = 0.5

**Steady state:**
```
π = [0, 0, 0, 0.5, 0.5]ᵀ
```

This means in the long run, parcels oscillate between D and E!

---

**Method 2: Power Iteration Method**

**Steps:**

1. **Start with initial distribution:**
   ```
   x₀ = any valid probability distribution (e.g., uniform)
   ```

2. **Iterate:**
   ```
   xₜ₊₁ = Aᵀxₜ
   ```

3. **Normalize after each iteration:**
   ```
   xₜ₊₁ = xₜ₊₁ / ||xₜ₊₁||₁
   ```

4. **Repeat until convergence:**
   ```
   ||xₜ₊₁ - xₜ|| < ε
   ```

5. **Result:** π ≈ xₜ as t → ∞

**Algorithm:**
```python
def find_steady_state(A_transpose, max_iter=1000, tol=1e-6):
    n = A_transpose.shape[0]
    x = np.ones(n) / n  # Start with uniform distribution

    for i in range(max_iter):
        x_new = A_transpose @ x
        x_new = x_new / np.sum(x_new)  # Normalize

        if np.linalg.norm(x_new - x) < tol:
            return x_new

        x = x_new

    return x
```

**Advantages:**
- Simple to implement
- Works for large sparse matrices
- Numerical stability

**Disadvantages:**
- May be slow to converge
- Requires many iterations
- May not converge if eigenvalue = 1 is not dominant

---

**Comparison:**

| Method | Advantages | Disadvantages |
|--------|------------|---------------|
| Eigenvalue | Exact solution, theoretically sound | Computationally expensive for large matrices |
| Power Iteration | Simple, works for large sparse matrices | Approximate, requires many iterations |

**Both methods should give the same result: π = [0, 0, 0, 0.5, 0.5]ᵀ**

---

### Part (c)(i): Singular values of A [3 marks]

**Given SVD decomposition:**
```
A = UΣVᵀ
```

where:
```
U = [0  1]     Σ = [1.5  0   0 ]     V = [0  1  0]
    [1  0]         [0    0.5 0 ]         [1  0  0]
                                          [0  0  1]
```

**Definition:**

The **singular values** of matrix A are the diagonal elements of the matrix Σ in the SVD decomposition.

For an m×n matrix A with SVD A = UΣVᵀ:
- Σ is an m×n diagonal matrix
- Diagonal elements σ₁ ≥ σ₂ ≥ ... ≥ σᵣ ≥ 0 are the singular values
- r = rank(A) is the number of non-zero singular values

**From the given Σ matrix:**
```
Σ = [1.5  0   0 ]
    [0    0.5 0 ]
```

The diagonal elements are: **1.5** and **0.5**

**Answer:**

The singular values of A are:
```
σ₁ = 1.5
σ₂ = 0.5
```

Or in set notation: **{1.5, 0.5}**

**Properties:**
- Both singular values are positive (σᵢ > 0)
- Ordered in descending order: σ₁ ≥ σ₂
- Rank of A = 2 (two non-zero singular values)
- Condition number: κ(A) = σ₁/σ₂ = 1.5/0.5 = 3

**Relationship to eigenvalues:**
- Singular values of A are square roots of eigenvalues of AᵀA or AAᵀ
- σᵢ² are eigenvalues of AᵀA
- 1.5² = 2.25 and 0.5² = 0.25 are eigenvalues of AᵀA

**Verification:**

We can verify by computing AᵀA:
```
A = UΣVᵀ
AᵀA = (VΣᵀUᵀ)(UΣVᵀ) = VΣᵀΣVᵀ

ΣᵀΣ = [1.5  0  ]  [1.5  0   0 ]   [2.25  0    0  ]
      [0    0.5]  [0    0.5 0 ] = [0     0.25 0  ]
      [0    0  ]  [0    0   0 ]   [0     0    0  ]
```

Eigenvalues of AᵀA: 2.25, 0.25, 0
Square roots: 1.5, 0.5, 0 ✓

---

### Part (c)(ii): Calculate pseudo-inverse A⁺ from SVD [5 marks]

**Given:**
- SVD: A = UΣVᵀ
- Hint: (AB)⁺ = B⁺A⁺
- If A is invertible, then A⁺ = A⁻¹

**Formula for Pseudo-inverse using SVD:**

For A = UΣVᵀ, the Moore-Penrose pseudo-inverse is:
```
A⁺ = VΣ⁺Uᵀ
```

where Σ⁺ is the pseudo-inverse of Σ.

**Step-by-Step Derivation:**

**Step 1: Understand the formula**

Starting from A = UΣVᵀ, we want to find A⁺.

Since (AB)⁺ = B⁺A⁺, we have:
```
A = UΣVᵀ = (U)(ΣVᵀ) = (UΣ)(Vᵀ)
```

Using the hint:
```
A⁺ = ((UΣ)(Vᵀ))⁺ = (Vᵀ)⁺(UΣ)⁺ = ((Vᵀ)⁺)((UΣ)⁺)
```

**Step 2: Find (Vᵀ)⁺**

V is an orthogonal matrix (VᵀV = I), so:
```
(Vᵀ)⁺ = (Vᵀ)⁻¹ = V
```

**Step 3: Find (UΣ)⁺**

Using (AB)⁺ = B⁺A⁺ again:
```
(UΣ)⁺ = Σ⁺U⁺
```

Since U is orthogonal (UᵀU = I):
```
U⁺ = U⁻¹ = Uᵀ
```

Therefore:
```
(UΣ)⁺ = Σ⁺Uᵀ
```

**Step 4: Combine**
```
A⁺ = (Vᵀ)⁺(UΣ)⁺ = V(Σ⁺Uᵀ) = VΣ⁺Uᵀ
```

**Step 5: Compute Σ⁺**

For a diagonal matrix Σ, the pseudo-inverse Σ⁺ is obtained by:
1. Taking the reciprocal of each non-zero diagonal element
2. Transposing the result

```
Σ = [1.5  0   0 ]  (2×3 matrix)
    [0    0.5 0 ]

Σ⁺ = [1/1.5    0    ]  (3×2 matrix)
     [0        1/0.5 ]
     [0        0     ]

Σ⁺ = [0.667    0   ]
     [0        2   ]
     [0        0   ]
```

Or more precisely:
```
Σ⁺ = [2/3   0  ]
     [0     2  ]
     [0     0  ]
```

**Step 6: Compute A⁺ = VΣ⁺Uᵀ**

```
V = [0  1  0]     Σ⁺ = [2/3  0 ]     Uᵀ = [0  1]
    [1  0  0]            [0    2 ]          [1  0]
    [0  0  1]            [0    0 ]

Step 1: Compute VΣ⁺
VΣ⁺ = [0  1  0] [2/3  0 ]   [0    2 ]
      [1  0  0] [0    2 ] = [2/3  0 ]
      [0  0  1] [0    0 ]   [0    0 ]

Step 2: Compute (VΣ⁺)Uᵀ
A⁺ = [0    2 ] [0  1]   [2   0]
     [2/3  0 ] [1  0] = [0   2/3]
     [0    0 ]          [0   0 ]
```

**Final Answer:**
```
A⁺ = [2     0  ]
     [0     2/3]
     [0     0  ]
```

Or in decimal:
```
A⁺ = [2.0   0    ]
     [0     0.667]
     [0     0    ]
```

**Verification:**

We can verify A⁺ satisfies the Moore-Penrose conditions:
1. AA⁺A = A
2. A⁺AA⁺ = A⁺
3. (AA⁺)ᵀ = AA⁺
4. (A⁺A)ᵀ = A⁺A

Let's check condition 1:

First compute A:
```
A = UΣVᵀ = [0  1] [1.5  0   0 ] [0  1  0]
           [1  0] [0    0.5 0 ] [1  0  0]
                                  [0  0  1]

ΣVᵀ = [1.5  0   0 ] [0  1  0]   [0   1.5 0  ]
      [0    0.5 0 ] [1  0  0] = [0.5 0   0  ]
                     [0  0  1]

A = [0  1] [0   1.5 0  ]   [0.5  0   0  ]
    [1  0] [0.5 0   0  ] = [0    1.5 0  ]
```

So A is:
```
A = [0.5  0   0  ]
    [0    1.5 0  ]
```

Now verify AA⁺A:
```
AA⁺ = [0.5  0   0  ] [2     0  ]   [1  0  0]
      [0    1.5 0  ] [0     2/3] = [0  1  0]
                      [0     0  ]

(AA⁺)A = [1  0  0] [0.5  0   0  ]   [0.5  0   0  ]
         [0  1  0] [0    1.5 0  ] = [0    1.5 0  ]

This equals A! ✓
```

**Summary of Steps:**

1. Recognize A = UΣVᵀ is the SVD
2. Use formula: A⁺ = VΣ⁺Uᵀ
3. Compute Σ⁺ by taking reciprocals of non-zero diagonal elements and transposing
4. Use properties: U⁺ = Uᵀ and V⁺ = Vᵀ (orthogonal matrices)
5. Multiply: A⁺ = VΣ⁺Uᵀ

---

## Question 2: Optimization (20 marks)

### Part (a): Solve using normal equations [5 marks]

**Given:**

Minimize: f(x) = ||Ax - b||²

where:
```
A = [1  0]     b = [1]     x = [x₁]
    [0  1]         [1]         [x₂]
```

**Normal Equations Method:**

The normal equations are derived by setting the gradient of the least squares cost function to zero:

**∇f(x) = 2Aᵀ(Ax - b) = 0**

This gives:
```
AᵀAx = Aᵀb
```

**Step 1: Compute AᵀA**

```
AᵀA = [1  0]ᵀ [1  0]   [1  0] [1  0]   [1  0]
      [0  1]  [0  1] = [0  1] [0  1] = [0  1]
```

**AᵀA = I** (identity matrix)

**Step 2: Compute Aᵀb**

```
Aᵀb = [1  0]ᵀ [1]   [1  0] [1]   [1]
      [0  1]  [1] = [0  1] [1] = [1]
```

**Aᵀb = [1, 1]ᵀ**

**Step 3: Solve AᵀAx = Aᵀb**

```
[1  0] [x₁]   [1]
[0  1] [x₂] = [1]
```

This simplifies to:
```
x₁ = 1
x₂ = 1
```

**Step 4: Find (AᵀA)⁻¹**

Since AᵀA = I:
```
(AᵀA)⁻¹ = I⁻¹ = I
```

**Step 5: Compute x* = (AᵀA)⁻¹Aᵀb**

```
x* = I × [1]   [1]
         [1] = [1]
```

**Answer:**
```
x* = [1]
     [1]
```

Or x₁* = 1, x₂* = 1

**Verification:**

Check that Ax* = b:
```
Ax* = [1  0] [1]   [1]
      [0  1] [1] = [1] = b ✓
```

Cost function value:
```
f(x*) = ||Ax* - b||² = ||[1,1]ᵀ - [1,1]ᵀ||² = ||[0,0]ᵀ||² = 0 ✓
```

The solution is exact (zero error) because the system is perfectly determined!

---

### Part (b): Solve using gradient descent [5 marks]

**Given:**
- Initial guess: x₀ = [0, 0]ᵀ
- Step size: α = 0.5
- Perform 2 iterations
- Gradient: ∇f(x) = 2Aᵀ(Ax - b)

**Gradient Descent Update Rule:**
```
xₖ₊₁ = xₖ - α∇f(xₖ)
```

**Gradient Formula:**
```
∇f(x) = 2Aᵀ(Ax - b)
```

---

**Iteration 0 (Initial):**
```
x₀ = [0]
     [0]
```

---

**Iteration 1:**

**Step 1: Compute Ax₀**
```
Ax₀ = [1  0] [0]   [0]
      [0  1] [0] = [0]
```

**Step 2: Compute Ax₀ - b**
```
Ax₀ - b = [0] - [1]   [-1]
          [0]   [1] = [-1]
```

**Step 3: Compute ∇f(x₀) = 2Aᵀ(Ax₀ - b)**
```
∇f(x₀) = 2[1  0] [-1]   2[-1]   [-2]
          [0  1] [-1] = 2[-1] = [-2]
```

**Step 4: Update x₁ = x₀ - α∇f(x₀)**
```
x₁ = [0] - 0.5[-2]   [0] - [-1]   [1]
     [0]       [-2] = [0]   [-1] = [1]
```

**Result after iteration 1:**
```
x₁ = [1]
     [1]
```

---

**Iteration 2:**

**Step 1: Compute Ax₁**
```
Ax₁ = [1  0] [1]   [1]
      [0  1] [1] = [1]
```

**Step 2: Compute Ax₁ - b**
```
Ax₁ - b = [1] - [1]   [0]
          [1]   [1] = [0]
```

**Step 3: Compute ∇f(x₁) = 2Aᵀ(Ax₁ - b)**
```
∇f(x₁) = 2[1  0] [0]   2[0]   [0]
          [0  1] [0] = 2[0] = [0]
```

**Step 4: Update x₂ = x₁ - α∇f(x₁)**
```
x₂ = [1] - 0.5[0]   [1] - [0]   [1]
     [1]       [0] = [1]   [0] = [1]
```

**Result after iteration 2:**
```
x₂ = [1]
     [1]
```

---

**Summary:**

| Iteration | x | Gradient ∇f(x) | Cost f(x) |
|-----------|---|----------------|-----------|
| 0 | [0, 0]ᵀ | [-2, -2]ᵀ | 2 |
| 1 | [1, 1]ᵀ | [0, 0]ᵀ | 0 |
| 2 | [1, 1]ᵀ | [0, 0]ᵀ | 0 |

**Final Answer after 2 iterations:**
```
x₂ = [1]
     [1]
```

**Observations:**
- Converged in just 1 iteration!
- Gradient became zero after iteration 1
- Reached optimal solution x* = [1, 1]ᵀ
- This fast convergence happens because:
  - A is identity matrix (perfectly conditioned)
  - Step size α = 0.5 is optimal for this problem
  - Problem is convex quadratic

**Cost function values:**
```
f(x₀) = ||[0,0]ᵀ - [1,1]ᵀ||² = ||[-1,-1]ᵀ||² = 1 + 1 = 2
f(x₁) = ||[1,1]ᵀ - [1,1]ᵀ||² = ||[0,0]ᵀ||² = 0
f(x₂) = 0
```

---

### Part (c): Discuss merits of SGD for least squares [4 marks]

**Stochastic Gradient Descent (SGD) Overview:**

Instead of computing the gradient using ALL data points:
```
∇f(x) = 2Aᵀ(Ax - b)  (uses all n samples)
```

SGD uses a random subset (mini-batch) or single sample:
```
∇f(x) ≈ 2aᵢᵀ(aᵢx - bᵢ)  (uses one sample i)
```

where aᵢ is the i-th row of A and bᵢ is the i-th element of b.

---

**Merits of SGD for Least Squares Problems:**

**1. Computational Efficiency for Large Datasets**

**Problem with standard GD:**
- Computing ∇f(x) = 2Aᵀ(Ax - b) requires:
  - Matrix-vector multiplication: O(nd) operations
  - Where n = number of samples, d = dimensions
  - For n = 1 billion, d = 1000: 10¹² operations per iteration!

**SGD advantage:**
- Mini-batch gradient using b samples: O(bd) operations
- Typical b = 32, 64, 256 (much smaller than n)
- Speedup: n/b times faster per iteration
- Example: If n = 1,000,000 and b = 100, then 10,000× speedup!

**Formula:**
```
Per-iteration cost:
- Full GD: O(nd)
- SGD: O(bd) where b << n
```

---

**2. Memory Efficiency**

**Memory requirements:**
- Full batch GD: Must load entire dataset into memory
  - Requires n × d memory
  - For large datasets (e.g., ImageNet), this is prohibitive

**SGD:**
- Only needs mini-batch in memory: b × d
- Can process datasets larger than RAM
- Enables training on limited hardware (GPUs with 16GB memory)

---

**3. Faster Convergence (in terms of data seen)**

**Surprising benefit:**
- SGD makes more frequent updates (one per mini-batch)
- Full GD makes one update per full pass through data
- SGD can make 1000 updates while GD makes 1 update (if n = 1000)

**Trade-off:**
- Each SGD update is noisier (less accurate gradient)
- But frequency compensates for noise
- Often reaches good solution faster in wall-clock time

**Convergence rate:**
- Full GD: O(1/k) convergence (k = iterations)
- SGD: O(1/√k) convergence in expectation
- But SGD iterations are much cheaper!

---

**4. Regularization Effect (Implicit)**

**Noise as regularization:**
- Gradient noise acts as regularization
- Helps escape sharp local minima
- Can lead to better generalization
- Prevents overfitting to training data

**Effect:**
- SGD tends to find "flatter" minima
- Flatter minima generalize better to test data
- Full GD may overfit to training data

---

**5. Online Learning Capability**

**Streaming data:**
- SGD can process data one sample at a time
- No need to store entire dataset
- Can adapt to changing data distributions
- Useful for real-time applications

**Example:**
```python
for sample in data_stream:
    x = x - α * gradient(sample)
```

---

**6. Parallelization**

**Mini-batch SGD:**
- Can parallelize gradient computation across mini-batch
- Each GPU core processes different samples
- Scales well to distributed systems
- Data parallelism across multiple GPUs

---

**Drawbacks (for completeness):**

1. **Noisy convergence:**
   - Solution oscillates around optimum
   - Need to decrease learning rate over time

2. **Hyperparameter sensitivity:**
   - Learning rate α requires careful tuning
   - Mini-batch size b affects performance

3. **Non-deterministic:**
   - Different runs give different results
   - Harder to reproduce results

4. **May need more iterations:**
   - More iterations needed for high accuracy
   - But each iteration is much cheaper

---

**Summary Table:**

| Aspect | Full GD | SGD | Winner |
|--------|---------|-----|--------|
| Per-iteration cost | O(nd) | O(bd) | SGD |
| Memory | O(nd) | O(bd) | SGD |
| Convergence rate | O(1/k) | O(1/√k) | GD |
| Wall-clock time | Slower | Faster | SGD |
| Large datasets | Prohibitive | Feasible | SGD |
| Accuracy | High | Medium | GD |

---

**Practical Recommendation:**

For least squares problems:
- **Small datasets (n < 10,000):** Use full batch GD or normal equations
- **Large datasets (n > 100,000):** Use mini-batch SGD
- **Huge datasets (n > 1,000,000):** SGD is essential
- **Online/streaming:** Use SGD with single samples

**Best practice:**
- Start with SGD for prototyping (fast)
- Fine-tune with smaller mini-batches or full GD (accurate)
- Use adaptive methods (Adam, RMSprop) for better convergence

---

### Part (d): Solve constrained problem with Lagrange multipliers [6 marks]

**Problem:**

Minimize: f(x) = ||Ax - b||²

Subject to: g(x) = x₁ + x₂ - 1 = 0

where:
```
A = [1  0]     b = [1]
    [0  1]         [1]
```

**Lagrange Multiplier Method:**

**Step 1: Set up the Lagrangian**

The Lagrangian function is:
```
L(x, λ) = f(x) + λg(x)
L(x, λ) = ||Ax - b||² + λ(x₁ + x₂ - 1)
```

Expanding f(x):
```
f(x) = (Ax - b)ᵀ(Ax - b)
     = (x₁ - 1)² + (x₂ - 1)²
     = x₁² - 2x₁ + 1 + x₂² - 2x₂ + 1
     = x₁² + x₂² - 2x₁ - 2x₂ + 2
```

Therefore:
```
L(x, λ) = x₁² + x₂² - 2x₁ - 2x₂ + 2 + λ(x₁ + x₂ - 1)
```

---

**Step 2: Take partial derivatives**

For optimality, we need:
```
∇ₓL = 0  (gradient with respect to x)
∇λL = 0  (gradient with respect to λ)
```

**Partial derivative with respect to x₁:**
```
∂L/∂x₁ = 2x₁ - 2 + λ = 0
```

**Partial derivative with respect to x₂:**
```
∂L/∂x₂ = 2x₂ - 2 + λ = 0
```

**Partial derivative with respect to λ:**
```
∂L/∂λ = x₁ + x₂ - 1 = 0
```

---

**Step 3: Solve the system of equations**

We have three equations:
```
(1)  2x₁ - 2 + λ = 0  →  2x₁ + λ = 2
(2)  2x₂ - 2 + λ = 0  →  2x₂ + λ = 2
(3)  x₁ + x₂ = 1
```

From equations (1) and (2):
```
2x₁ + λ = 2
2x₂ + λ = 2
```

Subtracting:
```
2x₁ - 2x₂ = 0
x₁ = x₂
```

---

**Step 4: Use the constraint**

Substituting x₁ = x₂ into equation (3):
```
x₁ + x₂ = 1
x₁ + x₁ = 1
2x₁ = 1
x₁ = 1/2
```

Therefore:
```
x₂ = 1/2
```

---

**Step 5: Find λ**

Substituting back into equation (1):
```
2x₁ + λ = 2
2(1/2) + λ = 2
1 + λ = 2
λ = 1
```

---

**Step 6: Solution**

**Optimal solution:**
```
x* = [1/2]  = [0.5]
     [1/2]    [0.5]

λ* = 1
```

---

**Verification:**

**Check constraint:**
```
x₁* + x₂* = 0.5 + 0.5 = 1 ✓
```

**Check KKT conditions:**
```
∇f(x*) + λ*∇g(x*) = 0

∇f(x*) = 2Aᵀ(Ax* - b) = 2[1  0] ([1  0] [0.5] - [1])
                           [0  1]  [0  1] [0.5]   [1]

                       = 2[1  0] ([0.5] - [1])
                           [0  1]  [0.5]   [1]

                       = 2[1  0] [-0.5]   2[-0.5]   [-1]
                           [0  1] [-0.5] = 2[-0.5] = [-1]

∇g(x*) = [1]
         [1]

∇f(x*) + λ*∇g(x*) = [-1] + 1[1]   [-1] + [1]   [0]
                     [-1]    [1] = [-1]   [1] = [0] ✓
```

**Cost function at constrained optimum:**
```
f(x*) = ||Ax* - b||²
      = ||[0.5, 0.5]ᵀ - [1, 1]ᵀ||²
      = ||[-0.5, -0.5]ᵀ||²
      = 0.25 + 0.25
      = 0.5
```

**Compare with unconstrained optimum:**
- Unconstrained: x* = [1, 1]ᵀ, f(x*) = 0
- Constrained: x* = [0.5, 0.5]ᵀ, f(x*) = 0.5
- Cost increased due to constraint

---

**Summary of Steps:**

1. **Form Lagrangian:** L(x, λ) = f(x) + λg(x)

2. **Take gradients:**
   - ∇ₓL = ∇f(x) + λ∇g(x) = 0
   - ∇λL = g(x) = 0

3. **Solve system of equations:**
   - From ∇ₓL = 0: relationship between variables
   - From ∇λL = 0: constraint equation
   - Solve simultaneously

4. **Verify:**
   - Check constraint is satisfied
   - Check KKT conditions

5. **Interpret λ:**
   - λ* = 1 is the "shadow price"
   - If constraint relaxed by Δ (x₁ + x₂ = 1 + Δ), cost decreases by approximately λ*Δ

---

**General Matrix Form (for arbitrary A, b):**

**Lagrangian:**
```
L(x, λ) = (Ax - b)ᵀ(Ax - b) + λ(cᵀx - d)
```

where constraint is cᵀx = d (in our case, c = [1, 1]ᵀ, d = 1)

**KKT Conditions:**
```
∇ₓL = 2AᵀAx - 2Aᵀb + λc = 0
∇λL = cᵀx - d = 0
```

**System to solve:**
```
[2AᵀA   c ] [x]   [2Aᵀb]
[cᵀ     0 ] [λ] = [d   ]
```

This is a saddle point system that can be solved using:
- Direct methods (Gaussian elimination)
- Iterative methods (GMRES, conjugate gradients)
- Schur complement approach

---

## Question 3: Probabilities (20 marks)

### Part (a)(i): Parametrization of normal distribution [2 marks]

**Problem:**

We have 100 users, each with gaze location (x, y) where:
- x, y ∈ [0, 1]
- (0, 0) = top left corner
- (1, 1) = bottom right corner

Assume gaze locations are normally distributed.

**Model:**

The gaze location is a 2D random variable:
```
g = [x]  ∈ ℝ²
    [y]
```

For a 2D normal distribution (bivariate normal):
```
g ~ N(μ, Σ)
```

where:
- **μ** is the mean vector (location parameter)
- **Σ** is the covariance matrix (shape/spread parameter)

---

**Parameters:**

**1. Mean vector μ:**
```
μ = [μₓ]  ∈ ℝ²
    [μᵧ]
```

**Dimensionality:** 2 elements (2D vector)

**Interpretation:**
- μₓ = expected x-coordinate of gaze
- μᵧ = expected y-coordinate of gaze
- Center of the distribution on the webpage

---

**2. Covariance matrix Σ:**
```
Σ = [σₓ²      σₓᵧ  ]  ∈ ℝ²ˣ²
    [σₓᵧ      σᵧ²  ]
```

**Dimensionality:** 2×2 = 4 elements, but only 3 are independent (symmetric matrix)

**Components:**
- **σₓ²** : variance of x (spread in horizontal direction)
- **σᵧ²** : variance of y (spread in vertical direction)
- **σₓᵧ** : covariance between x and y (correlation)

**Properties:**
- Σ must be positive semi-definite
- Σ is symmetric: Σ = Σᵀ
- For valid covariance: σₓ² ≥ 0, σᵧ² ≥ 0, σₓ²σᵧ² ≥ σₓᵧ²

---

**Correlation:**

Related to covariance by:
```
ρ = σₓᵧ / (σₓσᵧ)  where -1 ≤ ρ ≤ 1
```

Can also parametrize with correlation:
```
Σ = [σₓ²        ρσₓσᵧ  ]
    [ρσₓσᵧ      σᵧ²     ]
```

---

**Summary:**

**Total parameters: 5 (but 3 independent in covariance)**

| Parameter | Symbol | Dimension | Description |
|-----------|--------|-----------|-------------|
| Mean vector | μ | 2 × 1 | Center of distribution |
| Covariance matrix | Σ | 2 × 2 | Shape and orientation |

**Independent parameters: 2 (mean) + 3 (covariance) = 5**

- μₓ, μᵧ (2 parameters)
- σₓ², σᵧ², σₓᵧ (3 parameters)

Or equivalently:
- μₓ, μᵧ (2 parameters)
- σₓ², σᵧ², ρ (3 parameters)

---

**Probability Density Function:**

```
p(g | μ, Σ) = (1/(2π|Σ|^(1/2))) exp(-1/2 (g - μ)ᵀΣ⁻¹(g - μ))
```

where |Σ| is the determinant of Σ.

---

### Part (a)(ii): Estimate parameters from D [3 marks]

**Given:**
- Database D with 100 gaze locations
- Each record: gᵢ = [xᵢ, yᵢ]ᵀ for i = 1, 2, ..., 100

**Goal:** Estimate μ and Σ

---

**Method: Maximum Likelihood Estimation (MLE)**

For a normal distribution, MLE gives the sample mean and sample covariance.

---

**Step 1: Estimate Mean Vector μ̂**

**Formula:**
```
μ̂ = (1/N) Σᵢ₌₁ᴺ gᵢ
```

where N = 100 (number of users)

**Component-wise:**
```
μ̂ₓ = (1/100) Σᵢ₌₁¹⁰⁰ xᵢ  (average x-coordinate)

μ̂ᵧ = (1/100) Σᵢ₌₁¹⁰⁰ yᵢ  (average y-coordinate)
```

**Result:**
```
μ̂ = [μ̂ₓ]
    [μ̂ᵧ]
```

**Example calculation:**
```python
import numpy as np

# Data: D is 100×2 array
# D[i] = [x_i, y_i]

mu_hat = np.mean(D, axis=0)
# mu_hat = [mean(x), mean(y)]
```

---

**Step 2: Estimate Covariance Matrix Σ̂**

**Formula (unbiased estimator):**
```
Σ̂ = (1/(N-1)) Σᵢ₌₁ᴺ (gᵢ - μ̂)(gᵢ - μ̂)ᵀ
```

**Expanding:**
```
Σ̂ = [σ̂ₓ²      σ̂ₓᵧ  ]
    [σ̂ₓᵧ      σ̂ᵧ²  ]
```

where:

**Variance of x:**
```
σ̂ₓ² = (1/(N-1)) Σᵢ₌₁ᴺ (xᵢ - μ̂ₓ)²
```

**Variance of y:**
```
σ̂ᵧ² = (1/(N-1)) Σᵢ₌₁ᴺ (yᵢ - μ̂ᵧ)²
```

**Covariance:**
```
σ̂ₓᵧ = (1/(N-1)) Σᵢ₌₁ᴺ (xᵢ - μ̂ₓ)(yᵢ - μ̂ᵧ)
```

**Note:** We use N-1 (Bessel's correction) for unbiased estimation.

---

**Matrix Form:**

Define centered data matrix:
```
G_centered = [g₁ - μ̂, g₂ - μ̂, ..., gₙ - μ̂]ᵀ  (100×2 matrix)
```

Then:
```
Σ̂ = (1/(N-1)) G_centeredᵀ G_centered
```

---

**Implementation:**

```python
import numpy as np

# Step 1: Estimate mean
mu_hat = np.mean(D, axis=0)  # Shape: (2,)

# Step 2: Center the data
D_centered = D - mu_hat  # Broadcasting: (100,2) - (2,)

# Step 3: Estimate covariance
Sigma_hat = np.cov(D.T)  # np.cov expects features as rows
# or manually:
Sigma_hat = (1/99) * (D_centered.T @ D_centered)

# Result:
# mu_hat = [mean_x, mean_y]
# Sigma_hat = [[var_x, cov_xy],
#              [cov_xy, var_y]]
```

---

**Alternative: Using scipy:**

```python
from scipy.stats import multivariate_normal

# Fit normal distribution
mu_hat, Sigma_hat = D.mean(axis=0), np.cov(D.T)

# Create distribution
rv = multivariate_normal(mean=mu_hat, cov=Sigma_hat)

# Evaluate probability of new gaze location
prob = rv.pdf([0.5, 0.5])
```

---

**Summary of Estimation:**

| Parameter | Estimator | Formula |
|-----------|-----------|---------|
| Mean μ | Sample mean | μ̂ = (1/N) Σᵢ gᵢ |
| Covariance Σ | Sample covariance | Σ̂ = (1/(N-1)) Σᵢ (gᵢ-μ̂)(gᵢ-μ̂)ᵀ |

**Properties of MLE for Normal Distribution:**
- Unbiased: E[μ̂] = μ, E[Σ̂] = Σ
- Consistent: μ̂ → μ, Σ̂ → Σ as N → ∞
- Efficient: Achieves Cramér-Rao lower bound
- Closed-form solution (no iterative optimization needed)

---

### Part (b)(i): When normal assumption is wrong [2 marks]

**When Normal Distribution is Obviously Wrong:**

**1. Multi-modal Distribution (Multiple Clusters)**

**Scenario:**
Users look at multiple distinct regions of the page:
- Product image (top left)
- Price tag (center)
- "Buy" button (bottom right)

**What you'd see in data:**
- Multiple clusters of gaze locations
- 2 or 3 peaks in density
- Not a single elliptical blob

**How to identify:**
```python
# Visual inspection
import matplotlib.pyplot as plt
plt.scatter(D[:, 0], D[:, 1])
plt.xlabel('x')
plt.ylabel('y')
plt.show()
# Multiple separated clusters visible
```

**Statistical test:**
- Dip test for unimodality
- Hartigan's dip statistic
- Visual: histogram or KDE plot shows multiple peaks

**Issue with normal:**
- Normal distribution is unimodal (single peak)
- Cannot capture multiple hotspots
- Will just average across all clusters

---

**2. Non-Elliptical Shapes**

**Scenario:**
Users scan in patterns:
- Reading pattern: left-to-right, top-to-bottom (L or Z shape)
- F-pattern: horizontal lines at top, vertical line on left
- Circular regions around images

**What you'd see:**
- Elongated non-elliptical regions
- Banana-shaped or crescent-shaped distributions
- Sharp boundaries (e.g., no one looks outside page bounds)

**How to identify:**
- Scatter plot shows non-elliptical shape
- High skewness or kurtosis
- Jarque-Bera test rejects normality

---

**3. Boundary Effects**

**Scenario:**
Coordinates bounded to [0, 1] × [0, 1]

**Issue:**
- Normal distribution has support on all of ℝ²
- Normal allows negative values or values > 1
- Truncation at boundaries violates normality

**How to identify:**
```python
# Check for clustering at boundaries
boundary_gazes = np.sum((D[:, 0] < 0.05) | (D[:, 0] > 0.95) |
                        (D[:, 1] < 0.05) | (D[:, 1] > 0.95))
if boundary_gazes > 0.2 * len(D):
    print("Boundary effects present!")
```

---

**4. Heavy Tails or Outliers**

**Scenario:**
- Occasional "distracted" users look at random locations
- Outliers far from main gaze area

**How to identify:**
```python
# Q-Q plot (Quantile-Quantile)
from scipy import stats
stats.probplot(D[:, 0], dist="norm", plot=plt)
plt.show()
# If normal, points lie on straight line
# Deviations at tails indicate non-normality
```

---

**Statistical Tests for Normality:**

**1. Shapiro-Wilk Test:**
```python
from scipy.stats import shapiro

stat, p_value = shapiro(D[:, 0])  # Test x-coordinate
if p_value < 0.05:
    print("Reject normality assumption")
```

**2. Anderson-Darling Test:**
```python
from scipy.stats import anderson

result = anderson(D[:, 0])
if result.statistic > result.critical_values[2]:  # 5% significance
    print("Reject normality")
```

**3. Visual Inspection:**
```python
# Scatter plot
plt.scatter(D[:, 0], D[:, 1], alpha=0.5)

# Marginal histograms
plt.hist(D[:, 0], bins=20)  # x distribution
plt.hist(D[:, 1], bins=20)  # y distribution

# 2D KDE plot
from scipy.stats import gaussian_kde
kde = gaussian_kde(D.T)
# Plot shows multiple peaks → not normal
```

---

**Summary:**

Normal distribution is wrong when:
1. **Multiple clusters** (multi-modal)
2. **Non-elliptical shapes** (non-Gaussian patterns)
3. **Boundary effects** (truncation, bounded domain)
4. **Heavy tails / outliers** (extreme values)

**How to identify:**
- Visual: scatter plot, histogram, Q-Q plot
- Statistical: Shapiro-Wilk, Anderson-Darling, Jarque-Bera tests
- Domain knowledge: Known patterns (F-pattern, Z-pattern)

---

### Part (b)(ii): Alternative model and parametrization [3 marks]

**Alternative Model: Gaussian Mixture Model (GMM)**

**Motivation:**
If data has multiple clusters (e.g., users look at 3 key regions), use a mixture of Gaussians.

---

**Model Definition:**

A GMM with K components:
```
p(g) = Σₖ₌₁ᴷ πₖ N(g | μₖ, Σₖ)
```

where:
- **K** = number of components (clusters)
- **πₖ** = mixing coefficient (weight) for component k
- **N(g | μₖ, Σₖ)** = multivariate normal distribution for component k

**Constraint:** Σₖ₌₁ᴷ πₖ = 1 and πₖ ≥ 0

---

**Parametrization:**

For K components in 2D:

**1. Mixing Coefficients π:**
```
π = [π₁, π₂, ..., πₖ]ᵀ
```

**Dimensionality:** K elements, but K-1 independent (due to constraint Σπₖ = 1)

**Interpretation:**
- πₖ = prior probability that gaze belongs to cluster k
- Σₖ πₖ = 1

---

**2. Mean Vectors μₖ:**

For each component k:
```
μₖ = [μₖₓ]  ∈ ℝ²
     [μₖᵧ]
```

**Dimensionality:** K × 2 = 2K elements

**Interpretation:**
- Center of each cluster
- μ₁ might be product image location
- μ₂ might be price location
- μ₃ might be buy button location

---

**3. Covariance Matrices Σₖ:**

For each component k:
```
Σₖ = [σₖₓ²      σₖₓᵧ  ]  ∈ ℝ²ˣ²
     [σₖₓᵧ      σₖᵧ²  ]
```

**Dimensionality:** K × 3 independent parameters = 3K

(Each covariance matrix has 3 independent parameters in 2D)

---

**Total Parameters:**

For K components in 2D:
- **Mixing coefficients:** K - 1 independent
- **Means:** 2K parameters
- **Covariances:** 3K parameters

**Total: (K-1) + 2K + 3K = 6K - 1 parameters**

**Example for K = 3:**
- Mixing: 2 parameters (π₁, π₂, with π₃ = 1 - π₁ - π₂)
- Means: 6 parameters (μ₁ₓ, μ₁ᵧ, μ₂ₓ, μ₂ᵧ, μ₃ₓ, μ₃ᵧ)
- Covariances: 9 parameters (3 per component)
- **Total: 17 parameters**

---

**Simplification Options:**

**1. Diagonal Covariances (σₓᵧ = 0):**
```
Σₖ = [σₖₓ²    0   ]
     [0       σₖᵧ² ]
```

Parameters per component: 2 (instead of 3)
Total: 3K - 1 parameters

**2. Spherical Covariances (σₓ² = σᵧ² = σ², σₓᵧ = 0):**
```
Σₖ = σₖ²I = [σₖ²   0  ]
            [0     σₖ² ]
```

Parameters per component: 1
Total: 4K - 1 parameters

**3. Tied Covariances (all components share same Σ):**
All Σₖ = Σ
Total: K - 1 + 2K + 3 = 3K + 2 parameters

---

**Summary Table:**

| Model | Parameters | Total (K=3, d=2) |
|-------|------------|------------------|
| Single Gaussian | μ (d), Σ (d(d+1)/2) | 5 |
| GMM (full covariance) | (K-1) + Kd + Kd(d+1)/2 | 17 |
| GMM (diagonal cov) | (K-1) + Kd + Kd | 11 |
| GMM (spherical cov) | (K-1) + Kd + K | 8 |

---

**Probability Density:**

```
p(g | θ) = Σₖ₌₁ᴷ πₖ (1/(2π|Σₖ|^(1/2))) exp(-1/2 (g-μₖ)ᵀΣₖ⁻¹(g-μₖ))
```

where θ = {π₁, ..., πₖ, μ₁, ..., μₖ, Σ₁, ..., Σₖ}

---

**Cluster Assignment:**

For a given gaze g, the responsibility (posterior probability) of cluster k is:
```
γₖ(g) = P(k | g) = (πₖ N(g|μₖ,Σₖ)) / (Σⱼ πⱼ N(g|μⱼ,Σⱼ))
```

---

### Part (b)(iii): Estimate GMM parameters [3 marks]

**Method: Expectation-Maximization (EM) Algorithm**

Since we have latent variables (cluster assignments), we use EM for maximum likelihood estimation.

---

**EM Algorithm for GMM:**

**Initialization:**
1. Choose K (number of components)
2. Initialize parameters θ⁽⁰⁾ = {π, μ, Σ}

Common initialization methods:
- Random initialization
- **K-means clustering** (recommended)
- K-means++ for better starting points

---

**Iterate until convergence:**

**E-Step (Expectation):**

For each data point gᵢ and component k, compute responsibility:
```
γᵢₖ = P(k | gᵢ) = (πₖ N(gᵢ|μₖ,Σₖ)) / (Σⱼ₌₁ᴷ πⱼ N(gᵢ|μⱼ,Σⱼ))
```

**Interpretation:**
- γᵢₖ = probability that gaze i belongs to cluster k
- Soft assignment (vs hard assignment in k-means)
- Σₖ γᵢₖ = 1 for each i

**Matrix form:**
Γ is 100×K matrix where Γ[i,k] = γᵢₖ

---

**M-Step (Maximization):**

Update parameters to maximize expected log-likelihood:

**1. Update mixing coefficients:**
```
πₖ = (1/N) Σᵢ₌₁ᴺ γᵢₖ = N_k / N
```

where N_k = Σᵢ γᵢₖ is the effective number of points in cluster k

**Interpretation:** Proportion of data assigned to cluster k

---

**2. Update means:**
```
μₖ = (Σᵢ₌₁ᴺ γᵢₖ gᵢ) / (Σᵢ₌₁ᴺ γᵢₖ) = (Σᵢ γᵢₖ gᵢ) / N_k
```

**Interpretation:** Weighted average of data points, weighted by responsibility

---

**3. Update covariances:**
```
Σₖ = (Σᵢ₌₁ᴺ γᵢₖ (gᵢ - μₖ)(gᵢ - μₖ)ᵀ) / (Σᵢ₌₁ᴺ γᵢₖ)
   = (Σᵢ γᵢₖ (gᵢ - μₖ)(gᵢ - μₖ)ᵀ) / N_k
```

**Interpretation:** Weighted covariance, weighted by responsibility

---

**Convergence:**

Stop when:
```
|log L(θ⁽ᵗ⁾) - log L(θ⁽ᵗ⁻¹⁾)| < ε
```

where log L is the log-likelihood:
```
log L(θ) = Σᵢ₌₁ᴺ log(Σₖ₌₁ᴷ πₖ N(gᵢ|μₖ,Σₖ))
```

Typical: ε = 10⁻⁶ or max 100-500 iterations

---

**Complete Algorithm:**

```
Algorithm: EM for GMM

Input: Data D = {g₁, ..., gₙ}, number of components K
Output: Parameters θ = {π, μ, Σ}

1. INITIALIZATION:
   Run K-means on D to get initial μₖ
   Set πₖ = 1/K for all k
   Set Σₖ = I (identity) for all k

2. REPEAT until convergence:

   E-STEP:
   For each i = 1 to N and k = 1 to K:
       Compute γᵢₖ = (πₖ N(gᵢ|μₖ,Σₖ)) / (Σⱼ πⱼ N(gᵢ|μⱼ,Σⱼ))

   M-STEP:
   For each k = 1 to K:
       N_k = Σᵢ γᵢₖ

       πₖ = N_k / N

       μₖ = (Σᵢ γᵢₖ gᵢ) / N_k

       Σₖ = (Σᵢ γᵢₖ (gᵢ-μₖ)(gᵢ-μₖ)ᵀ) / N_k

   Compute log-likelihood:
       log L = Σᵢ log(Σₖ πₖ N(gᵢ|μₖ,Σₖ))

   If |log L - log L_old| < ε:
       BREAK

3. RETURN θ = {π, μ, Σ}
```

---

**Python Implementation:**

```python
from sklearn.mixture import GaussianMixture

# Fit GMM with K=3 components
gmm = GaussianMixture(
    n_components=3,
    covariance_type='full',  # 'full', 'tied', 'diag', 'spherical'
    max_iter=100,
    random_state=42,
    n_init=10  # Run 10 times, keep best
)

gmm.fit(D)

# Extract parameters
pi = gmm.weights_  # Mixing coefficients, shape: (3,)
mu = gmm.means_  # Means, shape: (3, 2)
Sigma = gmm.covariances_  # Covariances, shape: (3, 2, 2)

# Predict cluster assignments
labels = gmm.predict(D)  # Hard assignment
responsibilities = gmm.predict_proba(D)  # Soft assignment, shape: (100, 3)

# Evaluate new gaze location
log_prob = gmm.score_samples([[0.5, 0.6]])  # Log probability
prob = np.exp(log_prob)
```

---

**Model Selection (Choosing K):**

How many components K?

**1. Bayesian Information Criterion (BIC):**
```
BIC = -2 log L + p log N
```

Choose K that minimizes BIC

**2. Akaike Information Criterion (AIC):**
```
AIC = -2 log L + 2p
```

Choose K that minimizes AIC

**3. Cross-validation:**
Split data, train on train set, evaluate on validation set

**4. Elbow method:**
Plot log-likelihood vs K, look for "elbow"

```python
from sklearn.mixture import GaussianMixture

bic_scores = []
aic_scores = []
K_range = range(1, 10)

for K in K_range:
    gmm = GaussianMixture(n_components=K)
    gmm.fit(D)
    bic_scores.append(gmm.bic(D))
    aic_scores.append(gmm.aic(D))

optimal_K = K_range[np.argmin(bic_scores)]
print(f"Optimal K: {optimal_K}")
```

---

**Advantages of EM:**
- Guaranteed to converge (to local optimum)
- Each iteration increases log-likelihood
- Handles soft assignments naturally

**Disadvantages:**
- Sensitive to initialization (use k-means++)
- Can get stuck in local optima (run multiple times)
- Requires choosing K

---

### Part (c): Probability of buying given gaze location [7 marks]

**Problem:**

Given:
- 100 users with gaze locations gᵢ
- 25 bought something (class B = "buy")
- 75 did not buy (class ¬B = "no buy")

Find: P(Buy | gaze at g₀)

---

**Approach: Bayes' Theorem**

We want to compute:
```
P(B | g₀) = P(g₀ | B) P(B) / P(g₀)
```

where:
- P(B | g₀) = probability of buying given gaze at g₀ (posterior)
- P(g₀ | B) = likelihood of gaze g₀ given buyer
- P(B) = prior probability of buying
- P(g₀) = evidence (marginal probability of gaze g₀)

---

**Step-by-Step Procedure:**

**Step 1: Estimate Class Priors**

**Prior probability of buying:**
```
P(B) = N_B / N = 25 / 100 = 0.25
```

**Prior probability of not buying:**
```
P(¬B) = N_¬B / N = 75 / 100 = 0.75
```

where:
- N_B = 25 (number of buyers)
- N_¬B = 75 (number of non-buyers)
- N = 100 (total users)

---

**Step 2: Split Data by Class**

Create two datasets:

**D_B:** Gaze locations of buyers
- Contains 25 gaze locations
- D_B = {gᵢ : user i bought}

**D_¬B:** Gaze locations of non-buyers
- Contains 75 gaze locations
- D_¬B = {gᵢ : user i did not buy}

```python
# Assume 'bought' is boolean array indicating who bought
D_buyers = D[bought]  # Shape: (25, 2)
D_non_buyers = D[~bought]  # Shape: (75, 2)
```

---

**Step 3: Estimate Class-Conditional Distributions**

Fit separate normal distributions for each class:

**For buyers:**
```
g | B ~ N(μ_B, Σ_B)
```

Estimate parameters:
```
μ̂_B = (1/N_B) Σᵢ∈B gᵢ  (mean of buyers' gazes)

Σ̂_B = (1/(N_B-1)) Σᵢ∈B (gᵢ - μ̂_B)(gᵢ - μ̂_B)ᵀ  (covariance of buyers' gazes)
```

```python
mu_B = np.mean(D_buyers, axis=0)  # Shape: (2,)
Sigma_B = np.cov(D_buyers.T)  # Shape: (2, 2)
```

**For non-buyers:**
```
g | ¬B ~ N(μ_¬B, Σ_¬B)
```

Estimate parameters:
```
μ̂_¬B = (1/N_¬B) Σᵢ∈¬B gᵢ

Σ̂_¬B = (1/(N_¬B-1)) Σᵢ∈¬B (gᵢ - μ̂_¬B)(gᵢ - μ̂_¬B)ᵀ
```

```python
mu_not_B = np.mean(D_non_buyers, axis=0)
Sigma_not_B = np.cov(D_non_buyers.T)
```

---

**Step 4: Compute Likelihoods**

For a new gaze location g₀:

**Likelihood for buyers:**
```
P(g₀ | B) = N(g₀ | μ̂_B, Σ̂_B)
          = (1/(2π|Σ̂_B|^(1/2))) exp(-1/2 (g₀-μ̂_B)ᵀΣ̂_B⁻¹(g₀-μ̂_B))
```

**Likelihood for non-buyers:**
```
P(g₀ | ¬B) = N(g₀ | μ̂_¬B, Σ̂_¬B)
           = (1/(2π|Σ̂_¬B|^(1/2))) exp(-1/2 (g₀-μ̂_¬B)ᵀΣ̂_¬B⁻¹(g₀-μ̂_¬B))
```

```python
from scipy.stats import multivariate_normal

# Create distributions
rv_B = multivariate_normal(mean=mu_B, cov=Sigma_B)
rv_not_B = multivariate_normal(mean=mu_not_B, cov=Sigma_not_B)

# Compute likelihoods
P_g0_given_B = rv_B.pdf(g0)
P_g0_given_not_B = rv_not_B.pdf(g0)
```

---

**Step 5: Compute Evidence (Marginal Probability)**

By law of total probability:
```
P(g₀) = P(g₀ | B)P(B) + P(g₀ | ¬B)P(¬B)
```

Substituting values:
```
P(g₀) = P(g₀ | B) × 0.25 + P(g₀ | ¬B) × 0.75
```

```python
P_g0 = P_g0_given_B * 0.25 + P_g0_given_not_B * 0.75
```

---

**Step 6: Apply Bayes' Theorem**

**Posterior probability of buying:**
```
P(B | g₀) = P(g₀ | B) P(B) / P(g₀)
          = (P(g₀ | B) × 0.25) / (P(g₀ | B) × 0.25 + P(g₀ | ¬B) × 0.75)
```

```python
P_B_given_g0 = (P_g0_given_B * 0.25) / P_g0
```

**Posterior probability of not buying:**
```
P(¬B | g₀) = P(g₀ | ¬B) P(¬B) / P(g₀)
           = (P(g₀ | ¬B) × 0.75) / P_g0
```

```python
P_not_B_given_g0 = (P_g0_given_not_B * 0.75) / P_g0
```

**Verification:** P(B | g₀) + P(¬B | g₀) = 1 ✓

---

**Complete Implementation:**

```python
import numpy as np
from scipy.stats import multivariate_normal

# Step 1: Prior probabilities
N_B = np.sum(bought)  # 25
N_not_B = np.sum(~bought)  # 75
N = len(bought)  # 100

P_B = N_B / N  # 0.25
P_not_B = N_not_B / N  # 0.75

# Step 2: Split data
D_buyers = D[bought]
D_non_buyers = D[~bought]

# Step 3: Estimate class-conditional distributions
mu_B = np.mean(D_buyers, axis=0)
Sigma_B = np.cov(D_buyers.T)

mu_not_B = np.mean(D_non_buyers, axis=0)
Sigma_not_B = np.cov(D_non_buyers.T)

# Create distributions
rv_B = multivariate_normal(mean=mu_B, cov=Sigma_B)
rv_not_B = multivariate_normal(mean=mu_not_B, cov=Sigma_not_B)

# Step 4: For new gaze location g0
g0 = np.array([0.5, 0.6])  # Example gaze location

# Compute likelihoods
P_g0_given_B = rv_B.pdf(g0)
P_g0_given_not_B = rv_not_B.pdf(g0)

# Step 5: Compute evidence
P_g0 = P_g0_given_B * P_B + P_g0_given_not_B * P_not_B

# Step 6: Compute posterior
P_B_given_g0 = (P_g0_given_B * P_B) / P_g0

print(f"Probability of buying given gaze at {g0}: {P_B_given_g0:.4f}")
```

---

**Interpretation:**

**Example results:**

If g₀ = [0.8, 0.3] (near "Buy" button):
- μ_B might be close to [0.8, 0.3]
- μ_¬B might be far from [0.8, 0.3]
- P(g₀ | B) >> P(g₀ | ¬B)
- **P(B | g₀) ≈ 0.8** (high probability of buying)

If g₀ = [0.1, 0.9] (bottom left, away from content):
- μ_B far from [0.1, 0.9]
- μ_¬B might be closer
- P(g₀ | B) << P(g₀ | ¬B)
- **P(B | g₀) ≈ 0.1** (low probability of buying)

---

**Alternative: Sklearn Implementation**

```python
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

# Fit QDA (equivalent to Gaussian Bayes classifier)
qda = QuadraticDiscriminantAnalysis()
qda.fit(D, bought)  # bought is boolean array

# Predict probability
prob_buy = qda.predict_proba([g0])[0, 1]  # P(B | g0)
print(f"P(Buy | g0): {prob_buy:.4f}")
```

---

**Summary of Approach:**

1. **Estimate priors:** P(B) = 25/100, P(¬B) = 75/100
2. **Split data:** Separate buyers' gazes from non-buyers' gazes
3. **Estimate likelihoods:** Fit N(μ_B, Σ_B) and N(μ_¬B, Σ_¬B)
4. **Compute evidence:** P(g₀) = Σ P(g₀|class)P(class)
5. **Apply Bayes:** P(B|g₀) = P(g₀|B)P(B) / P(g₀)
6. **Interpret:** High P(B|g₀) means gaze at g₀ indicates likely purchase

**This is Gaussian Naive Bayes classification (without naive assumption about feature independence)**

---

## Question 4: Databases (20 marks)

### Part (a)(i): Calculate number of blocks [6 marks]

**Given Data:**

**Course (C) Relation:**
- Schema: Course(Id, Description, Credits)
- Attributes:
  - Id: 4 bytes (primary key)
  - Description: 256 bytes
  - Credits: 1 byte
- Total Records: r_C = 32

**Transcript (T) Relation:**
- Schema: Transcript(StudentId, CourseId, Mark)
- Attributes:
  - StudentId: 4 bytes
  - CourseId: 4 bytes (foreign key to Course.Id)
  - Mark: 8 bytes (double precision)
- Primary Key: (StudentId, CourseId)
- Total Records: r_T = 51,200

**Block size:** 4096 bytes

---

**Step 1: Calculate Record Sizes**

**Course record size:**
```
R_C = sizeof(Id) + sizeof(Description) + sizeof(Credits)
    = 4 + 256 + 1
    = 261 bytes
```

**Transcript record size:**
```
R_T = sizeof(StudentId) + sizeof(CourseId) + sizeof(Mark)
    = 4 + 4 + 8
    = 16 bytes
```

---

**Step 2: Calculate Blocking Factors**

The blocking factor is the number of records that fit in one block.

**Blocking factor for Course:**
```
bfr_C = floor(Block size / R_C)
      = floor(4096 / 261)
      = floor(15.69...)
      = 15 records per block
```

**Blocking factor for Transcript:**
```
bfr_T = floor(Block size / R_T)
      = floor(4096 / 16)
      = floor(256)
      = 256 records per block
```

---

**Step 3: Calculate Number of Blocks**

**Number of blocks for Course:**
```
n_C = ceil(r_C / bfr_C)
    = ceil(32 / 15)
    = ceil(2.13...)
    = 3 blocks
```

**Number of blocks for Transcript:**
```
n_T = ceil(r_T / bfr_T)
    = ceil(51200 / 256)
    = ceil(200)
    = 200 blocks
```

---

**Answer:**

**Course relation:** 3 blocks
**Transcript relation:** 200 blocks

---

**Verification:**

**Course:**
- 2 blocks hold: 2 × 15 = 30 records
- 3rd block holds: 32 - 30 = 2 records
- Total: 3 blocks needed ✓

**Transcript:**
- 200 blocks hold: 200 × 256 = 51,200 records
- Exactly fits! ✓

---

**Python Notation:**

```python
import math

# Course
R_C = 4 + 256 + 1  # 261 bytes
bfr_C = math.floor(4096 / R_C)  # 15
n_C = math.ceil(32 / bfr_C)  # 3

# Transcript
R_T = 4 + 4 + 8  # 16 bytes
bfr_T = math.floor(4096 / R_T)  # 256
n_T = math.ceil(51200 / bfr_T)  # 200
```

Or using notation from hint:
```
n_C = ceil(32 / floor(4096 / 261)) = ceil(32 / 15) = 3
n_T = ceil(51200 / floor(4096 / 16)) = ceil(51200 / 256) = 200
```

---

### Part (a)(ii): Selection cardinality of join [2 marks]

**Query:**
```sql
SELECT * FROM Course C JOIN Transcript T ON C.Id = T.CourseId
```

**Given:**
- r_C = 32 courses
- r_T = 51,200 transcript records
- Assumption: Courses uniformly enrolled by all students

---

**Selection Cardinality:**

The selection cardinality is the **number of tuples in the result** of the join.

**Analysis:**

Each transcript record (StudentId, CourseId, Mark) references exactly one course (via CourseId).

Since CourseId in T is a foreign key to Id in C:
- Every transcript record matches exactly one course record
- No transcript records are dropped (assuming referential integrity)

**Result size:**
```
|C ⋈ T| = |T| = 51,200 tuples
```

---

**Why?**

**Foreign key relationship:**
- Each T record has CourseId that references C.Id
- This is a many-to-one relationship: many transcripts per course
- Join: T.CourseId = C.Id

**Uniform enrollment assumption:**
- Each course appears equally often in transcripts
- Number of transcripts per course: 51,200 / 32 = 1,600

**Join result:**
- Each of 51,200 transcript records joins with its course
- Result has 51,200 tuples
- Each tuple has attributes from both C and T

---

**Formal Calculation:**

**Average transcripts per course:**
```
avg_transcripts_per_course = r_T / r_C = 51,200 / 32 = 1,600
```

**Join cardinality:**
```
|C ⋈ T| = r_T = 51,200
```

Because each transcript joins with exactly one course.

---

**Alternatively (using selectivity):**

**Selectivity of join:**
```
Selectivity = |C ⋈ T| / (|C| × |T|)
            = 51,200 / (32 × 51,200)
            = 1 / 32
```

This matches the intuition: each T record matches 1 out of 32 C records.

---

**Answer:**

**Selection cardinality: 51,200 tuples**

---

**Summary:**
- Foreign key join: each T record matches exactly one C record
- No duplicates created (1-to-many relationship from C to T)
- Result size equals size of T (the "many" side)

---

### Part (a)(iii): How selectivity helps query process [2 marks]

**Selectivity Definition:**

Selectivity is the fraction of tuples that satisfy a condition:
```
Selectivity = (Number of tuples satisfying condition) / (Total number of tuples)
```

For joins:
```
Join selectivity = |R ⋈ S| / (|R| × |S|)
```

---

**How Selectivity Helps in Query Processing:**

**1. Cardinality Estimation**

**Purpose:** Predict size of intermediate results

**Why important:**
- Query optimizer needs to estimate cost of different execution plans
- Cost depends on size of intermediate results
- Selectivity helps estimate: |result| ≈ selectivity × |input|

**Example:**
```sql
SELECT * FROM Transcript WHERE Mark > 90
```

If selectivity = 0.1:
- Estimated result size: 0.1 × 51,200 = 5,120 tuples
- Helps decide whether to use index or table scan

---

**2. Join Order Optimization**

**Purpose:** Decide which join to perform first in multi-join queries

**Strategy:** Perform most selective joins first to minimize intermediate result sizes

**Example:**
```sql
SELECT * FROM C JOIN T ON C.Id = T.CourseId
          JOIN Students S ON T.StudentId = S.Id
```

Query optimizer uses selectivity to decide:
- Option A: (C ⋈ T) ⋈ S
- Option B: (T ⋈ S) ⋈ C

Choose option with smallest intermediate result.

---

**3. Access Method Selection**

**Purpose:** Choose between index scan, table scan, or hash join

**Decision based on selectivity:**

**Low selectivity (< 0.05):**
- Few tuples qualify
- Use index scan (if index available)
- Faster to lookup specific tuples

**High selectivity (> 0.2):**
- Many tuples qualify
- Use table scan
- Overhead of index not worth it

**Example:**
```sql
SELECT * FROM Transcript WHERE CourseId = 5
```

Selectivity = 1,600 / 51,200 = 0.031 (low)
→ Use index on CourseId

---

**4. Memory Allocation**

**Purpose:** Allocate appropriate buffer sizes

**Why important:**
- If join result is small (high selectivity filter), use less memory
- If result is large, allocate more memory or use disk-based algorithms

**Example:**
- Hash join: size hash table based on estimated join cardinality
- If selectivity predicts small result, use in-memory hash table
- If large result, use partitioned hash join with disk

---

**5. Parallelization Decisions**

**Purpose:** Decide whether to parallelize operation

**Based on selectivity:**
- High cardinality (low selectivity) → parallelize
- Low cardinality → sequential might be faster (less overhead)

---

**Concrete Example:**

**Query:**
```sql
SELECT * FROM Course C JOIN Transcript T ON C.Id = T.CourseId
WHERE C.Credits > 3
```

**Without selectivity info:**
- Optimizer might choose (C ⋈ T) then filter by Credits
- Produces 51,200 tuples, then filters

**With selectivity info:**
- If selectivity of "Credits > 3" is 0.25 (25% of courses)
- Optimizer chooses: filter C first (8 courses), then join with T
- Produces only 8 × 1,600 = 12,800 tuples
- **Much more efficient!**

---

**Summary:**

Selectivity helps query processing by:

1. **Estimating result sizes** → better cost estimation
2. **Optimizing join order** → minimize intermediate results
3. **Choosing access methods** → index vs table scan
4. **Allocating resources** → memory, buffers, parallelization
5. **Reducing I/O** → fewer blocks to read/write

**Bottom line:** Selectivity enables the query optimizer to choose the most efficient execution plan, significantly improving query performance.

---

### Part (b)(i): Database choice for music streaming [6 marks]

**Problem:**

Store and query song data with:
- High-dimensional feature vectors
- Acoustic attributes
- Artist information
- ML model embeddings
- Need efficient retrieval and recommendation

---

**Recommended Database Types:**

**1. Vector Database (Primary Recommendation)**

**Examples:** Pinecone, Weaviate, Milvus, Qdrant, FAISS

**Why?**

**Perfect for:**
- High-dimensional embeddings from ML models
- Similarity search (find similar songs)
- Approximate nearest neighbor (ANN) search
- Cosine similarity, Euclidean distance queries

**Features:**
- Optimized for vector operations
- Built-in similarity search algorithms (HNSW, IVF)
- Fast ANN queries: O(log n) instead of O(n)
- Handles dimensions from 100 to 1000+

**Example query:**
```python
# Find songs similar to current song
similar_songs = vector_db.query(
    embedding=current_song_embedding,
    top_k=10,
    metric="cosine"
)
```

**Justification:**
- Recommendation requires finding similar songs based on embeddings
- Vector DBs designed specifically for this use case
- Traditional RDBMS very slow for high-dim similarity search
- Can handle billions of vectors efficiently

---

**2. Document Database (Complementary)**

**Examples:** MongoDB, CouchDB, DynamoDB

**Why?**

**Perfect for:**
- Flexible schema (songs have varying attributes)
- Nested documents (artist info, album data)
- JSON-like storage
- Easy to add new fields

**Example document:**
```json
{
  "song_id": "12345",
  "title": "Bohemian Rhapsody",
  "artist": {
    "name": "Queen",
    "id": "artist_001",
    "genre": ["Rock", "Progressive Rock"]
  },
  "acoustic_features": {
    "tempo": 144,
    "key": "Bb major",
    "energy": 0.82,
    "danceability": 0.45
  },
  "embedding": [0.23, -0.45, 0.67, ...],  // 512-dim vector
  "duration_ms": 354000,
  "release_year": 1975
}
```

**Justification:**
- Song metadata is heterogeneous and evolving
- Artist info naturally nested
- Document model more natural than relational
- Easy to query by specific attributes

---

**3. Hybrid Approach (Best Solution)**

**Combination:** Vector DB + Document/Relational DB

**Architecture:**

```
┌─────────────────────────────────────┐
│      Application Layer              │
└─────────────────────────────────────┘
          │                  │
          │                  │
          ▼                  ▼
┌──────────────────┐  ┌──────────────┐
│   Vector DB      │  │  Document DB │
│  (Embeddings)    │  │  (Metadata)  │
│                  │  │              │
│  - song_id       │  │  - song_id   │
│  - embedding     │  │  - title     │
│  [512-dim vec]   │  │  - artist    │
│                  │  │  - features  │
└──────────────────┘  └──────────────┘
```

**Workflow:**

1. **Store embeddings:** Vector DB (Pinecone)
2. **Store metadata:** Document DB (MongoDB)
3. **Recommendation query:**
   ```
   a. Query vector DB for similar embeddings → get song_ids
   b. Query document DB for metadata of those song_ids
   c. Return rich song information to user
   ```

**Example:**
```python
# Step 1: Find similar songs by embedding
similar_song_ids = vector_db.query(
    embedding=current_song_embedding,
    top_k=50
)

# Step 2: Get metadata
songs = mongo_db.find({"song_id": {"$in": similar_song_ids}})

# Step 3: Filter by user preferences (e.g., genre, artist)
recommended = [s for s in songs if s['artist']['genre'] in user_prefs]
```

---

**4. Additional Database Types to Consider:**

**Graph Database (Neo4j, AWS Neptune):**

**Use case:** Artist relationships, playlist graphs

```
(User) -[:LIKES]-> (Song) -[:BY]-> (Artist)
                     |
                     └-[:SIMILAR_TO]-> (Song)
```

**Benefits:**
- Model complex relationships
- Find paths (users who like X also like Y)
- Collaborative filtering

**When to use:**
- Social features (friend recommendations)
- Complex recommendation logic
- Artist influence networks

---

**Search Engine (Elasticsearch):**

**Use case:** Text search for song titles, artists, lyrics

**Benefits:**
- Full-text search with ranking
- Fuzzy matching ("bohemian rapsody" → "Bohemian Rhapsody")
- Aggregations (top artists, genres)

**When to use:**
- User searches for songs by name
- Auto-complete suggestions
- Analytics dashboards

---

**Comparison Table:**

| Database Type | Use Case | Advantages | Query Example |
|---------------|----------|------------|---------------|
| **Vector DB** | Similarity search, embeddings | Fast ANN, optimized for vectors | Find songs similar to X |
| **Document DB** | Metadata, flexible schema | Easy evolution, nested data | Get all rock songs |
| **Relational DB** | Transactional data, user accounts | ACID, joins, integrity | User playlists, subscriptions |
| **Graph DB** | Relationships, social | Path queries, recommendations | Users who like X also like Y |
| **Search Engine** | Text search, autocomplete | Full-text, fuzzy, analytics | Search "queen bohemian" |

---

**Final Recommendation:**

**Primary:** **Vector Database (Pinecone, Milvus)** for embeddings and similarity search

**Secondary:** **Document Database (MongoDB)** for song metadata

**Optional:**
- Relational DB (PostgreSQL) for user accounts, transactions
- Graph DB (Neo4j) for social features
- Search Engine (Elasticsearch) for text search

**Justification:**
- Vector DB: Essential for ML-based recommendations (core requirement)
- Document DB: Flexible for evolving music metadata
- Hybrid approach: Combines strengths of both
- Scalable: Each database handles what it does best

---

### Part (b)(ii): Store and index song data [4 marks]

**Data Model:**

Each song has:
- **Metadata:** title, artist, album, genre, duration
- **Acoustic features:** tempo, key, energy, danceability (low-dim, 10-50 features)
- **Embedding:** ML-generated vector (high-dim, 128-512 dimensions)

---

**Storage Strategy:**

**1. Vector Database Storage**

**Store embeddings in vector DB:**

```python
# Using Pinecone
import pinecone

# Initialize
pinecone.init(api_key="...", environment="...")
index = pinecone.Index("songs")

# Insert song embedding
index.upsert([
    (
        "song_123",  # song_id (primary key)
        embedding_vector,  # [512-dim float array]
        {  # metadata (optional, for filtering)
            "genre": "rock",
            "artist_id": "artist_001",
            "year": 2020
        }
    )
])
```

**Key decisions:**

**Dimension:** 128-512 (trade-off: quality vs speed)
- Higher dim: Better representation, slower queries
- Lower dim: Faster, might lose information
- Recommendation: 256-384 dimensions

**Metric:** Cosine similarity (most common for song embeddings)
- Cosine: Measures angle (good for normalized vectors)
- Euclidean: Measures distance (good for spatial data)
- Dot product: Fast, works for normalized vectors

---

**2. Document Database Storage**

**Store metadata in MongoDB:**

```javascript
// MongoDB collection: songs
{
  "_id": "song_123",
  "title": "Song Title",
  "artist": {
    "id": "artist_001",
    "name": "Artist Name",
    "genres": ["Rock", "Alternative"]
  },
  "album": {
    "id": "album_456",
    "title": "Album Title",
    "year": 2020
  },
  "acoustic_features": {
    "tempo": 120.5,
    "key": "C major",
    "energy": 0.8,
    "danceability": 0.6,
    "valence": 0.7
  },
  "duration_ms": 240000,
  "popularity": 85,
  "explicit": false,
  "tags": ["upbeat", "summer", "driving"]
}
```

---

**Indexing Strategy:**

**1. Vector Index (in Vector DB)**

**Index type:** HNSW (Hierarchical Navigable Small World)

**Why HNSW?**
- Best balance of speed and accuracy
- O(log n) query time
- High recall (>95%)
- Standard for vector DBs

**Configuration:**
```python
# Pinecone
index = pinecone.create_index(
    name="songs",
    dimension=384,
    metric="cosine",
    pod_type="p1.x1"  # Performance pod
)

# Milvus
collection.create_index(
    field_name="embedding",
    index_params={
        "metric_type": "COSINE",
        "index_type": "HNSW",
        "params": {"M": 16, "efConstruction": 200}
    }
)
```

**Parameters:**
- **M:** Number of connections per layer (default: 16)
  - Higher M: Better recall, more memory
- **efConstruction:** Controls build quality
  - Higher: Better index, slower build
- **ef:** Controls search quality (query time)
  - Higher: Better recall, slower queries

**Alternative indices:**

**IVF (Inverted File Index):**
- Faster build, slightly lower recall
- Good for very large datasets (>10M songs)

**LSH (Locality Sensitive Hashing):**
- Probabilistic, very fast
- Lower recall, good for approximate search

---

**2. Secondary Indices (in Document DB)**

**Index on frequently queried fields:**

```javascript
// MongoDB indices
db.songs.createIndex({"artist.id": 1});  // Fast artist lookup
db.songs.createIndex({"genre": 1});  // Filter by genre
db.songs.createIndex({"year": 1});  // Filter by year
db.songs.createIndex({"popularity": -1});  // Sort by popularity

// Compound index for complex queries
db.songs.createIndex({
  "artist.id": 1,
  "year": 1,
  "popularity": -1
});

// Text index for search
db.songs.createIndex({
  "title": "text",
  "artist.name": "text",
  "tags": "text"
});
```

---

**Retrieval Strategy:**

**Scenario 1: Pure Similarity Search**

"Find songs similar to song X"

```python
# Query vector DB
similar_songs = vector_index.query(
    vector=song_x_embedding,
    top_k=20,
    filter={"year": {"$gte": 2015}}  # Optional metadata filter
)

# Get full metadata from MongoDB
song_ids = [hit['id'] for hit in similar_songs]
full_data = mongo_db.songs.find({"_id": {"$in": song_ids}})
```

**Query time:** ~10-50ms for 1M songs

---

**Scenario 2: Hybrid Search**

"Find upbeat rock songs similar to song X from 2020+"

```python
# Step 1: Metadata pre-filter (MongoDB)
candidate_ids = mongo_db.songs.distinct("_id", {
    "genre": "Rock",
    "acoustic_features.energy": {"$gt": 0.7},  # Upbeat
    "year": {"$gte": 2020}
})

# Step 2: Similarity search (Vector DB) with pre-filter
similar_songs = vector_index.query(
    vector=song_x_embedding,
    top_k=20,
    filter={"_id": {"$in": candidate_ids}}
)
```

---

**Scenario 3: Recommendation Pipeline**

```
User plays song → Get embedding →
  ↓
Find 100 similar songs (Vector DB) →
  ↓
Filter by user preferences (MongoDB):
  - Exclude explicit content
  - Match preferred genres
  - Recency bias (recent songs ranked higher) →
  ↓
Re-rank by popularity/freshness →
  ↓
Return top 20 recommendations
```

---

**Optimization Techniques:**

**1. Pre-filtering vs Post-filtering:**

**Pre-filtering (recommended):**
```python
# Filter candidates first, then similarity search
similar = vector_db.query(
    vector=emb,
    filter={"genre": "rock"}  # Vector DB does filtering
)
```

**Post-filtering:**
```python
# Get similar, then filter
similar = vector_db.query(vector=emb, top_k=100)
filtered = [s for s in similar if s.metadata['genre'] == 'rock']
```

**Trade-off:**
- Pre-filtering: Faster, but requires metadata in vector DB
- Post-filtering: More flexible, but wasteful

---

**2. Caching:**

```python
# Cache popular song recommendations
import redis

redis_client = redis.Redis()

def get_recommendations(song_id):
    # Check cache
    cached = redis_client.get(f"rec:{song_id}")
    if cached:
        return json.loads(cached)

    # Compute recommendations
    recs = compute_recommendations(song_id)

    # Cache for 1 hour
    redis_client.setex(
        f"rec:{song_id}",
        3600,
        json.dumps(recs)
    )

    return recs
```

---

**3. Sharding:**

For very large catalogs (>100M songs):

**Partition by genre:**
- Create separate vector indices per genre
- Rock index, Pop index, Classical index
- Query only relevant genre index

**Partition by popularity:**
- Hot index: Popular songs (fast, in-memory)
- Cold index: Rare songs (disk-based, slower)

---

**Summary:**

**Storage:**
- Embeddings → Vector DB (Pinecone/Milvus)
- Metadata → Document DB (MongoDB)

**Indexing:**
- HNSW index for embeddings (cosine similarity)
- B-tree indices on genre, artist, year in MongoDB
- Text index for song/artist search

**Retrieval:**
- Hybrid search: Pre-filter with metadata, then similarity search
- Cache popular recommendations
- Shard by genre for very large datasets

**Result:** Fast (<50ms), accurate recommendations with rich filtering

---

## End of Solutions

**Summary:**
- **Question 1 (20 marks):** Linear Algebra - adjacency matrices, transitions, steady state, SVD, pseudo-inverse
- **Question 2 (20 marks):** Optimization - normal equations, gradient descent, SGD, Lagrange multipliers
- **Question 3 (20 marks):** Probabilities - normal distributions, GMM, parameter estimation, Bayesian inference
- **Question 4 (20 marks):** Databases - block calculations, join cardinality, vector databases, music streaming

**Total: 80 marks**

---

**Prepared by: AI Assistant**
**Date: November 25, 2025**
**For: IDSS 2024-2025 Examination**
