# Scope
# A variable is only available from inside the region it is created. This is called scope.

# Local Scope : A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
def myfunc():
  x = 300
  print(x)

myfunc()

# Function Inside Function
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

# Global Scope : A variable created in the main body of the Python code is a global variable and belongs to the global scope.

x = 300

def myfunc():
  print(x)

myfunc()

print(x)

# Global keyword : If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = 300

myfunc()

print(x)

# Nonlocal Keyword
# The nonlocal keyword is used to work with variables inside nested functions.

# The nonlocal keyword makes the variable belong to the outer function.


def myfunc1():
  x = "Rijoan"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())



# The LEGB Rule
# Python follows the LEGB rule when looking up variable names, and searches for them in this order:

# Local - Inside the current function
# Enclosing - Inside enclosing functions (from inner to outer)
# Global - At the top level of the module
# Built-in - In Python's built-in namespace

