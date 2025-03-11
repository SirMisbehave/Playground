"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/numpy/numpy_array_split.asp
"""

# Splitting NumPy Arrays

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print("Splitting NumPy Arrays", newarr)

# Split the Array in 4 Parts

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print("Split the Array in 4 Parts:", newarr)

# Split Into Arrays

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print("Array Slit 1:", newarr[0])
print("Array Slit 2:", newarr[1])
print("Array Slit 3:", newarr[2])

# Splitting 2-D Arrays

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print("2-D Array Split:", newarr)

# Split 2-D Array into Three 2-D Arrays

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis = 1)

print("2-D Array into Three 2-D Arrays:", newarr)

# Split 2-D Array into Three 2-D Arrays Along Rows

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)

print("2-D Array into Three 2-D Arrays Along Rows:", newarr)