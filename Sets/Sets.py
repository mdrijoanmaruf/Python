# Store multiple items in single value
# Note : Set items are unchangeable, but you can remove items and add new items.
# Note: Sets are unordered, so you cannot be sure in which order the items will appear.
# Note: Duplicates not allowed

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

# Example: 
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset) # Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:

# Length of a Set :
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

# type()
myset = {"apple", "banana", "cherry"}
print(type(myset))

# The set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)