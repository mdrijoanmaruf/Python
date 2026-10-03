# Arguments
def my_function(fname):
  print("Hello ," , fname)

my_function("Rijoan")
my_function("Maruf")

# Parameters vs Arguments
# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the actual value that is sent to the function when it is called.

def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Rijoan") # "Rijoan" is an argument

# Number of Arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Rijoan", "Maruf")

# Default Parameter
def my_function(name = "friend"):
  print("Hello", name)

my_function("Rijoan")
my_function("Sakib")
my_function()
my_function("Sazzad")

# Keyword Arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

# Positional Arguments
# When you call a function with arguments without using keywords, they are called positional arguments.
# Positional arguments must be in the correct order:
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")

# Mixing Positional and Keyword Arguments
# You can mix positional and keyword arguments in a function call.
# However, positional arguments must come before keyword arguments:

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

# Return Values
def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)

# Returning Different Data Types
def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)

# *args : accepts any number of arguments
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Using *args with Regular Arguments
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")

# Practical Example :
def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

# **kwargs : **kwargs to accept any number of keyword arguments
def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")

# Using **kwargs with Regular Arguments
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

# Combining *args and **kwargs
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

# Unpacking Arguments
# Lists with *
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

# Dictionaries with **
def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Rijoan"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Rijoan")



