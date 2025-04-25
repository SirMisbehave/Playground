"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/numpy/numpy_array_indexing.asp
"""

# Access Array Elements

import numpy as np

arr = np.array([1, 2, 3, 4])

print("First Element:", arr[0]) 						# First Element
print("Second Element:", arr[1]) 						# Second Element
print("Add Third and Fourth Element:", arr[2] + arr[3]) # Add Third and Fourth Elements

# Access 2-D Arrays

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print("2nd element on 1st row:", arr[0, 1])
print("5th element on 2nd row:", arr[1, 4])

# Access 3-D Arrays

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print("Third Element of Second Array of the first Array:", arr[0, 1, 2])

# Negative Indexing

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("Last element from 2nd dim:", arr[1, -1])