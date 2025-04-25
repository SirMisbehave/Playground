"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/numpy/numpy_copy_vs_view.asp
"""

# Numpy Array Copy vs View

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print("Original Array:", arr)
print("Array Copy:", x)

# Check If Array Owns It's Data

arr - np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)