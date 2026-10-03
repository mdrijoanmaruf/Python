# Use a Module
import Module

Module.greeting("Rijoan")

# Use variable form module
a = Module.person1["age"]
print(a)

# Rename Module
import Module as mx

a = mx.person1["age"]
print(a)

# Built-In modules
import platform

x = platform.system()
print(x)

# Dir() Function : List all defined names belongs to the platform module
import platform

x = dir(platform)
print(x)

# Import Form Module
from Module import person1

print (person1["age"])