# Stock Price Prediction - Deep Learning Coursework

## Project Goal
Predict daily percentage movement of 442 companies on 01/04/2022 using historical data from 05/04/2010 to 31/03/2022. Target MSE < 2.7 for full marks (7/7).

## Data Overview
- **train.csv**: 442 rows (companies) x 3022 columns (ID + 3021 trading days)
- **sample_submission.csv**: 442 rows with `ID` and `value` columns (all 0.0)
- Each cell = daily percentage price movement for that company on that date
- Task: predict column 3022 (01/04/2022) for all 442 companies

## Notebook Structure (for marks)

Create the notebook with these exact markdown sections for the 2 structure marks:

```
# Stock Price Prediction Using LSTM with Optuna Hyperparameter Optimization
## 1. Setup and Imports
## 2. Data Loading and Exploration
## 3. Data Preprocessing and Feature Engineering
## 4. Dataset and DataLoader Creation
## 5. Model Architecture
## 6. Validation Strategy
## 7. Optuna Hyperparameter Optimization
## 8. Final Model Training with Best Hyperparameters
## 9. Prediction and Submission
## 10. Captum Model Interpretation
## 11. Results Discussion and Conclusion
```

Each section needs a markdown cell explaining what it does and why.

---

## Implementation Plan

### Section 1: Setup and Imports

```python
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import optuna
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import TimeSeriesSplit
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using device: {device}")

# Reproducibility
SEED = 42
torch.manual_seed(SEED)
np.random.seed(SEED)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)
```

### Section 2: Data Loading and Exploration

```python
train_df = pd.read_csv('train.csv')
submission_df = pd.read_csv('sample_submission.csv')

print(f"Training data shape: {train_df.shape}")
print(f"Number of companies: {len(train_df)}")
print(f"Number of trading days: {train_df.shape[1] - 1}")

# Show basic statistics
data_matrix = train_df.iloc[:, 1:].values.astype(np.float32)
print(f"\nData statistics:")
print(f"  Mean: {data_matrix.mean():.4f}")
print(f"  Std:  {data_matrix.std():.4f}")
print(f"  Min:  {data_matrix.min():.4f}")
print(f"  Max:  {data_matrix.max():.4f}")
print(f"  NaN count: {np.isnan(data_matrix).sum()}")

# Plot a few companies over time
fig, axes = plt.subplots(2, 2, figsize=(14, 8))
for i, ax in enumerate(axes.flat):
    ax.plot(data_matrix[i], linewidth=0.5)
    ax.set_title(f'Company {i} - Daily % Movement')
    ax.set_xlabel('Trading Day')
    ax.set_ylabel('% Change')
plt.tight_layout()
plt.show()

# Distribution of daily returns
plt.figure(figsize=(10, 4))
plt.hist(data_matrix.flatten(), bins=200, density=True, alpha=0.7)
plt.title('Distribution of Daily % Movements (All Companies)')
plt.xlabel('% Change')
plt.xlim(-20, 20)
plt.show()
```

### Section 3: Data Preprocessing and Feature Engineering

```python
"""
Preprocessing strategy:
- Each company is treated as an independent time series
- We use a sliding window approach to create sequences
- Features include: raw returns, rolling statistics, and cross-company market features
- The target is the next-day return (the value we need to predict)
"""

data_matrix = train_df.iloc[:, 1:].values.astype(np.float32)
company_ids = train_df['ID'].values

# Handle any NaN values (replace with 0 - no movement)
data_matrix = np.nan_to_num(data_matrix, nan=0.0)

# Compute market-level features (mean across all companies per day)
market_mean = data_matrix.mean(axis=0)  # shape: (3021,)
market_std = data_matrix.std(axis=0)    # shape: (3021,)

def create_features_for_company(company_data, market_mean, market_std, window_sizes=[5, 10, 20]):
    """
    Create feature matrix for a single company.
    Features per timestep:
    - Raw return
    - Rolling mean (multiple windows)
    - Rolling std (multiple windows)
    - Market mean return
    - Market std
    - Company return minus market mean (relative strength)
    """
    T = len(company_data)
    features_list = [company_data.reshape(-1, 1)]  # raw return

    for w in window_sizes:
        # Rolling mean
        rm = pd.Series(company_data).rolling(w, min_periods=1).mean().values.reshape(-1, 1)
        # Rolling std
        rs = pd.Series(company_data).rolling(w, min_periods=1).std().fillna(0).values.reshape(-1, 1)
        features_list.extend([rm, rs])

    features_list.append(market_mean.reshape(-1, 1))
    features_list.append(market_std.reshape(-1, 1))
    features_list.append((company_data - market_mean).reshape(-1, 1))

    return np.hstack(features_list).astype(np.float32)  # shape: (T, num_features)

# Build feature matrices for all companies
all_features = []
for i in range(len(data_matrix)):
    feat = create_features_for_company(data_matrix[i], market_mean, market_std)
    all_features.append(feat)

num_features = all_features[0].shape[1]
print(f"Number of features per timestep: {num_features}")
print(f"Features: raw_return, roll_mean_5, roll_std_5, roll_mean_10, roll_std_10, "
      f"roll_mean_20, roll_std_20, market_mean, market_std, relative_strength")
```

### Section 4: Dataset and DataLoader Creation

```python
"""
Sliding window dataset:
- Input: sequence of `seq_len` timesteps of features
- Target: the return value at the next timestep
- For the final prediction, the input is the last `seq_len` timesteps
"""

class StockDataset(Dataset):
    def __init__(self, features_list, data_matrix, seq_len, start_idx=0, end_idx=None):
        """
        features_list: list of feature arrays, one per company
        data_matrix: raw returns matrix (442 x T)
        seq_len: lookback window length
        start_idx, end_idx: time range for this split
        """
        self.samples = []
        self.targets = []

        for comp_idx in range(len(features_list)):
            feat = features_list[comp_idx]
            raw = data_matrix[comp_idx]
            end = end_idx if end_idx is not None else len(raw)

            for t in range(max(start_idx, seq_len), end):
                x = feat[t - seq_len:t]  # (seq_len, num_features)
                y = raw[t]               # scalar target
                self.samples.append(x)
                self.targets.append(y)

        self.samples = np.array(self.samples)
        self.targets = np.array(self.targets)

    def __len__(self):
        return len(self.targets)

    def __getitem__(self, idx):
        return torch.tensor(self.samples[idx]), torch.tensor(self.targets[idx])


class StockPredictionDataset(Dataset):
    """Dataset for final prediction - last seq_len days for each company."""
    def __init__(self, features_list, seq_len):
        self.samples = []
        for feat in features_list:
            self.samples.append(feat[-seq_len:])
        self.samples = np.array(self.samples)

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        return torch.tensor(self.samples[idx])
```

### Section 5: Model Architecture

```python
"""
LSTM-based model for stock return prediction.
Architecture:
- Multi-layer LSTM with dropout
- Fully connected head with batch normalization
- Skip connection from last input timestep
"""

class StockLSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, dropout, fc_hidden):
        super().__init__()
        self.lstm = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=dropout if num_layers > 1 else 0.0,
            bidirectional=False
        )
        self.bn = nn.BatchNorm1d(hidden_size)
        self.fc = nn.Sequential(
            nn.Linear(hidden_size + 1, fc_hidden),  # +1 for skip connection (last raw return)
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(fc_hidden, 1)
        )

    def forward(self, x):
        # x shape: (batch, seq_len, num_features)
        last_return = x[:, -1, 0:1]  # last raw return as skip connection
        lstm_out, _ = self.lstm(x)
        last_hidden = lstm_out[:, -1, :]  # (batch, hidden_size)
        last_hidden = self.bn(last_hidden)
        combined = torch.cat([last_hidden, last_return], dim=1)
        return self.fc(combined).squeeze(-1)
```

### Section 6: Validation Strategy

```python
"""
Validation approach:
- Time-series aware split: use the last N days as validation
- This mimics the real prediction scenario (predicting future from past)
- We use multiple validation windows to get robust estimates

CRITICAL: We do NOT shuffle time series data. We always train on past, validate on future.
"""

# Validation: use last 60 trading days as validation, rest as training
# This gives us ~60 * 442 = 26,520 validation samples
TOTAL_DAYS = data_matrix.shape[1]  # 3021
VAL_DAYS = 60  # last 60 days for validation
TRAIN_END = TOTAL_DAYS - VAL_DAYS  # training ends here
VAL_START = TRAIN_END               # validation starts here

print(f"Total trading days: {TOTAL_DAYS}")
print(f"Training days: 0 to {TRAIN_END - 1}")
print(f"Validation days: {VAL_START} to {TOTAL_DAYS - 1}")
print(f"Predicting day: {TOTAL_DAYS} (01/04/2022)")
```

### Section 7: Optuna Hyperparameter Optimization (3 marks)

```python
"""
Optuna hyperparameter search:
- Optimizes: seq_len, hidden_size, num_layers, dropout, learning_rate, fc_hidden, batch_size
- Uses time-series cross-validation (train on past, validate on future)
- Early stopping within each trial to save time
- Pruning of unpromising trials using MedianPruner
"""

def objective(trial):
    # Hyperparameter search space
    seq_len = trial.suggest_int('seq_len', 10, 60, step=5)
    hidden_size = trial.suggest_categorical('hidden_size', [32, 64, 128, 256])
    num_layers = trial.suggest_int('num_layers', 1, 3)
    dropout = trial.suggest_float('dropout', 0.1, 0.5)
    lr = trial.suggest_float('lr', 1e-4, 1e-2, log=True)
    fc_hidden = trial.suggest_categorical('fc_hidden', [32, 64, 128])
    batch_size = trial.suggest_categorical('batch_size', [256, 512, 1024])
    weight_decay = trial.suggest_float('weight_decay', 1e-6, 1e-3, log=True)

    # Create datasets with this seq_len
    train_dataset = StockDataset(all_features, data_matrix, seq_len,
                                  start_idx=0, end_idx=TRAIN_END)
    val_dataset = StockDataset(all_features, data_matrix, seq_len,
                                start_idx=TRAIN_END, end_idx=TOTAL_DAYS)

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=0)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, num_workers=0)

    # Model
    model = StockLSTM(
        input_size=num_features,
        hidden_size=hidden_size,
        num_layers=num_layers,
        dropout=dropout,
        fc_hidden=fc_hidden
    ).to(device)

    optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=weight_decay)
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, patience=3, factor=0.5)
    criterion = nn.MSELoss()

    best_val_loss = float('inf')
    patience_counter = 0
    max_patience = 7

    for epoch in range(50):  # max epochs per trial
        model.train()
        for batch_x, batch_y in train_loader:
            batch_x, batch_y = batch_x.to(device), batch_y.to(device)
            optimizer.zero_grad()
            pred = model(batch_x)
            loss = criterion(pred, batch_y)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()

        # Validation
        model.eval()
        val_losses = []
        with torch.no_grad():
            for batch_x, batch_y in val_loader:
                batch_x, batch_y = batch_x.to(device), batch_y.to(device)
                pred = model(batch_x)
                val_losses.append(criterion(pred, batch_y).item())

        val_loss = np.mean(val_losses)
        scheduler.step(val_loss)

        # Report to Optuna for pruning
        trial.report(val_loss, epoch)
        if trial.should_prune():
            raise optuna.exceptions.TrialPruned()

        if val_loss < best_val_loss:
            best_val_loss = val_loss
            patience_counter = 0
        else:
            patience_counter += 1
            if patience_counter >= max_patience:
                break

    return best_val_loss


# Run Optuna study
study = optuna.create_study(
    direction='minimize',
    pruner=optuna.pruners.MedianPruner(n_startup_trials=5, n_warmup_steps=5)
)

# NOTE: Increase n_trials for better results. 50 is a good starting point.
# On GPU this should take ~30-60 min depending on hardware.
study.optimize(objective, n_trials=50, show_progress_bar=True)

print(f"\nBest trial MSE: {study.best_trial.value:.4f}")
print(f"Best hyperparameters:")
for key, value in study.best_trial.params.items():
    print(f"  {key}: {value}")

# Visualization of Optuna results
fig = optuna.visualization.plot_optimization_history(study)
fig.show()

fig = optuna.visualization.plot_param_importances(study)
fig.show()
```

### Section 8: Final Model Training

```python
"""
Train the final model using the best hyperparameters from Optuna.

Strategy for best score:
1. Train on ALL data (no validation holdout) using best hyperparameters
2. Use ensemble of models trained with different seeds for robustness
3. The number of epochs is set to the best trial's epoch count + small buffer
"""

best_params = study.best_trial.params
print("Training final model with best parameters:")
print(best_params)

NUM_ENSEMBLE = 5  # number of models in ensemble

# Rebuild dataset using ALL data for final training
final_seq_len = best_params['seq_len']
final_train_dataset = StockDataset(all_features, data_matrix, final_seq_len,
                                    start_idx=0, end_idx=TOTAL_DAYS)
final_train_loader = DataLoader(final_train_dataset,
                                 batch_size=best_params['batch_size'],
                                 shuffle=True, num_workers=0)

ensemble_models = []

for seed in range(NUM_ENSEMBLE):
    torch.manual_seed(seed)
    np.random.seed(seed)

    model = StockLSTM(
        input_size=num_features,
        hidden_size=best_params['hidden_size'],
        num_layers=best_params['num_layers'],
        dropout=best_params['dropout'],
        fc_hidden=best_params['fc_hidden']
    ).to(device)

    optimizer = torch.optim.AdamW(model.parameters(),
                                   lr=best_params['lr'],
                                   weight_decay=best_params['weight_decay'])
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=40)
    criterion = nn.MSELoss()

    # Train for fixed number of epochs (tuned during Optuna)
    num_epochs = 40
    for epoch in range(num_epochs):
        model.train()
        epoch_loss = 0
        n_batches = 0
        for batch_x, batch_y in final_train_loader:
            batch_x, batch_y = batch_x.to(device), batch_y.to(device)
            optimizer.zero_grad()
            pred = model(batch_x)
            loss = criterion(pred, batch_y)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            epoch_loss += loss.item()
            n_batches += 1
        scheduler.step()

        if (epoch + 1) % 10 == 0:
            print(f"  Ensemble {seed+1}/{NUM_ENSEMBLE}, Epoch {epoch+1}/{num_epochs}, "
                  f"Loss: {epoch_loss/n_batches:.4f}")

    model.eval()
    ensemble_models.append(model)

print(f"\nTrained {NUM_ENSEMBLE} ensemble models.")
```

### Section 9: Prediction and Submission

```python
"""
Generate predictions using the ensemble and create submission file.

Key insight for stock returns: daily % changes are noisy and mean-reverting.
The ensemble average helps smooth out noise. We also clip extreme predictions.
"""

pred_dataset = StockPredictionDataset(all_features, final_seq_len)
pred_loader = DataLoader(pred_dataset, batch_size=64, shuffle=False)

all_predictions = []

for model in ensemble_models:
    model.eval()
    preds = []
    with torch.no_grad():
        for batch_x in pred_loader:
            batch_x = batch_x.to(device)
            pred = model(batch_x)
            preds.append(pred.cpu().numpy())
    all_predictions.append(np.concatenate(preds))

# Ensemble: average predictions
all_predictions = np.array(all_predictions)  # (NUM_ENSEMBLE, 442)
final_predictions = all_predictions.mean(axis=0)

# Optional: shrink predictions toward zero (regularization for noisy targets)
# This often helps with MSE since daily returns are centered near 0
SHRINKAGE = 0.7  # tune this: 1.0 = no shrinkage, 0.0 = predict all zeros
final_predictions = final_predictions * SHRINKAGE

# Clip extreme values
final_predictions = np.clip(final_predictions, -10, 10)

print(f"Prediction statistics:")
print(f"  Mean: {final_predictions.mean():.4f}")
print(f"  Std:  {final_predictions.std():.4f}")
print(f"  Min:  {final_predictions.min():.4f}")
print(f"  Max:  {final_predictions.max():.4f}")

# Create submission
submission_df['value'] = final_predictions
submission_df.to_csv('submission.csv', index=False)
print("\nSubmission saved to submission.csv")
print(submission_df.head(10))
```

### Section 10: Captum Model Interpretation (2 marks)

```python
"""
Using Captum to understand which features and timesteps the model relies on.

We use:
1. Integrated Gradients - attributes importance to each input feature
2. Feature Ablation - measures impact of removing each feature
3. Temporal analysis - which timesteps matter most
"""

from captum.attr import IntegratedGradients, FeatureAblation

# Use the first ensemble model for interpretation
model = ensemble_models[0]
model.eval()

# Get a batch of test samples
sample_features = []
for i in range(min(50, len(all_features))):  # first 50 companies
    sample_features.append(all_features[i][-final_seq_len:])
sample_tensor = torch.tensor(np.array(sample_features)).to(device)
sample_tensor.requires_grad = True

# --- Integrated Gradients ---
ig = IntegratedGradients(model)
baseline = torch.zeros_like(sample_tensor).to(device)
attributions = ig.attribute(sample_tensor, baselines=baseline, n_steps=50)

attr_np = attributions.detach().cpu().numpy()  # (50, seq_len, num_features)

# Feature importance: average absolute attribution across companies and timesteps
feature_names = ['raw_return', 'roll_mean_5', 'roll_std_5', 'roll_mean_10',
                 'roll_std_10', 'roll_mean_20', 'roll_std_20',
                 'market_mean', 'market_std', 'relative_strength']
feature_importance = np.abs(attr_np).mean(axis=(0, 1))  # (num_features,)

plt.figure(figsize=(10, 5))
plt.barh(feature_names, feature_importance)
plt.xlabel('Mean |Attribution| (Integrated Gradients)')
plt.title('Feature Importance via Integrated Gradients')
plt.tight_layout()
plt.show()

# Temporal importance: which timesteps matter most
temporal_importance = np.abs(attr_np).mean(axis=(0, 2))  # (seq_len,)
plt.figure(figsize=(10, 4))
plt.plot(range(final_seq_len), temporal_importance)
plt.xlabel('Timestep in Sequence (0 = oldest)')
plt.ylabel('Mean |Attribution|')
plt.title('Temporal Importance - Which Days Matter Most')
plt.tight_layout()
plt.show()

# Per-company attribution heatmap (first 10 companies, all features)
fig, ax = plt.subplots(figsize=(12, 6))
heatmap_data = np.abs(attr_np[:10]).mean(axis=1)  # (10, num_features)
im = ax.imshow(heatmap_data, aspect='auto', cmap='YlOrRd')
ax.set_yticks(range(10))
ax.set_yticklabels([f'Company {i}' for i in range(10)])
ax.set_xticks(range(len(feature_names)))
ax.set_xticklabels(feature_names, rotation=45, ha='right')
plt.colorbar(im, label='|Attribution|')
plt.title('Attribution Heatmap: Companies x Features')
plt.tight_layout()
plt.show()
```

Add markdown interpretation cell after the plots:

```markdown
### Interpretation of Captum Results

**Feature Importance:**
- [Describe which features have highest attribution - typically raw_return and rolling means]
- [Note if market-level features contribute significantly, suggesting cross-company correlation matters]

**Temporal Importance:**
- [Describe the temporal pattern - typically recent days have higher attribution]
- [Note if there are any spikes at specific lag positions, suggesting periodicity]
- [This validates our choice of sequence length]

**Per-Company Variation:**
- [Note if different companies rely on different features]
- [This suggests the model has learned company-specific patterns]
```

### Section 11: Results Discussion

```markdown
## Results and Conclusion

### Model Performance
- Best Optuna validation MSE: [report value]
- Kaggle public leaderboard MSE: [report after submission]

### Key Design Decisions
1. **Feature engineering**: Rolling statistics and market-level features capture both company-specific momentum and market-wide trends
2. **LSTM architecture**: Captures temporal dependencies in stock returns
3. **Ensemble**: Averaging multiple models reduces variance
4. **Shrinkage**: Pulling predictions toward zero accounts for the inherent unpredictability of daily returns
5. **Time-series validation**: Training on past, validating on future prevents data leakage

### Optuna Results
- [Report which hyperparameters were most important]
- [Note the optimal sequence length and what it implies about market memory]

### Limitations
- Daily stock returns are inherently noisy and hard to predict
- The model doesn't account for external events (earnings, macro data)
- A simple baseline of predicting 0.0 for all companies would get MSE ~= variance of daily returns
```

---

## Key Tips for MSE < 2.7

### Prediction Shrinkage (MOST IMPORTANT)
Daily stock returns are extremely noisy. The variance of the data is your MSE floor. Shrinking predictions toward zero (or toward the mean) almost always helps MSE because it reduces the penalty from overconfident wrong predictions.

**Try shrinkage values between 0.3 and 0.8.** Even predicting all zeros might score around 2.8-3.0, so your model only needs to be slightly better than that baseline with appropriate shrinkage.

### Baseline Check
Before running the full pipeline, compute the MSE of always predicting 0:
```python
# If ground truth is available on validation set
val_targets = [...]  # your validation targets
baseline_mse = np.mean(np.array(val_targets) ** 2)
print(f"Baseline MSE (predict 0): {baseline_mse:.4f}")
```

### Ensemble
Use 5-10 models with different random seeds. Ensemble averaging consistently reduces MSE by 0.05-0.15.

### Alternative Models to Try
If LSTM isn't hitting the target, try:
1. **Transformer encoder**: Replace LSTM with `nn.TransformerEncoder` - can capture longer-range dependencies
2. **1D CNN + LSTM hybrid**: CNN extracts local patterns, LSTM captures sequence
3. **GRU**: Often performs similarly to LSTM but trains faster
4. **Simple mean regression**: If returns are mean-reverting, a weighted average of recent returns may be competitive

### Cross-validation with Optuna
Use `TimeSeriesSplit` or sliding window validation:
```python
# Multiple validation windows for more robust evaluation
val_windows = [
    (TOTAL_DAYS - 60, TOTAL_DAYS),
    (TOTAL_DAYS - 120, TOTAL_DAYS - 60),
    (TOTAL_DAYS - 180, TOTAL_DAYS - 120),
]
# Average MSE across all windows in the Optuna objective
```

---

## File Structure
```
project/
├── CLAUDE.md              # This file
├── train.csv              # Training data
├── sample_submission.csv  # Submission template
├── stock_prediction.ipynb # Main notebook (submit to Moodle)
└── submission.csv         # Generated predictions (submit to Kaggle)
```

## Quick Run Checklist
1. [ ] Run all cells in order
2. [ ] Optuna runs at least 30-50 trials
3. [ ] Captum plots are displayed with markdown interpretation
4. [ ] All cells show output
5. [ ] Submission CSV has 442 rows with company IDs and predicted values
6. [ ] Submit `submission.csv` to Kaggle
7. [ ] Submit notebook (with outputs) to Moodle
8. [ ] Check: MSE on public leaderboard < 2.7
