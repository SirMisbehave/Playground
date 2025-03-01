"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/numpy/numpy_data_types.asp
"""

# Checking the Data Type of an Array

import numpy as np

arr = np.array([1, 2, 3, 4])
print("Checking Data Type of an Array:", arr.dtype)

# Data Type of an Array Containing Strings

arr = np.array(['apple', 'banana', 'cherry'])
print("Data Type of Array Containing Strings:", arr.dtype)

# Creating Arrays with a Defined Data Type

arr = np.array([1, 2, 3, 4], dtype = 'S')

print(arr)
print(arr.dtype)

# Create an Array with Data Type 4 Bytes Integer

arr = np.array([1, 2, 3, 4], dtype = 'i4')

print(arr)
print(arr.dtype)

# Converting Data Type on Existing Arrays

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)

# Change Data Type from Float to Integer

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)

# Change Data Type from Integer to Boolean

arr = np.array([1, 0, 3])
newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)