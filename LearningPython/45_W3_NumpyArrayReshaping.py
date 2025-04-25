"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/numpy/numpy_array_reshape.asp
"""

# Reshape from 1-D to 2-D

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print("Reshaped Array 1-D to 2-D:", newarr)

# Reshape from 1-D to 3-D

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print("Reshape Array 1-D to 3-D:", newarr)

# Check if Reshaped Array Returns Copy or View

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print("Reshaped Array Copy or View:", arr.reshape(2, 4).base)

# Unknown Dimensions

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print("Convert 1-D with 8 Elements to 3-D with 2x2 Elements:", newarr)

# Flattening the Arrays

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print("Flattening the Arrays:", newarr)