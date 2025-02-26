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