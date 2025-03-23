"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/numpy/numpy_array_sort.asp
"""

# Sorting Arrays

import numpy as np

arr = np.array([3, 4, 0, 1])

print("Sorting Arrays:", np.sort(arr))

# Sorting Alphabetically

arr = np.array(['banana', 'cherry', 'apple'])

print("Alphabetical Sorting:", np.sort(arr))

# Sort a Boolean Array

arr = np.array([True, False, True])

print("Boolean Sorting:", np.sort(arr))

# Sorting a 2-D Array

arr = np.array([[3, 2, 4], [5, 0, 1]])

print("2-D Array Sorting:", np.sort(arr))