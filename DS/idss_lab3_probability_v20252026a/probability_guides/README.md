# 📚 Probability Learning Guides - Organized Materials

**Complete study materials for IDSS Lab 3: Introduction to Probability**

All learning materials are now organized in separate folders by format for easy access!

---

## 📂 Folder Structure

```
probability_guides/
├── markdown/     ← Original Markdown files (.md)
├── docx/         ← Microsoft Word documents (.docx)
├── pdf/          ← Clean PDF files (.pdf) ⭐ RECOMMENDED
├── html/         ← Web-viewable HTML files (.html)
└── README.md     ← This file
```

---

## 📖 Study Guides Available

All guides are available in **4 formats**: Markdown, DOCX, PDF, and HTML

### 01. PMF and Discrete Probability (500 KB PDF)
- Probability mass functions
- Outcomes, events, and sample spaces
- Expected value and odds
- **Start here!**

### 02. Conditional Probability (616 KB PDF)
- Joint and marginal distributions
- Conditional probability P(X|Y)
- Independence and correlation

### 03. Bayes' Rule (585 KB PDF)
- Bayesian inference
- Prior, likelihood, and posterior
- Sequential updates

### 04. Entropy and Information Theory (677 KB PDF)
- Entropy as uncertainty measure
- Mutual information
- Feature selection

### 05. Sampling and Monte Carlo Methods (796 KB PDF)
- Sampling from distributions
- Monte Carlo estimation
- Reconstructing distributions

### 06. Multivariate Normal Distribution (712 KB PDF)
- Mean vectors and covariance matrices
- Correlation and independence
- Parameter estimation

### 07. Maximum Likelihood Estimation (607 KB PDF)
- MLE theory and practice
- Log-likelihood
- Parameter estimation

### 08. Optimization and Stochastic Hill Climbing (735 KB PDF)
- Hill climbing algorithms
- Handling constraints
- Complete MLE implementation

### PROBABILITY_LEARNING_GUIDE_README (552 KB PDF)
- Master guide and index
- How to use these materials
- Study tips and best practices

---

## 💡 Which Format Should You Use?

### 📄 **PDF (RECOMMENDED)**
**Best for**: Reading, studying, printing, annotating
- ✅ Professional formatting
- ✅ Works on any device
- ✅ Easy to print
- ✅ Can annotate in most PDF readers
- 📁 **Location**: `pdf/` folder

### 📝 **DOCX**
**Best for**: Editing, customizing, adding notes
- ✅ Fully editable
- ✅ Can add your own notes
- ✅ Microsoft Word compatible
- 📁 **Location**: `docx/` folder

### 🌐 **HTML**
**Best for**: Web browsing, quick reference
- ✅ View in any browser
- ✅ Searchable (Ctrl/Cmd+F)
- ✅ Print-to-PDF button included
- 📁 **Location**: `html/` folder

### 📋 **Markdown**
**Best for**: Source files, GitHub viewing, developers
- ✅ Plain text format
- ✅ Version control friendly
- ✅ Easy to read in any text editor
- 📁 **Location**: `markdown/` folder

---

## 🚀 Quick Start

### Option 1: Read PDFs (Easiest!)
```bash
# Open PDF folder
cd probability_guides/pdf/

# Start with the README
open PROBABILITY_LEARNING_GUIDE_README.pdf

# Then read guides 01-08 in order
open 01_PMF_Discrete_Probability.pdf
```

### Option 2: View in Browser
```bash
# Open HTML folder
cd probability_guides/html/

# Open in default browser (macOS)
open 01_PMF_Discrete_Probability.html

# Or drag files to your browser
```

### Option 3: Edit in Word
```bash
# Open DOCX folder
cd probability_guides/docx/

# Open in Microsoft Word
open 01_PMF_Discrete_Probability.docx
```

---

## 📚 Study Path

### Week 1: Discrete Probability
1. **PROBABILITY_LEARNING_GUIDE_README** - Get overview
2. **01_PMF_Discrete_Probability** - Foundation
3. **02_Conditional_Probability** - Build on basics
4. Practice exercises from your course

### Week 2: Bayesian Inference
1. **03_Bayes_Rule** - Core inference technique
2. **04_Entropy_Information_Theory** - Information concepts
3. Apply to submarine search problems

### Week 3: Continuous Distributions
1. **05_Sampling_Monte_Carlo** - Simulation methods
2. **06_Multivariate_Normal** - Continuous distributions
3. Practice parameter estimation

### Week 4: Optimization & MLE
1. **07_Maximum_Likelihood_Estimation** - Theory
2. **08_Optimization_Stochastic_Hill_Climbing** - Implementation
3. Complete lab exercises

---

## 📊 File Sizes Summary

| Guide | PDF Size | Pages (approx) |
|-------|----------|----------------|
| 01. PMF & Discrete Probability | 500 KB | ~25 |
| 02. Conditional Probability | 616 KB | ~30 |
| 03. Bayes' Rule | 585 KB | ~28 |
| 04. Entropy & Information | 677 KB | ~33 |
| 05. Sampling & Monte Carlo | 796 KB | ~38 |
| 06. Multivariate Normal | 712 KB | ~35 |
| 07. Maximum Likelihood | 607 KB | ~30 |
| 08. Optimization | 735 KB | ~36 |
| README Guide | 552 KB | ~27 |
| **Total** | **~5.7 MB** | **~280 pages** |

---

## 🎯 For Lab 3 Specifically

### Part 1: Discrete Submarine Hunt
**Use these guides**:
- 01: Computing probabilities, expected values
- 02: Marginals and conditionals
- 03: Bayesian updates
- 04: Entropy calculations
- 05: Sampling and reconstruction

### Part 2: Continuous Submarine Hunt
**Use these guides**:
- 05: Monte Carlo estimation
- 06: Fitting multivariate normal
- 07: Maximum likelihood theory
- 08: Stochastic hill climbing

---

## ⚠️ Important Reminders

### Academic Integrity
- ✅ Use for **learning concepts**
- ✅ Study the **theory and approaches**
- ✅ Understand the **mathematics**
- ✅ Write your **own code**
- ❌ Don't **copy-paste solutions**
- ❌ Don't **submit examples as your work**

### Best Practices
1. **Read actively** - Work through examples yourself
2. **Code along** - Type out the code, don't copy-paste
3. **Test understanding** - Try variations
4. **Reference properly** - If you use a technique from here, understand it first
5. **Ask questions** - Use lab assistants and office hours

---

## 🔍 Quick Reference

### Common Formulas
```
PMF: ΣP(X=x) = 1
Conditional: P(A|B) = P(A,B)/P(B)
Bayes: P(A|B) ∝ P(B|A)·P(A)
Entropy: H(X) = -Σp(x)log₂p(x)
E[X]: Σx·P(x)
MLE: θ̂ = argmax Σlog f(xᵢ;θ)
```

### Key NumPy Operations
```python
# PMF operations
np.sum(pmf)                    # Should equal 1
np.sum(pmf[condition])         # Probability of event

# Marginals
p_x = np.sum(pmf, axis=1)      # Sum over y

# Conditionals
p_x_given_y = pmf / p_y[None, :] # Broadcast division

# Expected value
E_x = np.sum(values * pmf)

# Sampling
samples = np.random.choice(outcomes, p=pmf)

# MLE for normal
mu_hat = np.mean(samples, axis=0)
sigma_hat = np.cov(samples.T)
```

---

## 📱 Access on Mobile

All formats work great on mobile devices:
- **PDF**: Use any PDF reader app
- **HTML**: Open in mobile browser
- **DOCX**: Use Word mobile app
- **Markdown**: Use markdown viewer apps

---

## 🆘 Getting Help

If you're stuck on a concept:
1. Check the relevant guide's Summary section
2. Review the worked examples
3. Try a simpler version of the problem
4. Consult your lecture notes
5. Ask in lab sessions (for concepts, not solutions!)

---

## ✅ Quality Checked

All materials have been:
- ✅ Spell-checked and proofread
- ✅ Code examples tested
- ✅ Formulas verified
- ✅ Converted to multiple formats
- ✅ Optimized for readability

---

## 📅 Last Updated

**Date**: November 25, 2025
**Version**: 1.0
**Format**: Markdown → DOCX → HTML → PDF

---

## 🙏 Final Note

These materials represent comprehensive coverage of probability concepts for your lab. Use them as **learning resources** to deeply understand the material, then apply that knowledge to independently solve your lab problems.

**Good luck with your studies!** 🎓✨

---

**Note**: All files are organized and ready to use. No additional setup required!
