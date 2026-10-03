# range() : The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times.

# Note: Immutable means that it cannot be modified after it is created.
x = range(10)
print(x)
print(list(x))

# Call range() With Two Arguments
x = range(3, 10)
print(x)
print(list(x))

# Call range() with Three Arguments
x = range(3, 10, 2)
print(x)
print(list(x))

# For loop using range()
for i in range(10):
  print(i)

# Length
r = range(0, 10, 2)
print(len(r))