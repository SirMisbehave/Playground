"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_dictionaries.asp
"""

# Dictionaries

thisdict = {
	"brand": "Ford",
	"model": "Mustange",
	"year": 1964
}

print("Dictionary:", thisdict)

# Dictionary Items

print("Dictionary Items:", thisdict["brand"])

# Duplicates Not Allowed - Overwrites Existing Values with Same Key

thisdict = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964,
	"year": 2020
}

print("Non Duplicate Dictionary:", thisdict)

# Dictionary Length

print("Dictionary Length:", len(thisdict))

# Dictionary Items - Data Types

thisdict = {
	"brand": "Ford",
	"electric": False,
	"year": 1964,
	"color": ["red", "white", "blue"]
}

print("Dictionary Data Types:", thisdict)

thisdict = {
	"brand": "Ford", 
	"model": "Mustang",
	"year": 1964
}

print("Dictionary Type:", type(thisdict))

# dict() Constructor

thisdict = dict(name = "John", age = 36, country = "Norway")
print("dict() Constructor:", thisdict)

# Access Dictionary Items

thisdict = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964,
}

x = thisdict["model"]
print("Access Dictionary Items:", x)

# get() the Value via Key

x = thisdict.get("model")
print("get() Value via Key:", x)

# Get Keys

x = thisdict.keys()
print("Get Keys:", x)

# Updating Keys

car = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964
}

x = car.keys()
print("Get Keys Before Update:", x)

car["color"] = "white"
print("Get Keys After Update:", x)

# Get Values

car = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964
}

x = car.values()
print("Values Before the Update:", x)

car["year"] = 2020
car["color"] = "red" # Adding An Item Based On Next Example Consolidated
print("Values After the Update:", x)

# Get Items

car = {
	"brand": "Ford",
	"model": "Mustange",
	"year": 1964
}

x = car.items()
print("Get Items Before the Change:", x)

car["year"] = 2020
car["color"] = "red" # Add New Item Based On Next Example Consolidated
print("Get Items After the Change:", x)

# Check If Key Exists

thisdict = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964
}

if "model" in thisdict:
	print("Yes, 'model' is one of the keys in the thisdict dictionary.")

# Change Values

thisdict = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964
}

thisdict["year"] = 2018
print("Normal Change Values:", thisdict)

# Update Dictionary

thisdict.update({"year": 2020})
print("Update Dictionary Using update():", thisdict)

# Adding Items

thisdict["color"] = "red"
print("Normal Adding Items to Dictionary:", thisdict)

# Adding Items via Update

thisdict.update({"anotherColor": "blue"})
print("Add Item to Dictionary via update():", thisdict)

# Remove Specific Dictionary Item

thisdict = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964
}

print("Dictionary Before Removal:", thisdict)

thisdict.pop("model")
print("Remove Specific Dictionary Item via pop():", thisdict)

# Remove Dictionary Last Inserted Item

thisdict = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964
}

print("Before Removal of Dictionary Item:", thisdict)

thisdict.popitem()
print("Remove Dictionary Item via popitem():", thisdict)

# Remove Dictionary Item via 'del' Keyword

thisdict = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964
}

del thisdict
# print(thisdict) # This will cause an error because 'thisdict' no longer exists.

# Empty Dictionary via clear() Method

thisdict = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964
}

thisdict.clear()
print("Empty Dictionary via clear() Method:", thisdict)

# Loop Through a Dictionary - Keys

thisdict = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964
}

for x in thisdict:
	print("Looped Item Key Name:", x)

# Loop Through a Dictionary - Values

for x in thisdict:
	print("Looped Item Value:", thisdict[x])

# Look Through a Dictionary - values()

for x in thisdict.values():
	print("Looped Item Value via values():", x)

# Loop Through a Dictionary - keys()

for x in thisdict.keys():
	print("Looped Item Keys via keys():", x)

# Loop Through a Dictionary - items()

for x, y in thisdict.items():
	print("Looped Item via items():", x, y)

# Copy a Dictionary

thisdict = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964
}

mydict = thisdict.copy()
print("Copied Dictionary:", mydict)

# Copy a Dictionary - dict()

thisdict = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964
}

mydict = dict(thisdict)
print("Copied Dictionary via dict():", mydict)

# Nested Dictionaries

myfamily = {
	"child1": {
		"name": "Emil",
		"year": 2004
	},
	"child2": {
		"name": "Tobias",
		"year": 2007
	},
	"child3": {
		"name": "Linus",
		"year": 2011
	}
}

print("Nested Dictionary:", myfamily)

# Create 3 Separate Dictionaries - Then Contain All 3 Within 1 Single Dictionary

child1 = {
	"name": "Emil",
	"year": 2004
}

child2 = {
	"name": "Tobias",
	"year": 2007
}

child3 = {
	"name": "Linus",
	"year": 2011
}

myfamily = {
	"child1": child1,
	"child2": child2,
	"child3": child3
}

print("Nested Dictionary Created Separately:", myfamily)

# Access Items in Nested Dictionaries

print("Access Item in Nested Dictionary:", myfamily["child2"]["name"])

# Loop Through Nested Dictionaries

for x, obj in myfamily.items():
	print("Looped Item in Dictionary, First Layer:", x)

	for y in obj:
		print("Looped Item in Dictionary, Second Layer:", y + ':', obj[y])

"""
Dictionary Methods

clear() 		- Removes all the elements from the dictionary.
copy() 			- Returns a copy of the dictionary.
fromkeys()		- Returns a dictionary with the specified keys and value.
get()			- Returns the value of the specified key.
items()			- Returns a list containing a tuple for each key value pair.
keys() 			- Returns a list containing the dictionary's keys.
pop() 			- Removes the element with the specified key.
popitem() 		- Removes the last inserted key-value pair.
setdefault() 	- Returns the value of the specified key. If the key does not exist: insert the key, with the specified value.
update() 		- Updates the dictionary with the specified key-value pairs.
values() 		- Returns a list of all the values in the dictionary.
"""