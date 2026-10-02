a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# More example
temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")

# Short hand if else
a = 2
b = 330
print("A") if a > b else print("B")

# Multiple Conditions on One line
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")