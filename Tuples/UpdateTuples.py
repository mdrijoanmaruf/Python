# Change Tuple values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

# print(x)


# Add Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(y)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# Remove Items (You can't remove items in a tuple)
thistuple = ("apple", "banana", "cherry")
y = list(thistuple) # First convert into list then remove
y.remove("apple")
thistuple = tuple(y)
print(y)

# Completely Delete tuple
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists