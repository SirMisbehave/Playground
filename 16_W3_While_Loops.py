"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_while_loops.asp
"""

# While Loop

i = 1
while i < 6:
	print("While Looped Item:", i)
	i += 1

# Break Statement

i = 1
while i < 6:
	print("While Looped Item (break):", i)
	if i == 3:
		break
	i += 1

# Continue Statement

i = 0
while i < 6:
	i += 1
	if i == 3:
		continue
	print("While Looped Item (continue)", i)

# Else Statement

i = 1
while i < 6:
	print("While Looped Item (else)", i)
	i += 1
else:
	print("i is no longer less than 6")