"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_for_loops.asp
"""

# For Loops

fruits = ["apple", "banana", "cherry"]
for x in fruits:
	print("For Loop Items:", x)

# Looping Through a String

for x in "banana":
	print("For Loop Through String:", x)

# For Loop Break Statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
	print("For Loop Items (break):", x)
	if x == "banana":
		break

# For Loop Continue Statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
	if x == "banana":
		continue
	print(x)
print("This statement is printed outside of the For Loop if 'x' is equals to 'banana'.")

# Range Function

for x in range(6):
	print("Range with Single Item:", x)

for x in range(2, 6): # Specify Starting Point
	print("Range with Starting Point and End Point:", x)

for x in range(2, 30, 3): # Increment by 3
	print("Range with Incremental Argument:", x)

# Else in For Loop with Range

for x in range(6):
	print("Range Item:", x)
else:
	print("Finally finished!")

# Nested For Loops

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
	for y in fruits:
		print(x, y)

# For Loop Pass Statement

for x in [0, 1, 2]:
	pass