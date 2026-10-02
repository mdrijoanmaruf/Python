# Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Loop Through the index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

# Using while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# Looping using list Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]