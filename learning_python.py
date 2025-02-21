# Hello World
print("Hello World")

# Python Version
import sys
print(sys.version)

# Syntax - Python Indentation
if 5 > 2:
    print("Five is greater than two!")

# Syntax - Variables
x = 5
y = "Hello, World!"

# Syntax - Comments (Like this one.)
print("Comment after this print function.") # Just another comment.

# Syntax - Multiline Comments
# Like this.
# And this.
# Or

"""
Or we can use something like this.
"""

# Variables
x = 5
y = "John"
print(x)
print(y)

# Variables = Type changing on the fly.
x = 4
x = "Sally"
print(x)

# Variables - Casting
x = str(3)
y = int(3)
z = float(3)

# Variables - Get Type
x = 5
y = "John"
print(type(x))
print(type(y))

# Variables - Single or Double Quotes?
x = "John"
# Is the same as...
y = 'John'

# Variables - Case-Sensitive
a = 4
A = "Sally" # This will not overwrite a.

# Variable Names - Legal
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Variable Names - Illegal
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Multi Words Variable Name
myVariableName = "John" # Camel Case
MyVariableName = "John" # Pascal Case
my_variable_name = "John" # Snake Case

# Variables - Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Variables - One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Variables - Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables
x = "Python is awesome."
print(x)

x = "Python"
y = "is"
z = "awesome."
print(x, y, z)

x = "Python "
y = "is "
z = "awesome."
print(x, y, z)

x = 5
y = 10
print(x + y)

"""
The following will not work:
x = 5
y = "John"
print(x + y)
"""

# But will.
x = 5
y = "John"
print(x, y)

# Global Variables
x = "awesome."

def myfunc():
    print("Python is " + x)

myfunc()

x = "awesome."

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x) # Reprinting the X from outside the function returns the global result.

# Global Keyword - Global Variable Inside Function
def myfunc():
    global x
    x = "fantastic."

myfunc()

print("Python is " + x)

# Global Keyword - Change local variable to global from inside function even if local was created first.
x = "awesome."

def myfunc():
    global x
    x = "fantastic."

myfunc()

print("Python is " + x)

# Data Type

# Text Type: str
# Numeric Type: int, float, complex
# Sequence Type: list, tuple, range
# Mapping Type: dict
# Set Type: set, frozenset
# Boolean Type: bool
# Binary Type: bytes, bytearray, memoryview
# None Type: NoneType

x = "Hello World" # str
x = 20 # int
x = 20.5 # float
x = 1j # complex
x = ["apple", "banana", "cherry"] # list
x = ("apple", "banana", "cherry") # tuple
x = range(6) # range
x = {"name":"John", "age": "36"} # dict
x = {"apple", "banana", "cherry"} # set
x = frozenset({"apple", "banana", "cherry"}) # frozen set
x = True # bool
x = b"Hello" # bytes
x = bytearray(5) # bytearray
x = memoryview(bytes(5)) # memoryview
x = None # NoneType

# Set Specific Data Types

x = str("Hello World") # str
x = int(20) # int
x = float(20.5) # float
x = complex(1j) # complex
x = list(("apple", "banana", "cherry")) # list
x = tuple(("apple", "banana", "cherry")) # tuple
x = range(6) # range
x = dict(name="John", age=36) # dict
x = set(("apple", "banana", "cherry")) # set
x = frozenset(("apple", "banana", "cherry")) # frozenset
x = bool(5) # bool
x = bytes(5) # bytearray
x = bytearray(5) # bytearray
x = memoryview(bytes(5)) # memoryview

# Numbers

x = 1 # int
y = 2.8 # float
z = 1j # complex

print(type(x))
print(type(y))
print(type(z))

# Numbers - Int

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# Numbers - Float

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# Numbers - Float - Scientific Numbers

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

# Numbers - Complex

x = 3 + 5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# Type Conversion

x = 1 # int
y = 2.8 # float
z = 1j # complex

# Convert from Int to Float

a = float(x)

# Convert from Float to Int

b = int(y)

# Convert from Int to Complex

c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Random Number

import random
print(random.randrange(1, 10))

# Casting - Integers

x = int(1)
y = int(2.8)
z = int("3")

# Casting - Floats

x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")

# Casting - Strings

x = str("s1")
y = str(2)
z = str(3.0)

# Strings

print("Hello") # Double Quotes
print('Hello') # Single Quotes

# Quotes Inside Quotes

print("It's alright.")
print("He is called 'Johnny'.")
print('He is called "Johnny".')

# Assign String to a Variable

a = "Hello"
print(a)

# Multiline Strings

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a) 

# Strings are Arrays

a = "Hello World!"
print(a[1])

# Looping Through a String

for x in "banana":
    print(x)

# String Length

a = "Hello, World!"
print(len(a))

# Check String

txt = "The best things in life are free!"
print("free" in txt)
if "free" in txt:
    print("Yes, 'free' is present.")
    print("expensive" not in txt)
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

# Slicing

b = "Hello, World!"
print(b[2:5]) # Slicing
print(b[:5]) # Slice from the Start
print(b[2:]) # Slice to the End
print(b[-5:-2]) # Negative Indexing

# Modify Strings

a = "Hello, World!"
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("H", "J"))
print(a.split(","))

# String Concatenation

a = "Hello"
b = "World"
c = a + b
print(c)

c = a + " " + b
print(c)

# String Format

# age = 36
# txt = "My name is John, I am " + age
# print(txt)

# F Strings

age = 36
txt = f"My name is John, I am {age}"
print(txt)

# Placeholders and Modifiers

price = 59
txt = f"The price is {price} dollars."
print(txt)

txt = f"The price is {price:.2f} dollars."
print(txt)

txt = f"The price is {20 * 59} dollars."
print(txt)

# Escape Characters

# The following will error:
# txt = "We are the so-called "Vikings" from the north."

txt = "We are the so-called \"Vikings\" from the north."

# Escape Characters

# \'
# \\
# \n
# \r
# \t
# \b
# \f
# \000
# \xhh

# Boolean Values

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if  b > a:
    print("B is greater than a.")
else:
    print("B is not greater than a.")

# Evaluate Values and Variables

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Most Values are True

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# Some Values are False

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

# Functions Can Return a Boolean

def myFunction():
    return True

print(myFunction())

def myFunction():
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")

x = 200
print(isinstance(x, int))

# Arithmetic Operators

# + Addition
# - Subtraction
# * Multiplication
# / Division
# % Modulus
# ** Exponentiation
# // Floor Division

# Assignment Operators

# = - x = 5
# += - x = x + 5
# -= - x = x - 5
# *= - x = x * 5
# /= - x = x / 5
# %= - x = x % 5
# //= - x = x // 5
# **= - x = x ** 5
# &= - x = x & 5
# |= - x = x | 5
# ^= - x = x ^ 5
# >>= - x = x >> 5
# <<= - x = x << 5
# := - x = 3 print(x)

# == - Equal
# != - Not Equal
# > - Greater Than
# < - Less Than
# >= - Greater Than or Equal To
# <= - Less Than or Equal To

# Logical Operators

# and - Returns True if both statements are true.
# or - Returns True if one of the statements is true.
# not - Reverse the result, returns False if the result is true.

# Identity Operators

# is - Returns True if both variables are the same object.
# is not - Returns True if both variables are not the same object.

# Membership Operators

# in - Returns True if a sequence with the specified value is present in the object.
# not in - Returns True if a sequence with the specified value is not present in the object.

# Bitwise Operators

# & - AND
# | - OR
# ^ - XOR
# ~ - NOT
# << - Zero Fill Left Shift
# >> - Signed Right Shift

# Operator Precedence

print((6 + 3) - (6 + 3))
print(100 + 5 * 3)

# () - Parentheses
# ** - Exponentiation
# +x -x ~x - Unary Plus, Unary Minus and Bitwise NOT
# * / // % - Multiplication, Division, Floor Division and Modulus
# + - - Addition and Subtraction
# << >> - Bitwise Left and Right Shifts
# & - Bitwise AND
# ^ - Bitwise XOR
# |  - Bitwise OR
# == != > >= < <= - is, is not, in, not in - Comparisons, Identity and Membership Operators
# not - Logical NOT
# and - AND
# or - OR

print(5 + 4 - 7 + 3)

# Lists

mylist = ["apple", "banana", "cherry"]

thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# List Length

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# List Items - Data Types

list1 = ["apple", "banana", "cherry"] # String
list2 = [1, 5, 7, 9, 3] # Int
list3 = [True, False, False] # Boolean

list1 = ["abc", 34, True, 40, "male"]

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# list() Constructor

thislist = list(("apple", "banana", "cherry"))
print(thislist)

# Access List Items

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[:2])

# Range of Negative Indexes

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4: -1])

# Check If Item Exists

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list.")

# Change Item Value

thislist[1] = "blackcurrent"
print(thislist)

# Change a Range of Item Values

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Append Items

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Insert Items

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Extend List

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Add Any Iterable

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# Remove Specified Item

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove First Instance of Item

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Remove Last Item

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# Remove First Item

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Delete Entire List

thislist = ["apple", "banana", "cherry"]
del thislist

# Clear the List

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Loop Through a List

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# Loop Through Index Numbers

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

# Using a While Loop

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# Looping Using List Comprehension

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# Only Accept Items That Are Not "Apple"

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)
newlist = [x for x in fruits]
print(newlist)
newlist = [x for x in range(10)]
print(newlist)

# Accept Only Numbers Lower Than 5

newlist = [x for x in range(10) if x < 5]
print(newlist)

# Expression

newlist = [x.upper() for x in fruits]
print(newlist)

# Set All Values to "Hello"

newlist = ["Hello" for x in fruits]
print(newlist)

# Return "Orange" Instead of "Banana"

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

# Sort List Alphanumerically

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort List Numerically

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort Descending

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# Sort List Descending

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# Customize Sort Function

def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# Case Sensitive Sort - Unexpected Results

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Case Insensitive Sort

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Reverse Order

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# Use the copy() Method

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Use the list() Method

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Use the slice Operator

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

# Join Two Lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# Append list2 into list1

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

# Extend 

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# Tuples

mytuple = ("apple", "banana", "cherry")
print(mytuple)

# Tuple Length

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# Single Item Tuple

thistuple = ("apple",)
print(type(thistuple))

# Not a Tuple

thistuple = ("apple")
print(type(thistuple))

# Tuple Items - Data Types

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

# Tuple With Different Data Types

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
print(type(tuple1))

# tuple() Constructor

thistuple = tuple(("apple", "banana", "cherry")) # Double Brackets
print(thistuple)
print(type(thistuple))

# Access Tuple Items

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Tuple Negative Indexing

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# Range of Indexes

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# Not Included

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
print(thistuple[2:])

# Range of Negative Indexes

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# Check If Item Exists

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple.")

# Change Tuple Values

x = ("apple", "banana", "cherry")
y = list(x) # First Convert to List - Since Tuples Cannot Be Changed
y[1] = "kiwi"
x = tuple(y)
print(x)

# Add Items

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# Add Tuple to Tuple

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# Remove Item from Tuple

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# Delete Tuple

thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) # This will throw an error.

# Unpacking a Tuple

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Unpacking a Tuple with Asterisk

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

# Loop Through a Tuple

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

# Loop Through Tuple Index Numbers

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

# Tuple While Loop

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

# Join Two Tuples

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply Tuples

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

# Sets

myset = {"apple", "banana", "cherry"}
print(myset)

# Duplicates Ignored in Sets

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# True and 1 Considered the Same Value

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# False and 0 Considered the Same Value

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

# Set Length

thiset = {"apple", "banana", "cherry"}
print(len(thisset))

# Set Items - Data Types

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

# Set with Many Data Types

set1 = {"abc", 34, True, 40, "male"}
print(set1)
print(type(set1))

# set() Constructor

thiset = set(("apple", "banana", "cherry"))
print(thisset)

# Access Set Items

thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
print("banana" not in thisset)

# Add Set Items

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Add Many Sets

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Add Any Iterable to Set

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# Remove Set Items

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# Discard Set Items

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# Pop Random Set Items

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# Clear Set

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# Delete Set Completely

thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset) This causes an error because it doesn't exist anymore.

# Loop Sets

thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

# Join Sets

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
set4 = set1 | set2
print(set4)

# Join Multiple Sets

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)
myotherset = set1 | set2 | set3 | set4
print(myotherset)

# Join a Set and a Tuple

x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

# Update Set

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# Set Intersection

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

# Join Two Sets

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

# Intersection Update

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

# Set Difference

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

# Dictionary

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# Dictionary Items

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])

# Dictionary - Duplicated Not Allowed

thisdict = {
    "brand": "Ford",
    "model": "Mustange",
    "year": 1964,
    "year": 2020 # Only this one will show due to it being the last update to the 'year' key.
}
print(thisdict)

# Dictionary Length

print(len(thisdict))

# Dictionary - Data Types

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(thisdict)
print(type(thisdict))

# dict() Constructor

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

# Dictionary - Accessing Items

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
print(x)
x = thisdict.get("model")
print(x)

# Dictionary - Get Keys

x = thisdict.keys()
print(x)

# Add New Item to Dictionary and Update Key

car = {
    "brand": "Ford",
    "model": "Mustange",
    "year": 1964
}
x = car.keys()
print(x)
car["color"] = "white"

print(x)

# Get Values

x = thisdict.values()
print(x)

# Get Items

x = thisdict.items()
print(x)

# Check If Key Exists

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary.")

# Change Dictionary Items

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

# Update Dictionary 

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

# Add Dictionary Items

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# Removing Dictionary Items

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict) 
thisdict.popitem()
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)

# Clear Dictionary

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)

# Loop Through Dictionary

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(x)
for x in thisdict:
    print(thisdict[x])
for x in thisdict.keys():
    print(x)
for x, y in thisdict.items():
    print(x, y)

# Copy Dictionary

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Dictionary dict()

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# Nested Dictionaries

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child2"]["name"])

# Loop Through Nested Dictionaries

for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])

# If Else Statements

a = 33
b = 200
if b > a:
    print("b is greater than a")

"""
a = 33
b = 200
if b > a:
print("b is greater than a ) # This will cause an error as it isn't indented after the ':' from the line above.
"""

# Elif

a = 33
b = 33
if b > a:
    print("b is greater then a")
elif a == b:
    print("a and b are equal")

# Else

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater then b")

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Short Hand If

if a > b: print("a is greater then b")

# Short Hand If Else

a = 2
b = 300
print("A") if a > b else print("B")

# Short Hand If Else 3 Conditions

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# And

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# Or

a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

# Not

a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")

# Nested If

x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# Pass Statement

a = 33
b = 200
if b > a:
    pass

# While Loops

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

# While Else Statement

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# For Loops

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Looping Through a String

for x in "banana":
    print(x)

# For Loop Break Statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# For Loop Continue Statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# For Loop range() Function

for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)

for x in range(2, 30, 3):
    print(x)