# while loop
i = 1
while i < 6:
  print(i)
  i += 1

# Break Statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# Continue Statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# Else Statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")