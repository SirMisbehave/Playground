"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/numpy/numpy_array_iterating.asp
"""

# NumPy Array Iterating

import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
    print("Iterated Loop Item:", x)

# Iterating 2-D Arrays

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    print("Iterated Loop 2-D Item:", x)

# Iterate on Each Scalar Element of 2-D Array

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    for y in x:
        print("Iterated Loop Item (Second Layer):", y)

# Iterating 3-D Arrays

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
    print("Iterated Loop Item in 3-D Array:", x)

# Iterating 3-D Arrays Down to Scalars

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
    for y in x:
        for z in y:
            print("4th Layer Iterated Loop Item:", z)

# Iterating Arrays Using nditer()

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
    print("Iterating Arrays Using nditer():", x)

# Iterating Array with Different Data Types

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags = ['buffered'], op_dtypes = ['S']):
    print("Array Iteration as String:", x)

# Iterating with Different Step Size

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
    print("Array Iteration with Different Step Size:", x)

# Enumerated Iteration Using ndenumerate()

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
    print("Enumerated Loop Item via ndenumerate():", idx, x)