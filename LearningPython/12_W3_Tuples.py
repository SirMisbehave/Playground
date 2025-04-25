"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_tuples.asp
"""

# Tuple

thistuple = ("apple", "banana", "cherry")
print("Tuple:", thistuple)

# Tuples are Ordered and Unchangeable

# Allow Duplicates

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print("Tuples With Duplicates:", thistuple)

# Tuple Length

thistuple = ("apple", "banana", "cherry")
print("Tuple Length:", len(thistuple))

# Create Tuple With One Item

thistuple = ("apple",)
print("Tuple With One Item:", thistuple, "with a type of", type(thistuple))

# Not a Tuple

thistuple = ("apple")
print("Not a Tuple:", thistuple, "with a type of", type(thistuple))

# Tuple Items = Data Types

tuple1 = ("apple", "banana", "cherry") # Strings
tuple2 = (1, 5, 7, 9, 3) # Integer
tuple3 = (True, False, False) # Booleans

print("Strings:", tuple1)
print("Integers:", tuple2)
print("Booleans:", tuple3)

# Multi Data Type Tuple

tuple1 = ("abc", 34, True, 40, "male")
print("Multi Data Type Tuple:", tuple1)

# Tuple Data Type

mytuple = ("apple", "banana", "cherry")
print("Tuple Data Type:", type(mytuple))

# tuple() Constructor

thistuple = tuple(("apple", "banana", "cherry"))
print("tulpe() Constructor:", thistuple)

# Access Tuple Items

thistuple = ("apple", "banana", "cherry")
print("Access Tuple Items:", thistuple[1])

# Negative Indexing

thistuple = ("apple", "banana", "cherry")
print("Negative Indexing:", thistuple[-1])

# Range of Indexes

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print("Range of Indexes:", thistuple[2:5])

# Beginning to 'kiwi' But NOT Including 'kiwi'

print("Beginning to 'kiwi' But NOT Including:", thistuple[:4])

# From 'cherry' to the End

print("From 'cherry' to the End:", thistuple[2:])

# Range of Negative Indexes

print("Range of Negative Indexes:", thistuple[-4:-1])

# Check If Item Exists

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
	print("Yes, 'apple' is in the fruits tuple.")

# Change Tuple Values

x = ("apple", "banana", "cherry")
y = list(x) 	# Convert Tuple to List
y[1] = "kiwi"
x = tuple(y) 	# Convert Back to Tuple

print("Change 'banana' to 'kiwi':", x)

# Add Items

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print("Add Items Using append():", thistuple)

# Add Tuple to Tuple

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print("Add Tuple to Tuple:", thistuple)

# Remove Items

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print("Remove Items Using remove():", thistuple)

# Delete Tuple Completely

thistuple = ("apple", "banana", "cherry")
del thistuple
# print("Deleted Tuple:", thistuple) # This will error as 'thistuple' no longer exists.

# Unpack Tuples

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print("Green:", green)
print("Yellow:", yellow)
print("Red:", red)

# Using Asterisk *

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print("Green:", green)
print("Yellow:", yellow)
print("Red:", red)

# Add a List of Values to 'tropic' Values

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits

print("Green:", green)
print("Tropic*:", tropic)
print("Red:", red)

# Loop Through a Tuple

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
	print("Looped Tuple Item:", x)

# Loop Through the Index Numbers

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
	print("Looped Tuple Item Via Index:", thistuple[i])

# Using a While Loop

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
	print("While Loop Item:", thistuple[i])
	i = i + 1

# Join Two Tuples

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print("Join Two Tuples:", tuple3)

# Multiple Tuples

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print("Multiple Tuples:", mytuple)

"""
Tuple Methods

count() 	- Returns the number of times a specified value occurs in a tuple.
index() 	- Searches the tuple for a specified value and returns the position where it was found.
"""