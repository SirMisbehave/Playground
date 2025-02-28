"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_arrays.asp
"""

# Python does not have built-in support for Arrays, but Python Lists can be used instead.

# To work with arrays in Python you will have to import a library, like the NumPy library.

# Create an Array Containing Car Names

cars = ["Ford", "Volvo", "BMW"]
print("Array:", cars)

# Access the Elements of an Array

x = cars[0]
print("Array Element:", x)

# Modify Value of First Array Item

cars[0] = "Toyota"
print("Modified Array Element:", cars[0])

# Length of an Array

x = len(cars)
print("Array Length:", x)

# The length of an array is always one more than the highest array index.

# Looping Array Elements

for x in cars:
	print("Looped Array Elements:", x)

# Adding Array Elements

cars.append("Honda")
print("Added Array Element:", cars)

# Removing Array Elements

cars.pop(1)
print("Removing Array Element:", cars)

# Remove Array Element via remove()

cars.remove("Honda")
print("Remove Honda Specifically:", cars)

"""
Array Methods

append() 	- Adds an element at the end of the list.
clear() 	- Removes all the elements from the list.
copy() 		- Returns a copy of the list.
count() 	- Returns the number of elements with the specified value.
extend() 	- Add the elements of a list (or any iterable), to the end of the current list.
index() 	- Returns the index of the first element with the specified value.
insert() 	- Adds an element at the specified position.
pop() 		- Removes the element at the specified position.
remove() 	- Removes the first item with the specified value.
reverse() 	- Reverses the order of the list.
sort() 		- Sorts the list.
"""