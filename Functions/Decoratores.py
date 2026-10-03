# Decorators : Decorators let you add extra behavior to a function, without changing the function's code.

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase # By placing @changecase directly above the function definition, the function myfunction is being "decorated" with the changecase function.
def myfunction():
  return "Hello Sally"

print(myfunction())

# Multiple Decorator Calls
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())

# ARguments in the Decorated Function
def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))


# Decorator with arguments
def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Linus"

print(myfunction())