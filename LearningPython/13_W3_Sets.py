"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_sets.asp
"""

# Set

thisset = { "apple", "banana", "cherry" }
print("Set:", thisset)

"""
Set Items

Sets items are unordered, unchangeable and do not allow duplicate values.

Unordered

Unordered means that the items in a set do not have a defnied order.

Unchangeable

Items cannot be changed, but items can be removed and added.
"""

# Duplicates Not Allowed

thisset = { "apple", "banana", "cherry", "apple" }
print("Sets Have No Duplicates:", thisset)

# Sets With Boolean Items - True

thisset = { "apple", "banana", "cherry", True, 1, 2 }
print("Sets With Boolean Items - True:", thisset)

# Sets With Boolean Items - False

thisset = { "apple", "banana", "cherry", False, True, 0 }
print("Sets With Boolean Items - False:", thisset)

# Get the Length of a Set

thisset = { "apple", "banana", "cherry" }
print("Set Length:", len(thisset))

# Set Items - Data Types

set1 = { "apple", "banana", "cherry" } 	# Strings
set2 = { 1, 5, 7, 9, 3 } 				# Integers
set3 = { True, False, False } 			# Booleans

# Multi Data Type Set

set1 = { "abc", 34, True, 40, "male" }
print("Multi Data Type Set:", set1)

# Set Data Type

myset = { "apple", "banana", "cherry" }
print("Set Data Type:", type(myset))

# set() Constructor

thisset = set(("apple", "banana", "cherry")) # Note Double Round Brackets
print("set() Constructor:", thisset)

# Access Items

thisset = { "apple", "banana", "cherry" }
for x in thisset:
	print("Access Set Items:", x)

# Set If Print Statement

thisset = { "apple", "banana", "cherry" }
print("banana" in thisset)

# Set If Not Print Statement

thisset = { "apple", "banana", "cherry" }
print("banana" not in thisset)

# Add Items to Set

thisset = { "apple", "banana", "cherry" }
thisset.add("orange")
print("Add Items via add() Method:", thisset)

# Add Sets

thisset = { "apple", "banana", "cherry" }
tropical = { "pineapple", "mango", "papaya" }
thisset.update(tropical)
print("Add Sets via update() Method:", thisset)

# Add Any Iterable

thisset = { "apple", "banana", "cherry" }
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print("Add Any Iterable via update():", thisset)

# Remove Item

thisset = { "apple", "banana", "cherry" }
thisset.remove("banana")
print("Remove Item via remove() Method:", thisset)

# Discard Item

thisset = { "apple", "banana", "cherry" }
thisset.discard("banana")
print("Remove Item via discard() Method:", thisset)

# Remove Item via pop()

thisset = { "apple", "banana", "cherry" }
x = thisset.pop()
print("This Set Before pop():", thisset)
print("Remove Item via pop() Method:", x)

# Clear Item

thisset = { "apple", "banana", "cherry" }
thisset.clear()
print("Clear Item via clear() Method:", thisset)

# Delete Item

thisset = { "apple", "banana", "cherry" }
del thisset
# print("Delete Item:", thisset) # This will throw an error as it doesn't exist anymore.

# Loop Items

thisset = { "apple", "banana", "cherry" }
for x in thisset:
	print("Looped Set Item:", x)

# Join Sets - Union

set1 = { "a", "b", "c" }
set2 = { 1, 2, 3 }
set3 = set1.union(set2)
print("Join Sets With Union:", set3)

# Join Sets - '|' Operator

set1 = { "a", "b", "c" }
set2 = { 1, 2, 3 }
set3 = set1 | set2
print("Join Sets With the '|' Operator:", set3)

# Join Multiple Sets

set1 = { "a", "b", "c" }
set2 = { 1, 2, 3 }
set3 = { "John", "Elena" }
set4 = { "apple", "banana", "cherry" }

myset = set1.union(set2, set3, set4)
print("Join Multiple Sets:", myset)

# Join Many Sets - '|' Operator

set1 = { "a", "b", "c" }
set2 = { 1, 2, 3 }
set3 = { "John", "Elena" }
set4 = { "apple", "bananas", "cherry" }

myset = set1 | set2 | set3 | set4
print("Join Many Sets With '|' Operator:", myset)

# Join a Set and a Tuple

x = { "a", "b", "c" }
y = (1, 2, 3)
z = x.union(y)
print("Join a Set and a Tuple:", z)

# Insert Items Into Set via update()

set1 = { "a", "b", "c" }
set2 = { 1, 2, 3 }
set1.update(set2)
print("Insert Items Into Set via update() Method:", set1)

# Set Intersection

set1 = { "apple", "banana", "cherry" }
set2 = { "google", "microsoft", "apple" }
set3 = set1.intersection(set2)
print("Set Intersection:", set3)

# Join Two Sets With '&' Operator

set1 = { "apple", "banana", "cherry" }
set2 = { "google", "microsoft", "apple" }
set3 = set1 & set2
print("Join Two Sets With '&' Operator:", set3)

# intersection_update() Method

set1 = { "apple", "banana", "cherry" }
set2 = { "google", "microsoft", "apple" }
set1.intersection_update(set2)
print("intersection_update() Method:", set1)

# Set Intersection With Booleans

set1 = { "apple", 1, "banana", 0, "cherry" }
set2 = { False, "google", 1, "apple", 2, True }
set3 = set1.intersection(set2)
print("Set Intersection With Booleans:", set3)

# Set Difference

set1 = { "apple", "banana", "cherry" }
set2 = { "google", "microsoft", "apple" }
set3 = set1.difference(set2)
print("Set Difference:", set3)

# Set Difference With '-' Operator

set1 = { "apple", "banana", "cherry" }
set2 = { "google", "microsoft", "apple" }
set3 = set1 - set2
print("Set Difference With '-' Operator:", set3)

# difference_update() Method

set1 = { "apple", "banana", "cherry" }
set2 = { "google", "microsoft", "apple" }
set1.difference_update(set2)
print("difference_update() Method:", set1)

# Symmetric Differences

set1 = { "apple", "banana", "cherry" }
set2 = { "google", "microsoft", "apple" }
set3 = set1.symmetric_difference(set2)
print("Symmetric Differences:", set3)

# Symmetric Differences With '^' Operator

set1 = { "apple", "banana", "cherry" }
set2 = { "google", "microsoft", "apple" }
set3 = set1 ^ set2
print("Symmetric Differenes With '^' Operator:", set3)

# symmetric_difference_update()

set1 = { "apple", "banana", "cherry" }
set2 = { "google", "microsoft", "apple" }
set1.symmetric_difference_update(set2)
print("symmetric_difference_update():", set1)

"""
Set Methods

add() 									- Adds an element to the set.
clear() 								- Removes all the elements from the set.
copy() 									- Returns a copy of the set.
differences() 					- '-' 	- Returns a set containing the difference between two or more set.
difference_update() 			- '-=' 	- Removes the items in this set that are also included in another, specified set.
discard() 								- Remove the specified item.
intersection() 					- & 	- Returns a set, that is the intersection of two other sets.
intersection_update() 			- &= 	- Removes the items in this set that are not present in other, specified set(s).
isdisjoin() 							- Returns whether two sets have a intersection or not.
issubset() 						- <= 	- Returns whether another set contains this set or not.
issuperset() 					- >= 	- Returns whether this set contains another set or not.
pop() 									- Removes an element from the set.
remove() 								- Removes the specified elements.
symmetric_difference() 			- ^ 	- Returns a set with the symmetric differences of to sets.
symmetric_difference_update() 	- ^= 	- Inserts the symmetric from this set sets.
union() 						- | 	- Return a set containing the union of sets.
update() 						- != 	- Update the set with the union of this set and others.
"""