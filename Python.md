<div align="center">

# Python Notes

> A complete reference of everything I have practiced.

</div>

---

## Table of Contents

- [Intro](#intro)
- [Print, Comment, Variable and Naming](#print--comment--variable-and-naming)
- [Type Casting](#type-casting)
- [Data Types](#data-types)
  - [Numbers](#numbers)
  - [Booleans](#booleans)
  - [Strings](#strings)
- [Operators](#operators)
  - [Arithmetic Operators](#arithmetic-operators)
  - [Assignment Operators](#assignment-operators)
  - [Comparison Operators](#comparison-operators)
  - [Logical Operators](#logical-operators)
  - [Identity Operators](#identity-operators)
  - [Membership Operators](#membership-operators)
  - [Bitwise Operators](#bitwise-operators)
  - [Operator Precedence](#operator-precedence)
- [Lists](#lists)
  - [Access List Items](#access-list-items)
  - [Change List Items](#change-list-items)
  - [Add List Items](#add-list-items)
  - [Remove List Items](#remove-list-items)
  - [Loop in List](#loop-in-list)
  - [List Comprehension](#list-comprehension)
  - [Sort List](#sort-list)
  - [Copy List](#copy-list)
  - [Join Lists](#join-lists)
  - [List Methods](#list-methods--quick-reference)

---

## Intro

Python is a **high-level**, **interpreted**, **general-purpose** programming language.
It emphasizes **code readability** and **simplicity** — designed so that developers can express concepts in fewer lines of code.

```python
print("Hello World!")
print("Learning Python")
print("It is awesome!")
```

> **Key Facts:**
> - Python files use the `.py` extension
> - Python uses **indentation** instead of `{}` braces for code blocks
> - Python is **dynamically typed** — no need to declare variable types

---

## Print , Comment , Variable and Naming

### Print

The `print()` function outputs text or values to the console.

```python
print("Hello World!")           # String output
print(10)                       # Number output
print("Hello", "World")         # Multiple values (separated by space)
print("a", "b", "c", sep="-")   # Custom separator — Output: a-b-c
print("Hello", end=" ")         # Custom end character (default is newline)
```

---

### Comment

Comments are **ignored by the interpreter** and are used to explain code.

```python
# This is a single-line comment

"""
This is a
multi-line comment (docstring)
"""
```

> **Note:** Triple-quoted strings used as comments are technically **docstrings**, not comments. But they work the same way when not assigned to a variable.

---

### Variable

Variables **store data values**. Python has no keyword for declaring variables — just assign a value directly.

```python
x = 10
name = "Rijoan Maruf"
is_active = True
```

---

### Variable Naming Rules

| Allowed | Not Allowed |
|---|---|
| Start with a letter or `_` | Start with a number |
| Letters, digits, underscores | Hyphens `-` or spaces |
| Case-sensitive (`name` != `Name`) | Python keywords (`if`, `for`, etc.) |

```python
# Valid names
myVariable = "hello"
my_variable = "hello"
_variable = "hello"
VARIABLE = "hello"
myVar2 = "hello"

# Invalid names
# 2variable = "hello"   # Cannot start with a number
# my-variable = "hello" # Hyphens not allowed
```

---

### Multiple Variables

**Assign different values in one line:**

```python
x, y, z = "Orange", "Banana", "Cherry"
print(x)  # Orange
print(y)  # Banana
print(z)  # Cherry
```

**Assign the same value to multiple variables:**

```python
x = y = z = "Orange"
print(x)  # Orange
print(y)  # Orange
print(z)  # Orange
```

---

### Unpack from a Collection

Extract values from a list (or tuple) directly into variables.

```python
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)  # apple
print(y)  # banana
print(z)  # cherry
```

---

### Global Variable

| Scope | Meaning |
|---|---|
| **Global** | Created outside a function — accessible everywhere |
| **Local** | Created inside a function — only accessible inside it |

```python
x = "awesome"          # Global variable

def myfunc():
    x = "fantastic"    # Local variable (does NOT change global x)
    print("Python is " + x)

myfunc()                  # Output: Python is fantastic
print("Python is " + x)  # Output: Python is awesome
```

> **Note:** Use the `global` keyword inside a function if you want to **modify** the global variable.
>
> ```python
> x = "awesome"
> def myfunc():
>     global x
>     x = "fantastic"
> myfunc()
> print(x)  # fantastic
> ```

---

## Type Casting

Type casting is the process of **converting one data type into another**.

| Function | Converts To | Example | Output |
|---|---|---|---|
| `int()` | Integer | `int(2.9)` | `2` |
| `float()` | Float | `float(1)` | `1.0` |
| `str()` | String | `str(10)` | `"10"` |

### int()

Converts to an **integer** (drops the decimal — does NOT round).

```python
x = int(1)      # 1
y = int(2.2)    # 2  (truncates, not rounds)
z = int("2")    # 2  (from string)

print(x, y, z)  # Output: 1 2 2
```

---

### float()

Converts to a **floating-point** number.

```python
x = float(1)      # 1.0
y = float(2.8)    # 2.8
z = float("3")    # 3.0
w = float("4.2")  # 4.2

print(x, y, z, w)  # Output: 1.0 2.8 3.0 4.2
```

---

### str()

Converts to a **string**.

```python
x = str("s1")  # 's1'
y = str(2)     # '2'
z = str(3.0)   # '3.0'

print(x, y, z)  # Output: s1 2 3.0
```

---

## Data Types

Python has several built-in data types. Here are the ones practiced so far:

| Category | Types |
|---|---|
| Numeric | `int`, `float`, `complex` |
| Text | `str` |
| Boolean | `bool` |
| Sequence | `list`, `tuple`, `range` |

---

### Numbers

Python has **three** numeric types: `int`, `float`, and `complex`.

#### int — Integer

Whole numbers, positive or negative, with **unlimited length**.

```python
x = 1
y = 35656222554887711
z = -3255522

print(type(x))  # <class 'int'>
print(type(y))  # <class 'int'>
print(type(z))  # <class 'int'>
```

#### float — Floating Point

Numbers **with a decimal point**. Also supports scientific notation with `e` or `E`.

```python
x = 1.10
y = 1.0
z = -35.59

print(type(x))  # <class 'float'>

# Scientific notation
a = 35e3    # 35000.0
b = 12E4    # 120000.0
c = -87.7e100

print(type(a))  # <class 'float'>
```

#### complex — Complex Number

Written with a **`j`** as the imaginary part.

```python
x = 3 + 5j
y = 5j
z = -5j

print(type(x))  # <class 'complex'>
print(type(y))  # <class 'complex'>
```

#### Random Number

Python has no built-in `random()` function — use the **`random` module**.

```python
import random

print(random.randrange(1, 10))  # Output: Random integer between 1 and 9
```

---

### Booleans

Booleans represent one of two values: **`True`** or **`False`**.

```python
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")  # Output: b is not greater than a
```

> **Tip:** Almost any value evaluates to `True`. Empty values like `0`, `""`, `[]`, `None` evaluate to `False`.

---

### Strings

Strings are **sequences of characters** surrounded by single `'...'` or double `"..."` quotes.

```python
print("My Name is Rijoan Maruf")  # Output: My Name is Rijoan Maruf
```

#### Multi-line String

Use **triple quotes** for strings that span multiple lines.

```python
x = """
hello,
i am rijoan maruf,
i am a full stack developer
"""
print(x)
```

#### String as a Character Array

Strings are **arrays of characters**. Access individual characters using index notation.

```python
a = "Rijoan, Maruf"
print(a[0])   # Output: R  (first character)
print(a[-1])  # Output: f  (last character)
```

#### Loop Through a String

Iterate over every character using a `for` loop.

```python
for i in "Md Rijoan Maruf":
    print(i)  # Prints each character on a new line
```

#### String Length

Use `len()` to count characters.

```python
x = "Rijoan"
print(len(x))  # Output: 6
```

#### Check String — `in` / `not in`

Check whether a substring exists inside a string.

```python
text = "Hello i am rijoan"
print("am" in text)       # Output: True

text = "Hello, i am a full stack web developer"
print("web" not in text)  # Output: False
```

#### String Slicing

Extract a portion of a string using `[start:end]` notation.

| Slice | Meaning |
|---|---|
| `x[2:4]` | Characters from index 2 up to (not including) 4 |
| `x[:5]` | From the start up to index 4 |
| `x[5:]` | From index 5 to the end |
| `x[-5:-2]` | Negative indexing — counts from end |

```python
x = "Rijoan Maruf"
print(x[2:4])    # Output: jo
print(x[:5])     # Output: Rijoa
print(x[5:])     # Output: n Maruf
print(x[-5:-2])  # Output: Mar
```

#### String Concatenation

Join strings using the **`+`** operator.

```python
a = "Hello"
b = "World"
c = a + " " + b
print(c)  # Output: Hello World
```

#### F-String (Formatted String Literal)

The **most modern** and readable way to embed expressions inside strings. Prefix the string with `f`.

```python
age = 24
name = "Rijoan Maruf"
txt = f"My name is {name}, I am {age} years old"
print(txt)  # Output: My name is Rijoan Maruf, I am 24 years old

# Expressions work inside {}
print(f"5 + 3 = {5 + 3}")  # Output: 5 + 3 = 8
```

#### Escape Character

Use `\` to insert special characters that would otherwise break the string.

| Escape | Result |
|---|---|
| `\"` | Double quote |
| `\'` | Single quote |
| `\\` | Backslash |
| `\n` | New line |
| `\t` | Tab |

```python
txt = "We are the so-called \"Vikings\" from the north."
print(txt)  # Output: We are the so-called "Vikings" from the north.
```

#### String Methods — Quick Reference

| Method | Description |
|---|---|
| `upper()` | Converts string to uppercase |
| `lower()` | Converts string to lowercase |
| `strip()` | Removes whitespace from both ends |
| `replace(old, new)` | Replaces a substring with another |
| `split(sep)` | Splits string into a list |
| `capitalize()` | Uppercases only the first character |
| `casefold()` | Converts to lowercase (aggressive, for comparisons) |
| `center(width)` | Centers the string in a given width |
| `count(value)` | Counts occurrences of a value |
| `endswith(value)` | Returns `True` if string ends with value |
| `find(value)` | Returns index of first match, `-1` if not found |
| `index(value)` | Like `find()` but raises `ValueError` if not found |

#### 1. `upper()` — Convert to Uppercase

```python
x = "Software Engineering"
print(x.upper())  # Output: SOFTWARE ENGINEERING
```

#### 2. `lower()` — Convert to Lowercase

```python
x = "Web DEVELOPMENT"
print(x.lower())  # Output: web development
```

#### 3. `strip()` — Remove Whitespace from Both Ends

```python
a = "   Rijoan    Maruf"
print(a.strip())  # Output: Rijoan    Maruf
```

#### 4. `replace(old, new)` — Replace a Substring

```python
a = "Hello World"
print(a.replace("H", "J"))  # Output: Jello World
```

#### 5. `split(separator)` — Split into a List

```python
a = "Md Rijoan Maruf"
print(a.split(" "))  # Output: ['Md', 'Rijoan', 'Maruf']
```

#### 6. `capitalize()` — Uppercase the First Character

```python
txt = "hello, welcome to my project"
print(txt.capitalize())  # Output: Hello, welcome to my project
```

#### 7. `casefold()` — Aggressive Lowercase

More thorough than `lower()` — handles special international characters.

```python
txt = "Hello, And Welcome To My World!"
print(txt.casefold())  # Output: hello, and welcome to my world!
```

#### 8. `center(width)` — Center the String

```python
txt = "banana"
print(txt.center(40))  # Output:                  banana
```

#### 9. `count(value)` — Count Occurrences

```python
txt = "I love apples, apple are my favorite fruit. apple"
print(txt.count("apple"))  # Output: 3

# With range: count(value, start, end)
txt = "I love apples, apple are my favorite fruit"
print(txt.count("apple", 10, 24))  # Output: 1
```

#### 10. `endswith(value)` — Check End of String

```python
txt = "Hello, welcome to my world."
print(txt.endswith("."))  # Output: True
```

#### 11. `find(value)` — Find Position of Substring

Returns the **index** of the first occurrence. Returns **`-1`** if not found.

```python
txt = "Hello, welcome to my world."
print(txt.find("welcome"))  # Output: 7

# With range: find(value, start, end)
print(txt.find("e", 5, 10))  # Output: 8
```

#### 12. `index(value)` — Like `find()` but Raises Error

Same as `find()`, but raises a **`ValueError`** if the value is not found.

```python
txt = "Hello, welcome to my world."
print(txt.index("welcome"))  # Output: 7
```

---

## Operators

Python supports **7 categories of operators**: Arithmetic, Assignment, Comparison, Logical, Identity, Membership, and Bitwise. Each serves a different purpose when working with data.

### Arithmetic Operators

Perform basic **mathematical** operations.

| Operator | Name | Example | Result |
|---|---|---|---|
| `+` | Addition | `15 + 4` | `19` |
| `-` | Subtraction | `15 - 4` | `11` |
| `*` | Multiplication | `15 * 4` | `60` |
| `/` | Division | `15 / 4` | `3.75` |
| `%` | Modulus | `15 % 4` | `3` |
| `**` | Exponentiation | `15 ** 4` | `50625` |
| `//` | Floor Division | `15 // 4` | `3` |

```python
x = 15
y = 4

print(x + y)   # Output: 19
print(x - y)   # Output: 11
print(x * y)   # Output: 60
print(x / y)   # Output: 3.75
print(x % y)   # Output: 3
print(x ** y)  # Output: 50625
print(x // y)  # Output: 3
```

---

### Assignment Operators

Used to **assign values** to variables.

| Operator | Example | Equivalent |
|---|---|---|
| `=` | `x = 5` | `x = 5` |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 3` | `x = x * 3` |
| `/=` | `x /= 3` | `x = x / 3` |
| `%=` | `x %= 3` | `x = x % 3` |
| `//=` | `x //= 3` | `x = x // 3` |
| `**=` | `x **= 3` | `x = x ** 3` |
| `&=` | `x &= 3` | `x = x & 3` |
| `\|=` | `x \|= 3` | `x = x \| 3` |
| `^=` | `x ^= 3` | `x = x ^ 3` |
| `>>=` | `x >>= 3` | `x = x >> 3` |
| `<<=` | `x <<= 3` | `x = x << 3` |

---

### Comparison Operators

Compare two values and return a **boolean** (`True` or `False`).

| Operator | Name | Example | Result |
|---|---|---|---|
| `==` | Equal | `5 == 3` | `False` |
| `!=` | Not equal | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |
| `<=` | Less than or equal | `5 <= 3` | `False` |

```python
x = 5
y = 3

print(x == y)  # Output: False
print(x != y)  # Output: True
print(x > y)   # Output: True
print(x < y)   # Output: False
print(x >= y)  # Output: True
print(x <= y)  # Output: False
```

---

### Logical Operators

**Combine** multiple conditions into one expression.

| Operator | Description | Example |
|---|---|---|
| `and` | Both conditions must be `True` | `x > 0 and x < 10` |
| `or` | At least one condition must be `True` | `x > 0 or x < 10` |
| `not` | Reverses the result | `not(x > 3)` |

```python
x = 5
print(x > 0 and x < 10)        # Output: True
print(x > 0 or x < 10)         # Output: True
print(not(x > 3 and x < 10))   # Output: False
```

---

### Identity Operators

Check if two variables point to the **same object in memory** — not just equal values.

| Operator | Description |
|---|---|
| `is` | Returns `True` if both variables are the same object |
| `is not` | Returns `True` if they are different objects |

```python
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x                   # z points to the SAME object as x

print(x is z)      # Output: True  — same object
print(x is y)      # Output: False — different objects (even though values are equal)
print(x == y)      # Output: True  — values are equal

print(x is not z)  # Output: False
print(x is not y)  # Output: True
```

> **`is` vs `==`:** Use `==` to compare **values**. Use `is` to check if two variables are the **exact same object** in memory.

---

### Membership Operators

Check if a value **exists** inside a sequence (list, string, tuple, etc.).

| Operator | Description |
|---|---|
| `in` | Returns `True` if the value is in the sequence |
| `not in` | Returns `True` if the value is NOT in the sequence |

```python
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)         # Output: True
print("pineapple" not in fruits)  # Output: True

# Also works with strings
text = "Hello World"
print("Hello" in text)            # Output: True
```

---

### Bitwise Operators

Operate on numbers at the **binary (bit) level**.

| Operator | Name | Example | Result |
|---|---|---|---|
| `&` | AND | `6 & 3` | `2` |
| `\|` | OR | `6 \| 3` | `7` |
| `^` | XOR | `6 ^ 3` | `5` |
| `~` | NOT | `~3` | `-4` |
| `<<` | Left Shift | `3 << 2` | `12` |
| `>>` | Right Shift | `8 >> 2` | `2` |

```python
print(6 & 3)   # Output: 2  — AND:         0110 & 0011 = 0010
print(6 | 3)   # Output: 7  — OR:          0110 | 0011 = 0111
print(6 ^ 3)   # Output: 5  — XOR:         0110 ^ 0011 = 0101
print(~3)      # Output: -4 — NOT:         inverts all bits
print(3 << 2)  # Output: 12 — Left Shift:  multiplies by 2^2
print(8 >> 2)  # Output: 2  — Right Shift: divides by 2^2
```

---

### Operator Precedence

When an expression has multiple operators, Python evaluates them by **priority** (highest first):

| Priority | Operator | Description |
|---|---|---|
| 1 (Highest) | `()` | Parentheses |
| 2 | `**` | Exponentiation |
| 3 | `+x`, `-x`, `~x` | Unary operators |
| 4 | `*`, `/`, `//`, `%` | Multiplication / Division |
| 5 | `+`, `-` | Addition / Subtraction |
| 6 | `<<`, `>>` | Bitwise Shifts |
| 7 | `&` | Bitwise AND |
| 8 | `^` | Bitwise XOR |
| 9 | `\|` | Bitwise OR |
| 10 | `==`, `!=`, `>`, `>=`, `<`, `<=`, `is`, `is not`, `in`, `not in` | Comparisons |
| 11 | `not` | Logical NOT |
| 12 | `and` | Logical AND |
| 13 (Lowest) | `or` | Logical OR |

---

## Lists

A **list** is one of Python's most versatile data structures.

| Property | Detail |
|---|---|
| **Ordered** | Items have a defined order and keep it |
| **Changeable** | You can add, remove, and modify items |
| **Allows Duplicates** | Same value can appear multiple times |
| **Mixed Types** | Can hold different data types together |

```python
# Basic list
fruits = ["apple", "banana", "cherry"]
print(fruits)          # Output: ['apple', 'banana', 'cherry']
print(len(fruits))     # Output: 3

# Duplicates allowed
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(len(thislist))   # Output: 5

# Mixed data types
mixed = ["abc", 34, True, 40, "male"]
print(mixed)

# Check the type
print(type(fruits))    # Output: <class 'list'>
```

---

### Access List Items

#### By Index (0-based)

```python
thislist = ["apple", "banana", "cherry"]
print(thislist[0])   # Output: apple
print(thislist[1])   # Output: banana
print(thislist[2])   # Output: cherry
```

#### Negative Index (Count from End)

```python
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])  # Output: cherry  (last item)
print(thislist[-2])  # Output: banana  (second from last)
```

#### Range / Slicing

```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[2:5])    # Output: ['cherry', 'orange', 'kiwi']
print(thislist[:4])     # Output: ['apple', 'banana', 'cherry', 'orange']
print(thislist[2:])     # Output: ['cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thislist[-4:-1])  # Output: ['orange', 'kiwi', 'melon']
```

#### Check if Item Exists

```python
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
```

---

### Change List Items

```python
# Change a single item
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)  # Output: ['apple', 'blackcurrant', 'cherry']

# Change a range of items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)  # Output: ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

# Insert at specific position (no replacement)
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)  # Output: ['apple', 'banana', 'watermelon', 'cherry']
```

---

### Add List Items

| Method | Description |
|---|---|
| `append(item)` | Adds item to the **end** |
| `insert(index, item)` | Inserts item at a **specific position** |
| `extend(iterable)` | Adds all items from another list/iterable |

```python
# append()
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)  # Output: ['apple', 'banana', 'cherry', 'orange']

# insert()
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)  # Output: ['apple', 'orange', 'banana', 'cherry']

# extend()
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)  # Output: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
```

---

### Remove List Items

| Method | Description |
|---|---|
| `remove(value)` | Removes first item with the given value |
| `pop(index)` | Removes item at given index (default: last) |
| `del list[index]` | Deletes item at index or the entire list |
| `clear()` | Empties the list (list still exists) |

```python
# remove()
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)  # Output: ['apple', 'cherry']

# pop()
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)  # Output: ['apple', 'cherry']

# del
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)  # Output: ['banana', 'cherry']

# del (entire list)
thislist = ["apple", "banana", "cherry"]
del thislist     # list no longer exists!

# clear()
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)  # Output: []
```

---

### Loop in List

**4 ways to loop through a list:**

```python
thislist = ["apple", "banana", "cherry"]

# 1. for loop (most common)
for x in thislist:
    print(x)

# 2. for loop with index (using range + len)
for i in range(len(thislist)):
    print(thislist[i])

# 3. while loop
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# 4. List Comprehension loop
[print(x) for x in thislist]
```

---

### List Comprehension

A **concise one-liner** to create a new list based on an existing iterable.

**Syntax:** `newlist = [expression for item in iterable if condition]`

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# Traditional way (5 lines)
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)  # Output: ['apple', 'banana', 'mango']

# List Comprehension (1 line — same result!)
newlist = [x for x in fruits if "a" in x]
print(newlist)  # Output: ['apple', 'banana', 'mango']
```

> **More Examples:**
>
> ```python
> # All items uppercase
> upper_list = [x.upper() for x in fruits]
>
> # Only items that are not "apple"
> no_apple = [x for x in fruits if x != "apple"]
>
> # Squares of numbers 0-9
> squares = [x ** 2 for x in range(10)]
> ```

---

### Sort List

```python
# Sort ascending (A-Z / smallest to largest)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)  # Output: ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

# Sort descending (Z-A / largest to smallest)
thislist.sort(reverse=True)
print(thislist)  # Output: ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

# Custom sort — sort by closeness to 50
def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)  # Output: [50, 65, 23, 82, 100]

# Reverse current order (does NOT sort, just reverses)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)  # Output: ['cherry', 'Kiwi', 'Orange', 'banana']
```

---

### Copy List

> **Warning:** `list2 = list1` does **NOT** copy the list — it creates another reference to the **same** object. Changing one will change the other!

| Method | How |
|---|---|
| `copy()` | Built-in list copy method |
| `list()` | Pass original into `list()` constructor |
| `[:]` | Slice the whole list |

```python
thislist = ["apple", "banana", "cherry"]

# 1. copy() method
mylist = thislist.copy()
print(mylist)  # Output: ['apple', 'banana', 'cherry']

# 2. list() constructor
mylist = list(thislist)
print(mylist)  # Output: ['apple', 'banana', 'cherry']

# 3. Slice operator [:]
mylist = thislist[:]
print(mylist)  # Output: ['apple', 'banana', 'cherry']
```

---

### Join Lists

```python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

# 1. Using + operator
list3 = list1 + list2
print(list3)  # Output: ['a', 'b', 'c', 1, 2, 3]

# 2. Using a loop with append()
for x in list2:
    list1.append(x)
print(list1)  # Output: ['a', 'b', 'c', 1, 2, 3]

# 3. Using extend()
list1 = ["a", "b", "c"]
list1.extend(list2)
print(list1)  # Output: ['a', 'b', 'c', 1, 2, 3]
```

---

### List Methods — Quick Reference

| Method | Description |
|---|---|
| `append(item)` | Adds an element at the **end** |
| `insert(i, item)` | Inserts element at position `i` |
| `extend(iterable)` | Adds all items from another iterable |
| `remove(value)` | Removes first occurrence of `value` |
| `pop(index)` | Removes and returns item at `index` |
| `clear()` | Removes all elements |
| `sort()` | Sorts the list in-place |
| `reverse()` | Reverses the list in-place |
| `copy()` | Returns a shallow copy |
| `index(value)` | Returns index of first `value` |
| `count(value)` | Returns number of occurrences of `value` |

---

## What's Next

Topics coming up in practice:

| Topic | Description |
|---|---|
| **Tuples** | Ordered, unchangeable collection |
| **Sets** | Unordered, no duplicates |
| **Dictionaries** | Key-value pairs |
| **If / Else** | Conditional statements |
| **Loops** | `for`, `while` loops |
| **Functions** | Defining and calling functions |
| **Lambda** | Anonymous functions |
| **Classes & Objects** | Object-oriented programming |
| **Modules** | Importing and using modules |
| **File Handling** | Read and write files |

---

<div align="center">

*Python Notes — Up to Lists*

</div>
