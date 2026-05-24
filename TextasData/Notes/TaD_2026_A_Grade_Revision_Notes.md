# Text as Data 2026 — A-Grade Revision Notes
**Module:** COMPSCI 5096/5106 | University of Glasgow
**Exam format:** Open book, online, 1h30m, 3 questions × 20 marks = 60 marks total
**Lecturers:** Sean MacAvaney & Jake Lever

> **How to use these notes:** Each topic has (1) core theory, (2) at least one worked example, (3) common pitfalls, and (4) model answers for repeated exam questions. The "Exam-style Q&A" boxes are A-grade templates — practise reproducing them in your own words.

---

## Table of Contents

1. [Tokens & Document Similarity](#1-tokens--document-similarity)
2. [Vectors, TF-IDF & Clustering](#2-vectors-tf-idf--clustering)
3. [Language Modelling](#3-language-modelling)
4. [Text Classification](#4-text-classification)
5. [Contextual Word Embeddings & Transformers](#5-contextual-word-embeddings--transformers)
6. [POS Tagging & Parsing](#6-pos-tagging--parsing)
7. [Ethics in NLP](#7-ethics-in-nlp)
8. [Information Extraction](#8-information-extraction)
9. [Large Language Models](#9-large-language-models)
10. [Latest Research (RAG, Tool Use, Agentic AI)](#10-latest-research)
11. [Exam Strategy & Time Management](#11-exam-strategy)

---

# 1. Tokens & Document Similarity

## 1.1 The NLP Pipeline

Standard preprocessing pipeline:

1. **Data Cleaning** — strip HTML, links, boilerplate, tables
2. **Tokenisation** — split text into tokens (and often sentences)
3. **Normalisation** — reduce variation:
   - **Case folding** ("Textile" → "textile")
   - **Stemming** — rule-based suffix stripping ("running" → "run"). Fast, crude.
   - **Lemmatisation** — dictionary lookup to base form ("better" → "good"). Slower, accurate.
4. **Stopword removal** — drop high-frequency low-info words ("the", "is", "of")

**Key principle:** every step is a *choice*. Justify it for the application.

### A-grade reasoning template
> "For [task], I would/wouldn't use [step] because [task-specific consequence]. For example, [concrete example from the domain]."

## 1.2 Encodings

| Encoding | Bytes per char | Coverage |
|---|---|---|
| ASCII | 1 byte | 128 chars (English + symbols) |
| Unicode (UTF-8) | 1–4 bytes (variable) | 150,000+ chars (all world scripts, emojis, maths) |

**Key fact for exam:** Unicode is **variable-length** (1–4 bytes per character). UTF-8 encodes ASCII chars in 1 byte but Chinese chars in 3, emojis in 4.

## 1.3 Tokenisation Approaches

| Method | How it works | Strength | Weakness |
|---|---|---|---|
| Whitespace | split on spaces | trivial | fails on punctuation, no-space languages (Chinese, Japanese), contractions |
| Rule-based (regex) | hand-crafted patterns | precise, interpretable | brittle, language-specific, can't handle unseen words |
| Subword (BPE, WordPiece, SentencePiece) | learned from corpus | handles OOV, multilingual, compact vocab | needs training data, can split meaningfully different words |

### Exam-style Q&A: word vs token (2023 Q1a)
> **Q:** What is the difference between a word and a token? Why do text processing systems usually operate over tokens instead of words?
>
> **A:** A *word* is a linguistic unit defined by meaning and orthography (e.g. "don't", "São Paulo"). A *token* is an algorithmically-produced unit — what comes out of the tokeniser — which may be a word, subword, punctuation mark, or symbol. Systems operate over tokens because (1) tokens are unambiguous and reproducible by code, (2) subword tokenisers handle unseen words gracefully, and (3) tokens align with the units the downstream model was trained on.

### Exam-style Q&A: why tokenisers differ across languages (2023 Q1b)
> **Q:** Why do tokenisers differ across languages? Give an example.
>
> **A:** Languages have different orthographic conventions. (1) Chinese, Japanese, and Thai have no spaces between words, so whitespace tokenisation fails entirely. (2) German compounds words ("Donaudampfschifffahrtsgesellschaft") — an English tokeniser would treat this as one token, losing semantic structure. (3) Arabic and Hebrew use clitics attached to roots that should be split off. An English tokeniser applied to Chinese would treat an entire sentence as a single token.

## 1.4 Set Similarity Measures

Given documents as sets of tokens X and Y:

| Measure | Formula | Range |
|---|---|---|
| Overlap count | \|X ∩ Y\| | [0, min(\|X\|,\|Y\|)] |
| Overlap Coefficient | \|X ∩ Y\| / min(\|X\|, \|Y\|) | [0, 1] |
| Sørensen–Dice | 2·\|X ∩ Y\| / (\|X\| + \|Y\|) | [0, 1] |
| Jaccard | \|X ∩ Y\| / \|X ∪ Y\| | [0, 1] |

**Relationship:** similarity(X, Y) ∝ −distance(X, Y). Convert similarity to distance via `d = 1 - sim`.

### Worked Example: Set similarity calculation

**Recipe A** = {tomato, onion, garlic, basil, salt, olive_oil} → \|A\| = 6
**Recipe B** = {tomato, garlic, oregano, salt, olive_oil, pepper, chilli} → \|B\| = 7

- Intersection: {tomato, garlic, salt, olive_oil} → \|A ∩ B\| = 4
- Union: {tomato, onion, garlic, basil, salt, olive_oil, oregano, pepper, chilli} → \|A ∪ B\| = 9

Calculations:
- **Overlap** = 4 / min(6, 7) = 4/6 = **0.667**
- **Dice** = 2·4 / (6+7) = 8/13 = **0.615**
- **Jaccard** = 4/9 = **0.444**

**Sanity check:** Overlap ≥ Dice ≥ Jaccard always (because denominators grow).

## 1.5 Properties of a Metric (Distance Function)

A function d is a **metric** if it satisfies ALL four:

1. **Identity:** d(X, X) = 0
2. **Positivity:** d(X, Y) > 0 when X ≠ Y
3. **Symmetry:** d(X, Y) = d(Y, X)
4. **Triangle inequality:** d(X, Z) ≤ d(X, Y) + d(Y, Z)

- **Semi-metric** = violates triangle inequality (e.g. 1 − Dice)
- **Pseudo-metric** = violates positivity (d(X,Y) = 0 possible even when X ≠ Y)

### Worked Example: Proving Dice is a semi-metric (2022 Q2d style)

Construct three sets where 1 − Dice violates triangle inequality:

Let A = {a, b}, B = {b, c}, C = {a, c}

- Dice(A, B) = 2·1 / (2+2) = 0.5 → distance = 0.5
- Dice(A, C) = 2·1 / (2+2) = 0.5 → distance = 0.5
- Dice(B, C) = 2·1 / (2+2) = 0.5 → distance = 0.5

Triangle inequality requires d(A,C) ≤ d(A,B) + d(B,C) → 0.5 ≤ 1.0 ✓ (holds here)

**Stronger counter-example** (from 2022 paper):

A = {a, eda, bceda, bcda, bce} (\|A\| = 5)
B = {ca, eda, bcba, bceda, eda, bce} → unique: {ca, eda, bcba, bceda, bce} (\|B\| = 5)
C = {beda, bceda, bceca, ebeda, b} (\|C\| = 5)

- A ∩ B = {eda, bceda, bce} = 3 → Dice(A,B) = 6/10 = 0.6 → d=0.4
- A ∩ C = {bceda} = 1 → Dice(A,C) = 2/10 = 0.2 → d=0.8
- B ∩ C = {bceda} = 1 → Dice(B,C) = 2/10 = 0.2 → d=0.8

Triangle inequality check: d(A,C) ≤ d(A,B) + d(B,C) → 0.8 ≤ 0.4 + 0.8 ✓ (holds)

Try: d(B,C) ≤ d(B,A) + d(A,C) → 0.8 ≤ 0.4 + 0.8 ✓

Often you need to search more aggressively for a violation. **Key insight for exam:** the property *can* be violated for sufficiently dissimilar sets, even if your first example doesn't show it.

### Exam-style Q&A: 3 problems with a similarity measure (2025 Q1e)

> Generic answer template — adapt to the specific measure given:
>
> 1. **Range / direction confusion** — does it return higher for more similar, or for more distant? Make this explicit.
> 2. **Symmetry** — does sim(A,B) = sim(B,A)? Asymmetric measures cause downstream issues.
> 3. **Division by zero** — what happens when one set is empty, or A ∩ B = ∅?
> 4. **Triangle inequality** — does it form a true metric? If not, you can't use efficient indexing structures (e.g. metric trees).
> 5. **Unbounded values** — is there an upper bound, or could it return arbitrarily large numbers?
> 6. **Sensitivity to set size** — does it score short documents unfairly?

## 1.6 Regular Expressions Quick Reference

| Pattern | Meaning |
|---|---|
| `.` | any character |
| `[abc]` | one of a, b, c |
| `[^abc]` | any char except a, b, c |
| `[a-z]` | range |
| `\d` `\w` `\s` | digit, word char, whitespace |
| `\D` `\W` `\S` | negated versions |
| `*` `+` `?` | 0+, 1+, 0 or 1 |
| `^` `$` | start/end of string |
| `\b` | word boundary |

## 1.7 N-grams

An **n-gram** is a contiguous sequence of n items (chars or tokens) from text.

**Theoretical max n-grams** for alphabet size A and text length L:
- If A^n ≤ L − n + 1: max = A^n (limited by alphabet)
- If A^n > L − n + 1: max = L − n + 1 (limited by text length)

### Worked Example: Theoretical max n-grams (2022 Q2b)

Alphabet = 5 chars (a, b, c, d, e), text length L = 593:

| n | A^n | L−n+1 | max |
|---|---|---|---|
| 1 | 5 | 593 | 5 (alphabet-limited) |
| 2 | 25 | 592 | 25 |
| 3 | 125 | 591 | 125 |
| 4 | 625 | 590 | 590 (text-limited, since 625 > 590) |
| 5 | 3125 | 589 | 589 |

**Key insight:** as n grows, you flip from alphabet-limited to text-limited.

---

# 2. Vectors, TF-IDF & Clustering

## 2.1 Term Frequency Variants

| Method | Formula |
|---|---|
| Raw TF | tf(t,d) = count of t in d |
| Log-transformed TF | 1 + log₁₀(tf) if tf > 0, else 0 |
| IDF | log(N / df(t)), where N = total docs, df = docs containing t |
| TF-IDF | (1 + log(tf)) · log(N / df) |

**Why log on TF?** Diminishing returns — the 100th occurrence of "the" shouldn't count 100× more than the 1st.

**Why IDF?** Down-weight common words (stopwords get IDF ≈ 0), boost rare-but-meaningful words.

## 2.2 Zipf's Law

In any natural language corpus, word frequency is inversely proportional to rank:

```
frequency(rank) ∝ 1 / rank
```

The most common word is roughly twice as frequent as the 2nd, 3× as frequent as the 3rd, etc. Practical implication: a tiny set of stopwords dominate any text; the vast majority of vocabulary is rare.

## 2.3 Worked Example: Build TF-IDF vector (2025 Q1a style)

**Vocabulary with IDFs:**

| Token | A | B | C | D | E | F | G | H | I | J |
|---|---|---|---|---|---|---|---|---|---|---|
| IDF | 2 | 4 | 1 | 3 | 6 | 4 | 1 | 3 | 3 | 5 |

**Document:** `G C G A H A G`

Step 1 — Count tokens:
- A: 2, C: 1, G: 3, H: 1 (others: 0)

Step 2 — Apply TF × IDF (using *linear* TF as specified):
- A: 2 × 2 = 4
- B: 0
- C: 1 × 1 = 1
- D: 0
- E: 0
- F: 0
- G: 3 × 1 = 3
- H: 1 × 3 = 3
- I: 0
- J: 0

**Vector:** [4, 0, 1, 0, 0, 0, 3, 3, 0, 0]

### Reverse direction: reconstruct doc from TF-IDF (2025 Q1b style)

Given `[6, 8, 0, 6, 6, 0, 2, 3, 3, 10]` and IDFs above:

| Token | TF-IDF | IDF | Count = TF-IDF / IDF |
|---|---|---|---|
| A | 6 | 2 | 3 |
| B | 8 | 4 | 2 |
| C | 0 | 1 | 0 |
| D | 6 | 3 | 2 |
| E | 6 | 6 | 1 |
| F | 0 | 4 | 0 |
| G | 2 | 1 | 2 |
| H | 3 | 3 | 1 |
| I | 3 | 3 | 1 |
| J | 10 | 5 | 2 |

**Tokens (multiset):** A A A B B D D E G G H I J J
**Ambiguity:** Word order is lost — could be any permutation.

## 2.4 Vector Similarity (Geometric)

For dense vectors x⃗, y⃗ of length n:

**Euclidean distance:**
```
d(x⃗, y⃗) = √(Σᵢ(xᵢ − yᵢ)²)
```

**Cosine similarity:**
```
cos(θ) = (x⃗ · y⃗) / (‖x⃗‖ · ‖y⃗‖)
```

| | Euclidean | Cosine |
|---|---|---|
| Returns | distance (0 = same) | similarity (1 = same direction) |
| Sensitive to magnitude? | Yes | No (length-normalised) |
| Best for | when magnitudes are meaningful | text (where doc length shouldn't matter) |

### Worked Example: Cosine similarity

x⃗ = [3, 4], y⃗ = [4, 3]

- Dot product: 3·4 + 4·3 = 24
- ‖x⃗‖ = √(9+16) = 5
- ‖y⃗‖ = √(16+9) = 5
- cos(θ) = 24 / (5·5) = 0.96

## 2.5 K-Means Clustering (DUE for first appearance!)

**Goal:** partition data into k clusters by minimising within-cluster distance.

**Algorithm:**
- **Step 0:** Initialise k centroids
- **Step 1:** Assign each point to its nearest centroid
- **Step 2:** Recompute each centroid as the mean of its assigned points
- Repeat 1–2 until convergence (assignments stop changing)

### Initialisation methods

| Method | How |
|---|---|
| **Random selection** | Pick k random points from the data as centroids |
| **Forgy partition** | Same as above (alternative name) |
| **Random Partition** | Randomly assign each point to a cluster, compute centroid from each |
| **k-means++** | Pick centroids that are far apart from each other (better convergence) |

**Why initialisation matters:** K-means is sensitive to initialisation — can converge to local minima. Run multiple times and pick the best.

### Choosing k: the Elbow Method

Plot the **within-cluster sum of squares (WCSS)** for k = 1, 2, 3, ... Look for the "elbow" where additional clusters give diminishing returns.

### Measuring Clustering Quality

**Intrinsic (no labels needed):**

| Metric | Formula | Interpretation |
|---|---|---|
| **Cohesion(i)** | avg distance of i to other points in *same* cluster | low = tight cluster |
| **Separation(i)** | min(avg distance of i to points in *another* cluster) | high = well-separated |
| **Silhouette(i)** | piecewise (see below) | range [−1, 1], higher = better |

**Silhouette formula:**
```
silhouette(i) = 1 − cohesion/separation,   if cohesion < separation
              = 0,                          if cohesion = separation
              = separation/cohesion − 1,   if cohesion > separation
```

**Interpretation:**
- Close to **+1**: point is well-clustered
- Close to **0**: point is on the border
- Close to **−1**: point may be in the wrong cluster

**Extrinsic:** clustering is part of a larger task — judge by downstream performance (e.g. classification accuracy).

### Worked Example: K-Means iteration

**Data:** points at (1,1), (1,2), (5,4), (6,5)
**Initial centroids:** C1 = (1,1), C2 = (5,4)

**Iteration 1:**
- (1,1): dist to C1 = 0, dist to C2 = √(16+9)=5 → C1
- (1,2): dist to C1 = 1, dist to C2 = √(16+4)=4.47 → C1
- (5,4): dist to C1 = 5, dist to C2 = 0 → C2
- (6,5): dist to C1 = √(25+16)=6.4, dist to C2 = √(1+1)=1.41 → C2

New centroids: C1 = mean of (1,1),(1,2) = (1, 1.5); C2 = mean of (5,4),(6,5) = (5.5, 4.5)

**Iteration 2:** assignments unchanged → converged.

### Exam-style Q&A: When does K-Means struggle?

> 1. **Non-spherical clusters** — assumes Euclidean distance gives round clusters; fails on elongated/curved shapes (use DBSCAN instead).
> 2. **Different cluster sizes/densities** — tends to produce equal-sized clusters.
> 3. **Outliers** — pull centroids; use median (K-medoids) instead.
> 4. **Wrong k** — must be chosen ahead of time; use elbow or silhouette.
> 5. **High-dimensional data** — curse of dimensionality flattens distances.

---

# 3. Language Modelling

## 3.1 Probability Foundations

- Range: 0 ≤ P(x) ≤ 1, and Σ P(x) = 1
- **Bayes' rule:** P(A|B) = P(B|A)·P(A) / P(B)
- **Chain rule:** P(A,B,C) = P(A|B,C)·P(B|C)·P(C)
- **Independence:** P(A|B) = P(A) and P(B|A) = P(B)

## 3.2 Language Models

**Goal:** estimate P(w₁, w₂, ..., wₙ) — the probability of a sequence — or equivalently, P(wₖ₊₁ | w₁...wₖ) — the probability of the next word.

**Direct counting** is hopeless for long sequences (no corpus is big enough). So we use the **Markov assumption**:

```
P(wᵢ | w₁...wᵢ₋₁) ≈ P(wᵢ | wᵢ₋ₙ₊₁...wᵢ₋₁)
```

— only the previous n−1 tokens matter.

| n | Name | What it conditions on |
|---|---|---|
| 1 | unigram | nothing |
| 2 | bigram | previous 1 token |
| 3 | trigram | previous 2 tokens |

**Trade-off:**
- Small n: high-bias (ignores context), low-variance (good counts)
- Large n: low-bias (rich context), high-variance (sparse counts, many zeros)

## 3.3 Smoothing

**Why smooth?** If a bigram never appears in training, MLE gives P = 0 — which zeroes out the whole sequence probability.

**Add-k smoothing (Laplace if k=1):**
```
P_add-k(t | θ) = (count(t,θ) + k) / (Σ_t' count(t',θ) + k·|V|)
```

**Interpolation:** mix n-gram models of different orders
```
P_interp(tᵢ|tᵢ₋₁,tᵢ₋₂) = λ₁·P(tᵢ|tᵢ₋₁,tᵢ₋₂) + λ₂·P(tᵢ|tᵢ₋₁) + λ₃·P(tᵢ)
```
where λ₁+λ₂+λ₃ = 1.

**Jelinek-Mercer (smoothing with collection):**
```
P_JM(t | θ_d, θ_c) = λ·P(t|θ_d) + (1−λ)·P(t|θ_c)
```
where θ_d is the document model and θ_c the collection model.

### Exam-style Q&A: Why smoothing? (2023 Q2c)

> **A:** Without smoothing, any unseen n-gram in test data gets probability 0, which propagates: a single zero zeroes out the entire sequence probability (and gives infinite perplexity). Smoothing redistributes a small amount of probability mass to unseen events.
>
> **Which values benefit most?** Cells with very low or zero counts — the rare or unseen transitions.
>
> **Negatives of too much smoothing:** flattens the distribution, washing out the actual signal — frequent patterns get under-weighted, rare events get over-weighted. The model loses discriminative power.

## 3.4 LM Evaluation

**Intrinsic:** evaluate the LM directly
- **Perplexity** — how surprised the model is by held-out data; lower = better
- **Cross-entropy** — average negative log probability
- **Entropy** — uncertainty in the distribution

**Extrinsic:** plug LM into a downstream task (machine translation, speech recognition) and measure that.

**Formulas:**
```
Cross-entropy: H = −(1/n)·Σ log₂ P(wᵢ)
Perplexity:    PP = 2^H = (Π P(wᵢ))^(−1/n)
```

### Worked Example: Perplexity calculation (2023 Q2a style)

Sequence: `<S> a b b a <E>` (5 transitions)

**Model X probabilities:**
- P(a|<S>) = 0.1
- P(b|a) = 0.3
- P(b|b) = 0.4
- P(a|b) = 0.3
- P(<E>|a) = 0.5

Sequence probability:
```
P = 0.1 × 0.3 × 0.4 × 0.3 × 0.5 = 0.0018
```

Per-token probability (5 transitions):
```
Perplexity_X = (0.0018)^(−1/5) = (1/0.0018)^(1/5)
             = 555.56^0.2 ≈ 3.51
```

**Model Y probabilities:**
- P(a|<S>) = 0.3
- P(b|a) = 0.1
- P(b|b) = 0.6
- P(a|b) = 0.3
- P(<E>|a) = 0.1

```
P = 0.3 × 0.1 × 0.6 × 0.3 × 0.1 = 0.00054
Perplexity_Y = (0.00054)^(−1/5) ≈ 4.55
```

**Conclusion:** Model X represents the sequence better (perplexity 3.51 < 4.55). Lower perplexity = the model is *less surprised* by the data.

## 3.5 Text Generation

| Method | How |
|---|---|
| **Greedy** | At each step, pick highest-probability token |
| **Sampling** | Sample from the distribution |
| **Beam search** | Keep top-k partial sequences at each step |
| **Top-k** | Sample only from top k tokens |
| **Top-p (nucleus)** | Sample from smallest set with cumulative probability ≥ p |
| **Contrastive search** | Penalise similarity to already-generated tokens |

**Greedy** = boring, repetitive, deterministic.
**Sampling** = diverse but can be incoherent.
**Beam search** = good for tasks with one "correct" answer (translation, summarisation).

### Worked Example: Beam search with b=2 (2023 Q2b style)

**Setup:** prefix `<S> a c`, beam width = 2. Extend each beam with the top 2 most-likely tokens.

**Model X transitions from c:**
- P(a|c) = 0.1, P(b|c) = 0.6, P(c|c) = 0.2, P(<E>|c) = 0.1

**Step 1** — Extend `<S> a c` with top-2 next tokens:
- Top 2: b (0.6), c (0.2)
- Beam 1: `<S> a c b` with prob = 0.6
- Beam 2: `<S> a c c` with prob = 0.2

**Step 2** — Extend each beam:

From `<S> a c b` (transitions from b):
- P(a|b)=0.3, P(b|b)=0.4, P(c|b)=0.2, P(<E>|b)=0.1
- Top 2: b (0.4), a (0.3)
- → `<S> a c b b` = 0.6·0.4 = 0.24
- → `<S> a c b a` = 0.6·0.3 = 0.18

From `<S> a c c`:
- Top 2 from c: b (0.6), c (0.2)
- → `<S> a c c b` = 0.2·0.6 = 0.12
- → `<S> a c c c` = 0.2·0.2 = 0.04

**Keep top 2 across all candidates:** `<S> a c b b` (0.24), `<S> a c b a` (0.18)

**Comparison with greedy:** Greedy would pick b → b → b (always highest), giving `<S> a c b b b...`. Beam search keeps multiple options open and can recover from a suboptimal early choice.

### Worked Example: Greedy generation (2024 Q2 style)

**Text:** BCBBCBBABCCCBBCCBCCB (20 chars)

**Unigram counts:**
- A: 1, B: 11, C: 8

**Unigram greedy** picks the highest-probability token at every step → next 3 tokens: `B B B`

**Bigram counts (sliding window):**
- BC: 5, CB: 5, BB: 4, CC: 2, BA: 1, AB: 1

From last character `B`:
- P(C|B) = 5/(5+4+1) = 5/10 = 0.5
- P(B|B) = 4/10 = 0.4
- P(A|B) = 1/10 = 0.1

Greedy bigram → C. Then from C:
- P(B|C) = 5/(5+2) = 0.71
- P(C|C) = 2/7 = 0.29

Greedy → B. Then from B → C again.

**Next 3 tokens (greedy bigram): C B C**

### Worked Example: Sequence a bigram CAN'T generate (2024 Q2d)

Given the same text, the bigram model has only seen these transitions: B→C, C→B, B→B, C→C, B→A, A→B.

A sequence the bigram **cannot** generate: `AA` — because P(A|A) = 0 (never seen "AA" in training).

**Fix:** apply **add-k smoothing** so every transition gets a small non-zero probability. Use sampling (instead of greedy) so the smoothed low-probability transition can occasionally be selected.

---

# 4. Text Classification

## 4.1 Problem Types

| Type | Definition | Example |
|---|---|---|
| **Binary** | 2 mutually exclusive labels | spam / not spam |
| **Multi-class** | >2 mutually exclusive labels | news topic (sport / politics / tech) |
| **Multi-label** | document can have multiple labels | movie genres (action AND comedy) |

**Common error in exam answers:** confusing multi-class with multi-label. If a recipe could be both "Italian" AND "pasta", it's multi-label, NOT multi-class.

## 4.2 Confusion Matrix & Binary Metrics

|  | Predicted +ve | Predicted −ve |
|---|---|---|
| **Actual +ve** | TP | FN |
| **Actual −ve** | FP | TN |

| Metric | Formula | When it matters |
|---|---|---|
| **Accuracy** | (TP+TN)/(TP+FP+TN+FN) | balanced classes |
| **Precision** | TP/(TP+FP) | when FP is costly (e.g. spam filter) |
| **Recall (Sensitivity)** | TP/(TP+FN) | when FN is costly (e.g. cancer screening) |
| **F1** | 2·P·R / (P+R) | balance precision and recall |
| **Fβ** | (1+β²)·P·R / (β²·P+R) | weight recall (β>1) or precision (β<1) |

**Key intuitions:**
- High accuracy can be misleading with class imbalance (90% accuracy on 99/1 split is worse than random)
- F1 is the harmonic mean of P and R — penalises imbalance between them
- F1 always lies between P and R (handy sanity check)

## 4.3 Multi-Class Metrics

Three ways to average per-class metrics:

| Method | How | When to use |
|---|---|---|
| **Macro** | unweighted mean across classes | when all classes matter equally |
| **Weighted** | mean weighted by class support | reflects overall performance with class imbalance |
| **Micro** | pool TP/FP/TN/FN across classes, then compute | overall granular performance |

For multi-class accuracy: simply correct / total.

## 4.4 ROC Curve & AUROC

- Plot True Positive Rate (recall) vs False Positive Rate
- Start bottom-left, traverse ordered predictions:
  - Actual +ve → move UP
  - Actual −ve → move RIGHT
- **AUROC** = area under curve; 1.0 = perfect, 0.5 = random, <0.5 = worse than random

## 4.5 Train/Validation/Test & Cross-Validation

- **Training set** — learn parameters
- **Validation/Dev set** — tune hyperparameters, choose model
- **Test set** — final evaluation, touched ONCE

**K-fold cross-validation:** split data into k folds; train on k−1, validate on the remaining one, rotate. Use when dataset is small.

## 4.6 Classifier Problems

| Problem | Symptom | Fix |
|---|---|---|
| **Noisy labels** | low train AND test performance | clean data, use robust loss |
| **Noisy features** | inconsistent performance | feature selection, denoising |
| **Missing features** | features can't separate classes | feature engineering, richer representations |
| **Underfitting** | low train AND test | more capacity (deeper/wider model) |
| **Overfitting** | high train, low test | regularisation, dropout, more data, early stopping |
| **Class imbalance** | model predicts majority class | resampling (SMOTE), class weights, F1 instead of accuracy |

### Exam-style Q&A: Interpret train vs test metrics (2022 Q3d / 2025 Q2c)

> Given a table of precision/recall on train and test:
>
> 1. **Overfitting** — System B's train metrics (0.67/0.48) are much higher than test (0.51/0.42). The model memorised training peculiarities that don't generalise.
> 2. **Generalisation** — System A has similar train and test scores (0.62/0.43 train, 0.58/0.51 test) — it generalises well, only modestly above baseline but the improvement is significant on the test set.
> 3. **Statistical significance** — only test-set significance matters for deployment decisions. System A is significantly better than baseline on test; System B is not (drops below baseline).
> 4. **Recommendation:** prefer System A — modest gains that hold up out-of-sample.

### Exam-style Q&A: 4 effects of triplicated training data (2025 Q2b)

> **A:**
> 1. **Class imbalance** — the triplicated class becomes 3× more common, skewing the prior.
> 2. **Biased training** — the model over-focuses on patterns in that class, hurting performance on others.
> 3. **Test set leakage** — if duplicates ended up in both train and test, evaluation metrics are inflated and meaningless.
> 4. **Unrealistic class distribution** — metrics won't reflect real-world performance because the test split doesn't match production distribution.

### Exam-style Q&A: Anomalies in metrics table (2025 Q2c)

> Standard anomalies to scan for:
> 1. **Wrong metric for the task** (perplexity is for LMs, not classification)
> 2. **Class count mismatch** between train and validation
> 3. **Numbers in confusion matrix don't sum to stated total**
> 4. **Sample counts inconsistent** with confusion matrix
> 5. **Class distribution flipped** between train and validation
> 6. **Validation set larger than training set** (against best practice)
> 7. **F1 outside [min(P,R), max(P,R)]** range (impossible)
> 8. **Macro precision on binary problems** (should just be precision)
> 9. **Train performance worse than validation** (suspicious — should be opposite or close)
> 10. **Perfect validation scores** (suggests data leakage)

---

# 5. Contextual Word Embeddings & Transformers

## 5.1 Three Types of Word Vectors

| Type | Example | Length | Handles synonymy? | Handles polysemy? |
|---|---|---|---|---|
| **Static sparse** | IBM model (context counts) | vocab size | ✓ | ✗ |
| **Static dense** | word2vec, GloVe, SVD | ~100–1000 | ✓ | ✗ |
| **Contextual dense** | ELMo, BERT, GPT | ~768 | ✓ | ✓ |

**Synonymy:** "car" ≈ "automobile" (different words, same meaning)
**Polysemy:** "bank" = riverbank OR financial institution (same word, different meanings)

**Why static fails polysemy:** one vector per word averages ALL meanings, giving a vector that's near nothing in particular.

### Exam-style Q&A: Word2vec on polysemous words (2022 Q1f)

> **Q:** What would you expect as nearest neighbours of "jaguar", "bank", or "python"? What's the problem for downstream tasks?
>
> **A:** Nearest neighbours would be a mix of senses — "jaguar" might cluster near "lion" AND "Ford" AND "Apache" (animal, car, helicopter). The vector becomes a meaningless average of unrelated meanings.
>
> **Downstream problem:** For text classification, a sentence's bag-of-vectors representation gets dominated by these ambiguous high-magnitude vectors that don't reflect the actual sense in context. The classifier can't distinguish "I deposited money at the bank" from "I sat by the river bank". Solution: use contextual embeddings (BERT) that produce different vectors for different uses.

### Exam-style Q&A: Why are function-word vectors unreliable? (2022 Q1d)

> **A:** Function words like "the", "of", "is" co-occur with virtually every content word. Their context vectors are flat distributions over the entire vocabulary — every dimension has a similar value. This means:
> 1. They have low information content for distinguishing meanings
> 2. Their cosine similarity to most other words is uniformly moderate
> 3. They drown out signal in bag-of-vectors representations
>
> Example: "the" appears next to "cat", "dog", "house", "philosophy"... so its vector is essentially the average of all word contexts — meaningless.

## 5.2 Self-Attention

The mechanism that lets a transformer build context-aware vectors.

**Inputs:** Query (Q), Key (K), Value (V) matrices — each obtained by multiplying input vectors by learned weight matrices:
```
Q = X · W_Q
K = X · W_K
V = X · W_V
```

**Attention formula:**
```
Attention(Q, K, V) = softmax(Q · K^T / √d_k) · V
```

**Intuition:**
- Q asks "what am I looking for?"
- K answers "what do I contain?"
- V provides "the actual content"
- Q · K^T computes similarity (how much each token attends to each other token)
- Softmax normalises to weights
- Weighted sum of V gives the contextual representation

**Multi-head attention:** do attention multiple times in parallel (different W matrices each time) — captures different relationships.

## 5.3 BPE (Byte Pair Encoding) — CRITICAL TOPIC

**Why BPE?** Handles open vocabulary (unseen words), keeps vocab compact, language-agnostic.

### Training Algorithm
1. **Pre-tokenise** corpus into words (whitespace + punctuation rules) — *this removes whitespace*
2. **Initial vocab** = all unique characters in the corpus
3. **Repeat until target vocab size:**
   - Find the most frequent adjacent symbol pair in the corpus
   - Add the merged pair as a new symbol to the vocab
   - Replace all occurrences in the corpus

### Inference (applying learned BPE rules)
1. Pre-tokenise the input
2. For each word, split into characters
3. Apply learned merge rules in order (greedily, repeatedly)
4. Output the resulting subwords

### Worked Example: Training BPE for "mississippi is pie" (2023 Q1c style)

**Target vocab size: 8**

Pre-tokenise → words: [mississippi, is, pie]

Initial vocab = {m, i, s, p, e} (5 symbols)

**Iteration 1:** count adjacent pairs across all words:
- mississippi: (m,i), (i,s), (s,s), (s,i), (i,s), (s,s), (s,i), (i,p), (p,p), (p,i)
- is: (i,s)
- pie: (p,i), (i,e)

Most common: **(i,s) = 3 occurrences** → new symbol "is", vocab = {m, i, s, p, e, is} (6)

Update corpus: m-is-s-is-s-i-p-p-i, is, p-i-e

**Iteration 2:** count pairs again:
- m-is-s-is-s-i-p-p-i: (m,is), (is,s), (s,is), (is,s), (s,i), (i,p), (p,p), (p,i)
- is: (no pairs, single token)
- p-i-e: (p,i), (i,e)

Most common: **(p,i) = 2** → new symbol "pi", vocab = {m, i, s, p, e, is, pi} (7)

Update: m-is-s-is-s-i-p-pi, is, pi-e

**Iteration 3:** vocab needs to reach 8. Count pairs:
- (m,is)=1, (is,s)=2, (s,is)=1, (s,i)=1, (i,p)=1, (p,pi)=1, (pi,e)=1

Most common: **(is,s) = 2** → new symbol "iss", vocab = {m, i, s, p, e, is, pi, iss} (8) ✓ STOP

**Learned merge rules (in order):**
1. (i,s) → is
2. (p,i) → pi
3. (is,s) → iss

### Worked Example: Applying BPE rules (2024 Q1c style)

**Rules (in order):**
```
i, s    → is
p, i    → pi
i, e    → ie
p, ie   → pie
p, pi   → ppi
si, ppi → sippi
```

**Tokenise:** `mississippi pie`

After pre-tokenisation: [mississippi, pie]

**Word 1: mississippi → [m, i, s, s, i, s, s, i, p, p, i]**

Apply rule (i,s)→is:
- positions 1-2, 4-5, 6-7 → [m, is, s, is, s, is, p, p, i]
- Wait, after merging (i,s) at position 1-2, we get [m, is, s, i, s, s, i, p, p, i]
- Continue scanning: position 3-4 is (s,i) — not "is" rule
- Position 4-5 is (i,s) → merge → [m, is, s, is, s, i, p, p, i]
- Continue scanning from position 4 onward: position 5-6 is (s,i), not is. Position 6-7 is (i,p) — no rule yet
- Apply rule (p,i)→pi: position 9-10 is (p,i) → [m, is, s, is, s, i, p, pi]
- Apply rule (p,pi)→ppi: positions 7-8 (p, pi) → [m, is, s, is, s, i, ppi]
- Apply rule (si,ppi)→sippi: position 5-6 is (i, ppi) — not (si, ppi). But position 4-5 is (s, i)... no. We need adjacent (si, ppi). There's no "si" merged yet.

Hmm, looking again — we don't have rule for s,i→si in this list. Let me re-trace:

Actually re-reading: there's no (s,i)→si rule. So the rule (si, ppi)→sippi requires "si" to already exist as a token. It won't fire.

Final result for `mississippi`: **[m, is, s, is, s, i, ppi]**

**Word 2: pie → [p, i, e]**

Apply rule (i,s)→is: no "i,s" here. Skip.
Apply rule (p,i)→pi: position 0-1 → [pi, e]
Apply rule (i,e)→ie: no (i,e) adjacent now. Skip.
Apply rule (p,ie)→pie: no (p,ie). Skip.

Final result for `pie`: **[pi, e]**

**Combined output:** [m, is, s, is, s, i, ppi, pi, e]

**Exam tip:** apply rules **in order**, **greedily**, and **repeat** until no rule fires on a pass.

### Exam-style Q&A: BPE vs rule-based, advantages each way (2023 Q1d)

> **BPE advantages over rule-based:**
> 1. **Handles out-of-vocabulary words** by decomposing into known subwords — no [UNK] needed for novel words.
> 2. **Language-agnostic** — learns directly from data, works on any language without hand-crafting rules.
> 3. **Compact vocabulary** — fixed size means smaller embedding matrices.
> 4. **Captures morphological structure** — affixes like "ing", "tion" often emerge naturally.
>
> **Rule-based advantages over BPE:**
> 1. **Interpretable and predictable** — you know exactly why a token was split.
> 2. **Preserves linguistic units** — splits at word boundaries, never breaks meaningful units mid-morpheme.
> 3. **No training data needed** — works from a pre-built rule set.
> 4. **Stable across deployments** — won't change behaviour if you retrain on new data.

### Exam-style Q&A: Effect of wrong BPE vocab size (2024 Q1d)

> **Too low (e.g. 100):**
> - Most words split into many subwords (or characters)
> - Sequences become very long, increasing memory and compute cost
> - Loses semantic units — model has to learn word meanings from character sequences
> - High [UNK] rate becomes meaningless since everything is small enough
>
> **Too high (e.g. 100,000,000):**
> - Embedding matrix becomes enormous → memory blowup
> - Most vocabulary entries appear rarely → poor embeddings (low gradient signal)
> - Long training time
> - Approaches whole-word tokenisation, losing OOV handling
> - Effectively wastes the BPE algorithm — most rare words still get [UNK] in practice

### Exam-style Q&A: Is [UNK] needed for BPE? (2024 Q1b)

> **A:** In principle, *almost* never — BPE's base vocabulary includes individual characters (or bytes in BBPE), so any input string can be decomposed character-by-character if no merges apply. This means BPE can encode literally any string of characters from its base alphabet.
>
> **However:** if the input contains characters outside the training alphabet (e.g. emoji or scripts not seen during training), even BPE will hit [UNK]. Unicode has 150,000+ characters across many scripts; BPE training data likely doesn't cover all of them. **Byte-level BPE (BBPE)** solves this completely — it operates on raw UTF-8 bytes, and since there are only 256 possible byte values, the base vocab can cover everything.
>
> **Conclusion:** for standard BPE, [UNK] is rarely but still occasionally needed. For BBPE, [UNK] is truly unnecessary.

## 5.4 Special Tokens

| Token | Purpose | Used by |
|---|---|---|
| `[CLS]` | classification — final hidden state used for whole-sequence prediction | BERT |
| `[SEP]` | sentence separator | BERT |
| `[PAD]` | padding to batch length | most |
| `[MASK]` | masked token for MLM training | BERT |
| `<S>`, `<E>` | start/end of sequence | various LMs |

## 5.5 Stopword Removal — BoW vs Transformer

### Exam-style Q&A: Why remove stopwords in BoW but not in transformer? (2024 Q1a)

> **A:** In **bag-of-words**, word order is lost — only counts matter. Stopwords ("the", "of", "is") appear in nearly every document with high frequency, dominate the feature space, and contribute no discriminative signal. Removing them reduces noise and shrinks the feature space.
>
> **Example for BoW:** Two news articles, one about sports and one about politics, both contain "the" hundreds of times. Including "the" wastes a feature dimension that adds zero classification signal.
>
> In **transformers**, the model receives the full sequence with positional information and uses self-attention to weight each token's contribution dynamically. Stopwords carry crucial syntactic and semantic information: "I am the king" vs "I am king" mean different things. The model can learn to attend to or ignore stopwords as needed.
>
> **Example for transformer:** In "the cat sat on the mat", the second "the" provides positional/syntactic context that helps the model understand "mat" is a definite reference. Removing stopwords would corrupt the input.

## 5.6 Transformer Encoder vs Decoder

| Architecture | Example | Self-attention | Use case |
|---|---|---|---|
| **Encoder-only** | BERT | bidirectional (attend in both directions) | classification, NER, embeddings |
| **Decoder-only** | GPT | causal (only attend to earlier tokens) | text generation |
| **Encoder-decoder** | T5, BART | encoder bidirectional, decoder causal + cross-attention | translation, summarisation |

**Causal masking** in decoders prevents the model from "cheating" by looking at future tokens.

## 5.7 Pretraining + Fine-tuning Paradigm

**Pretraining objectives:**
- **Masked Language Modelling (MLM)** — BERT: mask 15% of tokens, predict them
- **Causal LM** — GPT: predict next token
- **Next Sentence Prediction** — BERT extension (does B follow A?)
- **Spot the corrupted word** — ELECTRA

**Why it works:** language modelling has nearly unlimited training data; the model learns general linguistic patterns that transfer to specific tasks via fine-tuning on small labelled datasets.

**Fine-tuning:** keep most parameters, replace final layer(s) for the downstream task (e.g. add a classifier on top of BERT's [CLS] token).

---

# 6. POS Tagging & Parsing

## 6.1 Hidden Markov Models (HMM)

**Components:**
- **Transitions:** P(yᵢ | yᵢ₋₁) — probability of tag yᵢ given previous tag
- **Emissions:** P(xᵢ | yᵢ) — probability of word xᵢ given its tag

**Goal:** find the most likely tag sequence Y given observed words X.

### Greedy decoding
At each position, pick the tag with highest P(yᵢ | yᵢ₋₁) · P(xᵢ | yᵢ).

**Problem:** locally optimal ≠ globally optimal. A bad early choice can't be undone.

### Viterbi algorithm (DP-based optimal decoding)

```
For each tag y at position i:
    V[i][y] = max over y' of (V[i-1][y'] · P(y|y') · P(x_i|y))
    backptr[i][y] = argmax y'
Backtrack from final position to get tag sequence.
```

**Complexity:** O(n · |T|²) where n = sequence length, |T| = number of tags. Polynomial — practical.

### Exam-style Q&A: Why HMMs for POS tagging? (2023 Q3d)

> **A:** HMMs model the *sequential dependency* between tags — the probability that an adjective precedes a noun, for example. POS tags strongly depend on neighbouring tags, so naive classifiers that tag each word independently miss this signal. HMMs also handle the *emission* probability — P(word | tag) — which captures lexical preferences (e.g. "run" is more likely a verb than a noun).
>
> The **Viterbi algorithm** finds the globally optimal tag sequence in polynomial time, which is critical because greedy left-to-right tagging can propagate early errors. However, HMMs have limitations: they make a strong independence assumption (current tag depends only on previous tag), they can't use rich features (e.g. capitalisation, suffixes, word shape), and they struggle with domain-specific vocabulary unless retrained.

### Exam-style Q&A: Why HMM POS tagger fails on domain text (2022 Q3c)

> **A:** The HMM was trained on general-domain text (Penn Treebank, Wall Street Journal). It learned emission probabilities P(word | tag) for general vocabulary. On domain-specific text (e.g. patents, biomedical), it encounters words it has never seen — the emissions for these words default to [UNK] or backoff, providing no information to disambiguate.
>
> Additionally, domain text often uses standard English words in unusual ways (e.g. "claim" in patents is a noun, but in news it's typically a verb). The transition probabilities also differ — patents use heavy nominal compounds rarely seen in news.
>
> **Fixes:**
> 1. Fine-tune the HMM on a small labelled in-domain corpus
> 2. Use a transformer-based tagger pre-trained on the domain (e.g. SciBERT, BioBERT)
> 3. Add hand-crafted features for the domain (custom suffixes, technical term lists)
> 4. Apply self-training: use the HMM's high-confidence predictions as additional training data

## 6.2 Constituency Parsing

Decompose sentences into hierarchical phrases:
- **NP** (Noun Phrase): "the big red ball"
- **VP** (Verb Phrase): "kicked the ball hard"
- **PP** (Prepositional Phrase): "in the park"

Trees show how phrases nest within each other.

## 6.3 Dependency Parsing

Represents grammar as a directed graph where each word has a single head:
- **Directed** edges from head to dependent
- **Weakly connected** (one tree)
- **Acyclic**
- Root is the main verb

### Transition-based parsing
Maintains a stack and a buffer; uses three actions:
- **Shift** — move next word from buffer to stack
- **Left-Arc** — add edge from stack[top] to stack[top-1], pop stack[top-1]
- **Right-Arc** — add edge from stack[top-1] to stack[top], pop stack[top]

Trained with a classifier that picks the action at each step.

---

# 7. Ethics in NLP

## 7.1 Key Issues

| Issue | Description |
|---|---|
| **Bias** | Models inherit biases from training data (gender, race, geography) |
| **Environmental cost** | Training large LMs consumes massive energy (e.g. GPT-3 ≈ 1287 MWh) |
| **Transparency** | Black-box models — hard to explain decisions; problematic for high-stakes use |
| **Copyright** | Training on copyrighted material without permission; output reproduction |
| **Liability** | Who's responsible when an LM makes a harmful recommendation? |
| **Education impact** | Students using LMs to complete coursework; integrity concerns |
| **Privacy** | Models can memorise and leak training data (medical records, personal info) |
| **Dual use** | Disinformation, deepfakes, automated phishing |

## 7.2 Best Practices

- **Datasheets for datasets** — document collection process, demographics, limitations (Gebru et al.)
- **Model cards** — document intended use, evaluation metrics, known biases (Mitchell et al.)
- **Bias audits** — test models on fairness benchmarks (StereoSet, CrowS-Pairs)
- **Carbon reporting** — disclose training energy consumption
- **Opt-out mechanisms** — let people remove their data from training sets

### Exam-style Q&A: Two challenges of LM encoding knowledge (2023 Q3f)

> **A:**
> 1. **Knowledge becomes stale** — the model only knows what was in its training data; world facts change (CEOs, elections, scientific discoveries). Updating requires expensive retraining or knowledge editing techniques.
> 2. **No grounded source attribution** — the model produces fluent text but can't cite where a fact came from, can't distinguish memorised fact from confabulation (hallucination), and may confidently produce wrong information.
>
> Other valid answers: privacy leakage (training data extraction), legal liability for incorrect outputs, biased knowledge reflecting training data demographics.

---

# 8. Information Extraction

## 8.1 Named Entity Recognition (NER)

Identify spans referring to entities (people, organisations, locations, dates, etc.).

### IOB Tagging Scheme
- **I**nside an entity
- **O**utside any entity
- **B**eginning of an entity (used when two entities are adjacent)

Example:
```
Tim    Cook   announced  Apple   in    Cupertino
B-PER  I-PER  O          B-ORG   O     B-LOC
```

### Methods
| Method | Description |
|---|---|
| **CRF** (Conditional Random Field) | Discriminative sequence model; models tag transitions |
| **BiLSTM-CRF** | Neural backbone + CRF on top — strong baseline |
| **Transformer (BERT)** | Pretrained encoder + token classification head — state of the art |

### Exam-style Q&A: Nested entity mentions (2023 Q3e)

> **A:** A nested entity mention is one entity span contained within another. Example: in "the **University of Glasgow** Computing Science Department", "**Glasgow**" is a LOCATION nested inside "University of Glasgow" which is an ORGANISATION.
>
> Standard IOB tagging assumes flat, non-overlapping spans — each token has exactly one tag. To handle nesting, you need:
> - **Multiple tag layers** (one per nesting level)
> - **Span-based models** that predict (start, end, label) triples directly
> - **Graph-based models** that allow overlapping spans

## 8.2 Entity Linking

Map entity mentions ("strings") to canonical entries in a knowledge base ("things").

**Pipeline:**
1. **NER** — find mentions
2. **Candidate generation** — for each mention, retrieve possible KB entries
   - **Dictionary lookup** — match string against alias dictionary
   - **Dense vector retrieval** — encode mention + context, find nearest KB entries by embedding similarity
3. **Reranking** (optional but high-accuracy) — use a transformer to score each (mention, candidate) pair given context

**Example:** "Apple" in "Apple released the iPhone" → Apple Inc. (not the fruit, not the record label)

## 8.3 Relation Extraction

Extract structured triples (subject, relation, object) from text.

**Methods:**
| Method | Description | Pros | Cons |
|---|---|---|---|
| **Co-occurrence** | Count entities appearing together | simple, fast | no relation type |
| **Rule-based** | Patterns like "X, who starred in Y" → starred_in | high precision | low recall, brittle |
| **BERT-based** | Insert entity marker tokens, classify the relation | high accuracy | needs labelled data |

**Entity markers:** wrap entities with special tokens to help the model focus:
```
[E1]Tim Cook[/E1] is the CEO of [E2]Apple[/E2].
```

## 8.4 Coreference Resolution

Determine which mentions refer to the same entity.

**Types of reference:**
- **Anaphora** — refers backward ("**Mary** went to the shop. **She** bought milk.")
- **Cataphora** — refers forward ("After **she** sat down, **Mary** ordered.")
- **Exophora** — refers outside the text ("Look at **this**!" — needs visual context)

**Methods:**
1. **Mention detection** — find candidate spans (pronouns, named entities, noun phrases)
2. **Coreference clustering** — group mentions referring to the same entity
3. **Hobbs algorithm** — classical syntactic approach to find the antecedent of a pronoun

---

# 9. Large Language Models

## 9.1 Training Pipeline

```
1. Pretraining        →  next-token prediction on huge corpus (trillions of tokens)
2. Instruction tuning →  supervised on (instruction, response) pairs
3. RLHF              →  reinforcement learning from human feedback for alignment
4. Safety fine-tuning →  reduce harmful, biased, or unsafe outputs
```

**Instruction tuning:** teaches the model to follow natural-language instructions ("Summarise this article in 2 sentences").

**RLHF (Reinforcement Learning from Human Feedback):**
1. Collect human preference data (pair of model outputs, human picks better one)
2. Train a **reward model** to predict human preferences
3. Use PPO (Proximal Policy Optimisation) to fine-tune the LM to maximise reward

## 9.2 Prompt Engineering

| Technique | Description | Example |
|---|---|---|
| **Zero-shot** | Just describe the task | "Classify this review as positive or negative: [review]" |
| **Few-shot** | Include examples in the prompt | "Review: 'Loved it!' → Positive. Review: 'Terrible.' → Negative. Review: '[new]' → ?" |
| **Chain-of-Thought (CoT)** | Ask the model to reason step-by-step | "Let's think step by step. First, ..." |
| **Self-consistency** | Sample multiple CoT chains, take majority answer | reduces variance |
| **Explicit instructions** | "Answer in JSON. Use only these keys: ..." | structured output |

## 9.3 LLM Issues

| Issue | Description | Mitigation |
|---|---|---|
| **Hallucination** | confidently wrong outputs | RAG, fact-checking, smaller temperature |
| **Test set leakage / data contamination** | benchmark data appeared in pretraining | use newer benchmarks, manual examples |
| **Cost** | API calls expensive at scale | smaller fine-tuned models, caching, distillation |
| **Latency** | autoregressive generation is slow | speculative decoding, smaller models |
| **Bias** | inherits training data bias | RLHF, debiasing prompts, audits |
| **Dangerous generations** | unsafe instructions | safety fine-tuning, content filters |
| **Privacy leakage** | can regurgitate training data verbatim | differential privacy in training |

### Exam-style Q&A: Rank LogReg, BERT, LLaMA by deployment cost (2025 Q3a)

> **A:** Logistic Regression < BERT-base < LLaMA-70B.
>
> Logistic regression is a linear model over sparse features — extremely lightweight (millions of parameters, runs on CPU in milliseconds). BERT-base and LLaMA are both transformer architectures, but BERT-base has ~110M parameters while LLaMA-70B has ~70 billion (≈600× more). LLaMA requires multiple high-end GPUs even for inference, while BERT-base runs comfortably on a single GPU.

### Exam-style Q&A: Zero-shot vs data contamination (2024 Q3a)

> **A:** Before claiming a result is "zero-shot," verify the LLM wasn't trained on the test data. LLMs are pretrained on massive web crawls that often include public benchmark datasets — a phenomenon called **data contamination**. If the test set (or even similar examples) appeared in pretraining, the model has effectively *seen* the data, and the result isn't truly zero-shot. Check the model's training data documentation (if available) and consider whether the dataset is well-known enough to have been crawled.

### Exam-style Q&A: BERT classifier predicting "positive" on brand mentions (2025 Q3d)

> **A:** The brand name "BeStep" is not in BERT's vocabulary as a single token, so the sub-word tokeniser splits it into recognisable substrings — most likely `best` + `##ep`. The model sees the token "best" in every sentence mentioning the brand and learns to associate it with positive sentiment (since "best" is strongly positive in training data).
>
> **Fix:** Replace the brand name with a placeholder before classification:
> ```python
> text = text.replace("BeStep", "[BRAND]")
> ```
> Now the model sees a neutral placeholder and classifies based on the actual sentiment content. Alternatively, add "BeStep" as a new vocabulary token and fine-tune.

### Exam-style Q&A: Cross-lingual classification limitations (2025 Q3c)

> **A:**
>
> **Logistic regression problem:** The classifier learned weights for English tokens only. Tokens in another language won't have learned weights — they map to [UNK] or zero vectors. Most input is treated as unknown, drastically reducing performance.
>
> **BERT-base problem:** BERT splits words into sub-tokens, so multilingual input won't go to [UNK]. However, BERT-base was pretrained on English Wikipedia and BookCorpus — its sub-token vocabulary is biased toward English. Words in unseen languages get split into many sub-tokens (often per-character), producing degenerate representations.
>
> **Solution that addresses both:** Use a **multilingual pretrained model** (mBERT, XLM-R) that was trained on text from 100+ languages. Its tokeniser knows sub-tokens from many scripts, and its pretraining objective produces aligned embeddings across languages. Fine-tune this multilingual model on your sentiment data.

### Exam-style Q&A: 3 counter-arguments to LLM-only labelling (2024 Q3b)

> **Setup:** Fleiss κ=0.61 is "substantial agreement" in standard interpretation, not low. The claim that this implies unreliable labels is wrong.
>
> **A:**
> 1. **κ = 0.61 IS reliable** by standard interpretation (Landis & Koch: 0.61–0.80 = substantial agreement). The claim's premise is wrong.
> 2. **LLMs have their own biases and errors** — they're trained on text that reflects particular viewpoints, and their "labels" carry these biases without the diversity that comes from multiple human annotators.
> 3. **Using an LLM for labels and an LLM for the classifier creates circular evaluation** — you're essentially asking "does the LLM agree with itself?" rather than measuring true task performance. Results won't generalise to deployment where labels come from humans.
>
> **Additional valid points:** (4) Data contamination risk — if the LLM saw similar examples during pretraining, your "new" labels aren't independent. (5) Cost at scale may exceed human annotation. (6) Reproducibility issues — LLM versions change.

---

# 10. Latest Research

These topics appear in Lecture 10 and are increasingly likely to feature in Q3.

## 10.1 Retrieval-Augmented Generation (RAG)

**Problem:** LLMs hallucinate; their knowledge is frozen at training time.

**Solution:** at inference time, retrieve relevant documents from an external corpus, concatenate them with the question, and let the LM generate an answer grounded in retrieved evidence.

**Pipeline:**
```
Query → Retriever (dense or sparse) → top-k passages → LLM → grounded answer
```

**Benefits:**
- Updatable knowledge (just update the corpus)
- Source attribution possible
- Smaller LMs can match larger ones with good retrieval
- Less hallucination (when retrieval is accurate)

**Architectures:**
- **Fusion-in-Decoder (FiD)** — encode each passage separately, concatenate before decoder
- **RETRO (DeepMind)** — cross-attention to retrieved chunks within the transformer
- **REALM** — joint retriever-reader training

**Limitations:**
- Still hallucinates from suggestive prompts (susceptible to power-of-suggestion)
- Retrieval quality is the bottleneck — bad passages produce bad answers
- "Lost in the middle" effect (see below)

## 10.2 Lost in the Middle

When given many passages, LLMs show U-shaped accuracy: high when the answer is at the start or end of the context, low when in the middle. Implication: don't rely on long-context LLMs to extract specific facts from middle passages without explicit prompting.

## 10.3 Tool Use

LLMs can be trained to invoke external tools when needed:
- **Calculators** — for arithmetic
- **Search APIs** — for current information
- **Translation tools** — for language pairs
- **Code execution** — for computation

**Mechanism:** the LM generates special tokens like `[Calculator(2+2) → 4]`. Generation pauses, the tool executes, the result is inserted, generation resumes.

**Example (Toolformer):**
```
"Out of 1400 participants, 400 (or [Calculator(400/1400) → 0.29] 29%) passed."
```

## 10.4 Knowledge Editing

**Problem:** A specific fact in the LM is wrong; full retraining is too expensive.

**Approaches:**
- **Minimal weight edits** — modify a few parameters to update one fact (ROME, MEMIT)
- **External memory** — store edits in a key-value store consulted at inference time
- **Adapter modules** — small trainable modules added on top of frozen base model

## 10.5 Reasoning

**Chain-of-thought (CoT) prompting** improves performance on multi-step problems by encouraging the model to reason step-by-step.

**Latest reasoning models** (e.g. OpenAI o1, DeepSeek-R1) are trained specifically to produce hidden reasoning chains before final answers. Massively increases token cost but improves on hard reasoning tasks.

## 10.6 Agentic AI

Chain multiple LLM calls together:
1. **Planner** — break the goal into subtasks
2. **Worker** — execute each subtask (possibly using tools)
3. **Critic** — evaluate progress, decide next action
4. **Loop** until done or stuck

**Strengths:** complex multi-step tasks, iterative refinement.
**Weaknesses:** can degrade into nonsense, hard to debug, expensive (many LLM calls).

## 10.7 Exam-style synthesis question (predicted 2026 Q3 angle)

> **Q (predicted):** You're building an LLM-powered assistant for a healthcare company. Patients ask medical questions and the system should answer accurately. Discuss the issues you would face and how you would mitigate them.
>
> **Model answer:**
> 1. **Hallucination** — LLMs invent confident wrong answers, dangerous in healthcare. *Mitigation:* RAG with curated medical literature; require source citations; refuse to answer when retrieval confidence is low.
> 2. **Data contamination & outdated knowledge** — pretraining may include old guidelines. *Mitigation:* RAG ensures answers come from up-to-date sources; flag model knowledge cutoff.
> 3. **Liability and transparency** — model can't be held responsible. *Mitigation:* always include disclaimers, source links, and human-physician review for high-risk recommendations.
> 4. **Privacy** — patient data in prompts must not be stored. *Mitigation:* on-prem deployment or zero-retention API agreements; PII redaction before prompt construction.
> 5. **Bias** — training data may underrepresent minority groups, leading to differential accuracy. *Mitigation:* evaluate per-demographic; involve diverse medical experts in evaluation.
> 6. **Test set contamination** — public medical benchmarks may have leaked into pretraining. *Mitigation:* construct fresh hold-out evaluation sets with domain experts.
> 7. **Lost in the middle** — long medical records may have crucial info in the middle. *Mitigation:* use retrieval to focus on relevant sections rather than passing entire records.

---

# 11. Exam Strategy

## 11.1 Time Budget (90 minutes total)

| Activity | Time |
|---|---|
| Scan all 3 questions | 3 min |
| Q1 (20 marks) | ~27 min |
| Q2 (20 marks) | ~27 min |
| Q3 (20 marks) | ~27 min |
| Review | 6 min |

Roughly **1.3 min per mark**. A 6-mark question deserves ~8 min, no more.

## 11.2 Mark-Detail Calibration

> "Each mark is roughly one idea or one point in the answer." — Sean MacAvaney, Lecture 10

| Marks | Expected length |
|---|---|
| 1 | 1 sentence |
| 2 | 2 sentences OR 1 paragraph |
| 3–4 | structured paragraph with example |
| 5–8 | multiple paragraphs OR bullet list with explanation |

**Common failures:**
- **Too little detail** on a 4-mark question → only 1–2 marks awarded
- **Too much detail** on a 2-mark question → wastes time, can include wrong info that loses marks

## 11.3 Answer Templates

### "Discuss N problems with..."
Use bullet points. Number them. Each bullet = 1 problem + 1-sentence justification.

### "Justify whether you would use X for Y..."
1. State your decision (yes/no/sometimes)
2. Give the reasoning principle
3. Provide a domain-specific example

### "Calculate..."
1. Write the formula
2. Substitute the values explicitly
3. Show intermediate arithmetic
4. State the final answer with units

### "Critique this response..."
1. Identify each factual error or omission
2. Provide the correct version
3. Where the response is correct, briefly affirm

## 11.4 Pitfalls to Avoid

1. **Copy-pasting from crib sheet** — explicitly mentioned by Sean as not scoring well
2. **Not showing work on calculations** — can't get partial credit
3. **Vague generic answers** — "stopwords don't carry meaning" without a domain example
4. **Going over on early questions** and rushing later ones
5. **Answering more sub-parts than asked** ("Discuss 4 problems" — don't list 6, you might pick the weakest 4)
6. **Confusing similar concepts** — multi-class vs multi-label; encoder vs decoder; macro vs micro

## 11.5 What to Bring (Open-Book)

- **The crib sheet** (provided, but know it inside-out)
- **These notes** — bookmarked by section
- **The past papers** with model answers
- **A calculator** for arithmetic
- **Scratch paper** for working out calculations before writing the final answer

## 11.6 Final-Week Revision Plan

**Day 1–2:** Re-do all past paper Q1 sub-parts. Focus on BPE, set similarity, metric properties.
**Day 3–4:** Re-do all past paper Q2 sub-parts. Practise beam search until automatic; do 2 perplexity calculations per day.
**Day 5–6:** Read Lectures 7, 8, 9, 10 and write your own 3-sentence summary of each topic. Practise BERT/LLM scenario questions.
**Day 7:** Cold simulate the exam — pick one past paper, answer under 90-min timed conditions, then mark yourself against the sample answers.

---

## Appendix A: Critical Formulas at a Glance

```
SIMILARITY
  Overlap     = |X ∩ Y| / min(|X|, |Y|)
  Dice        = 2|X ∩ Y| / (|X| + |Y|)
  Jaccard     = |X ∩ Y| / |X ∪ Y|
  Cosine      = (x · y) / (||x|| · ||y||)
  Euclidean   = sqrt(Σ(xᵢ - yᵢ)²)

TF-IDF
  TF (log)    = 1 + log₁₀(tf)            if tf > 0
  IDF         = log(N / df)
  TF-IDF      = (1 + log(tf)) · log(N/df)

LANGUAGE MODEL
  Add-k       = (count + k) / (Σcount + k·|V|)
  Perplexity  = (Π P(wᵢ))^(-1/n) = 2^(Cross-Entropy)
  Cross-Ent   = -(1/n) Σ log₂ P(wᵢ)

CLASSIFICATION
  Precision   = TP / (TP + FP)
  Recall      = TP / (TP + FN)
  F1          = 2·P·R / (P + R)
  Accuracy    = (TP + TN) / total

ATTENTION
  Attention   = softmax(Q·K^T / √d_k) · V
```

## Appendix B: Topic-to-Lecture Map

| Lecture | Title | Key concepts | Likely exam Q |
|---|---|---|---|
| 1 | Intro, Tokens, Doc Similarity | NLP pipeline, encodings, set sim, n-grams | **Q1** |
| 2 | Geometric Sim, Distributions, Clustering | TF-IDF, cosine, K-Means | **Q1** |
| 3 | Language Modelling | n-grams, smoothing, perplexity, beam search | **Q2** |
| 4 | Text Classification | metrics, splits, overfitting | **Q2** |
| 5 | Contextual Word Embeddings | BPE, BERT, attention | **Q1** (BPE) or **Q3** (BERT) |
| 6 | POS Tagging & Parsing | HMM, Viterbi | **Q3** |
| 7 | Ethics | bias, transparency, environmental cost | **Q3** (sub-part) |
| 8 | Information Extraction | NER, entity linking, relation extraction | **Q3** |
| 9 | Large Language Models | RLHF, prompt engineering, hallucination | **Q3** |
| 10 | Latest Research | RAG, agentic, tool use | **Q3** (sub-part) |

---

*End of revision notes. Estimated study time: 15–20 hours over 1 week, plus 4–6 hours of past-paper practice.*

*Good luck on the exam — you've got this.*
