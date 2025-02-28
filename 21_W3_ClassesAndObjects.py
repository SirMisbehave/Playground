"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_classes.asp
"""

# Classes / Objects

# Create a Class

class MyClass:
	x = 5

# Create Object

p1 = MyClass()
print("New Class Object:", p1.x)

# The __init__() Function

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

p1 = Person("John", 36)

print("Person Object Name:", p1.name)
print("Person Object Age:", p1.age)

# The __str__() Function

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return f"{self.name}({self.age})"

p1 = Person("John", 36)
print("Person Class with __str__ Function:", p1)

# Object Methods

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def myfunc(self):
		print("Object Methods: Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# The 'self' Parameter

class Person:
	def __init__(mySillyObject, name, age): # mySillyObject Instead of 'self' - Instance of Itself, Hence 'self' as Default Convention
		mySillyObject.name = name
		mySillyObject.age = age

	def myfunc(abc):
		print("Object Methods: Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

# Modify Object Properties

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def myfunc(self):
		print("Object Methods: Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

p1.age = 40 # Update Age
print("Updated Age:", p1.age)

# Delete Object Properties

del p1.age
print("Delete p1 Object Property:", p1)

# Delete Objects

del p1

# The 'pass' Statement

class Person:
	pass