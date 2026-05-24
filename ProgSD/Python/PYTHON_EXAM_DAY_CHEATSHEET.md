# Python Exam Day Cheatsheet - Ultimate Edition
## Data Analysis, Visualization, Database & File Handling

> **Based on**: 2024 Lab Exam + Final.ipynb + All Possible Scenarios
>
> **2024 Exam Pattern**: Task 1 (13 marks) + Task 2 (15 marks) = 28 marks Python portion
>
> ⏰ **YOU HAVE EXACTLY 60 MINUTES!** ⏰

---

## 🚨 ULTRA QUICK START (READ THIS IN 30 SECONDS!)

### ⏱️ ACTUAL EXAM - 3 TASKS (90 Minutes Total!)

**IMPORTANT**: If exam has 3 tasks (90 min) vs 2 tasks (60 min), adjust accordingly!

#### **Option A: 2 Tasks Only (60 min)**
```
✓ 15 min: Task 1a done (load + clean)
✓ 29 min: Task 1b done (2 charts saved)
✓ 48 min: Task 2a done (data in database)
✓ 58 min: Task 2b done (queries run)
✓ 60 min: SUBMIT!
```

#### **Option B: 3 Tasks (90 min - like Final.ipynb)**
```
✓ 15 min: Task 1a done (load + clean)
✓ 30 min: Task 1b done (2 charts saved)
✓ 50 min: Task 2a done (data in database)
✓ 60 min: Task 2b done (queries run)
✓ 78 min: Task 3 done (file handling + stats)
✓ 85 min: Final testing
✓ 90 min: SUBMIT!
```

### 🎯 Critical Success Formula
```python
# 1. IMPORTS (30 sec)
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# 2. LOAD (1 min)
df = pd.read_csv('sales_data.csv', parse_dates=['Date'], dayfirst=True)

# 3. CLEAN (3 min)
df.fillna({'Product': 'Unknown', 'Quantity': 0, 'Price': 0.0, 'Total': 0.0}, inplace=True)
df['Total'] = df['Quantity'] * df['Price']

# 4. CHARTS (14 min)
df.groupby('Product')['Quantity'].sum().plot(kind='bar')
plt.savefig('chart1.png'); plt.show()

df['Month'] = df['Date'].dt.to_period('M')
df.groupby('Month')['Total'].sum().plot(kind='line')
plt.savefig('chart2.png'); plt.show()

# 5. DATABASE (31 min)
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
conn = sqlite3.connect('SalesDB.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Sales (Date TEXT, Product TEXT, Quantity INTEGER, Price REAL, Total REAL)')
for _, row in df.iterrows():
    cursor.execute('INSERT OR IGNORE INTO Sales VALUES (?, ?, ?, ?, ?)',
                   (row['Date'], row['Product'], row['Quantity'], row['Price'], row['Total']))
conn.commit()

# 6. QUERIES (10 min)
cursor.execute("SELECT SUM(Total) FROM Sales WHERE strftime('%Y', Date) = '2023'")
print(cursor.fetchone()[0])
cursor.execute("SELECT Product, SUM(Quantity) FROM Sales WHERE strftime('%Y', Date) = '2023' GROUP BY Product ORDER BY SUM(Quantity) DESC")
for p, q in cursor.fetchall(): print(f"{p}: {q}")
conn.close()
```

### ⚠️ TOP 3 MISTAKES (Don't Do These!)
1. ❌ Forgetting `dayfirst=True` → Dates load wrong!
2. ❌ `plt.show()` before `plt.savefig()` → Charts don't save!
3. ❌ No `conn.commit()` → Data not saved to database!

---

## 🎯 2024 ACTUAL EXAM PATTERN (READ THIS FIRST!)

### Exam Overview
- **Total Time**: **60 MINUTES** for Python portion (Part 1 of full exam)
- **Total Marks**: 28 marks (Task 1: 13 marks, Task 2: 15 marks)
- **Data**: sales_data.csv (Date, Product, Quantity, Price, Total)
- **Year to analyze**: 2023
- **All code in ONE Python file**
- **NO Task 3** - Neural Network task is optional/bonus (skip if short on time!)

### Task 1: Data Manipulation & Visualization (13 marks)
```
Task 1a: Data Loading & Preprocessing (9 marks)
  - Load CSV into DataFrame [2 marks]
  - Fill missing values [3 marks]
  - Convert Date to datetime [2 marks]
  - Validate/correct Total column [2 marks]

Task 1b: Data Visualization (4 marks)
  - Bar chart: Product sales distribution [2 marks]
  - Line plot: Sales over time (2023 monthly) [2 marks]
```

### Task 2: Database Management (15 marks)
```
Task 2a: Database Creation & Insertion (9 marks)
  - Create SQLite database "SalesDB" [2 marks]
  - Create "Sales" table [3 marks]
  - Insert data with NO duplicates [4 marks]

Task 2b: Querying (6 marks)
  - Total sales for 2023 [3 marks]
  - Product sales summary (DESC order) [3 marks]
```

---

## ⏰ EXAM TIME STRUCTURE (60 MINUTES TOTAL)

### Python Portion Time Breakdown
```
YOU HAVE EXACTLY 60 MINUTES FOR PYTHON!

Task 1: Data Analysis & Visualization (45% = ~27 min)
  - Load CSV data
  - Clean and preprocess data
  - Create 2 visualizations (bar, line)

Task 2: Database Management (55% = ~33 min)
  - Create SQLite database
  - Insert data from pandas DataFrame
  - Query with GROUP BY, SUM, ORDER BY

Optional Task 3: Neural Network (SKIP if time-pressured!)
  - This is BONUS/separate marks
  - Focus on Tasks 1 & 2 first
```

### Recommended Time Allocation (60 min)
```
0-2 min     → Read entire exam, plan approach
2-8 min     → Task 1a: Load & fill missing [6 min]
8-15 min    → Task 1a: Convert Date & validate Total [7 min]
15-24 min   → Task 1b: Bar chart [9 min]
24-29 min   → Task 1b: Line plot [5 min]
29-35 min   → Task 2a: Create database & table [6 min]
35-48 min   → Task 2a: Insert data [13 min]
48-55 min   → Task 2b: Run queries [7 min]
55-60 min   → Final checks, verify outputs [5 min]
```

---

## ESSENTIAL IMPORTS (Copy First!)

```python
# Standard imports for EVERY exam
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3
from datetime import datetime, timedelta
import os

# Optional (check exam requirements)
import random
import logging
```

**Time**: 30 seconds - copy this first!

---

## 🔥 2024 EXAM COMPLETE SOLUTION (60 Minutes)

### COPY-PASTE READY SOLUTION for 2024 Pattern

```python
"""
Programming and Systems Development - Python Tasks
Student Name: [YOUR NAME]
Task 1: Data Manipulation & Visualization
Task 2: Database Management
"""

import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# =============================================================================
# TASK 1: PYTHON BASICS AND DATA MANIPULATION [13 MARKS]
# =============================================================================

# -----------------------------------------------------------------------------
# Task 1a: Data Loading and Preprocessing [9 marks]
# -----------------------------------------------------------------------------

# [1] Load the Data [2 marks]
df = pd.read_csv('sales_data.csv', parse_dates=['Date'], dayfirst=True)
print("Data Loaded Successfully")
print(df.head())

# [2] Data Cleaning: Fill missing values [3 marks]
df.fillna({
    'Product': 'Unknown',
    'Quantity': 0,
    'Price': 0.0,
    'Total': 0.0
}, inplace=True)
print("\nMissing values handled")

# [3] Convert Date to datetime object [2 marks]
# Already done during CSV loading with parse_dates parameter
# Keep original datetime for operations
df['Date_original'] = df['Date']
# Create Month period for grouping
df['Month'] = df['Date_original'].dt.to_period('M')
print(f"Date dtype: {df['Date'].dtype}")

# [4] Ensure Total column is correct [2 marks]
df['Total'] = df['Quantity'] * df['Price']
print("\nTotal column validated and corrected")
print(df.head())

# -----------------------------------------------------------------------------
# Task 1b: Data Visualization [4 marks]
# -----------------------------------------------------------------------------

# [1] Product Sales Distribution - Bar Chart [2 marks]
product_sales = df.groupby('Product')['Quantity'].sum()
plt.figure(figsize=(10, 6))
product_sales.plot(
    kind='bar',
    title='Product Sales Distribution',
    ylabel='Total Quantity Sold',
    xlabel='Product',
    color='steelblue',
    edgecolor='black'
)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('product_sales_distribution.png', dpi=150)
plt.show()
print("\n[Task 1b-1] Bar chart saved: product_sales_distribution.png")

# [2] Sales Over Time - Line Plot (2023 monthly) [2 marks]
monthly_sales = df.groupby('Month')['Total'].sum()
plt.figure(figsize=(10, 6))
monthly_sales.plot(
    kind='line',
    title='Total Sales Over Time (2023)',
    ylabel='Total Sales',
    xlabel='Month',
    color='steelblue',
    marker='o',
    linewidth=2
)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('sales_over_time_2023.png', dpi=150)
plt.show()
print("[Task 1b-2] Line chart saved: sales_over_time_2023.png")

# =============================================================================
# TASK 2: PYTHON DATABASE MANAGEMENT [15 MARKS]
# =============================================================================

# Convert Date to string format for database storage
df['Date'] = df['Date_original'].dt.strftime('%Y-%m-%d')

# -----------------------------------------------------------------------------
# Task 2a: Database Creation and Data Insertion [9 marks]
# -----------------------------------------------------------------------------

# [1] Create SQLite database [2 marks]
conn = sqlite3.connect('SalesDB.db')
cursor = conn.cursor()
print("\n[Task 2a-1] Database 'SalesDB.db' created successfully")

# [2] Create Sales table [3 marks]
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Sales (
        Date TEXT,
        Product TEXT,
        Quantity INTEGER,
        Price REAL,
        Total REAL
    )
''')
conn.commit()
print("[Task 2a-2] Table 'Sales' created successfully")

# [3] Insert data with NO duplicates [4 marks]
rows_inserted = 0
for _, row in df.iterrows():
    cursor.execute('''
        INSERT OR IGNORE INTO Sales (Date, Product, Quantity, Price, Total)
        VALUES (?, ?, ?, ?, ?)
    ''', (row['Date'], row['Product'], row['Quantity'], row['Price'], row['Total']))
    if cursor.rowcount > 0:
        rows_inserted += 1

conn.commit()
print(f"[Task 2a-3] Data inserted successfully: {rows_inserted} rows")

# -----------------------------------------------------------------------------
# Task 2b: Querying the Database [6 marks]
# -----------------------------------------------------------------------------

# [1] Total Sales Calculation for 2023 [3 marks]
cursor.execute('''
    SELECT SUM(Total) FROM Sales
    WHERE strftime('%Y', Date) = '2023'
''')
total_sales = cursor.fetchone()[0]
if total_sales is None:
    total_sales = 0
print(f"\n[Task 2b-1] Total Sales in 2023: £{total_sales:.2f}")

# [2] Product Sales Summary in descending order [3 marks]
cursor.execute('''
    SELECT Product, SUM(Quantity) as TotalQuantity
    FROM Sales
    WHERE strftime('%Y', Date) = '2023'
    GROUP BY Product
    ORDER BY TotalQuantity DESC
''')
product_summary = cursor.fetchall()

print("\n[Task 2b-2] Product Sales Summary (2023):")
print("-" * 40)
for product, total_quantity in product_summary:
    print(f"Product: {product:15s} | Total Quantity: {total_quantity}")

# Close database connection
conn.close()
print("\n[INFO] Database connection closed")
print("\n" + "=" * 60)
print("ALL TASKS COMPLETED SUCCESSFULLY!")
print("=" * 60)
```

### ⏰ Precise Time Breakdown (60 min Total)
```
TASK 1: Data Manipulation (27 minutes)
├─ 0-2 min    → Read exam, copy imports
├─ 2-5 min    → Task 1a: Load CSV [2 marks]
├─ 5-9 min    → Task 1a: Fill missing values [3 marks]
├─ 9-12 min   → Task 1a: Convert Date [2 marks]
├─ 12-15 min  → Task 1a: Validate Total [2 marks]
├─ 15-22 min  → Task 1b: Bar chart [2 marks]
└─ 22-29 min  → Task 1b: Line plot [2 marks]

TASK 2: Database (31 minutes)
├─ 29-32 min  → Task 2a: Create database [2 marks]
├─ 32-36 min  → Task 2a: Create table [3 marks]
├─ 36-48 min  → Task 2a: Insert data [4 marks]
├─ 48-53 min  → Task 2b: Query total sales [3 marks]
└─ 53-58 min  → Task 2b: Product summary [3 marks]

FINAL: Verify & Submit (2 minutes)
└─ 58-60 min  → Quick checks, ensure files saved
```

**CRITICAL**: Stick to this timeline! Move on even if not perfect.

### Key Points for 2024 Exam
1. ✅ **Use `parse_dates=['Date'], dayfirst=True`** - Critical for DD/MM/YYYY format
2. ✅ **Keep original datetime** - Create `Date_original` before converting to string
3. ✅ **Use `dt.to_period('M')`** - For monthly grouping
4. ✅ **`INSERT OR IGNORE`** - Prevents duplicate entries
5. ✅ **`strftime('%Y', Date)`** - SQL date filtering for specific year
6. ✅ **All in ONE file** - Not separate scripts
7. ✅ **Close connection** - `conn.close()` at the end

---

## TASK 1: DATA LOADING & CLEANING (15-20 min)

### 1.1 Load CSV File

```python
# Basic load
df = pd.read_csv('filename.csv')

# Load with date parsing (IMPORTANT!)
df = pd.read_csv('sales_data.csv', parse_dates=['Date'], dayfirst=True)

# Load with specific delimiter
df = pd.read_csv('data.csv', delimiter=';')

# Print first rows and shape (ALWAYS required)
print("First 5 rows:")
print(df.head())
print(f"\nDataFrame shape: {df.shape}")  # (rows, columns)
```

**Common Variations:**
- `parse_dates=['Date']` - Convert Date column to datetime
- `dayfirst=True` - For DD/MM/YYYY format (European dates)
- `header=None` - If CSV has no header row
- `names=['col1', 'col2']` - Specify column names

---

### 1.2 Data Cleaning - Handle Missing Values

```python
# METHOD 1: Check for missing values
print("Missing values per column:")
print(df.isnull().sum())

# Total missing values
total_missing = df.isnull().sum().sum()
print(f"Total missing values: {total_missing}")

# METHOD 2: Drop rows with missing values
df = df.dropna()  # Drop any row with ANY missing value
df = df.dropna(subset=['Date'])  # Drop only if Date is missing

# METHOD 3: Fill missing values with specific value
df['Product'].fillna('Unknown', inplace=True)
df['Quantity'].fillna(0, inplace=True)
df['Price'].fillna(0.0, inplace=True)

# METHOD 4: Forward fill (use previous value)
df = df.ffill()

# METHOD 5: Fill with mean/median
df['Price'].fillna(df['Price'].mean(), inplace=True)
df['Quantity'].fillna(df['Quantity'].median(), inplace=True)

# Complete example from exam:
df.fillna({
    'Product': 'Unknown',
    'Quantity': 0,
    'Price': 0.0,
    'Total': 0.0
}, inplace=True)
```

**When to use which method:**
- Drop: When data is critical (like Date column)
- Fill with constant: For categorical data (Product -> 'Unknown')
- Fill with 0: For numerical counts
- Forward fill: For time-series data
- Mean/Median: For continuous numerical data

---

### 1.3 Data Type Conversions

```python
# DATETIME CONVERSION (Most important!)
# Method 1: Using pd.to_datetime
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y', errors='coerce')

# Method 2: During CSV load
df = pd.read_csv('data.csv', parse_dates=['Date'], dayfirst=True)

# Check dtype after conversion
print(f"Date dtype: {df['Date'].dtype}")  # Should be datetime64[ns]

# STRING CLEANING (Always test for!)
df['Incident_Type'] = df['Incident_Type'].str.strip()  # Remove spaces
df['Incident_Type'] = df['Incident_Type'].str.upper()  # Uppercase
df['Product'] = df['Product'].str.lower()  # Lowercase

# NUMERIC CONVERSION
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df['Quantity'] = df['Quantity'].astype(int)

# Drop invalid dates (NaT - Not a Time)
rows_before = len(df)
df = df.dropna(subset=['Date'])
rows_dropped = rows_before - len(df)
print(f"Rows dropped: {rows_dropped}")
```

**Common Date Formats:**
- `%d/%m/%Y` → 25/12/2023
- `%Y-%m-%d` → 2023-12-25
- `%m/%d/%Y` → 12/25/2023
- `errors='coerce'` → Invalid dates become NaT

---

### 1.4 Create Calculated Columns

```python
# Extract year, month, day from datetime
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

# Create Year-Month column (for grouping)
df['YearMonth'] = df['Date'].dt.to_period('M')

# Calculate derived values
df['Total'] = df['Quantity'] * df['Price']

# Create categories based on conditions
df['Category'] = df['Price'].apply(
    lambda x: 'Expensive' if x > 100 else 'Affordable'
)

# Filter data for specific year
df_2025 = df[df['Date'].dt.year == 2025].copy()
df_2023 = df[df['Year'] == 2023].copy()
```

---

### 1.5 Check Unique Values & Data Info

```python
# Unique values in a column
unique_types = df['Incident_Type'].unique()
print(f"Unique incident types: {sorted(unique_types)}")

# Count unique values
print(f"Number of unique products: {df['Product'].nunique()}")

# Value counts (frequency)
print(df['Product'].value_counts())

# DataFrame info
print(df.info())  # Shows dtypes, non-null counts

# Basic statistics
print(df.describe())  # Mean, std, min, max, quartiles
```

---

## TASK 2: DATA VISUALIZATION (15-25 min)

### 2.1 Bar Chart (Most Common!)

```python
# PATTERN 1: Group and sum, then plot
incidents_by_type = df.groupby('Incident_Type')['Count'].sum()
incidents_by_type = incidents_by_type.sort_values(ascending=False)

plt.figure(figsize=(10, 6))
incidents_by_type.plot(
    kind='bar',
    color='steelblue',
    edgecolor='black'
)
plt.title('Total Incidents by Type')
plt.xlabel('Incident Type')
plt.ylabel('Total Incidents')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('incidents_by_type.png', dpi=150)
plt.show()

# PATTERN 2: Using matplotlib directly
product_sales = df.groupby('Product')['Quantity'].sum()
plt.figure(figsize=(10, 6))
plt.bar(product_sales.index, product_sales.values,
        color='steelblue', edgecolor='black')
plt.title('Product Sales Distribution')
plt.xlabel('Product')
plt.ylabel('Total Quantity Sold')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('product_sales.png', dpi=150)
plt.show()
```

**Key Points:**
- Always set `figsize=(10, 6)` for readability
- Use `rotation=45, ha='right'` for diagonal labels
- `tight_layout()` prevents label cutoff
- Save BEFORE `plt.show()`

---

### 2.2 Line Chart (Time Series)

```python
# PATTERN 1: Monthly totals over time
df_2025 = df[df['Date'].dt.year == 2025].copy()
df_2025['YearMonth'] = df_2025['Date'].dt.to_period('M')

monthly_totals = df_2025.groupby('YearMonth')['Count'].sum()

# Ensure all months are represented (fill missing with 0)
all_months = pd.period_range('2025-01', '2025-10', freq='M')
monthly_totals = monthly_totals.reindex(all_months, fill_value=0)

plt.figure(figsize=(10, 6))
plt.plot(
    range(len(monthly_totals)),
    monthly_totals.values,
    marker='o',
    linestyle='-',
    color='steelblue',
    linewidth=2,
    markersize=6
)
plt.title('Monthly Incident Totals (2025)')
plt.xlabel('Month (2025)')
plt.ylabel('Total Incidents')
plt.xticks(range(len(monthly_totals)),
           ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
            'Jul', 'Aug', 'Sep', 'Oct'])
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('monthly_totals_2025.png', dpi=150)
plt.show()

# PATTERN 2: Using pandas plot
monthly_sales = df.groupby('Month')['Total'].sum()
plt.figure(figsize=(10, 6))
monthly_sales.plot(
    kind='line',
    title='Total Sales Over Time',
    ylabel='Total Sales',
    xlabel='Month',
    marker='o'
)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('sales_over_time.png', dpi=150)
plt.show()
```

**Key Points:**
- Use `marker='o'` for data points
- Add `grid=True` for better readability
- `reindex()` to include missing months/dates
- Convert Period to list of strings for x-labels

---

### 2.3 Histogram (Distribution)

```python
# Basic histogram
plt.figure(figsize=(10, 6))
plt.hist(
    df['Height'],
    bins=10,  # Number of bins
    color='steelblue',
    edgecolor='black',
    alpha=0.7
)
plt.title('Height Distribution')
plt.xlabel('Height (cm)')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('height_distribution.png', dpi=100)
plt.show()

# Histogram with custom bins
plt.figure(figsize=(10, 6))
bins = [0, 50, 100, 150, 200, 250]
plt.hist(df['Price'], bins=bins, color='coral', edgecolor='black')
plt.title('Price Distribution')
plt.xlabel('Price Range')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('price_distribution.png')
plt.show()
```

---

### 2.4 Scatter Plot

```python
plt.figure(figsize=(10, 6))
plt.scatter(
    df['Quantity'],
    df['Total'],
    color='steelblue',
    alpha=0.6,
    s=50  # Point size
)
plt.title('Quantity vs Total Sales')
plt.xlabel('Quantity Sold')
plt.ylabel('Total Sales ($)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('quantity_vs_sales.png', dpi=150)
plt.show()
```

---

### 2.5 Pie Chart

```python
# Pie chart for proportions
product_counts = df.groupby('Product')['Quantity'].sum()

plt.figure(figsize=(8, 8))
plt.pie(
    product_counts.values,
    labels=product_counts.index,
    autopct='%1.1f%%',  # Show percentages
    startangle=90,
    colors=['steelblue', 'coral', 'lightgreen', 'gold']
)
plt.title('Product Sales Distribution')
plt.tight_layout()
plt.savefig('product_pie_chart.png', dpi=150)
plt.show()
```

---

### 2.6 Multiple Subplots

```python
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Subplot 1: Bar chart
axes[0, 0].bar(product_sales.index, product_sales.values)
axes[0, 0].set_title('Product Sales')
axes[0, 0].set_xlabel('Product')
axes[0, 0].set_ylabel('Quantity')

# Subplot 2: Line chart
axes[0, 1].plot(monthly_totals.values, marker='o')
axes[0, 1].set_title('Monthly Totals')
axes[0, 1].set_xlabel('Month')
axes[0, 1].set_ylabel('Total')

# Subplot 3: Histogram
axes[1, 0].hist(df['Price'], bins=10, color='coral')
axes[1, 0].set_title('Price Distribution')
axes[1, 0].set_xlabel('Price')
axes[1, 0].set_ylabel('Frequency')

# Subplot 4: Scatter
axes[1, 1].scatter(df['Quantity'], df['Total'])
axes[1, 1].set_title('Quantity vs Total')
axes[1, 1].set_xlabel('Quantity')
axes[1, 1].set_ylabel('Total')

plt.tight_layout()
plt.savefig('combined_plots.png', dpi=150)
plt.show()
```

---

## TASK 3: DATABASE OPERATIONS (20-30 min)

### 3.1 Create Database and Table

```python
# STEP 1: Connect to database (creates if doesn't exist)
conn = sqlite3.connect('DatabaseName.db')
cursor = conn.cursor()
print("Database created successfully.")

# STEP 2: Drop table if exists (for fresh start)
cursor.execute('DROP TABLE IF EXISTS TableName')

# STEP 3: Create table with appropriate columns
cursor.execute('''
    CREATE TABLE TableName (
        Date TEXT,
        System TEXT,
        Incident_Type TEXT,
        Count INTEGER,
        UNIQUE(Date, System, Incident_Type)
    )
''')
conn.commit()
print("Table created successfully.")

# Common column types:
# TEXT - for strings
# INTEGER - for whole numbers
# REAL - for decimals
# BLOB - for binary data
# PRIMARY KEY - unique identifier
# UNIQUE(col1, col2) - composite unique constraint
```

---

### 3.2 Insert Data from DataFrame

```python
# METHOD 1: Loop through DataFrame (SAFEST)
# Prepare DataFrame (convert datetime to string)
df_for_db = df.copy()
df_for_db['Date'] = df_for_db['Date'].dt.strftime('%Y-%m-%d')

# Insert rows
rows_inserted = 0
for _, row in df_for_db.iterrows():
    try:
        cursor.execute('''
            INSERT OR IGNORE INTO Incidents (Date, System, Incident_Type, Count)
            VALUES (?, ?, ?, ?)
        ''', (row['Date'], row['System'], row['Incident_Type'], row['Count']))

        if cursor.rowcount > 0:
            rows_inserted += 1
    except sqlite3.IntegrityError:
        pass  # Skip duplicates

conn.commit()
print(f"Rows inserted: {rows_inserted}")

# METHOD 2: Using to_sql (easier but less control)
df.to_sql('TableName', conn, if_exists='replace', index=False)

# METHOD 3: Bulk insert using executemany
data_tuples = [tuple(row) for row in df_for_db.values]
cursor.executemany('''
    INSERT OR IGNORE INTO Incidents (Date, System, Incident_Type, Count)
    VALUES (?, ?, ?, ?)
''', data_tuples)
conn.commit()
```

**Key Points:**
- Use `?` placeholders (prevents SQL injection)
- `INSERT OR IGNORE` skips duplicates
- Always `conn.commit()` after inserts
- Convert datetime to string before inserting

---

### 3.3 Query Database - Basic SELECT

```python
# SELECT all rows
cursor.execute('SELECT * FROM TableName')
all_rows = cursor.fetchall()
print(all_rows)

# SELECT specific columns
cursor.execute('SELECT Date, System, Count FROM Incidents')
results = cursor.fetchall()

# SELECT with WHERE clause
cursor.execute('''
    SELECT * FROM Incidents
    WHERE Incident_Type = 'FAILED LOGIN'
''')
failed_logins = cursor.fetchall()

# SELECT with date filtering
cursor.execute('''
    SELECT * FROM Incidents
    WHERE Date LIKE '2025%'
''')
incidents_2025 = cursor.fetchall()

# Using strftime for date filtering
cursor.execute('''
    SELECT * FROM Sales
    WHERE strftime('%Y', Date) = '2023'
''')
sales_2023 = cursor.fetchall()

# Fetch methods:
# fetchone() - returns one row (tuple)
# fetchall() - returns all rows (list of tuples)
# fetchmany(n) - returns n rows
```

---

### 3.4 Query with Aggregations (CRITICAL!)

```python
# SUM: Total incidents in 2025
cursor.execute('''
    SELECT SUM(Count) as total_incidents
    FROM Incidents
    WHERE Date LIKE '2025%'
''')
total = cursor.fetchone()[0]
print(f"Total incidents in 2025: {total}")

# Handle NULL from SUM
if total is None:
    total = 0

# COUNT: Number of records
cursor.execute('SELECT COUNT(*) FROM Incidents')
num_records = cursor.fetchone()[0]

# AVG: Average value
cursor.execute('SELECT AVG(Count) FROM Incidents')
avg_count = cursor.fetchone()[0]

# MIN/MAX
cursor.execute('SELECT MIN(Count), MAX(Count) FROM Incidents')
min_count, max_count = cursor.fetchone()
```

---

### 3.5 GROUP BY and ORDER BY (VERY COMMON!)

```python
# GROUP BY with SUM
cursor.execute('''
    SELECT System, SUM(Count) as total
    FROM Incidents
    WHERE Date LIKE '2025%'
    GROUP BY System
    ORDER BY total DESC
''')
system_totals = cursor.fetchall()

# Top N results with LIMIT
cursor.execute('''
    SELECT System, SUM(Count) as total
    FROM Incidents
    WHERE Date LIKE '2025%'
    GROUP BY System
    ORDER BY total DESC
    LIMIT 3
''')
top_3_systems = cursor.fetchall()
print("Top 3 systems:")
for system, count in top_3_systems:
    print(f"- {system}: {count}")

# GROUP BY multiple columns
cursor.execute('''
    SELECT Date, Incident_Type, SUM(Count) as daily_total
    FROM Incidents
    GROUP BY Date, Incident_Type
    ORDER BY Date, daily_total DESC
''')
daily_breakdown = cursor.fetchall()

# GROUP BY with HAVING (filter groups)
cursor.execute('''
    SELECT Product, SUM(Quantity) as total_sold
    FROM Sales
    GROUP BY Product
    HAVING total_sold > 100
    ORDER BY total_sold DESC
''')
high_selling_products = cursor.fetchall()
```

**Key Patterns:**
- `GROUP BY column` - Group rows by value
- `ORDER BY column DESC` - Sort descending
- `LIMIT n` - Get top n results
- `HAVING` - Filter after grouping (WHERE is before grouping)

---

### 3.6 Export Query Results to CSV

```python
# Execute query
cursor.execute('''
    SELECT System, SUM(Count) as total
    FROM Incidents
    WHERE Date LIKE '2025%'
    GROUP BY System
    ORDER BY total DESC
    LIMIT 3
''')
top_3_systems = cursor.fetchall()

# METHOD 1: Using pandas DataFrame
df_export = pd.DataFrame(top_3_systems, columns=['System', 'total'])
df_export.to_csv('top3_systems.csv', index=False)
print("Results exported to top3_systems.csv")

# METHOD 2: Using csv module
import csv
with open('results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['System', 'Total'])  # Header
    writer.writerows(top_3_systems)

# Always close connection when done
conn.close()
print("Database connection closed.")
```

---

## TASK 4: FILE HANDLING (10-15 min)

### 4.1 CSV File Operations

```python
# CHECK if file exists
import os

filename = 'data.csv'
if os.path.exists(filename):
    print(f"'{filename}' already exists.")
    file_mode = 'a'  # Append mode
    write_header = False
else:
    print(f"'{filename}' created.")
    file_mode = 'w'  # Write mode
    write_header = True

# WRITE to CSV (manual method)
with open(filename, file_mode) as f:
    if write_header:
        f.write("Name,Height\n")

    # Write data rows
    for record in records:
        f.write(f"{record['Name']},{record['Height']}\n")

print(f"Data saved to {filename}")

# READ CSV line by line
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())

# APPEND to existing file
with open('log.txt', 'a') as f:
    f.write(f"New entry: {datetime.now()}\n")
```

---

### 4.2 Text File Operations

```python
# WRITE to text file
summary_filename = "summary.txt"
with open(summary_filename, 'w') as f:
    f.write("Data Summary Report\n")
    f.write("=" * 50 + "\n")
    f.write(f"Total records: {total_records}\n")
    f.write(f"Average value: {avg_value:.2f}\n")
    f.write(f"Min value: {min_value}\n")
    f.write(f"Max value: {max_value}\n")

print(f"Summary saved to {summary_filename}")

# READ from text file
with open('data.txt', 'r') as f:
    content = f.read()  # Read entire file
    print(content)

# READ line by line
with open('data.txt', 'r') as f:
    for line in f:
        print(line.strip())  # strip() removes \n
```

---

### 4.3 User Input Collection

```python
# Collect data from user
records = []

while True:
    name = input("Enter name (or 'q' to quit): ").strip()

    if name.lower() == 'q':
        break

    try:
        height = int(input("Enter height (cm): "))
        records.append({'Name': name, 'Height': height})
        print()  # Blank line
    except ValueError:
        print("Invalid input. Please enter a number.\n")
        continue

# Save collected records
if records:
    with open('heights.csv', 'w') as f:
        f.write("Name,Height\n")
        for record in records:
            f.write(f"{record['Name']},{record['Height']}\n")
else:
    print("No data entered.")
```

---

## TASK 3: FILE HANDLING & USER INPUT (15-20 min)

**Used in**: Final.ipynb (heights.csv example) - Practice Task 3

### 3.1 Check if File Exists & Setup

```python
import os

csv_filename = "heights.csv"

# Check if file exists
if os.path.exists(csv_filename):
    # File exists - append mode
    print(f"'{csv_filename}' already exists.")
    print(f"'{csv_filename}' is open for appending.")
    file_mode = 'a'
    write_header = False  # Don't write header again
else:
    # File doesn't exist - create new
    print(f"'{csv_filename}' created successfully.")
    file_mode = 'w'
    write_header = True  # Write header
```

**Key Points:**
- Use `os.path.exists()` to check file existence
- `'w'` mode creates new file (overwrites if exists)
- `'a'` mode appends to existing file
- Track whether to write header with `write_header` flag

---

### 3.2 Collect User Input

```python
# Collect records from user
records = []

while True:
    name = input("Enter name (or 'q' to quit): ").strip()

    if name.lower() == 'q':
        break  # Exit loop

    try:
        height = int(input("Enter height (cm): "))
        records.append({'Name': name, 'Height': height})
        print()  # Blank line for readability
    except ValueError:
        print("Invalid height. Please enter an integer.\n")
        continue  # Skip this iteration, ask again

print(f"\n{len(records)} records collected")
```

**Key Patterns:**
- `input().strip()` - Remove whitespace
- `.lower()` - Case-insensitive comparison
- `try/except ValueError` - Handle invalid input
- `continue` - Skip to next iteration
- Store in list of dictionaries

---

### 3.3 Write to CSV File

```python
# Write records to CSV
if records:  # Only if we have data
    with open(csv_filename, file_mode) as f:
        # Write header if needed
        if write_header:
            f.write("Name,Height\n")

        # Write data rows
        for record in records:
            f.write(f"{record['Name']},{record['Height']}\n")

    print(f"Data saved to {csv_filename}")
else:
    # No data entered, but ensure header exists if new file
    if write_header:
        with open(csv_filename, 'w') as f:
            f.write("Name,Height\n")
    print("No new data entered.")
```

**Key Points:**
- Use `with open()` - automatically closes file
- Check `if records:` before writing
- Use f-string formatting for CSV rows
- Ensure header exists even if no data

---

### 3.4 Read CSV and Calculate Statistics

```python
import pandas as pd
import numpy as np

# Read CSV into DataFrame
df = pd.read_csv(csv_filename)

# Calculate statistics
total_records = len(df)
avg_height = np.mean(df['Height'])
min_height = np.min(df['Height'])
max_height = np.max(df['Height'])

# Print summary
print(f"Total number of records: {total_records}")
print(f"Average height: {avg_height:.2f} cm")
print(f"Minimum height: {min_height} cm")
print(f"Maximum height: {max_height} cm")
```

**Alternative using pandas methods:**
```python
# Using pandas built-in methods
avg_height = df['Height'].mean()
min_height = df['Height'].min()
max_height = df['Height'].max()
median_height = df['Height'].median()
std_height = df['Height'].std()

# Full statistical summary
print(df['Height'].describe())
```

---

### 3.5 Write Summary to Text File

```python
# Save summary statistics to text file
summary_filename = "height_summary.txt"

with open(summary_filename, 'w') as f:
    f.write("Height Summary Statistics\n")
    f.write("=" * 30 + "\n")
    f.write(f"Total number of records: {total_records}\n")
    f.write(f"Average height: {avg_height:.2f} cm\n")
    f.write(f"Minimum height: {min_height} cm\n")
    f.write(f"Maximum height: {max_height} cm\n")

print(f"Summary saved to {summary_filename}")
```

**Key Points:**
- Use `'w'` mode to overwrite file
- Format numbers with `:.2f` for 2 decimal places
- Create text separators with `"=" * 30`
- Write line by line with `\n`

---

### 3.6 Create Histogram Visualization

```python
import matplotlib.pyplot as plt

# Create histogram
plt.figure(figsize=(10, 6))
plt.hist(df['Height'], bins=10, color='steelblue', edgecolor='black', alpha=0.7)
plt.title('Height Distribution')
plt.xlabel('Height (cm)')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save and display
plt.savefig('height_distribution.png', dpi=100)
print("Histogram saved to 'height_distribution.png'")
plt.show()
```

---

### 3.7 Complete Task 3 Template (Final.ipynb Pattern)

```python
"""
Task 3: File Handling & Summary Statistics
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# STEP 1: Setup CSV file
csv_filename = "heights.csv"
if os.path.exists(csv_filename):
    file_mode = 'a'
    write_header = False
else:
    file_mode = 'w'
    write_header = True

# STEP 2: Collect data from user
records = []
while True:
    name = input("Enter name (or 'q' to quit): ").strip()
    if name.lower() == 'q':
        break
    try:
        height = int(input("Enter height (cm): "))
        records.append({'Name': name, 'Height': height})
        print()
    except ValueError:
        print("Invalid height. Please enter an integer.\n")
        continue

# STEP 3: Write to CSV
if records:
    with open(csv_filename, file_mode) as f:
        if write_header:
            f.write("Name,Height\n")
        for record in records:
            f.write(f"{record['Name']},{record['Height']}\n")
    print(f"Data saved to {csv_filename}")
else:
    if write_header:
        with open(csv_filename, 'w') as f:
            f.write("Name,Height\n")

# STEP 4: Calculate statistics
df = pd.read_csv(csv_filename)
total_records = len(df)
avg_height = np.mean(df['Height'])
min_height = np.min(df['Height'])
max_height = np.max(df['Height'])

print(f"\nTotal records: {total_records}")
print(f"Average: {avg_height:.2f} cm")
print(f"Min: {min_height} cm")
print(f"Max: {max_height} cm")

# STEP 5: Save summary to file
with open("height_summary.txt", 'w') as f:
    f.write("Height Summary Statistics\n")
    f.write("=" * 30 + "\n")
    f.write(f"Total: {total_records}\n")
    f.write(f"Average: {avg_height:.2f} cm\n")
    f.write(f"Min: {min_height} cm\n")
    f.write(f"Max: {max_height} cm\n")

# STEP 6: Create histogram
plt.figure(figsize=(10, 6))
plt.hist(df['Height'], bins=10, color='steelblue', edgecolor='black')
plt.title('Height Distribution')
plt.xlabel('Height (cm)')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('height_distribution.png')
plt.show()
```

**Time for Task 3: ~18 minutes**

---

## TASK 5: SUMMARY STATISTICS (5-10 min)

### 5.1 Using NumPy and Pandas

```python
# Read data
df = pd.read_csv('data.csv')

# Calculate statistics using NumPy
total_records = len(df)
avg_height = np.mean(df['Height'])
min_height = np.min(df['Height'])
max_height = np.max(df['Height'])
std_height = np.std(df['Height'])
median_height = np.median(df['Height'])

# Print formatted results
print(f"Total records: {total_records}")
print(f"Average height: {avg_height:.2f} cm")
print(f"Minimum height: {min_height} cm")
print(f"Maximum height: {max_height} cm")
print(f"Std deviation: {std_height:.2f} cm")
print(f"Median height: {median_height:.2f} cm")

# Using pandas methods
print(df['Height'].describe())  # Full statistical summary
```

---

### 5.2 GroupBy Statistics

```python
# Statistics by group
by_product = df.groupby('Product').agg({
    'Quantity': ['sum', 'mean', 'count'],
    'Price': ['min', 'max', 'mean']
})
print(by_product)

# Multiple statistics for one column
print(df.groupby('Incident_Type')['Count'].agg(['sum', 'mean', 'count']))

# Custom aggregation
summary = df.groupby('System').agg(
    total_incidents=('Count', 'sum'),
    avg_incidents=('Count', 'mean'),
    num_records=('Count', 'count')
)
print(summary)
```

---

## COMMON DATA CLEANING SCENARIOS

### Scenario 1: Remove Duplicates

```python
# Check for duplicates
print(f"Duplicates: {df.duplicated().sum()}")

# Remove duplicates
df = df.drop_duplicates()

# Remove duplicates based on specific columns
df = df.drop_duplicates(subset=['Date', 'System'], keep='first')
```

---

### Scenario 2: Handle Outliers

```python
# Identify outliers using IQR method
Q1 = df['Price'].quantile(0.25)
Q3 = df['Price'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Remove outliers
df_clean = df[(df['Price'] >= lower_bound) & (df['Price'] <= upper_bound)]

# Or cap outliers
df['Price'] = df['Price'].clip(lower=lower_bound, upper=upper_bound)
```

---

### Scenario 3: Standardize Text Data

```python
# Remove extra whitespace
df['Product'] = df['Product'].str.strip()

# Standardize case
df['Category'] = df['Category'].str.upper()

# Replace values
df['Status'] = df['Status'].replace({
    'complete': 'COMPLETED',
    'done': 'COMPLETED',
    'pending': 'PENDING'
})

# Remove special characters
df['Name'] = df['Name'].str.replace('[^a-zA-Z0-9\\s]', '', regex=True)
```

---

### Scenario 4: Filter Data

```python
# Filter by value
high_sales = df[df['Total'] > 1000]

# Filter by multiple conditions (AND)
filtered = df[(df['Year'] == 2025) & (df['Product'] == 'Laptop')]

# Filter by multiple conditions (OR)
filtered = df[(df['Status'] == 'PENDING') | (df['Status'] == 'IN_PROGRESS')]

# Filter by list of values (isin)
products_of_interest = ['Laptop', 'Phone', 'Tablet']
filtered = df[df['Product'].isin(products_of_interest)]

# Filter by date range
start_date = pd.to_datetime('2025-01-01')
end_date = pd.to_datetime('2025-12-31')
filtered = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
```

---

## QUICK REFERENCE: Common Operations

### Pandas GroupBy

```python
# Sum
df.groupby('Category')['Value'].sum()

# Multiple aggregations
df.groupby('Category').agg({'Value': 'sum', 'Count': 'mean'})

# Apply function to each group
df.groupby('Category')['Value'].apply(lambda x: x.max() - x.min())

# Get top N from each group
df.groupby('Category').head(3)
```

---

### Date/Time Operations

```python
# Extract components
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['MonthName'] = df['Date'].dt.month_name()
df['Weekday'] = df['Date'].dt.day_name()
df['Quarter'] = df['Date'].dt.quarter

# Format as string
df['DateStr'] = df['Date'].dt.strftime('%Y-%m-%d')
df['MonthYear'] = df['Date'].dt.strftime('%B %Y')

# Filter by date
df_recent = df[df['Date'] > '2025-01-01']
```

---

### SQL Date Functions

```python
# Extract year
cursor.execute("SELECT * FROM Sales WHERE strftime('%Y', Date) = '2023'")

# Extract month
cursor.execute("SELECT * FROM Sales WHERE strftime('%m', Date) = '01'")

# Date range
cursor.execute("""
    SELECT * FROM Sales
    WHERE Date BETWEEN '2023-01-01' AND '2023-12-31'
""")

# Group by month
cursor.execute("""
    SELECT strftime('%Y-%m', Date) as month, SUM(Total)
    FROM Sales
    GROUP BY month
""")
```

---

## ⏰ EXAM TIME MANAGEMENT (60 MINUTES!)

### ⚠️ STRICT 60-Minute Timeline

```
YOU ONLY HAVE 60 MINUTES - EVERY SECOND COUNTS!

0-2 min     → Read ENTIRE exam, identify dataset/columns
2-15 min    → Task 1a: Load, clean, validate [13 min]
15-29 min   → Task 1b: Create 2 charts [14 min]
29-48 min   → Task 2a: Database + insert [19 min]
48-58 min   → Task 2b: Run 2 queries [10 min]
58-60 min   → Final verification [2 min]

⏱️ SET A TIMER! Check every 15 minutes!
```

### 🚨 Time Checkpoints (CRITICAL!)

```
At 15 min: Should be DONE with Task 1a (all cleaning)
At 29 min: Should be DONE with Task 1b (both charts saved)
At 48 min: Should be DONE with Task 2a (data in database)
At 58 min: Should be DONE with Task 2b (both queries run)
At 60 min: SUBMIT! Even if incomplete!
```

---

### 🎯 Priority Order (60-min version)

#### **MUST HAVE (Critical 22/28 marks)**
1. ✅ Import statements (0.5 min)
2. ✅ Load CSV with parse_dates (1 min)
3. ✅ Fill missing values (2 min)
4. ✅ Convert Date to datetime (1 min)
5. ✅ Validate Total column (1 min)
6. ✅ Bar chart (7 min)
7. ✅ Line chart (7 min)
8. ✅ Create database & table (5 min)
9. ✅ Insert data (12 min)
10. ✅ Query: Total sales 2023 (4 min)
11. ✅ Query: Product summary (6 min)

**Total: ~47 minutes → 22-25 marks**

#### **SHOULD HAVE (Extra 3-4 marks)**
- Perfect chart formatting
- Print verification messages
- Handle NULL in SUM()
- Count rows inserted
- Formatted output

#### **SKIP IF SHORT ON TIME**
- Extra data validation
- Complex error handling
- Additional statistics
- Task 3 (Neural Network)
- Perfect code comments

---

## COMMON MISTAKES TO AVOID

### Top 10 Exam Errors

1. ❌ **Not saving plots before plt.show()**
   - `plt.savefig()` MUST come BEFORE `plt.show()`

2. ❌ **Forgetting to commit database changes**
   - Always `conn.commit()` after INSERT/UPDATE/DELETE

3. ❌ **Not converting datetime to string for database**
   - SQLite doesn't have datetime type, use TEXT

4. ❌ **Using inplace=True incorrectly**
   - Either `df.fillna(..., inplace=True)` OR `df = df.fillna(...)`

5. ❌ **Not handling None from SUM() query**
   - Check `if result is None: result = 0`

6. ❌ **Forgetting to close database connection**
   - Always `conn.close()` at the end

7. ❌ **Not using tight_layout() for plots**
   - Labels get cut off without it

8. ❌ **Mixing pandas and SQL datetime formats**
   - Pandas: `%d/%m/%Y`, SQL: `%Y-%m-%d`

9. ❌ **Not stripping/cleaning text before operations**
   - `str.strip().str.upper()` before comparisons

10. ❌ **Forgetting index=False when exporting CSV**
    - `to_csv('file.csv', index=False)`

---

## EMERGENCY TEMPLATES

### Complete Task 1 Template (15 min)

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data.csv', parse_dates=['Date'], dayfirst=True)
print(df.head())
print(f"Shape: {df.shape}")

# Clean data
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])
df['Category'] = df['Category'].str.strip().str.upper()

# Visualization 1: Bar chart
totals = df.groupby('Category')['Value'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
totals.plot(kind='bar', color='steelblue', edgecolor='black')
plt.title('Total by Category')
plt.xlabel('Category')
plt.ylabel('Total Value')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('chart1.png', dpi=150)
plt.show()

# Visualization 2: Line chart
df_year = df[df['Date'].dt.year == 2025].copy()
df_year['Month'] = df_year['Date'].dt.to_period('M')
monthly = df_year.groupby('Month')['Value'].sum()
plt.figure(figsize=(10, 6))
plt.plot(range(len(monthly)), monthly.values, marker='o')
plt.title('Monthly Totals')
plt.xlabel('Month')
plt.ylabel('Total')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('chart2.png', dpi=150)
plt.show()
```

---

### Complete Task 2 Template (15 min)

```python
import sqlite3
import pandas as pd

# Create database
conn = sqlite3.connect('DataDB.db')
cursor = conn.cursor()

# Create table
cursor.execute('DROP TABLE IF EXISTS DataTable')
cursor.execute('''
    CREATE TABLE DataTable (
        Date TEXT,
        Category TEXT,
        Value INTEGER
    )
''')
conn.commit()

# Insert data
df_db = df.copy()
df_db['Date'] = df_db['Date'].dt.strftime('%Y-%m-%d')
for _, row in df_db.iterrows():
    cursor.execute('''
        INSERT INTO DataTable (Date, Category, Value)
        VALUES (?, ?, ?)
    ''', (row['Date'], row['Category'], row['Value']))
conn.commit()

# Query: Total for year
cursor.execute('''
    SELECT SUM(Value) FROM DataTable
    WHERE Date LIKE '2025%'
''')
total = cursor.fetchone()[0] or 0
print(f"Total for 2025: {total}")

# Query: Top 3 categories
cursor.execute('''
    SELECT Category, SUM(Value) as total
    FROM DataTable
    WHERE Date LIKE '2025%'
    GROUP BY Category
    ORDER BY total DESC
    LIMIT 3
''')
top3 = cursor.fetchall()

# Export to CSV
df_export = pd.DataFrame(top3, columns=['Category', 'Total'])
df_export.to_csv('top3_results.csv', index=False)

conn.close()
```

---

## YOU'VE GOT THIS!

### Final Checklist

- [ ] All imports at the top
- [ ] Data loaded successfully
- [ ] Missing values handled
- [ ] Dates converted to datetime
- [ ] Text data cleaned (strip, upper)
- [ ] All visualizations saved as PNG
- [ ] Database created and data inserted
- [ ] All queries executed correctly
- [ ] Results exported to CSV
- [ ] Database connection closed
- [ ] Code runs without errors

**Remember:**
- Read the question carefully
- Follow the time allocation
- Save plots BEFORE showing
- Commit database changes
- Close connections
- Test your code!

**GOOD LUCK!** 🐍📊🎓

---

## 🎓 2024 EXAM VARIATIONS & ADAPTATIONS

### If Exam Uses Different Dataset

**Instead of sales_data.csv, you might get:**
- `orders_data.csv` - Order records
- `incidents_data.csv` - Security incidents
- `transactions_data.csv` - Financial transactions
- `student_data.csv` - Academic records

**Adapt the solution:**
```python
# Change filename
df = pd.read_csv('YOUR_FILE.csv', parse_dates=['DateColumn'], dayfirst=True)

# Change column names in fillna
df.fillna({
    'ColumnName1': 'DefaultValue',
    'ColumnName2': 0,
    # etc.
}, inplace=True)

# Change groupby columns
data_by_category = df.groupby('CategoryColumn')['ValueColumn'].sum()

# Change database/table names
conn = sqlite3.connect('YourDatabaseName.db')
cursor.execute('CREATE TABLE YourTableName (...)')
```

---

### If Exam Asks for Different Visualizations

#### Histogram Instead of Bar Chart
```python
plt.figure(figsize=(10, 6))
plt.hist(df['Price'], bins=10, color='steelblue', edgecolor='black')
plt.title('Price Distribution')
plt.xlabel('Price Range')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('price_histogram.png', dpi=150)
plt.show()
```

#### Scatter Plot
```python
plt.figure(figsize=(10, 6))
plt.scatter(df['Quantity'], df['Total'], color='steelblue', alpha=0.6)
plt.title('Quantity vs Total Sales')
plt.xlabel('Quantity')
plt.ylabel('Total Sales')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('quantity_vs_total.png', dpi=150)
plt.show()
```

#### Pie Chart
```python
product_totals = df.groupby('Product')['Quantity'].sum()
plt.figure(figsize=(8, 8))
plt.pie(product_totals.values, labels=product_totals.index,
        autopct='%1.1f%%', startangle=90)
plt.title('Product Distribution')
plt.tight_layout()
plt.savefig('product_pie.png', dpi=150)
plt.show()
```

---

### If Exam Asks for Different Year

**Filtering by Year:**
```python
# Method 1: Using datetime filter
df_2024 = df[df['Date'].dt.year == 2024]

# Method 2: String-based filter
df_2024 = df[df['Date'].astype(str).str.startswith('2024')]

# Method 3: SQL query
cursor.execute("""
    SELECT SUM(Total) FROM Sales
    WHERE strftime('%Y', Date) = '2024'
""")
```

---

### If Exam Asks for Different Aggregations

#### Average Instead of Sum
```python
# Pandas
avg_by_product = df.groupby('Product')['Price'].mean()

# SQL
cursor.execute("""
    SELECT Product, AVG(Price) as AvgPrice
    FROM Sales
    GROUP BY Product
""")
```

#### Count of Records
```python
# Pandas
count_by_product = df.groupby('Product').size()

# SQL
cursor.execute("""
    SELECT Product, COUNT(*) as RecordCount
    FROM Sales
    GROUP BY Product
""")
```

#### Multiple Aggregations
```python
# Pandas
summary = df.groupby('Product').agg({
    'Quantity': 'sum',
    'Price': 'mean',
    'Total': ['sum', 'count']
})

# SQL
cursor.execute("""
    SELECT Product,
           SUM(Quantity) as TotalQty,
           AVG(Price) as AvgPrice,
           SUM(Total) as TotalSales,
           COUNT(*) as NumRecords
    FROM Sales
    GROUP BY Product
""")
```

---

### If Exam Asks for Top N Products

```python
# Top 5 products by quantity
cursor.execute("""
    SELECT Product, SUM(Quantity) as TotalQty
    FROM Sales
    WHERE strftime('%Y', Date) = '2023'
    GROUP BY Product
    ORDER BY TotalQty DESC
    LIMIT 5
""")
top_5 = cursor.fetchall()

print("Top 5 Products:")
for i, (product, qty) in enumerate(top_5, 1):
    print(f"{i}. {product}: {qty} units")
```

---

### If Exam Asks for Date Range Filtering

```python
# Pandas: Filter by date range
start_date = pd.to_datetime('2023-01-01')
end_date = pd.to_datetime('2023-06-30')
df_q1_q2 = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

# SQL: Filter by date range
cursor.execute("""
    SELECT * FROM Sales
    WHERE Date BETWEEN '2023-01-01' AND '2023-06-30'
""")

# SQL: Filter by specific month
cursor.execute("""
    SELECT * FROM Sales
    WHERE strftime('%Y-%m', Date) = '2023-03'
""")
```

---

### If Exam Asks to Export Results

```python
# After query, export to CSV
cursor.execute("""
    SELECT Product, SUM(Quantity) as TotalQty
    FROM Sales
    WHERE strftime('%Y', Date) = '2023'
    GROUP BY Product
    ORDER BY TotalQty DESC
""")
results = cursor.fetchall()

# Convert to DataFrame and export
df_export = pd.DataFrame(results, columns=['Product', 'TotalQuantity'])
df_export.to_csv('product_summary_2023.csv', index=False)
print("Results exported to product_summary_2023.csv")
```

---

### If Exam Has Missing Data to Handle Differently

#### Drop Rows with Missing Values
```python
# Drop rows with ANY missing value
df = df.dropna()

# Drop rows with missing values in specific columns
df = df.dropna(subset=['Date', 'Product'])

# Drop columns with missing values
df = df.dropna(axis=1)
```

#### Forward/Backward Fill
```python
# Forward fill (use previous value)
df = df.ffill()

# Backward fill (use next value)
df = df.bfill()

# Fill by column
df['Price'] = df['Price'].ffill()
```

#### Fill with Mean/Median
```python
# Fill with mean
df['Price'].fillna(df['Price'].mean(), inplace=True)

# Fill with median
df['Quantity'].fillna(df['Quantity'].median(), inplace=True)

# Fill with mode (most common value)
df['Product'].fillna(df['Product'].mode()[0], inplace=True)
```

---

### If Exam Asks for Data Validation

```python
# Check for invalid values
print(f"Negative quantities: {(df['Quantity'] < 0).sum()}")
print(f"Zero prices: {(df['Price'] == 0).sum()}")

# Remove invalid rows
df = df[df['Quantity'] > 0]
df = df[df['Price'] > 0]

# Cap outliers
Q1 = df['Price'].quantile(0.25)
Q3 = df['Price'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['Price'] >= Q1 - 1.5*IQR) & (df['Price'] <= Q3 + 1.5*IQR)]
```

---

### If Exam Asks for Duplicate Handling

```python
# Check for duplicates
print(f"Duplicate rows: {df.duplicated().sum()}")

# Remove complete duplicates
df = df.drop_duplicates()

# Remove duplicates based on specific columns
df = df.drop_duplicates(subset=['Date', 'Product'], keep='first')

# SQL: Prevent duplicates with UNIQUE constraint
cursor.execute("""
    CREATE TABLE Sales (
        Date TEXT,
        Product TEXT,
        Quantity INTEGER,
        Price REAL,
        Total REAL,
        UNIQUE(Date, Product)
    )
""")

# Insert with duplicate prevention
cursor.execute("INSERT OR IGNORE INTO Sales ...")
```

---

## 📋 FINAL EXAM DAY CHECKLIST (60-Minute Version)

### ⏰ BEFORE Starting (0-2 min) - SET YOUR TIMER!
- [ ] Read ENTIRE exam paper
- [ ] Identify: CSV filename, columns to use
- [ ] Note: Year to analyze (probably 2023)
- [ ] Note: Database name, table name
- [ ] Check: What visualizations required (bar? line?)
- [ ] **START TIMER NOW!**

### ⏱️ Task 1a Checklist (2-15 min = 13 min)
- [ ] Import pandas, matplotlib, sqlite3
- [ ] Load CSV: `parse_dates=['Date'], dayfirst=True`
- [ ] Print `df.head()` - verify loaded correctly
- [ ] Fill missing values with dictionary
- [ ] Verify `df['Date'].dtype` is datetime64
- [ ] Calculate `df['Total'] = df['Quantity'] * df['Price']`
- [ ] **CHECK TIMER: Should be at 15 min mark!**

### ⏱️ Task 1b Checklist (15-29 min = 14 min)
- [ ] Bar chart: `df.groupby('Product')['Quantity'].sum()`
- [ ] Add title, xlabel, ylabel
- [ ] **CRITICAL: `plt.savefig()` BEFORE `plt.show()`**
- [ ] Line chart: Group by Month, sum Total
- [ ] Use `dt.to_period('M')` for monthly grouping
- [ ] Save second chart
- [ ] **CHECK TIMER: Should be at 29 min mark!**

### ⏱️ Task 2a Checklist (29-48 min = 19 min)
- [ ] Convert Date to string: `dt.strftime('%Y-%m-%d')`
- [ ] Create connection: `sqlite3.connect('SalesDB.db')`
- [ ] Create table with 5 columns (Date, Product, Quantity, Price, Total)
- [ ] Loop through DataFrame rows
- [ ] Use `INSERT OR IGNORE` in loop
- [ ] `conn.commit()` after loop
- [ ] **CHECK TIMER: Should be at 48 min mark!**

### ⏱️ Task 2b Checklist (48-58 min = 10 min)
- [ ] Query 1: `SUM(Total) WHERE strftime('%Y', Date) = '2023'`
- [ ] Handle NULL: `if result is None: result = 0`
- [ ] Print total sales result
- [ ] Query 2: `GROUP BY Product ORDER BY DESC`
- [ ] Print product summary in loop
- [ ] `conn.close()`
- [ ] **CHECK TIMER: Should be at 58 min mark!**

### ⏱️ Final Verification (58-60 min = 2 min)
- [ ] Run entire code - no errors?
- [ ] Check: 2 PNG files created?
- [ ] Check: SalesDB.db file exists?
- [ ] Check: Output shows correct values?
- [ ] **SUBMIT AT 60 MINUTES EXACTLY!**

---

### 🚨 PANIC CHECKS (If Running Behind)

**At 15 min checkpoint:**
- NOT done with Task 1a? → Skip print statements, just get data loaded!

**At 29 min checkpoint:**
- NOT done with charts? → Use minimal code, skip formatting!

**At 48 min checkpoint:**
- NOT done with database? → Use `df.to_sql()` instead of loop (faster!)

**At 58 min checkpoint:**
- NOT done with queries? → Run basic SELECT, skip formatting!

**At 60 min:**
- **SUBMIT WHATEVER YOU HAVE!** Partial credit > no credit!

---

## 🚀 EMERGENCY SPEED RUN (If Running Behind!)

### 🆘 Bare Minimum - 45 Minutes (Gets ~18-20/28 marks)

**Use this if you're at minute 15 and still struggling!**

```python
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# TASK 1a: Load & clean (FAST - 3 min)
df = pd.read_csv('sales_data.csv', parse_dates=['Date'], dayfirst=True)
df.fillna({'Product': 'Unknown', 'Quantity': 0, 'Price': 0.0, 'Total': 0.0}, inplace=True)
df['Total'] = df['Quantity'] * df['Price']

# TASK 1b: Charts (FAST - 10 min total)
# Bar chart (5 min)
df.groupby('Product')['Quantity'].sum().plot(kind='bar', title='Product Sales')
plt.savefig('chart1.png')
plt.show()

# Line chart (5 min)
df['Month'] = df['Date'].dt.to_period('M')
df.groupby('Month')['Total'].sum().plot(kind='line', title='Sales Over Time')
plt.savefig('chart2.png')
plt.show()

# TASK 2a: Database (FAST - 20 min)
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
conn = sqlite3.connect('SalesDB.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Sales (Date TEXT, Product TEXT, Quantity INTEGER, Price REAL, Total REAL)')
for _, row in df.iterrows():
    cursor.execute('INSERT OR IGNORE INTO Sales VALUES (?, ?, ?, ?, ?)',
                   (row['Date'], row['Product'], row['Quantity'], row['Price'], row['Total']))
conn.commit()

# TASK 2b: Queries (FAST - 10 min)
cursor.execute("SELECT SUM(Total) FROM Sales WHERE strftime('%Y', Date) = '2023'")
print(f"Total Sales 2023: {cursor.fetchone()[0]}")

cursor.execute("SELECT Product, SUM(Quantity) FROM Sales WHERE strftime('%Y', Date) = '2023' GROUP BY Product ORDER BY SUM(Quantity) DESC")
for p, q in cursor.fetchall():
    print(f"{p}: {q}")

conn.close()
```

**Time Breakdown:**
```
0-3 min    → Load & clean
3-8 min    → Bar chart
8-13 min   → Line chart
13-33 min  → Database creation & insert
33-43 min  → Queries
43-45 min  → Verify
```

**Estimated Marks: 18-20/28** (Good enough to pass!)

---

### ⚡ ULTRA SPEED - Last 30 Minutes Panic Mode

**If you only have 30 minutes left and nothing done:**

```python
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# ULTRA FAST - Skip validation, just core functionality
df = pd.read_csv('sales_data.csv', parse_dates=['Date'], dayfirst=True)
df.fillna(0, inplace=True)  # Fill everything with 0
df['Total'] = df['Quantity'] * df['Price']

# Quick bar chart
df.groupby('Product')['Quantity'].sum().plot(kind='bar')
plt.savefig('chart1.png'); plt.show()

# Quick line chart
df.groupby(df['Date'].dt.to_period('M'))['Total'].sum().plot(kind='line')
plt.savefig('chart2.png'); plt.show()

# Database - bare minimum
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
conn = sqlite3.connect('SalesDB.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Sales (Date TEXT, Product TEXT, Quantity INT, Price REAL, Total REAL)')
df.to_sql('Sales', conn, if_exists='replace', index=False)  # FAST insert

# Quick queries
cursor.execute("SELECT SUM(Total) FROM Sales WHERE Date LIKE '2023%'")
print(cursor.fetchone()[0])
cursor.execute("SELECT Product, SUM(Quantity) FROM Sales GROUP BY Product ORDER BY SUM(Quantity) DESC")
for row in cursor.fetchall(): print(row)
conn.close()
```

**Estimated Marks: 15-18/28** (Passing grade, barely!)

---

### 📊 Marks Breakdown by Time

| Time Available | Strategy | Expected Marks |
|----------------|----------|----------------|
| 60 min (full) | Complete solution | 25-28/28 |
| 50 min | Skip some polish | 23-26/28 |
| 45 min | Speed run version | 20-23/28 |
| 30 min | Ultra speed panic | 15-18/28 |
| 20 min | Bare minimum | 10-14/28 |

**Key Insight**: Even 45 minutes gets you 20+ marks (Pass!)

---

**YOU'RE FULLY PREPARED FOR THE 2024 PYTHON EXAM!** 🎯🐍📊
