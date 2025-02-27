"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_conditions.asp
"""

"""
Conditions & If Statements

Equals 						- a == b
Not Equals 					- a != b
Less Than 					- a < b
Less Than or Equal To 		- a <= b
Greater Than 				- a > b
Greater Than or Equal To 	- a >= b
"""

# If Statements

a = 33
b = 200

if b > a:
	print("If Statement: b is greater than a")

# Elif

a = 33
b = 33

if b > a:
	print("If Statement: b is greater than a")
elif a == b:
	print("Elif: a and b are equal")

# Else

a = 200
b = 33

if b > a:
	print("If Statement: b is greater than a")
elif a == b:
	print("Elif: a and b are equal")
else:
	print("Else: a is greater than b")

# Else Without the Elif

a = 200
b = 33

if b > a:
	print("If Statement: b is greater than a")
else:
	print("Else: b is not greater than a")

# Short Hand If

if a > b: print("Short Hand If: a is greater than b")

# Short Hand If Else

a = 2
b = 330

print("Short Hand If Else:")
print("A") if a > b else print("B")

# 3 Condition If Else Statement

a = 330
b = 330

print("3 Condition If Else Statement:")
print("A") if a > b else print("=") if a == b else print("B")

# 'and' Keyword

a = 200
b = 33
c = 500

if a > b and c > a:
	print("And Keyword If Statement: Both conditions are True.")

# 'or' Keyword

a = 200
b = 33
c = 500

if a > b or a > c:
	print("Or Keyword If Statement: At least one of the conditions is True.")

# 'not' Keyword

a = 33
b = 200

if not a > b:
	print("Not Keyword If Statement: a is NOT greater than b.")

# Nested If

x = 41

if x > 10:
	print("Nested If: Above ten,")

	if x > 20:
		print("and also above 20!")
	else:
		print("but not above 20.")

# Pass Statement

a = 33
b = 200

if b > a:
	pass