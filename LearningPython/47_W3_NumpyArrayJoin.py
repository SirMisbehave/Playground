"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/numpy/numpy_array_join.asp
"""

# Joining NumPy Arrays

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print("Join Two Numpy Arrays:", arr)

# Join Two 2-D Arrays Along Rows

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis = 1)

print("Join Two 2-D Arrays:", arr)

# Joining Arrays Using Stack Functions

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis = 1)
print("Join Array With Stack Function:", arr)

# Stacking Along Rows

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))
print("Stacking Along Rows:", arr)

# Stacking Along Columns

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print("Stacking Along Columns:", arr)

# Stacking Along Height (Depth)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print("Stacking Along Height:", arr)