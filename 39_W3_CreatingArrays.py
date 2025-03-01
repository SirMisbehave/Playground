"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/numpy/numpy_creating_arrays.asp
"""

# Create a NumPy ndarray Object

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print("np array:", arr)
print("np array type:", type(arr))

# Use Tuple to Create NumPy Array

arr = np.array((1, 2, 3, 4, 5))
print("np array:", arr)

# Dimensions in Arrays

# 0-D Arrays

arr = np.array(42)
print("0-D Array:", arr)

# 1-D Arrays

arr = np.array([1, 2, 3, 4, 5])

print("1-D Arrays:", arr)

# 2-D Arrays

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("2-D Arrays:", arr)

# 3-D Arrays

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("3-D Arrays:", arr)

# Check Number of Dimensions

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Higher Dimensional Arrays

arr = np.array([1, 2, 3, 4], ndmin = 5)
print(arr)
print("Number of Dimensions:", arr.ndim)