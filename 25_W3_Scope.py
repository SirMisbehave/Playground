"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_scope.asp
"""

# Local Scope

def myfunc():
	x = 300
	print("Local Scope:", x)

myfunc()

# Function Inside Function

def myfunc():
	x = 300
	def myinnerfunc():
		print("Function Inside Function:", x)
	myinnerfunc()

myfunc()

# Global Scope

x = 300

def myfunc():
	print("Global Scope:", x)

myfunc()
print(x)

# Naming Variables

x = 300

def myfunc():
	x = 200
	print("Local Variable:", x)

myfunc()
print("Global Variable:", x)

# Global Keyword

def myfunc():
	global x
	x = 300

myfunc()
print("Global Keyword:", x)

# Change Global Variable Inside Function

x = 300

def myfunc():
	global x
	x = 200

myfunc()
print("Change Global Variable:", x)

# Nonlocal Keyword

def myfunc1():
	x = "Jane"

	def myfunc2():
		nonlocal x
		x = "Hello"

	myfunc2()
	return x

print(myfunc1())