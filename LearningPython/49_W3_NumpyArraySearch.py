"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/numpy/numpy_array_search.asp
"""

# Searching Arrays

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)

print("Searching Arrays:", x)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)

print("Even Indexes:", x)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 1)

print("Odd Indexes:", x)

# Search Sorted

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)

print("Search Sorted:", x)

# Search from Right Side

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')

print("Search from Right:", x)

# Multiple Values

arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])

print("Multi-Value:", x)