"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_datatypes.asp
"""

# Getting the Data Type

x = 5
print("The type information of 'x' is", type(x), "and is set to", x)

# Setting the Data Type

x = "Hello World" # String
print("The type information of 'x' is", type(x), "and is set to", x)

x = 20 # Integer
print("The type information of 'x' is", type(x), "and is set to", x)

x = 20.5 # Float
print("The type information of 'x' is", type(x), "and is set to", x)

x = 1j # Complex
print("The type information of 'x' is", type(x), "and is set to", x)

x = ["apple", "banana" ,"cherry"] # List
print("The type information of 'x' is", type(x), "and is set to", x)

x = ("apple", "banana", "cherry") # Tuple
print("The type information of 'x' is", type(x), "and is set to", x)

x = range(6) # Range
print("The type information of 'x' is", type(x), "and is set to", x)

x = { "name": "John", "age": 36 } # Dictionary
print("The type information of 'x' is", type(x), "and is set to", x)

x = { "apple", "banana", "cherry" } # Set
print("The type information of 'x' is", type(x), "and is set to", x)

x = frozenset({"apple", "banana", "cherry"}) # Frozenset
print("The type information of 'x' is", type(x), "and is set to", x)

x = True # Boolean
print("The type information of 'x' is", type(x), "and is set to", x)

x = b"Hello" #  Bytes
print("The type information of 'x' is", type(x), "and is set to", x)

x = bytearray(5) # Bytearray
print("The type information of 'x' is", type(x), "and is set to", x)

x = memoryview(bytes(5)) # Memoryview
print("The type information of 'x' is", type(x), "and is set to", x)

x = None # NoneType
print("The type information of 'x' is", type(x), "and is set to", x)

# Setting the Specific Data Type

x = str("Hello World") # String
print("The type information of 'x' is", type(x), "and is set to", x, "specifically: str()")

x = int(20) # Integer
print("The type information of 'x' is", type(x), "and is set to", x, "specifically: int()")

x = float(20.5) # Float
print("The type information of 'x' is", type(x), "and is set to", x, "specifically: float()")

x = complex(1j) # Complex
print("The type information of 'x' is", type(x), "and is set to", x, "specifically: complex()")

x = list(("apple", "banana", "cherry")) # List
print("The type information of 'x' is", type(x), "and is set to", x, "specifically: list()")

x = tuple(("apple", "banana", "cherry")) # Tuple
print("The type information of 'x' is", type(x), "and is set to", x, "specifically: tuple()")

x = range(6) # Range
print("The type information of 'x' is", type(x), "and is set to", x, "specifically: range()")

x = dict(name = "John", age = 36) # Dictionary
print("The type information of 'x' is", type(x), "and is set to", x, "specifically: dict()")

x = set(("apple", "banana", "cherry")) # Set
print("The type information of 'x' is", type(x), "and is set to", x, "specifically: set()")

x = frozenset(("apple", "banana", "cherry")) # Frozenset
print("The type information of 'x' is", type(x), "and is set to", x, "specifically: frozenset()")

x = bool(5) # Boolean
print("The type information of 'x' is", type(x), "and is set to", x, "specifically: bool()")

x = bytes(5) # Bytes
print("The type information of 'x' is", type(x), "and is set to", x, "specifically: bytes()")

x = bytearray(5) # Bytearray
print("The type information of 'x' is", type(x), "and is set to", x, "specifically: bytearray()")

x = memoryview(bytes(5)) # Memoryview
print("The type information of 'x' is", type(x), "and is set to", x, "specifically: memoryview()")