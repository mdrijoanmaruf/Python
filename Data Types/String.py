print("My Name is rijoan Maruf")

# Multi line sting
x = """
hello , 
i am rijoan maruf , 
i am a full stack developer
"""
y = '''
hello , 
i am rijoan maruf , 
i am a full stack developer
'''

print(x)
print(y)

# String are arrays (character array)
a = "Rijoan, Maruf"
# print(a[0])

# For in loop in string
for i in "Md Rijoan Maruf" :
    print(i)

# String Length
x = "Rijoan"
print(len(a))

# Check string
text = "Hello i am rijoan"
print("am" in text)


# Check if not
text = "Hello , i am a full stack web developer"
print("web" not in text);

# String Slicing
x = "Rijoan Maruf"
print(x[2:4]) # 2 position
print(x[:5]) # From Start
print(x[5:]) # Slice to end
print(x[-5:-2]) # Negative indexing

# Upper Case
x = "Software Engineering"
print(x.upper())

# lower Case
x = "Web DEVELOPMENT"
print(x.lower())

# Remove Whitespace
a = "   Rijoan    Maruf"
print(a.strip()) # Only remove before and after white spaces

# Replace String
a = "Hello World"
print(a.replace("H" , "J"))

# Split String
a = "Md Rijoan Maruf"
print(a.split(" "))

# String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# F-String
age = 24
txt = f"My name is Rijoan Maruf, I am {age}"
print(txt)

# Escape Character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
