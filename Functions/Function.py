# Creating a Function
def my_function():
  print("Hello from a function")

# Calling a Function
my_function()

# Function Names
# Function names follow the same rules as variable names in Python:

# A function name must start with a letter or underscore
# A function name can only contain letters, numbers, and underscores
# Function names are case-sensitive (myFunction and myfunction are different)

# Return values
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

# The pass Statement
# Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:
def my_function():
  pass