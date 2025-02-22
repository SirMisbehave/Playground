"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_numbers.asp
"""

"""
Numbers

There are three numeric types in Python:
- int
- float
- complex
"""

x = 1 	# int
y = 2.8 # float
z = 1j 	# complex

print("'x' set as int:", x)
print("'y' set as float:", y)
print("'z' set as complex:", z)

print("'x' type is set to", type(x))
print("'y' type is set to", type(y))
print("'z' type is set to", type(z))

# Integer

x = 1
y = 35656222554887711
z = -3255522

print("'x' is set to", x, "and the type is", type(x))
print("'y' is set to", y, "and the type is", type(y))
print("'z' is set to", z, "and the type is", type(z))

# Float

x = 1.10
y = 1.0
z = -35.59

print("'x' is set to", x, "and the type is", type(x))
print("'y' is set to", y, "and the type is", type(y))
print("'z' is set to", z, "and the type is", type(z))

# Floats - Scientific Numbers

x = 35e3
y = 12E4
z = -87.7e100

print("'x' is set to", x, "and the type is", type(x))
print("'y' is set to", y, "and the type is", type(y))
print("'z' is set to", z, "and the type is", type(z))

# Complex

x = 3+5j
y = 5j
z = -5j

print("'x' is set to", x, "and the type is", type(x))
print("'y' is set to", y, "and the type is", type(y))
print("'z' is set to", z, "and the type is", type(z))

# Type Conversion

x = 1 	# int
y = 2.8 # float
z = 1j 	# complex

print("This is 'x' before type conversion:", x, "with a type of", type(x))
print("This is 'y' before type conversion:", y, "with a type of", type(y))
print("This is 'z' before type conversion:", z, "with a type of", type(z))

# Convert From Int to Float

a = float(x)
print("This is 'a' after the type conversion of 'x':", a, "with a type of", type(a))

# Convert From Float to Int

b = int(y)
print("This is 'b' after the type conversion of 'y':", b, "with a type of", type(b))

# Convert From Int to Complex

c = complex(x)
print("This is 'c' after the type conversion of 'x':", c, "with a type of", type(c))

# Random Number

import random # Import 'random' Module

print(random.randrange(1, 10))