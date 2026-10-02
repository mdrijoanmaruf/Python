# Tuple
# A tuple is a collection which is ordered and unchangeable.
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Without parentheses
thistuple = "apple", "banana", "cherry"
print(thistuple)

# Tuple Items :
    # Ordered
    # Unchangeable
    # Allow Duplicates

# Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# Tuple with one item
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Empty Tuple
thistuple = ()
print(type(thistuple))

# Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)