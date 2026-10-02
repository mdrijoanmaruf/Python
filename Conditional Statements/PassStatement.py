# Pass statement : if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
  pass

# Example
age = 20

if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")