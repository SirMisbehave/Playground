"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/numpy/numpy_array_slicing.asp
"""

# Slicing Arrays

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print("Slicing Array:", arr[1:5])

# Slice Elements from Index 4 to the End of the Array

print("Slicing Array:", arr[4:])

# Slice Elements from the Beginning to Index 4

print("Slice Elements:", arr[:4])

# Negative Slicing

print("Negative Slicing:", arr[-3:-1])

# STEP

print("STEP Every Other from Index 1 to Index 5:", arr[1:5:2])

# Every Other Element from Entire Array

print("STEP Every Other from Entire Element:", arr[::2])

# Slicing 2-D Arrays

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print("Slicing 2-D Arrays:", arr[1, 1:4])
print("Slicing 2-D Arrays:", arr[0:2, 2]) 	# From Both Elements, Return Index 2
print("Slicing 2-D arrays:", arr[0:2, 1:4])	# Slice Index 1 to Index 4