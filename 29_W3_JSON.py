"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_json.asp
"""

# JSON

import json

# Convert from JSON to Python

x = '{ "name": "John", "age": 30, "city": "New York"}' 	# JSON
y = json.loads(x) 										# Parse 'x'

print("JSON to Python:", y["age"]) 						# Result is a Python Dictionary

# Convert from Python to JSON

x = {
	"name": "John",
	"age": 30,
	"city": "New York"
} 														# Python Dictionary
y = json.dumps(x) 										# Convert into JSON

print("Convert from Python to JSON:", y) 				# Result is a JSON String

# Convert Python Objects into JSON Strings

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "banana"]))
print(json.dumps(("apple", "banana")))
print(json.dumps("Hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# Convert a Python Object Containing all Legal Data Types

x = {
	"name": "John",
	"age": 30,
	"married": True,
	"divorce": False,
	"children": ("Ann", "Billy"),
	"pets": None,
	"cars": [
		{ "model": "BMW 230", "mpg": 27.5 },
		{ "model": "Ford Edge", "mpg": 24.1 }
	]
}

print("Python Object:", json.dumps(x))

# Format the Result

print("Format the Result:", json.dumps(x, indent = 4))

# Format Using Separators

print("Format Using Separators:", json.dumps(x, indent = 4, separators = (". ", " = ")))

# Order the Result

print("Order the Result:", json.dumps(x, indent = 4, sort_keys = True))