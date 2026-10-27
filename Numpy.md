<div align="center">

# NumPy Notes

> A complete reference of everything I have practiced with NumPy.

</div>

---

## Table of Contents

- [Intro](#intro)
- [Installation and Import](#installation-and-import)
- [NumPy Array (ndarray)](#numpy-array-ndarray)
  - [Create Array](#create-array)
  - [Array Data Types](#array-data-types)
  - [Array Dimensions](#array-dimensions)
  - [Array Shape](#array-shape)
  - [Array Reshape](#array-reshape)
- [Array Indexing](#array-indexing)
  - [1D Indexing](#1d-indexing)
  - [2D Indexing](#2d-indexing)
  - [3D Indexing](#3d-indexing)
  - [Negative Indexing](#negative-indexing)
- [Array Slicing](#array-slicing)
  - [1D Slicing](#1d-slicing)
  - [2D Slicing](#2d-slicing)
  - [Step Slicing](#step-slicing)
- [Array Iteration](#array-iteration)
  - [nditer](#nditer)
  - [ndenumerate](#ndenumerate)
- [Array Join and Split](#array-join-and-split)
  - [Concatenate](#concatenate)
  - [Stack](#stack)
  - [Split](#split)
- [Array Search, Sort and Filter](#array-search-sort-and-filter)
  - [Search](#search)
  - [Sort](#sort)
  - [Filter](#filter)
- [Array Math Operations](#array-math-operations)
  - [Arithmetic Operations](#arithmetic-operations)
  - [Universal Functions (ufunc)](#universal-functions-ufunc)
  - [Aggregate Functions](#aggregate-functions)
- [Array Creation Functions](#array-creation-functions)
  - [zeros, ones, full](#zeros-ones-full)
  - [arange and linspace](#arange-and-linspace)
  - [eye and identity](#eye-and-identity)
  - [Random Arrays](#random-arrays)
- [Array Copy vs View](#array-copy-vs-view)
- [Broadcasting](#broadcasting)
- [NumPy String Functions](#numpy-string-functions)
- [NumPy Statistical Functions](#numpy-statistical-functions)
- [NumPy Linear Algebra](#numpy-linear-algebra)
- [NumPy Quick Reference](#numpy-quick-reference)

---

## Intro

**NumPy** (Numerical Python) is the fundamental package for **scientific computing** in Python. It provides a powerful N-dimensional array object and tools for working with arrays efficiently.

> **Key Facts:**
> - NumPy arrays are **faster** and use **less memory** than Python lists
> - NumPy arrays are **homogeneous** — all elements must be the same data type
> - NumPy is the foundation for libraries like **Pandas**, **Matplotlib**, **SciPy**, and **Scikit-learn**
> - The core object is the **ndarray** (N-dimensional array)

| Feature | Python List | NumPy Array |
|---|---|---|
| Speed | Slow (interpreted loop) | Fast (C-level operations) |
| Memory | More (stores Python objects) | Less (stores raw C types) |
| Types | Mixed types allowed | Homogeneous (same type) |
| Operations | Manual loops needed | Vectorized operations |

---

## Installation and Import

**Install NumPy using pip:**

```bash
pip install numpy
```

**Import NumPy (always aliased as `np`):**

```python
import numpy as np

# Check the installed version
print(np.__version__)  # Output: e.g., 1.26.4
```

---

## NumPy Array (ndarray)

The **ndarray** is the core data structure in NumPy — a grid of values, all of the **same type**, indexed by a tuple of non-negative integers.

### Create Array

```python
import numpy as np

# From a Python list
arr = np.array([1, 2, 3, 4, 5])
print(arr)         # Output: [1 2 3 4 5]
print(type(arr))   # Output: <class 'numpy.ndarray'>

# 2D array (matrix)
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)
# Output:
# [[1 2 3]
#  [4 5 6]]

# 3D array
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr3d)
# Output:
# [[[1 2]
#   [3 4]]
#  [[5 6]
#   [7 8]]]
```

---

### Array Data Types

NumPy supports many data types. You can set the type at creation with `dtype=`.

| NumPy Type | Description | Python Equivalent |
|---|---|---|
| `np.int8` to `np.int64` | Signed integers | `int` |
| `np.uint8` to `np.uint64` | Unsigned integers | — |
| `np.float32`, `np.float64` | Floating point | `float` |
| `np.complex64`, `np.complex128` | Complex numbers | `complex` |
| `np.bool_` | Boolean | `bool` |
| `np.str_` | Unicode string | `str` |

```python
import numpy as np

# Check data type
arr = np.array([1, 2, 3])
print(arr.dtype)  # Output: int64 (or int32 on Windows)

arr_f = np.array([1.5, 2.5, 3.5])
print(arr_f.dtype)  # Output: float64

# Specify dtype at creation
arr_int = np.array([1, 2, 3], dtype=np.int8)
print(arr_int.dtype)  # Output: int8

arr_str = np.array(["apple", "banana"], dtype=np.str_)
print(arr_str.dtype)  # Output: <U6

# Convert dtype — astype()
arr = np.array([1.9, 2.7, 3.1])
arr_int = arr.astype(int)
print(arr_int)  # Output: [1 2 3]  (truncates, does not round)

arr_bool = np.array([0, 1, 0, 2])
print(arr_bool.astype(bool))  # Output: [False  True False  True]
```

> **Tip:** Use smaller dtypes like `int8` or `float32` to save memory when working with large datasets.

---

### Array Dimensions

| Attribute | Description |
|---|---|
| `ndim` | Number of dimensions (axes) |
| `shape` | Tuple of sizes along each axis |
| `size` | Total number of elements |
| `itemsize` | Size in bytes of each element |
| `nbytes` | Total bytes consumed |

```python
import numpy as np

arr0 = np.array(42)                       # 0D — scalar
arr1 = np.array([1, 2, 3])               # 1D — vector
arr2 = np.array([[1, 2], [3, 4]])        # 2D — matrix
arr3 = np.array([[[1, 2], [3, 4]],
                 [[5, 6], [7, 8]]])      # 3D — tensor

print(arr0.ndim)   # Output: 0
print(arr1.ndim)   # Output: 1
print(arr2.ndim)   # Output: 2
print(arr3.ndim)   # Output: 3

# Force a specific number of dimensions at creation
arr = np.array([1, 2, 3], ndmin=5)
print(arr)         # Output: [[[[[1 2 3]]]]]
print(arr.ndim)    # Output: 5
```

---

### Array Shape

`shape` returns a **tuple** showing the size of each dimension `(rows, columns, ...)`.

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)  # Output: (2, 3)  — 2 rows, 3 columns

arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr3d.shape)  # Output: (2, 2, 2)

# Total element count
print(arr.size)      # Output: 6
print(arr.itemsize)  # Output: 8  (bytes per int64 element)
print(arr.nbytes)    # Output: 48 (6 elements x 8 bytes)
```

---

### Array Reshape

`reshape()` gives a new **shape** to an array **without changing its data**.

> **Rule:** The total number of elements must remain the same. `2x3 = 6`, so you can reshape `(2,3)` to `(6,)`, `(3,2)`, `(1,6)`, etc.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# 1D to 2D
arr2d = arr.reshape(4, 3)
print(arr2d)
# Output:
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

# 1D to 3D
arr3d = arr.reshape(2, 3, 2)
print(arr3d.shape)  # Output: (2, 3, 2)

# Use -1 to let NumPy calculate the dimension automatically
arr_auto = arr.reshape(3, -1)  # -1 means NumPy figures out it is 4
print(arr_auto.shape)           # Output: (3, 4)

# Flatten back to 1D
flat = arr2d.flatten()
print(flat)  # Output: [ 1  2  3  4  5  6  7  8  9 10 11 12]

# ravel() — like flatten() but returns a view when possible
raveled = arr2d.ravel()
print(raveled)  # Output: [ 1  2  3  4  5  6  7  8  9 10 11 12]
```

---

## Array Indexing

### 1D Indexing

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])   # Output: 10  (first element)
print(arr[2])   # Output: 30
print(arr[-1])  # Output: 50  (last element)
print(arr[-2])  # Output: 40

# Use in expressions
print(arr[1] + arr[3])  # Output: 60
```

---

### 2D Indexing

Access elements with `[row, column]` or `[row][column]`.

```python
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print(arr[0, 0])   # Output: 1   (row 0, col 0)
print(arr[1, 2])   # Output: 6   (row 1, col 2)
print(arr[2, -1])  # Output: 9   (row 2, last col)

# Access entire row
print(arr[1])      # Output: [4 5 6]

# Access entire column
print(arr[:, 1])   # Output: [2 5 8]
```

---

### 3D Indexing

Access elements with `[block, row, column]`.

```python
import numpy as np

arr = np.array([[[1, 2], [3, 4]],
                [[5, 6], [7, 8]]])

print(arr[0, 0, 0])  # Output: 1  (block 0, row 0, col 0)
print(arr[0, 1, 1])  # Output: 4  (block 0, row 1, col 1)
print(arr[1, 0, 1])  # Output: 6  (block 1, row 0, col 1)
print(arr[1, 1, 0])  # Output: 7  (block 1, row 1, col 0)
```

---

### Negative Indexing

Negative indices count **from the end**.

```python
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(arr[-1, -1])  # Output: 6  (last row, last col)
print(arr[-1, -2])  # Output: 5  (last row, second-to-last col)
print(arr[-2, 0])   # Output: 1  (second-to-last row, first col)
```

---

## Array Slicing

Slicing syntax: `[start:end:step]` — `end` is **exclusive**.

### 1D Slicing

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])    # Output: [2 3 4 5]   (index 1 to 4)
print(arr[:4])     # Output: [1 2 3 4]   (from start to index 3)
print(arr[4:])     # Output: [5 6 7]     (from index 4 to end)
print(arr[-3:])    # Output: [5 6 7]     (last 3 elements)
print(arr[::2])    # Output: [1 3 5 7]   (every 2nd element)
print(arr[::-1])   # Output: [7 6 5 4 3 2 1]  (reversed)
```

---

### 2D Slicing

```python
import numpy as np

arr = np.array([[1,  2,  3,  4],
                [5,  6,  7,  8],
                [9, 10, 11, 12]])

# Rows 0-1, all columns
print(arr[0:2, :])
# Output:
# [[1 2 3 4]
#  [5 6 7 8]]

# All rows, columns 1-2
print(arr[:, 1:3])
# Output:
# [[ 2  3]
#  [ 6  7]
#  [10 11]]

# Rows 1-2, columns 1-3
print(arr[1:3, 1:3])
# Output:
# [[ 6  7]
#  [10 11]]
```

---

### Step Slicing

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(arr[0:10:2])  # Output: [1 3 5 7 9]   (every 2nd, start 0)
print(arr[1:10:3])  # Output: [2 5 8]        (every 3rd, start 1)

arr2d = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8]])

print(arr2d[0:2, 0:4:2])  # Every 2nd column
# Output:
# [[1 3]
#  [5 7]]
```

---

## Array Iteration

### Basic Iteration

```python
import numpy as np

arr1d = np.array([1, 2, 3])
for x in arr1d:
    print(x)  # Prints: 1, 2, 3

arr2d = np.array([[1, 2, 3], [4, 5, 6]])
for row in arr2d:
    print(row)  # Prints each row: [1 2 3], [4 5 6]

# To iterate element by element in 2D:
for row in arr2d:
    for x in row:
        print(x)  # Prints: 1, 2, 3, 4, 5, 6
```

---

### nditer

`np.nditer()` lets you iterate through **any dimension** of an array element by element.

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

# Iterate every element regardless of shape
for x in np.nditer(arr):
    print(x, end=" ")  # Output: 1 2 3 4 5 6

print()

# Iterate with different step (every 2nd column)
for x in np.nditer(arr[:, ::2]):
    print(x, end=" ")  # Output: 1 3 4 6

print()

# Change dtype during iteration (op_dtypes)
for x in np.nditer(arr, flags=["buffered"], op_dtypes=["S"]):
    print(x, end=" ")  # Output: b'1' b'2' b'3' b'4' b'5' b'6'
```

---

### ndenumerate

`np.ndenumerate()` gives both the **index** and **value** during iteration.

```python
import numpy as np

arr1d = np.array([10, 20, 30])
for idx, val in np.ndenumerate(arr1d):
    print(idx, val)
# Output:
# (0,) 10
# (1,) 20
# (2,) 30

arr2d = np.array([[1, 2], [3, 4]])
for idx, val in np.ndenumerate(arr2d):
    print(idx, val)
# Output:
# (0, 0) 1
# (0, 1) 2
# (1, 0) 3
# (1, 1) 4
```

---

## Array Join and Split

### Concatenate

`np.concatenate()` joins arrays **along an existing axis**.

```python
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Join 1D arrays
result = np.concatenate((arr1, arr2))
print(result)  # Output: [1 2 3 4 5 6]

# Join 2D arrays along rows (axis=0, default)
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(np.concatenate((a, b), axis=0))
# Output:
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

# Join 2D arrays along columns (axis=1)
print(np.concatenate((a, b), axis=1))
# Output:
# [[1 2 5 6]
#  [3 4 7 8]]
```

---

### Stack

`np.stack()` joins arrays along a **new axis**. Differs from `concatenate` which uses an existing axis.

```python
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# stack — creates a new axis
result = np.stack((arr1, arr2))
print(result)
# Output:
# [[1 2 3]
#  [4 5 6]]

# hstack — stack along columns (horizontal)
print(np.hstack((arr1, arr2)))  # Output: [1 2 3 4 5 6]

# vstack — stack along rows (vertical)
print(np.vstack((arr1, arr2)))
# Output:
# [[1 2 3]
#  [4 5 6]]

# dstack — stack along depth (3rd axis)
print(np.dstack((arr1, arr2)))
# Output: [[[1 4] [2 5] [3 6]]]
```

---

### Split

`np.array_split()` splits an array into **multiple sub-arrays**.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

# Split into 3 equal parts
result = np.array_split(arr, 3)
print(result)  # Output: [array([1, 2]), array([3, 4]), array([5, 6])]

# Access individual splits
print(result[0])  # Output: [1 2]
print(result[1])  # Output: [3 4]

# Split into unequal parts (NumPy adjusts automatically)
result = np.array_split(arr, 4)
print(result)  # Output: [array([1, 2]), array([3, 4]), array([5]), array([6])]

# Split 2D array
arr2d = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
result = np.array_split(arr2d, 2)
print(result[0])  # Output: [[1 2] [3 4]]
print(result[1])  # Output: [[5 6] [7 8]]
```

> **Tip:** `np.split()` requires equal splits — use `np.array_split()` for flexible unequal splits.

---

## Array Search, Sort and Filter

### Search

`np.where()` returns the **indices** where a condition is `True`.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

# Find indices where value equals 4
idx = np.where(arr == 4)
print(idx)        # Output: (array([3, 5, 6]),)
print(idx[0])     # Output: [3 5 6]

# Find indices where value is even
even_idx = np.where(arr % 2 == 0)
print(even_idx)   # Output: (array([1, 3, 5, 6]),)

# np.searchsorted — find index to insert value (sorted array)
arr_sorted = np.array([1, 3, 5, 7, 9])
print(np.searchsorted(arr_sorted, 4))              # Output: 2
print(np.searchsorted(arr_sorted, 4, side="right")) # Output: 2
```

---

### Sort

`np.sort()` returns a **sorted copy** — the original is unchanged.

```python
import numpy as np

arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])

# Sort ascending (default)
print(np.sort(arr))   # Output: [1 1 2 3 4 5 6 9]

# Sort descending
print(np.sort(arr)[::-1])  # Output: [9 6 5 4 3 2 1 1]

# Sort strings
arr_str = np.array(["banana", "cherry", "apple"])
print(np.sort(arr_str))  # Output: ['apple' 'banana' 'cherry']

# Sort 2D array (sorts each row independently)
arr2d = np.array([[3, 1, 2], [9, 6, 7]])
print(np.sort(arr2d))
# Output:
# [[1 2 3]
#  [6 7 9]]

# argsort — returns indices that would sort the array
arr = np.array([30, 10, 20])
print(np.argsort(arr))  # Output: [1 2 0]  (10 is at index 1, etc.)
```

---

### Filter

Filtering creates a new array from elements that meet a condition — using **boolean indexing**.

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Manual boolean index array
filter_arr = [True, False, True, False, True]
print(arr[filter_arr])  # Output: [10 30 50]

# Direct boolean condition (most common)
print(arr[arr > 25])         # Output: [30 40 50]
print(arr[arr % 20 == 0])    # Output: [20 40]

# Filter with np.where (replace non-matching with 0)
result = np.where(arr > 25, arr, 0)
print(result)  # Output: [ 0  0 30 40 50]

# Filter strings
words = np.array(["apple", "mango", "banana", "cherry"])
print(words[np.char.startswith(words, "b")])  # Output: ['banana']
```

---

## Array Math Operations

### Arithmetic Operations

NumPy operations are **element-wise** — no loop needed.

```python
import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

print(a + b)    # Output: [11 22 33 44]
print(a - b)    # Output: [ 9 18 27 36]
print(a * b)    # Output: [ 10  40  90 160]
print(a / b)    # Output: [10. 10. 10. 10.]
print(a % b)    # Output: [0 0 0 0]
print(a ** b)   # Output: [    10    400  27000 2560000]
print(a // b)   # Output: [10 10 10 10]

# Scalar operations (broadcast to all elements)
arr = np.array([1, 2, 3, 4, 5])
print(arr + 10)   # Output: [11 12 13 14 15]
print(arr * 3)    # Output: [ 3  6  9 12 15]
print(arr ** 2)   # Output: [ 1  4  9 16 25]
```

---

### Universal Functions (ufunc)

Universal functions operate **element-wise** on arrays and support broadcasting.

| Function | Description |
|---|---|
| `np.add(a, b)` | Element-wise addition |
| `np.subtract(a, b)` | Element-wise subtraction |
| `np.multiply(a, b)` | Element-wise multiplication |
| `np.divide(a, b)` | Element-wise division |
| `np.power(a, b)` | Element-wise power |
| `np.mod(a, b)` | Element-wise modulus |
| `np.abs(a)` | Absolute value |
| `np.sqrt(a)` | Square root |
| `np.exp(a)` | Exponential (e^x) |
| `np.log(a)` | Natural logarithm |
| `np.log10(a)` | Base-10 logarithm |
| `np.sin(a)` | Sine (radians) |
| `np.cos(a)` | Cosine (radians) |
| `np.floor(a)` | Round down to nearest integer |
| `np.ceil(a)` | Round up to nearest integer |
| `np.round(a, n)` | Round to `n` decimal places |

```python
import numpy as np

arr = np.array([1, 4, 9, 16, 25])
print(np.sqrt(arr))   # Output: [1. 2. 3. 4. 5.]

arr = np.array([0.5, 1.0, 1.5, 2.0])
print(np.sin(arr))    # Output: [0.479 0.841 0.997 0.909]

arr = np.array([1.1, 2.5, 3.9])
print(np.floor(arr))     # Output: [1. 2. 3.]
print(np.ceil(arr))      # Output: [2. 3. 4.]
print(np.round(arr, 0))  # Output: [1. 2. 4.]

arr = np.array([-3, -1, 0, 1, 3])
print(np.abs(arr))    # Output: [3 1 0 1 3]
```

---

### Aggregate Functions

Reduce an array to a **single value** (or reduce along an axis).

```python
import numpy as np

arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])

print(np.sum(arr))     # Output: 31
print(np.min(arr))     # Output: 1
print(np.max(arr))     # Output: 9
print(np.mean(arr))    # Output: 3.875
print(np.median(arr))  # Output: 3.5
print(np.prod(arr))    # Output: 6480
print(np.std(arr))     # Output: 2.588  (standard deviation)
print(np.var(arr))     # Output: 6.7    (variance)
print(np.cumsum(arr))  # Output: [ 3  4  8  9 14 23 25 31]

# Axis operations on 2D arrays
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])

print(np.sum(arr2d, axis=0))   # Output: [5 7 9]   (sum each column)
print(np.sum(arr2d, axis=1))   # Output: [ 6 15]   (sum each row)
print(np.max(arr2d, axis=0))   # Output: [4 5 6]   (max of each column)
print(np.mean(arr2d, axis=1))  # Output: [2. 5.]   (mean of each row)
```

---

## Array Creation Functions

### zeros, ones, full

```python
import numpy as np

# zeros — filled with 0.0
print(np.zeros(5))              # Output: [0. 0. 0. 0. 0.]
print(np.zeros((2, 3)))
# Output:
# [[0. 0. 0.]
#  [0. 0. 0.]]

# ones — filled with 1.0
print(np.ones(4))               # Output: [1. 1. 1. 1.]
print(np.ones((3, 3)))
# Output:
# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]

# full — filled with a specific value
print(np.full(5, 7))            # Output: [7 7 7 7 7]
print(np.full((2, 4), 3.14))
# Output:
# [[3.14 3.14 3.14 3.14]
#  [3.14 3.14 3.14 3.14]]

# empty — uninitialized (contains garbage values)
print(np.empty((2, 2)))         # Output: random uninitialized values
```

---

### arange and linspace

```python
import numpy as np

# arange — like range() but returns an ndarray
print(np.arange(5))           # Output: [0 1 2 3 4]
print(np.arange(1, 10))       # Output: [1 2 3 4 5 6 7 8 9]
print(np.arange(0, 10, 2))    # Output: [0 2 4 6 8]  (step of 2)
print(np.arange(0, 1, 0.25))  # Output: [0.   0.25 0.5  0.75]

# linspace — evenly spaced values between start and stop (inclusive)
print(np.linspace(0, 1, 5))
# Output: [0.   0.25 0.5  0.75 1.  ]  (5 points between 0 and 1)

print(np.linspace(0, 100, 6))
# Output: [  0.  20.  40.  60.  80. 100.]

# endpoint=False excludes the stop value
print(np.linspace(0, 1, 5, endpoint=False))
# Output: [0.  0.2 0.4 0.6 0.8]
```

> **`arange` vs `linspace`:** Use `arange` when you know the **step size**. Use `linspace` when you know how many **evenly spaced points** you want.

---

### eye and identity

```python
import numpy as np

# eye — identity matrix (1s on diagonal, 0s elsewhere)
print(np.eye(3))
# Output:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# eye with offset k (k=1 means diagonal above main)
print(np.eye(3, k=1))
# Output:
# [[0. 1. 0.]
#  [0. 0. 1.]
#  [0. 0. 0.]]

# identity — strictly square identity matrix
print(np.identity(3))
# Output:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# diag — create diagonal matrix from 1D array
print(np.diag([1, 2, 3]))
# Output:
# [[1 0 0]
#  [0 2 0]
#  [0 0 3]]
```

---

### Random Arrays

NumPy's `np.random` module generates random data.

| Function | Description |
|---|---|
| `np.random.rand(shape)` | Uniform `[0, 1)` float values |
| `np.random.randn(shape)` | Standard normal distribution |
| `np.random.randint(low, high, size)` | Random integers in `[low, high)` |
| `np.random.random(size)` | Uniform `[0.0, 1.0)` |
| `np.random.choice(arr, size)` | Random samples from an array |
| `np.random.shuffle(arr)` | Shuffle in-place |
| `np.random.seed(n)` | Set seed for reproducibility |

```python
import numpy as np

np.random.seed(42)  # Set seed so results are reproducible

# Random floats [0, 1)
print(np.random.rand(5))
# Output: [0.374 0.951 0.732 0.599 0.156]

# Random floats in a shape
print(np.random.rand(2, 3))  # 2x3 matrix of random floats

# Random integers
print(np.random.randint(1, 10, size=6))
# Output: [7 4 8 5 7 3]

print(np.random.randint(1, 10, size=(3, 3)))  # 3x3 matrix of random ints

# Normal distribution (values centered around 0)
print(np.random.randn(5))

# Random choice
fruits = np.array(["apple", "banana", "cherry"])
print(np.random.choice(fruits, size=4))  # 4 randomly chosen fruits

# Shuffle in-place
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print(arr)  # Output: shuffled array
```

---

## Array Copy vs View

> **Warning:** NumPy slices return a **view** — not a copy. Changing the view changes the original!

| Method | Returns | Affects Original? |
|---|---|---|
| Slicing `arr[1:4]` | **View** | Yes — shared memory |
| `arr.view()` | **View** | Yes — shared memory |
| `arr.copy()` | **Copy** | No — independent |

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# View — modifying it changes original
view = arr[1:4]
view[0] = 99
print(arr)   # Output: [ 1 99  3  4  5]  (original changed!)

# Copy — independent
arr = np.array([1, 2, 3, 4, 5])
copy = arr.copy()
copy[0] = 99
print(arr)   # Output: [1 2 3 4 5]  (original unchanged)

# Check ownership via base attribute
print(copy.base)   # Output: None  (copy owns its data)
print(view.base)   # Output: [ 1 99  3  4  5]  (view points to original)
```

---

## Broadcasting

Broadcasting allows NumPy to perform operations on arrays of **different shapes** by automatically expanding the smaller array.

> **Rule:** Two dimensions are compatible if they are **equal**, or one of them is **1**.

```python
import numpy as np

# Scalar + array
arr = np.array([1, 2, 3])
print(arr + 10)       # Output: [11 12 13]  (10 broadcasts to each element)

# 1D + 2D
a = np.array([[1, 2, 3],
              [4, 5, 6]])       # shape: (2, 3)
b = np.array([10, 20, 30])     # shape: (3,) broadcasts to (2, 3)

print(a + b)
# Output:
# [[11 22 33]
#  [14 25 36]]

# Column vector + row vector
col = np.array([[1], [2], [3]])   # shape: (3, 1)
row = np.array([10, 20, 30])      # shape: (3,)

print(col + row)
# Output:
# [[11 21 31]
#  [12 22 32]
#  [13 23 33]]

# Practical: normalize each row by subtracting row mean
data = np.array([[1, 2, 3],
                 [10, 20, 30]])
row_means = data.mean(axis=1, keepdims=True)  # shape (2, 1)
normalized = data - row_means
print(normalized)
# Output:
# [[-1.  0.  1.]
#  [-10.  0. 10.]]
```

---

## NumPy String Functions

NumPy provides string operations via `np.char` for arrays of strings.

| Function | Description |
|---|---|
| `np.char.upper(arr)` | Converts to uppercase |
| `np.char.lower(arr)` | Converts to lowercase |
| `np.char.capitalize(arr)` | Capitalizes first letter |
| `np.char.title(arr)` | Title-cases each word |
| `np.char.strip(arr)` | Strips whitespace |
| `np.char.replace(arr, old, new)` | Replaces substrings |
| `np.char.split(arr)` | Splits into list |
| `np.char.join(sep, arr)` | Joins characters with separator |
| `np.char.add(arr1, arr2)` | Concatenates element-wise |
| `np.char.startswith(arr, prefix)` | Returns bool array |
| `np.char.endswith(arr, suffix)` | Returns bool array |
| `np.char.find(arr, sub)` | Returns index of substring |
| `np.char.count(arr, sub)` | Counts occurrences |

```python
import numpy as np

arr = np.array(["hello", "world", "numpy"])

print(np.char.upper(arr))         # Output: ['HELLO' 'WORLD' 'NUMPY']
print(np.char.capitalize(arr))    # Output: ['Hello' 'World' 'Numpy']
print(np.char.replace(arr, "l", "L"))  # Output: ['heLLo' 'worLd' 'numpy']

# Add / concatenate element-wise
a = np.array(["Hello", "Good"])
b = np.array([" World", " Morning"])
print(np.char.add(a, b))  # Output: ['Hello World' 'Good Morning']

# Boolean checks
words = np.array(["apple", "banana", "apricot"])
print(np.char.startswith(words, "a"))  # Output: [ True False  True]
print(np.char.find(words, "an"))       # Output: [-1  1 -1]
```

---

## NumPy Statistical Functions

```python
import numpy as np

data = np.array([4, 7, 2, 9, 1, 5, 8, 3, 6, 10])

print(np.mean(data))     # Output: 5.5    (arithmetic average)
print(np.median(data))   # Output: 5.5    (middle value)
print(np.std(data))      # Output: 2.872  (standard deviation)
print(np.var(data))      # Output: 8.25   (variance)
print(np.min(data))      # Output: 1
print(np.max(data))      # Output: 10
print(np.ptp(data))      # Output: 9      (peak-to-peak: max - min)
print(np.percentile(data, 25))  # Output: 3.25  (25th percentile / Q1)
print(np.percentile(data, 75))  # Output: 7.75  (75th percentile / Q3)

# Correlation coefficient matrix
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])
print(np.corrcoef(x, y))  # Output: 2x2 correlation matrix

# Histogram
counts, edges = np.histogram(data, bins=5)
print(counts)  # Output: frequency counts per bin
print(edges)   # Output: bin edge values

# Weighted average
weights = np.array([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
print(np.average(data, weights=weights))  # Output: weighted mean
```

---

## NumPy Linear Algebra

The `np.linalg` module provides linear algebra operations.

| Function | Description |
|---|---|
| `np.dot(a, b)` | Dot product / matrix multiplication |
| `np.matmul(a, b)` | Matrix multiplication (`@` operator) |
| `np.linalg.det(a)` | Determinant of a matrix |
| `np.linalg.inv(a)` | Inverse of a matrix |
| `np.linalg.eig(a)` | Eigenvalues and eigenvectors |
| `np.linalg.norm(a)` | Vector/matrix norm |
| `np.linalg.solve(a, b)` | Solve linear system `Ax = b` |
| `np.transpose(a)` or `a.T` | Transpose a matrix |

```python
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Matrix multiplication
print(np.dot(a, b))
# Output:
# [[19 22]
#  [43 50]]

# Same using @ operator (Python 3.5+)
print(a @ b)
# Output:
# [[19 22]
#  [43 50]]

# Transpose
print(a.T)
# Output:
# [[1 3]
#  [2 4]]

# Determinant
print(np.linalg.det(a))   # Output: -2.0

# Inverse
inv_a = np.linalg.inv(a)
print(inv_a)
# Output:
# [[-2.   1. ]
#  [ 1.5 -0.5]]

# Verify: A x A_inv = Identity
print(np.round(a @ inv_a))
# Output:
# [[1. 0.]
#  [0. 1.]]

# Solve Ax = b (find x where 3x + y = 9, x + 2y = 8)
A = np.array([[3, 1], [1, 2]])
b_vec = np.array([9, 8])
x = np.linalg.solve(A, b_vec)
print(x)  # Output: [2. 3.]

# Eigenvalues and Eigenvectors
vals, vecs = np.linalg.eig(a)
print(vals)   # Output: [-0.372  5.372]
print(vecs)   # Output: 2x2 matrix of eigenvectors
```

---

## NumPy Quick Reference

| Operation | Code | Notes |
|---|---|---|
| Import | `import numpy as np` | Always alias as `np` |
| Create from list | `np.array([1, 2, 3])` | 1D array |
| Create 2D | `np.array([[1,2],[3,4]])` | 2D array / matrix |
| Zeros | `np.zeros((m, n))` | Float 0s by default |
| Ones | `np.ones((m, n))` | Float 1s by default |
| Range | `np.arange(start, stop, step)` | Like `range()` |
| Evenly spaced | `np.linspace(start, stop, n)` | `n` points inclusive |
| Shape | `arr.shape` | Tuple of dimensions |
| Dimensions | `arr.ndim` | Number of axes |
| Size | `arr.size` | Total elements |
| Data type | `arr.dtype` | Element type |
| Change type | `arr.astype(dtype)` | Returns new array |
| Reshape | `arr.reshape(m, n)` | Must keep same total size |
| Flatten | `arr.flatten()` | Copy to 1D |
| Ravel | `arr.ravel()` | View to 1D when possible |
| Slice | `arr[1:4]` | Returns view |
| Copy | `arr.copy()` | Returns independent copy |
| Indexing 2D | `arr[row, col]` | Or `arr[row][col]` |
| Sort | `np.sort(arr)` | Returns sorted copy |
| Reverse | `arr[::-1]` | Slice trick |
| Find indices | `np.where(arr > 5)` | Returns tuple of index arrays |
| Concatenate | `np.concatenate((a, b))` | Along existing axis |
| Stack | `np.vstack` / `np.hstack` | New or column axis |
| Split | `np.array_split(arr, n)` | Flexible unequal splits |
| Sum | `np.sum(arr)` | Use `axis=` for rows/cols |
| Mean | `np.mean(arr)` | Average |
| Max / Min | `np.max(arr)` / `np.min(arr)` | Overall or along axis |
| Std / Var | `np.std(arr)` / `np.var(arr)` | Statistics |
| Matrix multiply | `a @ b` or `np.matmul(a, b)` | Not element-wise |
| Element multiply | `a * b` | Element-wise |
| Transpose | `arr.T` | Swap rows and columns |
| Inverse | `np.linalg.inv(arr)` | Square matrix only |
| Random int | `np.random.randint(l, h, size)` | `[l, h)` range |
| Random float | `np.random.rand(shape)` | `[0, 1)` range |
| Set seed | `np.random.seed(n)` | Reproducibility |

---

<div align="center">

*NumPy Notes — Complete Reference*

</div>
