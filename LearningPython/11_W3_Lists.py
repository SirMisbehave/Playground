"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_lists.asp
"""

# List

thislist = ["apple", "banana", "cherry"]
print("List:", thislist)

# Allow Duplicates

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print("List Duplicates:", thislist)

# List Length

thislist = ["apple", "banana", "cherry"]
print("List Length:", len(thislist))

# List Items - Data Types

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print("String List:", list1)
print("Integer List:", list2)
print("Boolean List:", list3)

# List Items - Multiple Data Types in a Single List

list1 = ["abc", 34, True, 40, "male"]

print("Multiple Data Type List:", list1)

# List type() Function

mylist = ["apple", "banana", "cherry"]
print("List Type:", type(mylist))

# list() Constructor

thislist = list(("apple", "banana", "cherry")) # Note the Double Round Brackets
print("List Constructor using list():", thislist)

"""
Python Collections (Arrays)

List - ordered and changeable collection; allows duplicates.
Tuple - ordered and unchangeable collection; allows duplicates.
Set - unordered, unchangeable* and unindexed collection; no duplicates.
Dictionary - ordered* and changeable collection; no duplicates.
"""

# Access Items

thislist = ["apple", "banana", "cherry"]
print("Access List Item:", thislist[1])

# Negative Indexing

print("Negative List Indexing:", thislist[-1])

# Range of Indexes

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("Range of Indexes:", thislist[2:5]) # Return Third, Fourth and Fifth Item

# Range - Beginning -> "kiwi" But NOT Including

print("Range from Beginning to but NOT including 'kiwi':", thislist[:4])

# Range - 'cherry' -> End

print("Range from 'cherry' to end:", thislist[2:])

# Range of Negative Indexes

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("Range of Negative Indexes:", thislist[-4:-1]) # NOT Including 'mango'.

# Check if Item Exists

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
	print("Yes, 'apple' is in the fruits list.")

# Change Item Value

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print("Replacing 'banana' with 'blackcurrant':", thislist)

# Change a Range of Item Values

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print("Replace 'banana' and 'cherry' with 'blackcurrant' and 'watermelon':", thislist)

# Change a Range of Item Values Using One Item

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print("Replacing 'banana' and 'cherry' with 'watermelon':", thislist)

# Insert Items

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print("Insert Item Using insert():", thislist)

# Add List Items

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print("Add List Items Using append():", thislist)

# Insert Items

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print("Insert Items Using insert():", thislist)

# Extend List

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print("Extend List Using extend():", thislist)

# Extend List - Add Any Iterable

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print("Extend List - Add Any Iterable Using extend():", thislist)

# Remove List Items

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print("Remove List Items Using remove():", thislist)

# Remove First Occurrence of "banana"

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana") # Yes, it's exactly the same as line 143 above: remove() only removes the first occurrence.
print("Remove First Occurrence Using remove():", thislist)

# Remove Specified Index

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print("Remove Specified Index Using pop():", thislist)

# Remove Index - Non-Specification Removes Last Items

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print("Remove Last Item Using pop():", thislist)

# Remove Specified Index via del Keyword

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print("Remove Specified Index via del Keyword:", thislist)

# Delete Entire List via del Keyword

thislist = ["apple", "banana", "cherry"]
del thislist

# Clear the List

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print("Clear the List Using clear():", thislist)

# Loop Through a List

thislist = ["apple", "banana", "cherry"]
for x in thislist:
	print("Looped List Item:", x)

# Loop Through the Index Numbers

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
	print("Looped List Item via Index Numbers:", thislist[i])

# Using a While Loop

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
	print("List Item via While Loop:", thislist[i])
	i = i + 1

# Looping Using List Comprehension

thislist = ["apple", "banana", "cherry"]
[print("Looping Items via List Comprehension:", x) for x in thislist]

# Normal Way of Looping Through a List

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
	if "a" in x:
		newlist.append(x)

print("Normal List For Loop:", newlist)

# List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print("List Comprehension Variant:", newlist)

"""
List Comprehension Syntax

newlist = [expression for item in iterable if condition == True]
"""

# List Comprehension - Only Accepts Items That Are Not "apple"

newlist = [x for x in fruits if x != "apple"]
print("List Comprehension NOT Condition:", newlist)

# List Comprehension - No if Statement

newlist = [x for x in fruits]
print("List Comprehension No if Statement:", newlist)

# List Comprehension - Create Iterable with range()

newlist = [x for x in range(10)]
print("List Comprehension Range:", newlist)

# List Comprehension - Accept Only Numbers Lower Than 5

newlist = [x for x in range(10) if x < 5]
print("List Comprehension Numbers Lower Than 5", newlist)

# List Comprehension - Expression

newlist = [x.upper() for x in fruits]
print("List Comprehension Expression", newlist)

# List Comprehension - Set All Values in the New List to 'hello'

newlist = ['hello' for x in fruits]
print("List Comprehension - Set All to 'hello':", newlist)

# List Comprehension - Return 'orange' Instead of 'banana'

newlist = [x if x != "banana" else "orange" for x in fruits]
print("List Comprehension - Return 'orange' Instead of 'banana':", newlist)

# Sort List - Alphanumerically

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print("Alphanumeric Sort:", thislist)

# Sort List - Numerically

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print("Numeric Sort:", thislist)

# Sort List - Descending

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print("Descending Sort (String):", thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print("Descending Sort (Integer)", thislist)

# Customize Sort Function

def myfunc(n):
	return abs(n - 50) # Sort Based On How Close Number is to 50

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print("Customize Sort:", thislist)

# Case Sensitive Sort By Default

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print("Case Sensitive Sort By Default:", thislist)

# Case Insensitive Sort

thislist.sort(key = str.lower)
print("Case Insensitive Sort:", thislist)

# Reverse Order

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print("Reverse Order:", thislist)

# Copy Lists - copy() Method

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print("Copy Using copy() Method:", mylist)

# Copy Lists - list() Method

mylist = list(thislist)
print("Copy Using list() Method:", mylist)

# Copy Lists - slice ':' Operator

mylist = thislist[:]
print("Copy Using slice ':' Operator:", mylist)

# Join Lists - Join Two Lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print("Join Two Lists:", list3)

# Append List

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
	list1.append(x)

print("Append List Using append():", list1)

# Extend List

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print("Extend List Using extend():", list1)

"""
List Methods

append() 	- Adds an element at the end of the list.
clear() 	- Revmoes all the elements from the list.
copy()		- Returns a copy of the list.
count() 	- Returns the number of elements with the specified value.
extend() 	- Add the elements of a list (or any iterable), to the end of the current list.
index() 	- Returns the index of he first element with the specified value.
insert() 	- Adds an element at the specified position.
pop() 		- Removes the element at the specified position.
remove() 	- Removes the item with the specified value.
reverse() 	- Reverses the order of the list.
sort() 		- Sorts the list.
"""