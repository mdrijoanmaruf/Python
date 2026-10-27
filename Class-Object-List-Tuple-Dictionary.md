<div align="center">

# Quiz 1 Notes — Data Structures & OOP

> Complete reference notes for: **List**, **Tuple**, **Dictionary**, **Class & Object**  
> Practiced concepts and complete reference extracted from Python Notes.

</div>

---

## Table of Contents

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
  - [List Methods — Quick Reference](#list-methods--quick-reference)
- [Tuples](#tuples)
  - [Access Tuple Items](#access-tuple-items)
  - [Update Tuples](#update-tuples)
  - [Unpack Tuple](#unpack-tuple)
  - [Loop In Tuple](#loop-in-tuple)
  - [Join Tuples](#join-tuples)
  - [Tuple Methods](#tuple-methods)
- [Dictionaries](#dictionaries)
  - [Access Dictionary Items](#access-dictionary-items)
  - [Change Dictionary Values](#change-dictionary-values)
  - [Add Dictionary Items](#add-dictionary-items)
  - [Remove Dictionary Items](#remove-dictionary-items)
  - [Loop In Dictionary](#loop-in-dictionary)
  - [Copy Dictionary](#copy-dictionary)
  - [Nested Dictionaries](#nested-dictionaries)
  - [Dictionary Methods](#dictionary-methods)
- [OOP — Object-Oriented Programming (Classes & Objects)](#oop--object-oriented-programming)
  - [Classes and Objects](#classes-and-objects)
  - [The `__init__()` Method](#the-__init__-method)
  - [The `self` Parameter](#the-self-parameter)
  - [Object Methods](#object-methods)
  - [Modify and Delete Object Properties](#modify-and-delete-object-properties)
  - [Inheritance](#inheritance)
  - [The `super()` Function](#the-super-function)
  - [Override Methods](#override-methods)
  - [Multiple Inheritance](#multiple-inheritance)
  - [Encapsulation](#encapsulation)
  - [Getters and Setters (`@property`)](#getters-and-setters-property)
  - [Polymorphism](#polymorphism)
  - [Abstraction](#abstraction)
  - [Class Variables vs Instance Variables](#class-variables-vs-instance-variables)
  - [Class Methods and Static Methods](#class-methods-and-static-methods)
  - [Magic / Dunder Methods](#magic--dunder-methods)
  - [OOP Quick Reference](#oop-quick-reference)

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

## Tuples

A **tuple** is a collection which is ordered and **unchangeable** (immutable).

| Property | Detail |
|---|---|
| **Ordered** | Items have a defined order and keep it |
| **Unchangeable** | You cannot change, add, or remove items after creation |
| **Allows Duplicates** | Same value can appear multiple times |

```python
# Basic tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)  # Output: ('apple', 'banana', 'cherry')

# Without parentheses
thistuple = "apple", "banana", "cherry"
print(thistuple)  # Output: ('apple', 'banana', 'cherry')

# Tuple Length
print(len(thistuple))  # Output: 3

# Tuple with one item (must have a comma)
thistuple = ("apple",)
print(type(thistuple))  # Output: <class 'tuple'>

# NOT a tuple (it's a string)
thistuple = ("apple")
print(type(thistuple))  # Output: <class 'str'>

# Empty Tuple
thistuple = ()
print(type(thistuple))  # Output: <class 'tuple'>

# Mixed Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)  # Output: ('apple', 'banana', 'cherry')
```

---

### Access Tuple Items

```python
# Access Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])  # Output: banana

# Negative Indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])  # Output: cherry

# Range of indexed
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])  # Output: ('cherry', 'orange', 'kiwi')
# Note: The search will start at index 2 (included) and end at index 5 (not included).

# Range of Negative Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])  # Output: ('orange', 'kiwi', 'melon')

# Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")  # Output: Yes, 'apple' is in the fruits tuple
```

---

### Update Tuples

Since tuples are **unchangeable**, you cannot add, remove, or change items directly. You must first convert the tuple to a list.

```python
# Change Tuple values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

# Add Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(y)  # Output: ['apple', 'banana', 'cherry', 'orange']

# Add items using another tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)  # Output: ('apple', 'banana', 'cherry', 'orange')

# Remove Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple) # First convert into list then remove
y.remove("apple")
thistuple = tuple(y)
print(y)  # Output: ['banana', 'cherry']

# Completely Delete tuple
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) # this will raise an error because the tuple no longer exists
```

---

### Unpack Tuple

Extracting values back into variables is called "unpacking".

```python
# Unpack Tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)   # Output: apple
print(yellow)  # Output: banana
print(red)     # Output: cherry

# Using Asterisk
# If the number of variables is less than the number of values,
# you can add an * to the variable name and the values will be assigned to it as a list.
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)   # Output: apple
print(yellow)  # Output: banana
print(red)     # Output: ['cherry', 'strawberry', 'raspberry']
```

---

### Loop In Tuple

```python
# Loop
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
  # Output: 
  # apple
  # banana
  # cherry

# Loop Through index number
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
  # Output:
  # apple
  # banana
  # cherry

# Using while loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
  # Output:
  # apple
  # banana
  # cherry
```

---

### Join Tuples

```python
# Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)  # Output: ('a', 'b', 'c', 1, 2, 3)

# Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)  # Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
```

---

### Tuple Methods

| Method | Description |
|---|---|
| `count(value)` | Returns the number of times a specified value occurs in a tuple |
| `index(value)` | Searches the tuple for a specified value and returns the position of where it was found |

```python
# count()
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)  # Output: 2

# index()
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)  # Output: 3
```

---

## Dictionaries

Dictionaries are used to store data values in **key:value** pairs.
As of Python 3.7, dictionaries are **ordered**. In Python 3.6 and earlier, dictionaries are **unordered**.

| Property | Detail |
|---|---|
| **Ordered** | Items have a defined order and that order will not change. |
| **Changeable** | We can change, add or remove items after the dictionary has been created. |
| **No Duplicates** | Dictionaries cannot have two items with the same key. |

```python
# Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# Dictionary Items
print(thisdict["brand"])  # Output: Ford

# Duplicates Not Allowed (Overwrites existing key)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# Length
print(len(thisdict))  # Output: 3

# Data types
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)  # Output: {'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}

# type()
print(type(thisdict))  # Output: <class 'dict'>

# The dict() Constructor
thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)  # Output: {'name': 'John', 'age': 36, 'country': 'Norway'}
```

---

### Access Dictionary Items

```python
# Accessing items
thisdict = dict(name="Md Rijoan Maruf", age=36, country="Norway")
print(thisdict)  # Output: {'name': 'Md Rijoan Maruf', 'age': 36, 'country': 'Norway'}

# get()
x = thisdict.get("name")
print(x)  # Output: Md Rijoan Maruf

# Keys - keys()
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) # Output: dict_keys(['brand', 'model', 'year']) (before the change)

car["color"] = "white"
print(x) # Output: dict_keys(['brand', 'model', 'year', 'color']) (after the change)

# Get Values - values()
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) # Output: dict_values(['Ford', 'Mustang', 1964]) (before the change)

car["year"] = 2020
print(x) # Output: dict_values(['Ford', 'Mustang', 2020]) (after the change)

# Get Items - items()
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) # Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)]) (before the change)

car["year"] = 2020
print(x) # Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)]) (after the change)

# Check if key exists
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
  # Output: Yes, 'model' is one of the keys in the thisdict dictionary
```

---

### Change Dictionary Values

```python
# Change Values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

# Update Dictionary - update()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
```

---

### Add Dictionary Items

```python
# Adding items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

# Update Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
```

---

### Remove Dictionary Items

```python
# Removing Items

# pop()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)  # Output: {'brand': 'Ford', 'year': 1964}

# popitem() - removes the last inserted item (in versions before 3.7, a random item is removed instead)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)  # Output: {'brand': 'Ford', 'model': 'Mustang'}

# del
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)  # Output: {'brand': 'Ford', 'year': 1964}
# The del keyword can also delete the dictionary completely (e.g. del thisdict).
```

---

### Loop In Dictionary

```python
# Loop Through a Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
  print(x)
  # Output:
  # brand
  # model
  # year

# Loop in keys
for x in thisdict.keys():
  print(x)
  # Output:
  # brand
  # model
  # year

# Loop in values
for x in thisdict.values():
  print(x)
  # Output:
  # Ford
  # Mustang
  # 1964
```

---

### Copy Dictionary

```python
# copy()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# dict()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
```

---

### Nested Dictionaries

```python
# Nested
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
# Output: {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

# Another Example
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
# Output: {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

# Access items in Nested
print(myfamily["child2"]["name"])  # Output: Tobias

# Loop in Nested 
for x, obj in myfamily.items():
  print(x)
  for y in obj:
    print(y + ':', obj[y])
    
# Output:
# child1
# name: Emil
# year: 2004
# child2
# name: Tobias
# year: 2007
# child3
# name: Linus
# year: 2011
```

---

### Dictionary Methods

| Method | Description |
|---|---|
| `clear()` | Removes all the elements from the dictionary |
| `copy()` | Returns a copy of the dictionary |
| `fromkeys()` | Returns a dictionary with the specified keys and value |
| `get()` | Returns the value of the specified key |
| `items()` | Returns a list containing a tuple for each key value pair |
| `keys()` | Returns a list containing the dictionary's keys |
| `pop()` | Removes the element with the specified key |
| `popitem()` | Removes the last inserted key-value pair |
| `setdefault()` | Returns the value of the specified key. If the key does not exist: insert the key, with the specified value |
| `update()` | Updates the dictionary with the specified key-value pairs |
| `values()` | Returns a list of all the values in the dictionary |

#### 1. `clear()`
```python
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.clear()
print(car)  # Output: {}
```

#### 2. `copy()`
```python
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.copy()
print(x)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
```

#### 3. `fromkeys()`
```python
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)  # Output: {'key1': 0, 'key2': 0, 'key3': 0}
```

#### 4. `get()`
```python
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.get("model")
print(x)  # Output: Mustang
```

#### 5. `items()`
```python
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.items()
print(x)  # Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
```

#### 6. `keys()`
```python
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.keys()
print(x)  # Output: dict_keys(['brand', 'model', 'year'])
```

#### 7. `pop()`
```python
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.pop("model")
print(car)  # Output: {'brand': 'Ford', 'year': 1964}
```

#### 8. `popitem()`
```python
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.popitem()
print(car)  # Output: {'brand': 'Ford', 'model': 'Mustang'}
```

#### 9. `setdefault()`
```python
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.setdefault("color", "white")
print(x)    # Output: white
print(car)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'white'}
```

#### 10. `update()`
```python
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.update({"color": "White"})
print(car)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'White'}
```

#### 11. `values()`
```python
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.values()
print(x)  # Output: dict_values(['Ford', 'Mustang', 1964])
```

---

## OOP — Object-Oriented Programming

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of **objects** — which bundle **data (attributes)** and **behavior (methods)** together.

| Pillar | Meaning |
|---|---|
| **Encapsulation** | Hiding internal data; exposing only what's needed |
| **Inheritance** | A class can inherit attributes and methods from another class |
| **Polymorphism** | The same method name can behave differently in different classes |
| **Abstraction** | Hiding complex implementation details behind a simple interface |

> **Key Facts:**
> - Everything in Python is an **object**
> - A **class** is a blueprint; an **object** is an instance of that blueprint
> - Use `class` keyword to define a class

---

### Classes and Objects

A **class** is like a template. An **object** is a real instance created from that template.

```python
class Dog:
    species = "Canis familiaris"  # Class variable (shared by all instances)

    def __init__(self, name, age):
        self.name = name          # Instance variable
        self.age = age            # Instance variable

    def bark(self):
        return f"{self.name} says Woof!"

# Creating objects (instances)
dog1 = Dog("Rex", 3)
dog2 = Dog("Buddy", 5)

print(dog1.name)    # Output: Rex
print(dog2.age)     # Output: 5
print(dog1.bark())  # Output: Rex says Woof!
print(type(dog1))   # Output: <class '__main__.Dog'>
```

---

### The `__init__()` Method

`__init__()` is the **constructor** — it runs automatically every time a new object is created.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Rijoan", 24)
print(p1.name)  # Output: Rijoan
print(p1.age)   # Output: 24
```

> **Note:** `__init__()` is called automatically — you never call it manually. It is the right place to set up all instance variables.

---

### The `self` Parameter

`self` refers to the **current instance** of the class. It must be the **first parameter** of every method.

```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def describe(self):
        return f"I drive a {self.color} {self.brand}."

my_car = Car("Toyota", "Red")
print(my_car.describe())  # Output: I drive a Red Toyota.
```

> **Tip:** `self` is a convention — you could technically name it anything, but always use `self` for readability.

---

### Object Methods

Methods are **functions defined inside a class** that describe what an object can do.

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew {amount}. Remaining: {self.balance}"

    def get_balance(self):
        return f"{self.owner}'s balance: {self.balance}"

account = BankAccount("Rijoan", 1000)
print(account.deposit(500))    # Output: Deposited 500. New balance: 1500
print(account.withdraw(200))   # Output: Withdrew 200. Remaining: 1300
print(account.get_balance())   # Output: Rijoan's balance: 1300
```

---

### Modify and Delete Object Properties

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

s1 = Student("Rijoan", "A")

# Modify a property
s1.grade = "A+"
print(s1.grade)  # Output: A+

# Add a new property
s1.subject = "Python"
print(s1.subject)  # Output: Python

# Delete a property
del s1.subject
# print(s1.subject)  # Would raise AttributeError

# Delete the entire object
del s1
# print(s1)  # Would raise NameError
```

---

### Inheritance

Inheritance allows a class (**child**) to **reuse** attributes and methods from another class (**parent**).

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

    def eat(self):
        return f"{self.name} is eating."

# Child class — inherits from Animal
class Cat(Animal):
    def speak(self):                          # Override parent method
        return f"{self.name} says Meow!"

class Dog(Animal):
    def speak(self):                          # Override parent method
        return f"{self.name} says Woof!"

cat = Cat("Whiskers")
dog = Dog("Rex")

print(cat.speak())  # Output: Whiskers says Meow!
print(dog.speak())  # Output: Rex says Woof!
print(cat.eat())    # Output: Whiskers is eating.  (inherited from Animal)
```

> **Syntax:** `class ChildClass(ParentClass):`

---

### The `super()` Function

`super()` lets the child class call methods from its **parent class** — most commonly used in `__init__()` to avoid repeating code.

```python
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def describe(self):
        return f"{self.name} goes {self.sound}."

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")  # Call parent __init__
        self.tricks = []                 # Extra instance variable

    def learn_trick(self, trick):
        self.tricks.append(trick)
        return f"{self.name} learned: {trick}!"

dog = Dog("Rex")
print(dog.describe())            # Output: Rex goes Woof.
print(dog.learn_trick("Sit"))    # Output: Rex learned: Sit!
print(dog.tricks)                # Output: ['Sit']
```

---

### Override Methods

A child class can **replace** a parent method with its own version by defining a method with the **same name**.

```python
class Shape:
    def area(self):
        return 0

    def describe(self):
        return f"This shape has area: {self.area()}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):                          # Override parent's area()
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):                          # Override parent's area()
        return 3.14159 * self.radius ** 2

rect = Rectangle(5, 3)
circ = Circle(4)

print(rect.describe())  # Output: This shape has area: 15
print(circ.describe())  # Output: This shape has area: 50.26544
```

---

### Multiple Inheritance

Python supports inheriting from **more than one parent class**.

```python
class Flyable:
    def fly(self):
        return "I can fly!"

class Swimmable:
    def swim(self):
        return "I can swim!"

class Duck(Flyable, Swimmable):    # Inherits from both
    def __init__(self, name):
        self.name = name

    def quack(self):
        return f"{self.name} says Quack!"

duck = Duck("Donald")
print(duck.fly())    # Output: I can fly!
print(duck.swim())   # Output: I can swim!
print(duck.quack())  # Output: Donald says Quack!
```

> **Tip:** Python uses **MRO (Method Resolution Order)** — left to right — when resolving methods from multiple parents. Use `ClassName.__mro__` to inspect the order.

---

### Encapsulation

Encapsulation means **restricting direct access** to some object data. Python uses naming conventions for this.

| Convention | Access | Example |
|---|---|---|
| `name` | Public — accessible from anywhere | `self.name` |
| `_name` | Protected — convention: internal use only | `self._salary` |
| `__name` | Private — name-mangled, hard to access from outside | `self.__password` |

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name             # Public
        self._department = "IT"      # Protected (convention)
        self.__salary = salary       # Private (name-mangled)

    def get_salary(self):            # Controlled access method
        return self.__salary

    def give_raise(self, amount):
        if amount > 0:
            self.__salary += amount

emp = Employee("Rijoan", 50000)
print(emp.name)           # Output: Rijoan
print(emp._department)    # Output: IT  (accessible but discouraged)
print(emp.get_salary())   # Output: 50000

emp.give_raise(5000)
print(emp.get_salary())   # Output: 55000

# print(emp.__salary)     # AttributeError — name is mangled to _Employee__salary
print(emp._Employee__salary)  # Output: 55000 (can access via mangled name)
```

---

### Getters and Setters (`@property`)

The `@property` decorator turns a method into a **read-only attribute**. Use `@name.setter` to allow writing.

```python
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):             # Getter
        return self.__celsius

    @celsius.setter
    def celsius(self, value):      # Setter with validation
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self.__celsius = value

    @property
    def fahrenheit(self):          # Computed property (no setter)
        return self.__celsius * 9/5 + 32

temp = Temperature(25)
print(temp.celsius)      # Output: 25
print(temp.fahrenheit)   # Output: 77.0

temp.celsius = 100
print(temp.fahrenheit)   # Output: 212.0

# temp.celsius = -300    # Would raise ValueError
```

---

### Polymorphism

Polymorphism means the **same interface** works differently depending on the object. The same method name behaves differently per class.

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Duck:
    def speak(self):
        return "Quack!"

# The same function works with any class that has .speak()
def make_sound(animal):
    print(animal.speak())

animals = [Dog(), Cat(), Duck()]
for animal in animals:
    make_sound(animal)
# Output:
# Woof!
# Meow!
# Quack!
```

> **Note:** This is also called **duck typing** — "if it walks like a duck and quacks like a duck, it's a duck." Python doesn't require formal interfaces; any object with the right method works.

---

### Abstraction

Abstraction hides complex implementation details. In Python, use the **`abc` module** to define abstract classes — classes that **cannot be instantiated** and force child classes to implement required methods.

```python
from abc import ABC, abstractmethod

class Shape(ABC):              # Abstract base class
    @abstractmethod
    def area(self):            # Must be implemented by every child
        pass

    @abstractmethod
    def perimeter(self):       # Must be implemented by every child
        pass

    def describe(self):        # Concrete method (shared, not abstract)
        return f"Area: {self.area()}, Perimeter: {self.perimeter()}"

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14159 * self.r ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.r

rect = Rectangle(4, 6)
circ = Circle(5)

print(rect.describe())  # Output: Area: 24, Perimeter: 20
print(circ.describe())  # Output: Area: 78.53975, Perimeter: 31.4159

# shape = Shape()  # TypeError — cannot instantiate abstract class
```

---

### Class Variables vs Instance Variables

| Type | Defined In | Shared? | Access |
|---|---|---|---|
| **Class variable** | Inside class, outside `__init__` | Yes — all instances share it | `ClassName.var` or `self.var` |
| **Instance variable** | Inside `__init__` via `self` | No — unique per object | `self.var` |

```python
class Counter:
    count = 0              # Class variable — shared by ALL instances

    def __init__(self, name):
        Counter.count += 1         # Modify class variable
        self.name = name           # Instance variable — unique per object
        self.id = Counter.count    # Assign current count as ID

c1 = Counter("Alice")
c2 = Counter("Bob")
c3 = Counter("Charlie")

print(Counter.count)   # Output: 3  (shared)
print(c1.id)           # Output: 1
print(c2.id)           # Output: 2
print(c3.name)         # Output: Charlie
```

---

### Class Methods and Static Methods

| Decorator | First Parameter | Can Access | Use Case |
|---|---|---|---|
| *(none)* | `self` | Instance + class data | Regular object method |
| `@classmethod` | `cls` | Class data only | Factory methods, class-level logic |
| `@staticmethod` | *(none)* | Nothing — standalone | Utility/helper functions |

```python
class Person:
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1

    def greet(self):                      # Regular instance method
        return f"Hi, I'm {self.name}!"

    @classmethod
    def get_population(cls):              # Class method
        return f"Total people: {cls.population}"

    @classmethod
    def from_birth_year(cls, name, birth_year):  # Factory class method
        age = 2026 - birth_year
        return cls(name, age)             # Creates a new instance

    @staticmethod
    def is_adult(age):                    # Static method — no self or cls
        return age >= 18

p1 = Person("Rijoan", 24)
p2 = Person.from_birth_year("Maruf", 2000)  # Use factory method

print(p1.greet())               # Output: Hi, I'm Rijoan!
print(Person.get_population())  # Output: Total people: 2
print(Person.is_adult(20))      # Output: True
print(Person.is_adult(15))      # Output: False
print(p2.age)                   # Output: 26
```

---

### Magic / Dunder Methods

Magic methods (also called **dunder methods** — double underscore) let you define how your objects behave with built-in Python operations.

| Method | Triggered By | Description |
|---|---|---|
| `__init__(self)` | `MyClass()` | Constructor |
| `__str__(self)` | `print(obj)` / `str(obj)` | Human-readable string representation |
| `__repr__(self)` | `repr(obj)` / in shell | Developer/debug string representation |
| `__len__(self)` | `len(obj)` | Returns length |
| `__add__(self, other)` | `obj1 + obj2` | Addition operator |
| `__eq__(self, other)` | `obj1 == obj2` | Equality check |
| `__lt__(self, other)` | `obj1 < obj2` | Less-than comparison |
| `__contains__(self, item)` | `item in obj` | Membership test |
| `__del__(self)` | `del obj` | Destructor |

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages})"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.pages < other.pages

    def __add__(self, other):
        combined_title = f"{self.title} & {other.title}"
        return Book(combined_title, "Various", self.pages + other.pages)

b1 = Book("Python Basics", "Rijoan", 300)
b2 = Book("Advanced Python", "Maruf", 500)

print(b1)            # Output: 'Python Basics' by Rijoan   (uses __str__)
print(repr(b1))      # Output: Book(title='Python Basics', ...)  (uses __repr__)
print(len(b1))       # Output: 300   (uses __len__)
print(b1 == b2)      # Output: False  (uses __eq__)
print(b1 < b2)       # Output: True   (uses __lt__)
combined = b1 + b2   # uses __add__
print(combined)      # Output: 'Python Basics & Advanced Python' by Various
print(len(combined)) # Output: 800
```

---

### OOP Quick Reference

| Concept | Keyword / Syntax | Purpose |
|---|---|---|
| Define a class | `class MyClass:` | Blueprint for objects |
| Constructor | `def __init__(self, ...)` | Runs on object creation |
| Create an object | `obj = MyClass(...)` | Instantiate a class |
| Instance method | `def method(self):` | Behavior tied to object |
| Class method | `@classmethod` + `cls` | Tied to the class itself |
| Static method | `@staticmethod` | Utility, no class/instance ref |
| Inheritance | `class Child(Parent):` | Reuse parent code |
| Call parent | `super().__init__(...)` | Access parent constructor/methods |
| Override | Redefine a method in child | Change parent behavior |
| Abstract class | `ABC` + `@abstractmethod` | Force child to implement methods |
| Property getter | `@property` | Access method like attribute |
| Property setter | `@name.setter` | Set with validation |
| Private attribute | `self.__name` | Name-mangled, access controlled |
| Protected attribute | `self._name` | Convention — internal use |
| String repr | `__str__` / `__repr__` | `print()` and `repr()` behavior |

---

<div align="center">

*Quiz 1 Notes — List, Tuple, Dictionary, Class & Object*

</div>
