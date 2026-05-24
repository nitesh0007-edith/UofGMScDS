# Probability and Statistical Learning - Complete Study Guide

**Author**: Study materials for IDSS Lab 3
**Date**: November 2025
**Purpose**: Comprehensive, beginner-friendly guides for understanding probability concepts in depth

---

## Overview

This collection contains **8 comprehensive guides** covering all the probability and statistical concepts needed for the IDSS Lab 3 assessment. Each guide is designed to be beginner-friendly, with:

- ✅ Clear explanations of theory
- ✅ Practical examples with code
- ✅ Visual intuitions
- ✅ Common mistakes to avoid
- ✅ Step-by-step implementations in NumPy/Python

---

## 📚 Study Guides

### 01. PMF and Discrete Probability
**File**: `01_PMF_Discrete_Probability.md`

**Topics covered**:
- What are random variables?
- Probability mass functions (PMFs)
- Valid PMF properties
- Computing probabilities from PMFs
- Events and outcomes
- Odds and log-odds
- Expected value and E[f(X)] vs f(E[X])
- Practical NumPy implementations

**When to read**: Start here! This is the foundation for everything else.

**Key takeaways**:
- PMF maps outcomes to probabilities
- Valid PMF: sums to 1, all values in [0,1]
- E[f(X)] ≠ f(E[X]) in general!

---

### 02. Conditional Probability
**File**: `02_Conditional_Probability.md`

**Topics covered**:
- Joint probability distributions
- Marginal probability (summing out variables)
- Conditional probability P(X|Y)
- Computing conditional PMFs
- Independence vs correlation
- Chain rule and sum rule

**When to read**: After understanding basic PMFs.

**Key takeaways**:
- P(X|Y) = P(X,Y) / P(Y)
- Marginal: sum over other variables
- P(X|Y) ≠ P(Y|X) in general!

---

### 03. Bayes' Rule
**File**: `03_Bayes_Rule.md`

**Topics covered**:
- Bayes' theorem and its importance
- Prior, likelihood, posterior, evidence
- Updating beliefs with data
- Sequential Bayesian updates
- Base rate fallacy
- Practical submarine search examples

**When to read**: After conditional probability.

**Key takeaways**:
- Posterior ∝ Likelihood × Prior
- Each posterior becomes the next prior
- Combines prior knowledge with new evidence

---

### 04. Entropy and Information Theory
**File**: `04_Entropy_Information_Theory.md`

**Topics covered**:
- What is information?
- Entropy as uncertainty measure
- Conditional entropy
- Mutual information
- Feature selection using entropy
- Application to decision making

**When to read**: After conditional probability.

**Key takeaways**:
- Entropy measures uncertainty/randomness
- H(X|Y) ≤ H(X) (information reduces uncertainty)
- Use entropy to find most informative features

---

### 05. Sampling and Monte Carlo Methods
**File**: `05_Sampling_Monte_Carlo.md`

**Topics covered**:
- What is sampling?
- Sampling from discrete and continuous distributions
- Monte Carlo estimation of expectations
- Reconstructing distributions from samples
- Law of Large Numbers
- Standard error and convergence

**When to read**: Before continuous distributions.

**Key takeaways**:
- E[f(X)] ≈ (1/n) Σf(xᵢ) for samples xᵢ
- Error decreases as 1/√n
- Can estimate anything via sampling!

---

### 06. Multivariate Normal Distribution
**File**: `06_Multivariate_Normal.md`

**Topics covered**:
- From 1D to multivariate normal
- Mean vector and covariance matrix
- Understanding correlation
- Properties of multivariate normal
- Parameter estimation from samples
- PDF and log-PDF computation

**When to read**: Before maximum likelihood estimation.

**Key takeaways**:
- Specified by μ (mean vector) and Σ (covariance matrix)
- Σ must be symmetric and positive definite
- μ̂ = sample mean, Σ̂ = sample covariance

---

### 07. Maximum Likelihood Estimation
**File**: `07_Maximum_Likelihood_Estimation.md`

**Topics covered**:
- Likelihood vs probability
- Maximum likelihood principle
- Log-likelihood and why we use it
- MLE for common distributions
- Properties of MLE
- MLE via optimization

**When to read**: After multivariate normal.

**Key takeaways**:
- θ̂_MLE = argmax L(θ|data)
- Always use log-likelihood for numerical stability
- MLE is consistent, asymptotically normal, efficient

---

### 08. Optimization and Stochastic Hill Climbing
**File**: `08_Optimization_Stochastic_Hill_Climbing.md`

**Topics covered**:
- Optimization basics
- Hill climbing algorithm
- Stochastic hill climbing
- Handling constraints (rejection, projection)
- Adaptive step sizes
- Complete MLE implementation
- Tuning and debugging

**When to read**: Last! This ties everything together.

**Key takeaways**:
- Use stochastic hill climbing when no analytical solution
- Multiple random restarts to avoid local optima
- Enforce constraints via clipping or rejection
- Monitor convergence and adjust hyperparameters

---

## 🎯 How to Use These Guides

### For Lab 3 Preparation

**Week 1**: Foundations
1. Read Guide 01 (PMF and Discrete Probability)
2. Work through examples in Python
3. Read Guide 02 (Conditional Probability)
4. Practice computing marginals and conditionals

**Week 2**: Bayesian Inference
1. Read Guide 03 (Bayes' Rule)
2. Implement Bayesian updates
3. Read Guide 04 (Entropy)
4. Practice entropy calculations

**Week 3**: Continuous and Estimation
1. Read Guide 05 (Sampling and Monte Carlo)
2. Read Guide 06 (Multivariate Normal)
3. Practice fitting distributions to data

**Week 4**: Optimization
1. Read Guide 07 (Maximum Likelihood Estimation)
2. Read Guide 08 (Optimization)
3. Implement stochastic hill climbing
4. Practice on submarine problem

### For Quick Reference

Each guide has a **Summary** section at the end with:
- Key formulas
- Main concepts
- Common mistakes
- Quick reference code snippets

Use these for quick lookups during the lab!

---

## 💻 Code Examples

All guides include:
- ✅ Complete, runnable Python code
- ✅ NumPy implementations
- ✅ Visualization examples
- ✅ Common patterns and templates

You can copy-paste and modify these examples for your lab work!

---

## 🚀 Converting to DOCX

To convert these Markdown files to DOCX for easier reading:

### Option 1: Using Pandoc (Recommended)
```bash
# Install pandoc first: https://pandoc.org/installing.html

# Convert single file
pandoc 01_PMF_Discrete_Probability.md -o 01_PMF_Discrete_Probability.docx

# Convert all files
for file in *.md; do
    pandoc "$file" -o "${file%.md}.docx"
done
```

### Option 2: Using Online Converters
1. Open https://cloudconvert.com/md-to-docx
2. Upload the .md file
3. Download the .docx file

### Option 3: Using VS Code
1. Install "Markdown to Word" extension
2. Open .md file
3. Right-click → "Markdown to Word"

---

## 📖 Study Tips

### For Understanding Concepts

1. **Read actively**: Don't just read, work through examples
2. **Code along**: Type out the examples yourself
3. **Visualize**: Use matplotlib to plot distributions
4. **Connect**: See how topics relate to each other
5. **Test yourself**: Try exercises before looking at solutions

### For the Lab Assessment

1. **Start early**: Don't wait until the last minute
2. **Test your code**: Verify with simple examples first
3. **Check constraints**: Make sure parameters are valid
4. **Use the guides**: Reference formulas and patterns
5. **Debug systematically**: Print intermediate values

### For Exam Preparation

1. **Understand, don't memorize**: Focus on concepts, not formulas
2. **Practice problems**: Work through many examples
3. **Explain to others**: Teaching is the best way to learn
4. **Review summaries**: Go through summary sections
5. **Connect to lectures**: These guides complement your lecture notes

---

## 🎓 Mapping to Lab Tasks

### Part 1: Discrete Submarine Hunt

**Relevant Guides**:
- 01: PMF basics, outcomes, events, expected value
- 02: Conditional probability, marginals
- 03: Bayes' rule, sequential updates
- 04: Entropy, information gain
- 05: Sampling, reconstructing PMFs

**Key Functions to Implement**:
- Computing probabilities from PMF
- Conditional distributions
- Expected values
- Entropy calculations
- Bayesian updates
- Sampling and reconstruction

### Part 2: Continuous Submarine Hunt

**Relevant Guides**:
- 05: Monte Carlo estimation
- 06: Multivariate normal distribution
- 07: Maximum likelihood estimation
- 08: Stochastic hill climbing optimization

**Key Functions to Implement**:
- Fitting multivariate normal
- Monte Carlo expected value
- Cross distribution optimization
- Stochastic hill climbing with constraints

---

## ⚠️ Important Notes

### Academic Integrity

These guides are for **learning and understanding concepts**. They provide:
- ✅ Conceptual explanations
- ✅ General patterns and approaches
- ✅ Example code for common tasks
- ✅ Theory and best practices

They do NOT provide:
- ❌ Direct solutions to lab questions
- ❌ Specific answers to submit
- ❌ Code that directly solves graded exercises

**You must**:
- Write your own code for the lab
- Understand what your code does
- Submit your own independent work
- Follow University of Glasgow's academic integrity policies

### Using These Materials

**Appropriate use**:
- Study before attempting the lab
- Reference formulas and patterns
- Understand concepts deeply
- Use as a learning resource

**Inappropriate use**:
- Copying code directly into lab
- Submitting examples as your own work
- Not understanding what you write
- Violating academic integrity policies

---

## 🔍 Quick Lookup

### Common Formulas

**PMF Properties**:
```
Σ P(X=x) = 1
0 ≤ P(X=x) ≤ 1
```

**Conditional Probability**:
```
P(A|B) = P(A,B) / P(B)
```

**Bayes' Rule**:
```
P(A|B) ∝ P(B|A) · P(A)
```

**Entropy**:
```
H(X) = -Σ p(x) log₂ p(x)
```

**MLE**:
```
θ̂ = argmax Σ log f(xᵢ; θ)
```

**Multivariate Normal**:
```
μ̂ = (1/n) Σ xᵢ
Σ̂ = (1/n) Σ (xᵢ-μ̂)(xᵢ-μ̂)ᵀ
```

---

## 📞 Getting Help

If you're stuck:

1. **Re-read the relevant guide** - Often the answer is there!
2. **Check the examples** - See how similar problems are solved
3. **Review lecture notes** - These guides complement lectures
4. **Ask lab assistants** - They can provide guidance (not answers!)
5. **Study groups** - Discuss concepts (not solutions!) with peers

---

## ✅ Checklist for Lab Success

Before starting the lab, make sure you can:

- [ ] Compute probabilities from a PMF
- [ ] Calculate marginal and conditional distributions
- [ ] Apply Bayes' rule to update beliefs
- [ ] Compute entropy and mutual information
- [ ] Sample from discrete distributions
- [ ] Reconstruct PMF from samples
- [ ] Fit multivariate normal to data
- [ ] Compute log-likelihood
- [ ] Implement stochastic hill climbing
- [ ] Handle parameter constraints

If you can do all these, you're ready! 🎉

---

## 🙏 Final Notes

These guides represent a comprehensive resource for learning probability and statistical inference. Use them wisely:

- **Learn actively**: Don't just read, practice!
- **Think deeply**: Understand why, not just what
- **Code yourself**: Type it out, don't copy-paste
- **Test thoroughly**: Verify your understanding
- **Submit honestly**: Do your own work

Good luck with your lab! You've got this! 💪

---

## 📝 Quick Reference Card

```
PMF: P(X=x)                    | Must sum to 1
Marginal: Σ_y P(X,Y)           | Sum out variable
Conditional: P(X|Y) = P(X,Y)/P(Y) | Restrict to condition
Bayes: P(A|B) ∝ P(B|A)P(A)     | Update beliefs
Entropy: -Σ p log p            | Uncertainty measure
E[X]: Σ x·P(x)                 | Expected value
Monte Carlo: (1/n)Σf(xᵢ)       | Approximate expectation
MLE: argmax Σlog f(xᵢ;θ)       | Find best parameters
```

---

**Remember**: These are learning materials to help you understand concepts. Master the concepts, then apply them independently in your lab work!
