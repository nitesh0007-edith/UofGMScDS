# MSc Data Science — University of Glasgow

> Coursework, lecture notes, lab notebooks, past papers, and projects from my **Master of Science in Data Science** at the **University of Glasgow**, School of Computing Science (2025–2026).

![University](https://img.shields.io/badge/University-Glasgow-003865?style=flat-square)
![Degree](https://img.shields.io/badge/Degree-MSc%20Data%20Science-blue?style=flat-square)
![Year](https://img.shields.io/badge/Year-2025--2026-green?style=flat-square)
![Modules](https://img.shields.io/badge/Modules-10-orange?style=flat-square)

---

## Table of Contents

- [About](#about)
- [Modules](#modules)
- [Key Projects & Coursework](#key-projects--coursework)
- [Topics Covered](#topics-covered)
- [Exam Preparation Resources](#exam-preparation-resources)
- [Student](#student)

---

## About

This repository contains all my coursework and study materials for the **MSc Data Science** programme at the **University of Glasgow**. It includes:

- Weekly lecture slides and notes
- Lab notebooks (Jupyter / Python / Java)
- Assessed coursework and group projects
- Past exam papers with solutions (2019–2025)
- Exam revision notes, cheatsheets, and study guides
- Optional reading papers (Attention Is All You Need, Seq2Seq, NMT, etc.)

The programme covers the full data science pipeline — from foundational programming and databases through to deep learning, NLP, information retrieval, and data visualisation.

---

## Modules

| Folder | Module Code | Module Name | Contents |
|--------|------------|-------------|----------|
| [`BigData/`](./BigData) | COMPSCI5080 | Big Data | Lectures (Weeks 1–10), MapReduce exercises, Hadoop, past papers, revision notes |
| [`CyberSecurityFundamentals/`](./CyberSecurityFundamentals) | COMPSCI5063 | Cyber Security Fundamentals | Lecture notes (9 topics), lab report, past papers, cheatsheets |
| [`DS/`](./DS) | COMPSCI5048 | Introduction to Data Science & Systems (IDSS) | Lecture notes, Lab 3 probabilistic inference, past papers 2019–2025 |
| [`DeepLearning/`](./DeepLearning) | COMPSCI5103 | Deep Learning for MSc | Lectures, CNN/RNN labs, Kaggle coursework, mock papers, crib sheet |
| [`IR/`](./IR) | COMPSCI5011 | Information Retrieval | Lectures, coursework 1 & 2, IR textbooks, past papers, cheatsheets |
| [`IV/`](./IV) | COMPSCI5050 | Information Visualisation | Group project dashboard (Altair/Vega-Lite), tutorials, exam prep |
| [`MLAI/`](./MLAI%20) | COMPSCI5049 | Machine Learning & AI for Data Science | Lectures, ECG explainability project, PCA 3D shape analysis, past papers |
| [`ProgSD/`](./ProgSD) | COMPSCI5062 | Programming for Software Development | Java exam solutions (2019–2025), Python labs, cheatsheets |
| [`RPS/`](./RPS) | COMPSCI5061 | Research and Professional Skills | Weekly lectures, handouts, past papers, exam guides |
| [`TextasData/`](./TextasData) | COMPSCI5106 | Text as Data (NLP) | Labs 0–6, coursework 1 & 2, lecture PDFs, past papers, study guides |

---

## Key Projects & Coursework

### 🧠 Deep Learning — Stock Market Daily Return Prediction
**File:** [`DeepLearning/stock-market-daily-return-prediction_Nitesh_3090808S.ipynb`](./DeepLearning/stock-market-daily-return-prediction_Nitesh_3090808S.ipynb)  
Kaggle-assessed coursework using deep neural networks (LSTM/RNN) to predict daily stock market returns from historical time-series data.

### ❤️ Explainable ML — ECG Arrhythmia Classification
**Folder:** [`MLAI/ECG_Explainable_Machine_Learning/`](./MLAI%20/ECG_Explainable_Machine_Learning/)  
Group coursework classifying heartbeat types on the MIT-BIH arrhythmia dataset, with model explanations generated using **LIME** and **SHAP**. Includes full report, preprocessing notebooks, and results.

### 📐 PCA on 3D Shape Analysis — Lumbar Spine Meshes
**Folder:** [`MLAI/PCA_in_3D_Shape_Analysis/`](./MLAI%20/PCA_in_3D_Shape_Analysis%E2%80%8B/)  
Applied Principal Component Analysis to 3D lumbar spine mesh sequences to identify dominant modes of anatomical shape variation. Includes animated GIFs of principal components.

### 📊 Information Visualisation — Happiness Data Dashboard
**Folder:** [`IV/GroupProject_IV_2026/`](./IV/GroupProject_IV_2026/)  
Group project building an interactive multi-system visualisation dashboard using **Python Altair** and **Vega-Lite**, exploring global happiness data across three linked visualisation systems.

### 🔍 Information Retrieval — IR System Notebooks
**Folders:** [`IR/CourseWork1/`](./IR/CourseWork1/) · [`IR/coursework2/`](./IR/coursework2/)  
Hands-on implementation of IR concepts — indexing, ranking (TF-IDF, BM25), evaluation metrics (MAP, NDCG), and query expansion using Python and PyTerrier.

### 🌊 IDSS — Probabilistic Inference (Submarine Search)
**Folder:** [`DS/idss_lab3_probability_v20252026a/`](./DS/idss_lab3_probability_v20252026a/)  
Lab implementing Bayesian search for a lost submarine using PMFs, conditional probability, Bayes' Rule, entropy, and Monte Carlo sampling.

---

## Topics Covered

### Machine Learning & AI
`Regression` · `Classification` · `SVMs` · `K-Means Clustering` · `Gaussian Mixture Models` · `PCA` · `Kernel Methods` · `LIME` · `SHAP` · `Explainable AI`

### Deep Learning
`MLPs` · `Backpropagation` · `CNNs` · `RNNs` · `LSTMs` · `Seq2Seq` · `Attention Mechanisms` · `Transformers` · `Autoencoders` · `VAEs` · `GANs` · `Transfer Learning`

### Natural Language Processing / Text as Data
`Tokenization` · `TF-IDF` · `Language Models` · `N-grams` · `Text Classification` · `Word2Vec` · `GloVe` · `BERT` · `Contextual Embeddings` · `Dependency Parsing` · `Named Entity Recognition` · `Large Language Models`

### Information Retrieval
`Inverted Index` · `Boolean Retrieval` · `Vector Space Model` · `BM25` · `Evaluation (MAP, NDCG)` · `Query Expansion` · `Dense Retrieval` · `Neural IR` · `PageRank` · `PyTerrier`

### Big Data
`Hadoop` · `HDFS` · `MapReduce` · `Apache Spark` · `NoSQL` · `Stream Processing` · `Distributed Systems`

### Data Systems
`Relational Databases` · `SQL` · `Indexing` · `Query Optimisation` · `Probabilistic Reasoning` · `Bayesian Inference` · `Monte Carlo Methods` · `Information Theory`

### Information Visualisation
`Vega-Lite` · `Altair` · `D3.js` · `Visual Encoding` · `Interaction Design` · `Dashboard Design` · `Perception & Cognition`

### Cyber Security
`Access Control` · `Cryptography` · `Authentication` · `Digital Forensics` · `Web Application Security` · `Phishing Analysis` · `OWASP`

### Programming
`Java OOP` · `Data Structures & Algorithms` · `Python` · `Pandas` · `NumPy` · `SQLite` · `Jupyter Notebooks`

---

## Exam Preparation Resources

Each module folder contains dedicated exam prep materials:

| Module | Resources |
|--------|-----------|
| Big Data | Crib sheet, revision notes (v2, v3), past papers 2015–2025 |
| Cyber Security | Past papers 2021–2025, exam solutions, cheatsheets |
| Deep Learning | Crib sheet, mock papers (x2), beginner guide, past papers 2021–2024 |
| Information Retrieval | 5 cheatsheet variants, mock exams A & B, past paper solutions 2022–2025 |
| Information Visualisation | Exam notes, 4 cheatsheet variants, example questions, practice solutions |
| ML & AI | Past papers 2019–2025 with solutions, exam-day cheatsheet |
| IDSS | Past papers 2019–2025 with solutions |
| Text as Data | Study guide, crib sheet, handwritten notes, past papers 2022–2025 |
| RPS | Past papers 2022–2024, exam question guides |
| ProgSD | Java solutions 2019–2025, Python cheatsheet |

---

## Repository Structure

```
UofGMScDS/
├── BigData/                  # Big Data
│   ├── Lecture/              # Weekly slides (Weeks 1–10)
│   ├── Exercise/             # Assessed exercise + Hadoop code
│   ├── Notes/                # Revision notes & crib sheets
│   └── LastYearExamPaper/    # Past papers 2015–2025
├── CyberSecurityFundamentals/
│   ├── Notes/                # Interactive HTML lecture notes
│   ├── LabGroupReport/       # Phishing email forensics lab
│   └── ExamPrep/             # Past papers & solutions
├── DS/                       # Intro to Data Science & Systems
│   ├── Data_System/          # Lecture notes
│   ├── idss_lab3_*/          # Lab 3: Probabilistic inference
│   └── IDSS_last_Year_Papers/# Past papers 2019–2025
├── DeepLearning/
│   ├── week_1_5/             # Lecture slides
│   ├── week6_10/             # Lecture slides
│   ├── LAB/ & DLLAB/         # Lab notebooks
│   └── Notes_Exam_Paper_and_Solution/
├── IR/                       # Information Retrieval
│   ├── Lecture_Notes/        # Weekly slides
│   ├── CourseWork1/ & coursework2/
│   ├── Books/                # IR textbooks
│   └── Notes_PastPaper_Solutions/
├── IV/                       # Information Visualisation
│   ├── GroupProject_IV_2026/ # Group dashboard project
│   ├── python_altair_tutorials/
│   ├── javascript_vegalite_tutorials/
│   └── ExamPrep/
├── MLAI/                     # Machine Learning & AI
│   ├── ECG_Explainable_Machine_Learning/
│   ├── PCA_in_3D_Shape_Analysis/
│   └── HTML/ & PastPaperSol/
├── ProgSD/                   # Programming for Software Dev
│   ├── Java/                 # Exam solutions 2019–2025
│   └── Python/               # Lab notebooks & midterm
├── RPS/                      # Research & Professional Skills
│   ├── Week1–Week5/          # Lecture slides
│   ├── Handout/              # Weekly handouts
│   └── RPS_Question_and_Past_Papers/
└── TextasData/               # Text as Data (NLP)
    ├── Lab/                  # Labs 0–6
    ├── LecturePDF/           # Lecture slides
    ├── CoursworkAssignment1/ # Assessed coursework
    ├── PreviousYearPapar&Solution/
    └── Notes/                # Study guides & cheatsheets
```

---

## Student

**Nitesh Ranjan Singh** — Student ID: 3090808S  
MSc Data Science, School of Computing Science, University of Glasgow  
📧 niteshranjansingh85389@gmail.com  

---

*If you find this repository useful for your own studies, feel free to star ⭐ it. These notes are shared for educational purposes.*
