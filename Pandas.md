<div align="center">

# Pandas Notes

> A complete reference of everything I have practiced with Pandas.

</div>

---

## Table of Contents

- [Intro](#intro)
- [Installation and Import](#installation-and-import)
- [Series](#series)
  - [Create Series](#create-series)
  - [Series Indexing and Slicing](#series-indexing-and-slicing)
  - [Series Operations](#series-operations)
  - [Series Methods](#series-methods)
- [DataFrame](#dataframe)
  - [Create DataFrame](#create-dataframe)
  - [Read CSV and JSON](#read-csv-and-json)
  - [DataFrame Info](#dataframe-info)
- [Access Data](#access-data)
  - [loc and iloc](#loc-and-iloc)
  - [Access Columns](#access-columns)
  - [Access Rows](#access-rows)
- [Cleaning Data](#cleaning-data)
  - [Handling Missing Values](#handling-missing-values)
  - [Drop Duplicates](#drop-duplicates)
  - [Replace Values](#replace-values)
  - [Rename Columns](#rename-columns)
  - [Change Data Types](#change-data-types)
- [Filter and Query](#filter-and-query)
  - [Boolean Filtering](#boolean-filtering)
  - [query() Method](#query-method)
  - [isin() Filter](#isin-filter)
- [Sorting and Ranking](#sorting-and-ranking)
  - [sort_values](#sort_values)
  - [sort_index](#sort_index)
  - [rank](#rank)
- [Add and Remove](#add-and-remove)
  - [Add Columns](#add-columns)
  - [Add Rows](#add-rows)
  - [Drop Columns and Rows](#drop-columns-and-rows)
- [GroupBy](#groupby)
  - [Basic GroupBy](#basic-groupby)
  - [Aggregation Functions](#aggregation-functions)
  - [agg() Method](#agg-method)
  - [transform()](#transform)
- [Merge, Join and Concat](#merge-join-and-concat)
  - [concat](#concat)
  - [merge](#merge)
  - [join](#join)
- [Reshape Data](#reshape-data)
  - [pivot_table](#pivot_table)
  - [melt](#melt)
  - [stack and unstack](#stack-and-unstack)
- [Apply and Map](#apply-and-map)
  - [apply](#apply)
  - [map](#map)
  - [applymap / map on DataFrame](#applymap--map-on-dataframe)
- [String Operations](#string-operations)
- [DateTime Operations](#datetime-operations)
- [Statistical Functions](#statistical-functions)
- [Pandas Quick Reference](#pandas-quick-reference)

---

## Intro

**Pandas** is a fast, powerful, and flexible open-source data analysis and manipulation library built on top of **NumPy**. It is the most widely used library for working with structured/tabular data in Python.

> **Key Facts:**
> - Pandas is built on top of **NumPy** — arrays power everything underneath
> - The two main data structures are **Series** (1D) and **DataFrame** (2D)
> - Pandas is the go-to tool for **data cleaning**, **exploration**, and **transformation**
> - It can read/write **CSV, Excel, JSON, SQL, HTML**, and many more formats

| Feature | Python List/Dict | Pandas |
|---|---|---|
| Labeled data | No built-in labels | Yes — index and column labels |
| Missing data | Manual handling | Built-in `NaN` handling |
| Operations | Manual loops | Vectorized (fast) |
| File I/O | Manual parsing | `read_csv()`, `read_excel()`, etc. |
| Grouping | Complex code | `groupby()` one-liner |

---

## Installation and Import

**Install Pandas using pip:**

```bash
pip install pandas
```

**Import Pandas (always aliased as `pd`):**

```python
import pandas as pd
import numpy as np  # Often used together

# Check the installed version
print(pd.__version__)  # Output: e.g., 2.2.2
```

---

## Series

A **Series** is a one-dimensional labeled array — like a column in a spreadsheet. It holds data of **any type** with an associated **index**.

### Create Series

```python
import pandas as pd

# From a list (default integer index 0, 1, 2...)
s = pd.Series([10, 20, 30, 40, 50])
print(s)
# Output:
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int64

# With a custom index
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s)
# Output:
# a    10
# b    20
# c    30
# dtype: int64

# From a dictionary (keys become the index)
data = {"Math": 95, "English": 88, "Science": 92}
s = pd.Series(data)
print(s)
# Output:
# Math       95
# English    88
# Science    92
# dtype: int64

# From a scalar (broadcasts the value)
s = pd.Series(7, index=["a", "b", "c"])
print(s)
# Output:
# a    7
# b    7
# c    7
# dtype: int64

# Check type
print(type(s))    # Output: <class 'pandas.core.series.Series'>
print(s.dtype)    # Output: int64
print(s.name)     # Output: None  (can be set with s.name = "Grade")
```

---

### Series Indexing and Slicing

```python
import pandas as pd

s = pd.Series([10, 20, 30, 40, 50], index=["a", "b", "c", "d", "e"])

# Access by label
print(s["b"])     # Output: 20
print(s[["a", "c"]])  # Output: a  10 / c  30

# Access by integer position
print(s.iloc[0])  # Output: 10
print(s.iloc[-1]) # Output: 50

# Slice by label (inclusive on both ends)
print(s["b":"d"])
# Output:
# b    20
# c    30
# d    40

# Slice by position (exclusive on end)
print(s.iloc[1:4])
# Output:
# b    20
# c    30
# d    40

# Boolean indexing
print(s[s > 25])
# Output:
# c    30
# d    40
# e    50
```

---

### Series Operations

```python
import pandas as pd

s1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
s2 = pd.Series([1, 2, 3], index=["a", "b", "c"])

# Arithmetic — element-wise, aligned by index
print(s1 + s2)   # Output: a  11 / b  22 / c  33
print(s1 * s2)   # Output: a  10 / b  40 / c  90
print(s1 ** 2)   # Output: a  100 / b  400 / c  900

# Mismatched index — NaN for missing
s3 = pd.Series([1, 2], index=["a", "d"])
print(s1 + s3)
# Output:
# a    11.0
# b     NaN
# c     NaN
# d     NaN

# Scalar operations
print(s1 + 100)  # Output: a  110 / b  120 / c  130
print(s1 > 15)   # Output: a False / b True / c True
```

---

### Series Methods

| Method | Description |
|---|---|
| `s.head(n)` | First `n` elements (default 5) |
| `s.tail(n)` | Last `n` elements (default 5) |
| `s.describe()` | Summary statistics |
| `s.value_counts()` | Count of unique values |
| `s.unique()` | Array of unique values |
| `s.nunique()` | Number of unique values |
| `s.sum()` | Sum of all values |
| `s.mean()` | Mean value |
| `s.min()` / `s.max()` | Min / Max value |
| `s.std()` | Standard deviation |
| `s.sort_values()` | Sort by values |
| `s.sort_index()` | Sort by index |
| `s.isnull()` | Boolean — `True` where NaN |
| `s.dropna()` | Remove NaN values |
| `s.fillna(val)` | Replace NaN with `val` |
| `s.apply(func)` | Apply a function element-wise |

```python
import pandas as pd

s = pd.Series([3, 1, 4, 1, 5, 9, 2, 6, 5])

print(s.describe())
# Output:
# count    9.000000
# mean     4.000000
# std      2.598076
# min      1.000000
# ...

print(s.value_counts())
# Output:
# 1    2
# 5    2
# 3    1  ...

print(s.unique())    # Output: [3 1 4 5 9 2 6]
print(s.nunique())   # Output: 7
print(s.sort_values())  # Sorted ascending
```

---

## DataFrame

A **DataFrame** is a two-dimensional labeled data structure — like a spreadsheet or SQL table. It has **rows** (index) and **columns**, each column being a Series.

### Create DataFrame

```python
import pandas as pd

# From a dictionary (keys = column names)
data = {
    "Name":   ["Rijoan", "Maruf", "Alice", "Bob"],
    "Age":    [24, 25, 23, 26],
    "Grade":  ["A", "B", "A+", "B+"],
    "Score":  [95, 82, 98, 79]
}
df = pd.DataFrame(data)
print(df)
# Output:
#      Name  Age Grade  Score
# 0   Rijoan   24     A     95
# 1    Maruf   25     B     82
# 2    Alice   23    A+     98
# 3      Bob   26    B+     79

# With custom index
df = pd.DataFrame(data, index=["s1", "s2", "s3", "s4"])
print(df.index.tolist())  # Output: ['s1', 's2', 's3', 's4']

# From a list of dicts (each dict is a row)
rows = [
    {"Name": "Rijoan", "Score": 95},
    {"Name": "Maruf",  "Score": 82},
]
df = pd.DataFrame(rows)
print(df)

# Basic info
print(df.shape)    # Output: (4, 4)  (rows, columns)
print(df.columns.tolist())  # Output: ['Name', 'Age', 'Grade', 'Score']
print(df.dtypes)   # Data type of each column
```

---

### Read CSV and JSON

```python
import pandas as pd

# Read CSV file
df = pd.read_csv("data.csv")

# With options
df = pd.read_csv(
    "data.csv",
    sep=",",         # Column separator (default comma)
    header=0,        # Row to use as column names (default 0)
    index_col=0,     # Column to use as row index
    nrows=100,       # Only read first 100 rows
    skiprows=2,      # Skip first 2 rows
    na_values=["N/A", "?"]  # Treat these as NaN
)

# Write to CSV
df.to_csv("output.csv", index=False)  # index=False avoids saving row numbers

# Read JSON
df = pd.read_json("data.json")

# Write to JSON
df.to_json("output.json", orient="records")

# Read Excel
df = pd.read_excel("data.xlsx", sheet_name="Sheet1")

# Write to Excel
df.to_excel("output.xlsx", index=False)

# Preview
print(df.head())    # First 5 rows
print(df.tail(3))   # Last 3 rows
```

---

### DataFrame Info

```python
import pandas as pd
import numpy as np

data = {
    "Name":   ["Rijoan", "Maruf", None, "Bob"],
    "Age":    [24, 25, 23, np.nan],
    "Score":  [95.0, 82.0, 98.0, 79.0]
}
df = pd.DataFrame(data)

print(df.shape)      # Output: (4, 3)  — 4 rows, 3 columns
print(df.ndim)       # Output: 2
print(df.size)       # Output: 12  — total elements

print(df.info())
# Output: Index, columns, non-null counts, dtypes, memory usage

print(df.describe())
# Output: count, mean, std, min, 25%, 50%, 75%, max  for numeric columns

print(df.describe(include="all"))  # Include non-numeric columns too

print(df.dtypes)
# Output:
# Name     object
# Age     float64
# Score   float64

print(df.columns)    # Output: Index(['Name', 'Age', 'Score'], dtype='object')
print(df.index)      # Output: RangeIndex(start=0, stop=4, step=1)
print(df.values)     # Output: 2D NumPy array of values

print(df.isnull().sum())    # Count of NaN per column
print(df.notnull().sum())   # Count of non-NaN per column
print(df.memory_usage())    # Memory per column in bytes
```

---

## Access Data

### loc and iloc

| Method | Access By | Endpoint |
|---|---|---|
| `loc[row, col]` | **Label** (index name / column name) | Inclusive on both ends |
| `iloc[row, col]` | **Integer position** (0-based) | Exclusive on end (like Python slicing) |

```python
import pandas as pd

data = {
    "Name":  ["Rijoan", "Maruf", "Alice", "Bob"],
    "Age":   [24, 25, 23, 26],
    "Score": [95, 82, 98, 79]
}
df = pd.DataFrame(data, index=["s1", "s2", "s3", "s4"])

# --- loc (label-based) ---
print(df.loc["s1"])                    # Entire row s1
print(df.loc["s1", "Name"])           # Single value: "Rijoan"
print(df.loc["s1":"s3", "Name":"Age"]) # Row s1 to s3, cols Name to Age
print(df.loc[:, "Score"])             # All rows, Score column
print(df.loc[df["Age"] > 24])         # Conditional row selection

# --- iloc (position-based) ---
print(df.iloc[0])                      # First row
print(df.iloc[0, 1])                   # Row 0, col 1 → 24
print(df.iloc[0:2, 0:2])              # First 2 rows and cols
print(df.iloc[:, -1])                  # Last column (Score)
print(df.iloc[[0, 2], :])             # Rows 0 and 2, all cols
```

---

### Access Columns

```python
import pandas as pd

data = {"Name": ["Rijoan", "Maruf"], "Age": [24, 25], "Score": [95, 82]}
df = pd.DataFrame(data)

# Single column — returns a Series
print(df["Name"])
print(df.Name)         # Dot notation (only if no spaces in name)

# Multiple columns — returns a DataFrame
print(df[["Name", "Score"]])

# Column names list
print(df.columns.tolist())  # Output: ['Name', 'Age', 'Score']
```

---

### Access Rows

```python
import pandas as pd

data = {"Name": ["Rijoan", "Maruf", "Alice"], "Score": [95, 82, 98]}
df = pd.DataFrame(data)

# By integer position using iloc
print(df.iloc[0])    # First row as a Series
print(df.iloc[1:3])  # Rows 1 and 2 as a DataFrame

# By label using loc
print(df.loc[0])     # Row with index label 0

# Iterate over rows
for index, row in df.iterrows():
    print(index, row["Name"], row["Score"])
# Output:
# 0 Rijoan 95
# 1 Maruf 82
# 2 Alice 98

# itertuples — faster alternative
for row in df.itertuples():
    print(row.Name, row.Score)
```

---

## Cleaning Data

### Handling Missing Values

```python
import pandas as pd
import numpy as np

data = {
    "Name":  ["Rijoan", None, "Alice", "Bob"],
    "Age":   [24, 25, np.nan, 26],
    "Score": [95.0, np.nan, 98.0, 79.0]
}
df = pd.DataFrame(data)

# Detect missing values
print(df.isnull())          # Boolean DataFrame
print(df.isnull().sum())    # Count per column
print(df.isnull().any())    # True if column has any NaN

# Drop rows with ANY missing values
df_dropped = df.dropna()
print(df_dropped)

# Drop rows only if ALL values are missing
df_dropped = df.dropna(how="all")

# Drop rows with NaN in specific columns
df_dropped = df.dropna(subset=["Score"])

# Drop columns with any NaN
df_dropped = df.dropna(axis=1)

# Fill NaN with a fixed value
df_filled = df.fillna(0)
print(df_filled)

# Fill with column mean
df["Score"] = df["Score"].fillna(df["Score"].mean())

# Fill with forward fill (propagate last valid value forward)
df_ffill = df.ffill()

# Fill with backward fill (propagate next valid value backward)
df_bfill = df.bfill()

# Interpolate (linear interpolation for numeric columns)
df["Age"] = df["Age"].interpolate()
```

> **Tip:** Always check `df.isnull().sum()` first to understand the scale of missing data before deciding whether to drop or fill.

---

### Drop Duplicates

```python
import pandas as pd

data = {
    "Name":  ["Rijoan", "Maruf", "Rijoan", "Alice", "Maruf"],
    "Score": [95, 82, 95, 98, 82]
}
df = pd.DataFrame(data)

# Check for duplicates
print(df.duplicated())         # Boolean Series
print(df.duplicated().sum())   # Output: 2

# Drop duplicate rows (keep first occurrence)
df_clean = df.drop_duplicates()
print(df_clean)

# Keep last occurrence
df_clean = df.drop_duplicates(keep="last")

# Drop duplicates based on specific column(s)
df_clean = df.drop_duplicates(subset=["Name"])
print(df_clean)

# Drop all duplicates (keep none)
df_clean = df.drop_duplicates(keep=False)
```

---

### Replace Values

```python
import pandas as pd

data = {"Grade": ["A", "B", "C", "B", "A"], "Score": [95, 82, 70, 88, 91]}
df = pd.DataFrame(data)

# Replace a single value
df["Grade"] = df["Grade"].replace("C", "C+")
print(df)

# Replace multiple values with a dict
df["Grade"] = df["Grade"].replace({"A": "Excellent", "B": "Good"})
print(df)

# Replace in entire DataFrame
df = df.replace(95, 100)

# Replace with regex
df["Grade"] = df["Grade"].replace(r"^Ex.*", "Top", regex=True)

# Replace NaN with a specific value
import numpy as np
df = pd.DataFrame({"val": [1, np.nan, 3, np.nan, 5]})
df["val"] = df["val"].replace(np.nan, 0)
print(df)
```

---

### Rename Columns

```python
import pandas as pd

data = {"name": ["Rijoan", "Maruf"], "age": [24, 25], "score": [95, 82]}
df = pd.DataFrame(data)

# Rename specific columns
df = df.rename(columns={"name": "Name", "age": "Age", "score": "Score"})
print(df.columns.tolist())  # Output: ['Name', 'Age', 'Score']

# Rename using a function
df = df.rename(columns=str.upper)
print(df.columns.tolist())  # Output: ['NAME', 'AGE', 'SCORE']

# Rename the index
df = df.rename(index={0: "s1", 1: "s2"})

# Set a column as the index
df = df.set_index("NAME")

# Reset the index back to integers
df = df.reset_index()

# Rename columns by reassigning the list directly
df.columns = ["Name", "Age", "Score"]
```

---

### Change Data Types

```python
import pandas as pd

data = {"Age": ["24", "25", "23"], "Score": ["95.5", "82.0", "98.1"], "Active": [1, 0, 1]}
df = pd.DataFrame(data)

print(df.dtypes)
# Output: Age object, Score object, Active int64

# Convert a column to numeric
df["Age"] = df["Age"].astype(int)
df["Score"] = df["Score"].astype(float)

# Convert to bool
df["Active"] = df["Active"].astype(bool)

# Convert to category (saves memory for low-cardinality columns)
grades = pd.Series(["A", "B", "A", "C", "B", "A"])
grades = grades.astype("category")
print(grades.dtype)     # Output: category
print(grades.cat.categories)  # Output: Index(['A', 'B', 'C'])

# Safe conversion (errors='coerce' turns bad values into NaN)
mixed = pd.Series(["1", "2", "abc", "4"])
mixed = pd.to_numeric(mixed, errors="coerce")
print(mixed)  # Output: [1.0, 2.0, NaN, 4.0]
```

---

## Filter and Query

### Boolean Filtering

```python
import pandas as pd

data = {
    "Name":  ["Rijoan", "Maruf", "Alice", "Bob", "Carol"],
    "Age":   [24, 25, 23, 30, 22],
    "Score": [95, 82, 98, 79, 88],
    "Grade": ["A", "B", "A+", "B+", "A"]
}
df = pd.DataFrame(data)

# Single condition
print(df[df["Score"] > 85])

# Multiple conditions — use & (and) and | (or), wrap each in ()
print(df[(df["Score"] > 85) & (df["Age"] < 25)])
print(df[(df["Score"] > 90) | (df["Grade"] == "A+")])

# Negate with ~
print(df[~(df["Grade"] == "B")])   # All rows where Grade is NOT "B"

# String condition
print(df[df["Name"].str.startswith("R")])

# Multiple values — isin
print(df[df["Grade"].isin(["A", "A+"])])
```

---

### query() Method

`query()` lets you filter using a **string expression** — cleaner for complex conditions.

```python
import pandas as pd

data = {
    "Name":  ["Rijoan", "Maruf", "Alice", "Bob"],
    "Age":   [24, 25, 23, 30],
    "Score": [95, 82, 98, 79]
}
df = pd.DataFrame(data)

# query() with conditions
print(df.query("Score > 85"))
print(df.query("Score > 85 and Age < 25"))
print(df.query("Score > 90 or Age > 28"))

# Use @ to reference a Python variable inside query
min_score = 85
print(df.query("Score > @min_score"))

# String matching
print(df.query("Name == 'Rijoan'"))
```

---

### isin() Filter

```python
import pandas as pd

data = {
    "Name":  ["Rijoan", "Maruf", "Alice", "Bob"],
    "City":  ["Dhaka", "Chittagong", "Dhaka", "Sylhet"],
    "Score": [95, 82, 98, 79]
}
df = pd.DataFrame(data)

# Keep only rows where City is in the list
print(df[df["City"].isin(["Dhaka", "Sylhet"])])
# Output: Rijoan, Alice, Bob

# Exclude rows — use ~ to negate
print(df[~df["City"].isin(["Dhaka"])])
# Output: Maruf, Bob
```

---

## Sorting and Ranking

### sort_values

```python
import pandas as pd

data = {
    "Name":  ["Rijoan", "Maruf", "Alice", "Bob"],
    "Age":   [24, 25, 23, 30],
    "Score": [95, 82, 98, 79]
}
df = pd.DataFrame(data)

# Sort by a single column ascending (default)
print(df.sort_values("Score"))

# Sort descending
print(df.sort_values("Score", ascending=False))

# Sort by multiple columns
print(df.sort_values(["Age", "Score"], ascending=[True, False]))

# Reset index after sorting
df_sorted = df.sort_values("Score", ascending=False).reset_index(drop=True)
print(df_sorted)
```

---

### sort_index

```python
import pandas as pd

data = {"Score": [95, 82, 98, 79]}
df = pd.DataFrame(data, index=["c", "a", "d", "b"])

# Sort by index label
print(df.sort_index())
# Output: sorted alphabetically: a, b, c, d

# Sort index descending
print(df.sort_index(ascending=False))
```

---

### rank

```python
import pandas as pd

data = {"Name": ["Rijoan", "Maruf", "Alice", "Bob"], "Score": [95, 82, 98, 82]}
df = pd.DataFrame(data)

# Rank scores (1 = lowest by default)
df["Rank"] = df["Score"].rank(ascending=False)  # 1 = highest
print(df)
# Output:
#      Name  Score  Rank
# 0  Rijoan     95   2.0
# 1   Maruf     82   3.5
# 2   Alice     98   1.0
# 3     Bob     82   3.5  (tie → average rank)

# method='min' — tie gets the lowest rank
df["Rank_min"] = df["Score"].rank(ascending=False, method="min")
```

---

## Add and Remove

### Add Columns

```python
import pandas as pd

data = {"Name": ["Rijoan", "Maruf", "Alice"], "Score": [95, 82, 98]}
df = pd.DataFrame(data)

# Add a new column with a constant value
df["Passed"] = True
print(df)

# Add computed column
df["Grade"] = df["Score"].apply(lambda x: "A" if x >= 90 else "B")
print(df)

# Add column based on another column
df["Bonus"] = df["Score"] * 0.1
print(df)

# Insert at a specific position
df.insert(1, "ID", [101, 102, 103])  # Insert at column index 1
print(df)
```

---

### Add Rows

```python
import pandas as pd

data = {"Name": ["Rijoan", "Maruf"], "Score": [95, 82]}
df = pd.DataFrame(data)

# Add a single row using concat (recommended in Pandas 2.0+)
new_row = pd.DataFrame([{"Name": "Alice", "Score": 98}])
df = pd.concat([df, new_row], ignore_index=True)
print(df)

# Add multiple rows
new_rows = pd.DataFrame([
    {"Name": "Bob",   "Score": 79},
    {"Name": "Carol", "Score": 88}
])
df = pd.concat([df, new_rows], ignore_index=True)
print(df)
```

> **Note:** `df.append()` was removed in Pandas 2.0. Always use `pd.concat()` to add rows.

---

### Drop Columns and Rows

```python
import pandas as pd

data = {
    "Name":  ["Rijoan", "Maruf", "Alice"],
    "Age":   [24, 25, 23],
    "Score": [95, 82, 98],
    "Bonus": [9.5, 8.2, 9.8]
}
df = pd.DataFrame(data)

# Drop a single column
df = df.drop(columns=["Bonus"])
print(df)

# Drop multiple columns
df = df.drop(columns=["Age", "Score"])
print(df)

# Drop rows by index label
df = pd.DataFrame(data)
df = df.drop(index=[0, 2])  # Drop rows with index 0 and 2
print(df)

# Drop rows by condition
df = pd.DataFrame(data)
df = df[df["Score"] >= 90]  # Keep rows where Score >= 90
print(df)
```

---

## GroupBy

### Basic GroupBy

`groupby()` splits the DataFrame into groups, applies a function, and combines the results.

```python
import pandas as pd

data = {
    "Name":   ["Rijoan", "Maruf", "Alice", "Bob", "Carol", "Dave"],
    "City":   ["Dhaka", "Dhaka", "Chittagong", "Dhaka", "Chittagong", "Sylhet"],
    "Score":  [95, 82, 98, 79, 88, 91],
    "Gender": ["M", "M", "F", "M", "F", "M"]
}
df = pd.DataFrame(data)

# Group by City and get mean Score
print(df.groupby("City")["Score"].mean())
# Output:
# City
# Chittagong    93.0
# Dhaka         85.33
# Sylhet        91.0

# Group by City and get count
print(df.groupby("City")["Name"].count())

# Group by multiple columns
print(df.groupby(["City", "Gender"])["Score"].mean())
```

---

### Aggregation Functions

```python
import pandas as pd

data = {
    "City":   ["Dhaka", "Dhaka", "Chittagong", "Dhaka", "Chittagong"],
    "Score":  [95, 82, 98, 79, 88],
    "Age":    [24, 25, 23, 30, 22]
}
df = pd.DataFrame(data)

grouped = df.groupby("City")

print(grouped["Score"].sum())    # Sum per city
print(grouped["Score"].mean())   # Mean per city
print(grouped["Score"].min())    # Min per city
print(grouped["Score"].max())    # Max per city
print(grouped["Score"].count())  # Count per city
print(grouped["Score"].std())    # Std dev per city

# Get all at once
print(grouped["Score"].describe())
```

---

### agg() Method

`agg()` applies **multiple functions** at once.

```python
import pandas as pd

data = {
    "City":   ["Dhaka", "Dhaka", "Chittagong", "Dhaka", "Chittagong"],
    "Score":  [95, 82, 98, 79, 88],
    "Age":    [24, 25, 23, 30, 22]
}
df = pd.DataFrame(data)

# Apply multiple aggregations to one column
print(df.groupby("City")["Score"].agg(["mean", "min", "max", "count"]))

# Apply different aggregations to different columns
result = df.groupby("City").agg(
    avg_score=("Score", "mean"),
    max_score=("Score", "max"),
    avg_age=("Age", "mean")
)
print(result)
# Output:
#             avg_score  max_score  avg_age
# City
# Chittagong       93.0         98     22.5
# Dhaka            85.33        95     26.33
```

---

### transform()

`transform()` applies a function to each group but **returns a Series the same size as the original DataFrame** — useful for adding group-level stats back to the original.

```python
import pandas as pd

data = {
    "City":  ["Dhaka", "Dhaka", "Chittagong", "Dhaka", "Chittagong"],
    "Score": [95, 82, 98, 79, 88]
}
df = pd.DataFrame(data)

# Add group mean as a new column
df["City_Mean_Score"] = df.groupby("City")["Score"].transform("mean")
print(df)
# Output:
#          City  Score  City_Mean_Score
# 0       Dhaka     95        85.333333
# 1       Dhaka     82        85.333333
# 2  Chittagong     98        93.000000
# 3       Dhaka     79        85.333333
# 4  Chittagong     88        93.000000

# Normalize scores within each city group
df["Score_Normalized"] = df.groupby("City")["Score"].transform(
    lambda x: (x - x.mean()) / x.std()
)
print(df)
```

---

## Merge, Join and Concat

### concat

`pd.concat()` stacks DataFrames **vertically** (rows) or **horizontally** (columns).

```python
import pandas as pd

df1 = pd.DataFrame({"Name": ["Rijoan", "Maruf"], "Score": [95, 82]})
df2 = pd.DataFrame({"Name": ["Alice", "Bob"],   "Score": [98, 79]})

# Stack vertically (like adding rows)
result = pd.concat([df1, df2], ignore_index=True)
print(result)
# Output:
#      Name  Score
# 0   Rijoan     95
# 1    Maruf     82
# 2    Alice     98
# 3      Bob     79

# Stack horizontally (like adding columns)
df3 = pd.DataFrame({"City": ["Dhaka", "Chittagong"]})
result = pd.concat([df1, df3], axis=1)
print(result)

# Keep track of source with keys
result = pd.concat([df1, df2], keys=["batch1", "batch2"])
print(result)
```

---

### merge

`pd.merge()` is like SQL JOIN — combines rows from two DataFrames based on a **common key**.

| Join Type | `how=` | Keeps |
|---|---|---|
| Inner | `"inner"` | Only matching rows (default) |
| Left | `"left"` | All rows from left + matching right |
| Right | `"right"` | All rows from right + matching left |
| Outer | `"outer"` | All rows from both, NaN for no match |

```python
import pandas as pd

students = pd.DataFrame({
    "ID":   [1, 2, 3, 4],
    "Name": ["Rijoan", "Maruf", "Alice", "Bob"]
})

scores = pd.DataFrame({
    "ID":    [1, 2, 3, 5],
    "Score": [95, 82, 98, 88]
})

# Inner join — only IDs in both
print(pd.merge(students, scores, on="ID", how="inner"))
# Output: IDs 1, 2, 3

# Left join — all students, NaN if no score
print(pd.merge(students, scores, on="ID", how="left"))
# Output: IDs 1, 2, 3, 4  (Bob gets NaN Score)

# Outer join — all records
print(pd.merge(students, scores, on="ID", how="outer"))
# Output: IDs 1, 2, 3, 4, 5

# Merge on columns with different names
df_a = pd.DataFrame({"StudentID": [1, 2], "Name": ["Rijoan", "Maruf"]})
df_b = pd.DataFrame({"SID": [1, 2], "Score": [95, 82]})
print(pd.merge(df_a, df_b, left_on="StudentID", right_on="SID"))
```

---

### join

`df.join()` is a simpler version of `merge` — joins on the **index** by default.

```python
import pandas as pd

df1 = pd.DataFrame({"Score": [95, 82, 98]}, index=["s1", "s2", "s3"])
df2 = pd.DataFrame({"Grade": ["A", "B", "A+"]}, index=["s1", "s2", "s3"])

result = df1.join(df2)
print(result)
# Output:
#     Score Grade
# s1     95     A
# s2     82     B
# s3     98    A+
```

---

## Reshape Data

### pivot_table

`pivot_table()` summarizes data like an Excel pivot table — rows, columns, and values.

```python
import pandas as pd

data = {
    "Name":    ["Rijoan", "Maruf", "Rijoan", "Maruf", "Alice"],
    "Subject": ["Math", "Math", "English", "English", "Math"],
    "Score":   [95, 82, 88, 79, 98]
}
df = pd.DataFrame(data)

# Pivot: rows = Name, columns = Subject, values = Score
pivot = df.pivot_table(
    values="Score",
    index="Name",
    columns="Subject",
    aggfunc="mean"    # default is mean
)
print(pivot)
# Output:
# Subject  English  Math
# Name
# Alice        NaN    98
# Maruf         79    82
# Rijoan        88    95

# Fill NaN in pivot
pivot = pivot.fillna(0)

# Multiple aggfuncs
pivot = df.pivot_table(
    values="Score",
    index="Name",
    columns="Subject",
    aggfunc=["mean", "max"],
    fill_value=0
)
print(pivot)
```

---

### melt

`melt()` is the **reverse of pivot** — converts wide format to long format.

```python
import pandas as pd

df = pd.DataFrame({
    "Name":    ["Rijoan", "Maruf"],
    "Math":    [95, 82],
    "English": [88, 79],
    "Science": [91, 85]
})
print(df)
# Wide format — one row per student

# Melt to long format
melted = df.melt(
    id_vars=["Name"],       # Column(s) to keep as identifier
    var_name="Subject",     # Name for the variable column
    value_name="Score"      # Name for the value column
)
print(melted)
# Output:
#      Name  Subject  Score
# 0   Rijoan     Math     95
# 1    Maruf     Math     82
# 2   Rijoan  English     88
# 3    Maruf  English     79
# 4   Rijoan  Science     91
# 5    Maruf  Science     85
```

---

### stack and unstack

```python
import pandas as pd

data = {
    "Math":    [95, 82],
    "English": [88, 79]
}
df = pd.DataFrame(data, index=["Rijoan", "Maruf"])
print(df)
# Output:
#         Math  English
# Rijoan    95       88
# Maruf     82       79

# stack — moves columns into rows (wide to long)
stacked = df.stack()
print(stacked)
# Output:
# Rijoan  English    88
#         Math       95
# Maruf   English    79
#         Math       82

# unstack — moves rows into columns (long to wide)
print(stacked.unstack())
# Output: back to the original DataFrame
```

---

## Apply and Map

### apply

`apply()` runs a function along **rows or columns** of a DataFrame, or over **elements** of a Series.

```python
import pandas as pd

data = {
    "Name":  ["Rijoan", "Maruf", "Alice"],
    "Score": [95, 82, 98],
    "Age":   [24, 25, 23]
}
df = pd.DataFrame(data)

# Apply to a Series (column)
df["Grade"] = df["Score"].apply(lambda x: "A" if x >= 90 else "B")
print(df)

# Apply a named function to a column
def classify(score):
    if score >= 90:
        return "Excellent"
    elif score >= 80:
        return "Good"
    else:
        return "Average"

df["Category"] = df["Score"].apply(classify)
print(df)

# Apply across rows (axis=1) — access multiple columns
df["Summary"] = df.apply(
    lambda row: f"{row['Name']} scored {row['Score']}", axis=1
)
print(df["Summary"])
# Output:
# 0    Rijoan scored 95
# 1     Maruf scored 82
# 2     Alice scored 98
```

---

### map

`map()` is used on **a Series** to map values using a dictionary or function — replaces each value.

```python
import pandas as pd

s = pd.Series(["A", "B", "C", "A", "B"])

# Map with a dictionary
grade_map = {"A": "Excellent", "B": "Good", "C": "Average"}
print(s.map(grade_map))
# Output:
# 0    Excellent
# 1         Good
# 2      Average
# 3    Excellent
# 4         Good

# Map with a function
print(s.map(lambda x: x.lower()))
# Output: ['a', 'b', 'c', 'a', 'b']

# Values not in the map become NaN
partial_map = {"A": "Excellent"}
print(s.map(partial_map))
# Output: Excellent, NaN, NaN, Excellent, NaN
```

---

### applymap / map on DataFrame

```python
import pandas as pd

df = pd.DataFrame({
    "Math":    [95, 82, 70],
    "English": [88, 79, 91]
})

# Apply element-wise across entire DataFrame
# Pandas 2.1+: use df.map()  |  older versions: df.applymap()
result = df.map(lambda x: x * 1.1)  # Apply 10% bonus to every cell
print(result.round(1))
# Output:
#    Math  English
# 0  104.5     96.8
# 1   90.2     86.9
# 2   77.0    100.1
```

---

## String Operations

Pandas provides vectorized string methods via **`.str`** accessor.

| Method | Description |
|---|---|
| `s.str.upper()` | Uppercase |
| `s.str.lower()` | Lowercase |
| `s.str.title()` | Title case |
| `s.str.strip()` | Remove whitespace |
| `s.str.replace(old, new)` | Replace substring |
| `s.str.contains(pat)` | Returns bool — contains pattern |
| `s.str.startswith(pat)` | Returns bool — starts with pattern |
| `s.str.endswith(pat)` | Returns bool — ends with pattern |
| `s.str.split(sep)` | Split into list |
| `s.str.len()` | Length of each string |
| `s.str.count(pat)` | Count occurrences |
| `s.str.find(sub)` | Index of first occurrence |
| `s.str.get(i)` | Get character at position `i` |
| `s.str.cat(sep)` | Concatenate strings |
| `s.str.extract(pat)` | Extract groups from regex |

```python
import pandas as pd

df = pd.DataFrame({
    "Name":  ["  rijoan maruf ", "MARUF", "alice"],
    "Email": ["rijoan@gmail.com", "maruf@yahoo.com", "alice@gmail.com"]
})

# Clean and standardize names
df["Name"] = df["Name"].str.strip().str.title()
print(df["Name"])
# Output: Rijoan Maruf, Maruf, Alice

# Check contains
print(df["Email"].str.contains("gmail"))
# Output: True, False, True

# Extract domain from email
df["Domain"] = df["Email"].str.split("@").str.get(1)
print(df["Domain"])
# Output: gmail.com, yahoo.com, gmail.com

# Filter using str
print(df[df["Email"].str.endswith("gmail.com")])

# Replace
df["Email"] = df["Email"].str.replace("gmail.com", "google.com")
print(df["Email"])

# Length of each name
df["Name_Length"] = df["Name"].str.len()
print(df["Name_Length"])
```

---

## DateTime Operations

```python
import pandas as pd

# Create a datetime Series
dates = pd.Series(["2024-01-15", "2024-06-20", "2025-03-10"])
dates = pd.to_datetime(dates)
print(dates)
# Output: DatetimeIndex with dtype datetime64

# Extract components
print(dates.dt.year)    # Output: [2024, 2024, 2025]
print(dates.dt.month)   # Output: [1, 6, 3]
print(dates.dt.day)     # Output: [15, 20, 10]
print(dates.dt.weekday) # Output: 0=Mon ... 6=Sun
print(dates.dt.day_name())  # Output: Monday, Thursday, Sunday

# Arithmetic
today = pd.Timestamp("2025-01-01")
print(dates - today)    # Timedelta difference

# Create DatetimeIndex ranges
date_range = pd.date_range(start="2024-01-01", end="2024-01-07", freq="D")
print(date_range)
# Output: 7 daily dates

# In a DataFrame
df = pd.DataFrame({
    "Date":  ["2024-01-15", "2024-06-20", "2025-03-10"],
    "Sales": [100, 200, 150]
})
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month
df["Year"] = df["Date"].dt.year
df["DayName"] = df["Date"].dt.day_name()
print(df)

# Set datetime as index for time series operations
df = df.set_index("Date")
print(df["2024"])          # Filter all rows in 2024
print(df["2024-06"])       # Filter all rows in June 2024
```

---

## Statistical Functions

```python
import pandas as pd
import numpy as np

data = {
    "Math":    [95, 82, 70, 88, 91],
    "English": [88, 79, 91, 85, 76],
    "Science": [91, 85, 78, 92, 83]
}
df = pd.DataFrame(data)

# Basic statistics for each column
print(df.sum())         # Sum
print(df.mean())        # Mean
print(df.median())      # Median
print(df.mode())        # Mode
print(df.std())         # Standard deviation
print(df.var())         # Variance
print(df.min())         # Minimum
print(df.max())         # Maximum
print(df.count())       # Non-null count

# Summary statistics at once
print(df.describe())
# Output: count, mean, std, min, 25%, 50%, 75%, max

# Axis — apply along rows (axis=1) instead of columns (axis=0)
df["Row_Mean"] = df.mean(axis=1)     # Row-wise mean
df["Row_Max"]  = df.max(axis=1)      # Row-wise max
print(df)

# Correlation matrix
print(df.corr())    # Pearson correlation between all numeric columns

# Covariance matrix
print(df.cov())

# Cumulative operations
print(df["Math"].cumsum())   # Cumulative sum
print(df["Math"].cumprod())  # Cumulative product
print(df["Math"].cummax())   # Cumulative max

# Percent change
print(df["Math"].pct_change())  # % change from previous row

# Quantiles
print(df["Math"].quantile(0.25))  # Q1
print(df["Math"].quantile(0.75))  # Q3
```

---

## Pandas Quick Reference

| Operation | Code | Notes |
|---|---|---|
| Import | `import pandas as pd` | Always alias as `pd` |
| Create Series | `pd.Series([1, 2, 3])` | With optional `index=` |
| Create DataFrame | `pd.DataFrame(dict)` | Keys = column names |
| Read CSV | `pd.read_csv("file.csv")` | Many options available |
| Write CSV | `df.to_csv("file.csv", index=False)` | `index=False` skips row numbers |
| Head / Tail | `df.head(n)` / `df.tail(n)` | Default 5 rows |
| Shape | `df.shape` | `(rows, cols)` |
| Info | `df.info()` | Types, non-null counts |
| Describe | `df.describe()` | Summary statistics |
| Column names | `df.columns.tolist()` | List of column names |
| Data types | `df.dtypes` | Type per column |
| Select column | `df["col"]` | Returns Series |
| Select columns | `df[["c1", "c2"]]` | Returns DataFrame |
| Select by label | `df.loc[row, col]` | Inclusive on both ends |
| Select by position | `df.iloc[row, col]` | Exclusive end (like Python) |
| Boolean filter | `df[df["col"] > 5]` | Standard boolean indexing |
| query | `df.query("col > 5")` | String-based filter |
| isin | `df[df["col"].isin([1,2])]` | Filter by list of values |
| Sort | `df.sort_values("col")` | Use `ascending=False` to reverse |
| Add column | `df["new"] = values` | Direct assignment |
| Drop column | `df.drop(columns=["col"])` | Returns new DataFrame |
| Drop rows | `df.drop(index=[0, 1])` | By index label |
| Rename | `df.rename(columns={"old": "new"})` | Dict of old to new names |
| Change type | `df["col"].astype(int)` | Or `float`, `str`, `bool` |
| Null check | `df.isnull().sum()` | Count NaN per column |
| Drop NaN rows | `df.dropna()` | `subset=["col"]` for specific cols |
| Fill NaN | `df.fillna(val)` | Or `ffill()`, `bfill()` |
| Drop duplicates | `df.drop_duplicates()` | `subset=` for specific cols |
| Replace values | `df.replace(old, new)` | Or dict `{old: new}` |
| GroupBy | `df.groupby("col")["val"].mean()` | Split-apply-combine |
| agg | `df.groupby("col").agg({"val": "mean"})` | Multiple aggregations |
| Merge | `pd.merge(df1, df2, on="key")` | Like SQL JOIN |
| Concat rows | `pd.concat([df1, df2])` | Stack vertically |
| Concat cols | `pd.concat([df1, df2], axis=1)` | Stack horizontally |
| Pivot table | `df.pivot_table(values, index, columns)` | Summarize like Excel |
| Melt | `df.melt(id_vars, var_name, value_name)` | Wide to long format |
| Apply | `df["col"].apply(func)` | Element-wise function |
| String ops | `df["col"].str.upper()` | Via `.str` accessor |
| To datetime | `pd.to_datetime(df["date"])` | Converts string to datetime |
| Datetime extract | `df["date"].dt.year` | `.dt.month`, `.dt.day` etc. |
| Correlation | `df.corr()` | Pearson correlation matrix |
| Cumulative sum | `df["col"].cumsum()` | Running total |

---

<div align="center">

*Pandas Notes — Complete Reference*

</div>
