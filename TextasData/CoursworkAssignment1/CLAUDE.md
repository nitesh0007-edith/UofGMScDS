# CLAUDE.md — Text-as-Data Coursework 1

## Project Overview

You are helping Nitesh complete Coursework 1 for the **Text-as-Data** module (MSc Data Science, University of Glasgow). Deadline: **19 March 2026, 4:30pm**. Worth **18%** of the final course mark. Solo work. Cannot be re-assessed.

**Scenario:** You are a "fixer" diagnosing problems with ML email-classification pipelines built for 7 fictitious clients. You have access to trained models and datasets but NOT the training code. You do NOT need to train any models.

**Email categories (5 classes, same for all clients):**

| Label | Description |
|---|---|
| Client & Partner Communications | Customers/partners re: relationships, projects, support |
| HR & Internal Admin | Hiring, policies, benefits, internal announcements |
| Operations & Maintenance | Daily ops, issue resolution, maintenance updates |
| Product & Engineering | Building, improving, maintaining products/systems |
| Sales & Marketing | Sales activities, marketing campaigns, lead engagement |

## Data & Model Access

Everything is on HuggingFace under the `TextAsData` org: <https://huggingface.co/TextAsData>

### Models (all ~0.1B params, text-classification)
- `TextAsData/Q2-NeuroBloom-model` (~86.9M)
- `TextAsData/Q3-HydroVine-model`
- `TextAsData/Q4-LumenGrid-model`
- `TextAsData/Q5-AeroSynth-model`
- `TextAsData/Q6-CryoNest-model`
- `TextAsData/Q7-NeonPixel-model`
- `TextAsData/Q8-SolaraMesh-model`

### Datasets
- `TextAsData/Q1-OrbitalForge-dataset` (tokenized only, no raw text)
- `TextAsData/Q2-NeuroBloom-dataset`
- `TextAsData/Q3-HydroVine-dataset`
- `TextAsData/Q4-LumenGrid-dataset`
- `TextAsData/Q5-AeroSynth-dataset`
- `TextAsData/Q6-CryoNest-dataset`
- `TextAsData/Q7-NeonPixel-dataset`
- `TextAsData/Q8-SolaraMesh-dataset`

### Python Access Pattern
```python
from datasets import load_dataset
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

# Load dataset
ds = load_dataset("TextAsData/Q3-HydroVine-dataset")

# Load model + tokenizer
model = AutoModelForSequenceClassification.from_pretrained("TextAsData/Q3-HydroVine-model")
tokenizer = AutoTokenizer.from_pretrained("TextAsData/Q3-HydroVine-model")

# Quick inference pipeline
clf = pipeline("text-classification", model=model, tokenizer=tokenizer)
```

## Questions & What to Investigate

### Q1 — OrbitalForge [2 marks]
**Task:** Identify which tokenizer was used. The dataset is already tokenized (no raw text). Match the token IDs against one of these candidate tokenizers:
- `roberta-base`
- `microsoft/deberta-base`
- `bert-base-uncased`
- `distilbert-base-uncased`
- `bert-base-cased`
- `allenai/scibert_scivocab_uncased`

**Approach:** Load each candidate tokenizer, compare vocab size, special token IDs (CLS, SEP, PAD), and decode sample token sequences to see which produces coherent text.

### Q2 — NeuroBloom [3 marks]
**Task:** A "brand-new BERT from scratch" with a "bespoke tokenizer" was claimed. Find what's wrong with the tokenizer.

**Approach:** Load the tokenizer from `TextAsData/Q2-NeuroBloom-model`. Inspect vocab, special tokens, coverage. Try encoding sample texts and look for anomalies (e.g., excessive `[UNK]` tokens, tiny vocab, tokenizer not actually trained on relevant data, mismatch between tokenizer vocab and model embeddings).

### Q3 — HydroVine [4 marks]
**Task:** The model isn't performing well. Diagnose why.

**Report:** macro-F1 and accuracy for train/val/test to 3 decimal places.

**Approach:** Evaluate the model on all splits. Investigate: label mapping issues, class imbalance, wrong label encoding, data leakage absence, model architecture problems, tokenizer mismatches.

### Q4 — LumenGrid [4 marks]
**Task:** Client says deployed performance doesn't match reported test performance. Evaluate and decide if something is wrong.

**Report:** macro-F1 and accuracy for train/val/test to 3 decimal places.

**Approach:** Evaluate model on all splits. Look for: data leakage (test data in training set), overfitting, label leakage, shuffling issues, suspiciously high test performance that wouldn't generalise.

### Q5 — AeroSynth [6 marks] ⭐ highest weight
**Task:** Client encountered "unusual performance results." Find what's unusual and what causes it.

**Report:** macro-F1 and accuracy for train/val/test to 3 decimal places.

**Approach:** Evaluate across splits. Look for: surprising discrepancies between metrics, per-class performance anomalies, data contamination, adversarial examples, label noise, distribution shift between splits.

### Q6 — CryoNest [4 marks]
**Task:** Client believes there's a dataset problem causing evaluation issues. Diagnose it.

**Report:** macro-F1 and accuracy for train/val/test to 3 decimal places.

**Approach:** Inspect the dataset closely. Look for: mislabelled examples, duplicate entries across splits, corrupted text, wrong split assignments, class distribution anomalies, label encoding mismatches.

### Q7 — NeonPixel [5 marks]
**Task:** Is the model ready to deploy? If not, what's the issue?

**Report:** macro-F1 and accuracy for train/val/test to 3 decimal places.

**Approach:** Full evaluation + deployment readiness check. Consider: performance thresholds, confidence calibration, edge cases, model robustness, whether the model generalises to unseen data.

### Q8 — SolaraMesh [5 marks]
**Task:** Client was told 94% accuracy and ready to deploy. Was this reported in good faith?

**Report:** macro-F1 and accuracy for train/val/test to 3 decimal places.

**Approach:** Reproduce the 94% claim. Investigate: was accuracy cherry-picked from the best split, was a misleading metric used, is there class imbalance making accuracy deceptive (compare with macro-F1), was evaluation done on training data.

### Q9 — Time Taken [0 marks]
Just log hours spent.

## Evaluation Code Template

Use this pattern for all questions requiring metric reporting:

```python
import numpy as np
from datasets import load_dataset
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
from sklearn.metrics import f1_score, accuracy_score

def evaluate_model(model_name, dataset_name):
    ds = load_dataset(dataset_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    clf = pipeline("text-classification", model=model, tokenizer=tokenizer, device=-1, batch_size=32)

    # Check model's label mapping
    print("Label mapping:", model.config.id2label)

    results = {}
    for split_name in ["train", "validation", "test"]:
        if split_name not in ds:
            print(f"  {split_name}: NOT FOUND")
            continue
        split = ds[split_name]
        texts = split["text"]
        true_labels = split["label"]

        preds = clf(texts, truncation=True, max_length=512)
        pred_labels = [p["label"] for p in preds]

        # Map string labels to ints if needed (match against true_labels format)
        # Adjust this mapping based on model.config.id2label

        acc = accuracy_score(true_labels, pred_labels_int)
        f1 = f1_score(true_labels, pred_labels_int, average="macro")
        results[split_name] = {"accuracy": round(acc, 3), "macro_f1": round(f1, 3)}
        print(f"  {split_name}: Accuracy={acc:.3f}, Macro-F1={f1:.3f}")

    return results
```

**Important:** The label mapping between model output labels and dataset integer labels varies per question. Always check `model.config.id2label` and `ds["train"].features["label"]` first.

## Submission Format

Submit through Moodle:
- **Text answers** explaining the diagnosis for each question
- **Associated code** for each question

## Key Principles

1. **Do NOT train any models.** Only load and evaluate existing ones.
2. **Always report metrics to 3 decimal places** (macro-F1 and accuracy, per split).
3. **Be a detective.** The problems could be in: tokenizer, labels, data splits, model config, data quality, or evaluation methodology.
4. **Check label mappings carefully.** Mismatched id2label configs are a common source of apparent poor performance.
5. **Compare macro-F1 vs accuracy.** Large gaps suggest class imbalance issues.
6. **Inspect the data.** Look at class distributions, duplicates across splits, text quality, and label correctness.
7. **Check tokenizer-model compatibility.** Vocab size mismatches, wrong special tokens, or untrained tokenizers will cause issues.

## File Structure
```
coursework/
├── CLAUDE.md          # This file
├── q1_orbitalforge.py
├── q2_neurobloom.py
├── q3_hydrovine.py
├── q4_lumengrid.py
├── q5_aerosynth.py
├── q6_cryonest.py
├── q7_neonpixel.py
├── q8_solaramesh.py
├── answers.md         # Written answers for all questions
└── requirements.txt   # transformers, datasets, scikit-learn, torch
```

## Dependencies
```
transformers
datasets
torch
scikit-learn
numpy
```
