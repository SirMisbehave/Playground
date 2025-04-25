"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_casting.asp
"""

# Specify a Variable Type - Integers

x = int(1) 		# x Will Be 1
y = int(2.8)	# y Will Be 2
z = int("3")	# z Will Be 3

print("'x' is set to 1 casted to int using the int() constructor :", x, "with a type of", type(x))
print("'y' is set to 2.8 casted to int using the int() constructor:", y, "with a type of", type(y))
print("'z' is set to \"3\" casted to int using the int() constructor:", z, "with a type of", type(z))

# Specify a Variable Type - Floats

x = float(1) 		# x Will Be 1.0
y = float(2.8) 		# y Will Be 2.8
z = float("3")		# z Will Be 3.0
w = float("4.2") 	# w Will Be 4.2

print("'x' is set to 1 casted to float using the float() constructor:", x, "with a type of", type(x))
print("'y' is set to 2.8 casted to float using the float() constructor:", y, "with a type of", type(y))
print("'z' is set to \"3\" casted to float using the float() constructor:", z, "with a type of", type(z))
print("'w' is set to \"4.2\" casted to float using the float() constructor:", w, "with a type of", type(w))

# Specift a Variable Type = Strings

x = str("s1") 	# x Will Be 's1'
y = str(2) 		# y Will Be '2'
z = str(3.0) 	# z Will Be '3.0'

print("'x' is set to \"s1\" casted to string using the str() constructor:", x, "with a type of", type(x))
print("'y' is set to 2 casted to string using the str() constructor:", y, "with a type of", type(y))
print("'z' is set to 3.0 casted to string using the str() constructor:", z, "with a type of", type(z))