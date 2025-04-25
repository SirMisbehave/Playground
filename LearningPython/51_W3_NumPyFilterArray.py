"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/numpy/numpy_array_filter.asp
"""

# Filtering Arrays

import numpy as np

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print("Filtering Arrays:", newarr)

# Creating the Filter Array

arr = np.array([41, 42, 43, 44])

# Create an Empty List
filter_arr = []

# Go Through Each Element in Arr
for element in arr:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print("Higher Then 42:", filter_arr)
print("New Array:", newarr)

# Return Only Even Elements

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an Empty List
filter_arr = []

# Go Through Each Element in Arr
for element in arr:
    if element % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print("Even Items:", filter_arr)
print("New Array:", newarr)

# Creating Filter Directly from Array

arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]

print("Higher then 42:", filter_arr)
print("New Array:", newarr)

# Creating Filter Directly from Array - Even Only

arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]

print("Even Only:", filter_arr)
print("New Array:", newarr)