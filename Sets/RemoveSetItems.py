# Remove Item
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")
print(thisset)
# Note: If the item to remove does not exist, remove() will raise an error.

# using discard()
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")
print(thisset)
# Note: If the item to remove does not exist, discard() will NOT raise an error.

# pop()
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

# Clear()
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

# del
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)