"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_inheritance.asp
"""

"""
Inheritance

Parent Class 	- is the class being inherited from, also called base class.
Child Class 	- is the class that inherits from another class, also called derived class.
"""

# Create a Parent Class

class Person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname

	def printname(self):
		print(self.firstname, self.lastname)

# Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

# Create a Child Class

class Student(Person):
	pass

x = Student("Mike", "Olsen")
x.printname()

# Add the __init__() Function

class Student(Person):
	def __init__(self, fname, lname):
		Person.__init__(self, fname, lname) # Inherit Parent __init__() Function

# Use the super() Function

class Student(Person):
	def __init__(self, fname, lname, year):
		super().__init__(fname, lname)
		self.graduationyear = year # Add Properties

x = Student("Mike", "Olsen", 2019)
print("Student Child Class:", x)

# Add Methods

class Student(Person):
	def __init__(self, fname, lname, year):
		super().__init__(fname, lname)
		self.graduationyear = year

	def welcome(self):
		print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()