# And Operator
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# Or operator
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# Not operator
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

# Combining Multiple Operators
age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")