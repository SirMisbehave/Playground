"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/numpy/numpy_array_shape.asp
"""

# Get the Shape of an Array

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print("Shape Array:", arr.shape)

# Get the Shape of an Array with 5 Dimensions

arr = np.array([1, 2, 3, 4], ndmin = 5)

print("Array:", arr)
print("Shape of Array:", arr.shape)