"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_polymorphism.asp
"""

# Function Polymorphism - String Example

x = "Hello World!"
print("String Length:", len(x))

# Function Polymorphism - Tuple Example

mytuple = ("apple", "banana", "cherry")
print("Tuple Length:", len(mytuple))

# Function Polymorphism - Dictionary Example

thisdict = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964
}

print("Dictionary Length:", len(thisdict))

# Class Polymorphism

class Car:
	def __init__(self, brand, model):
		self.brand = brand
		self.model = model

	def move(self):
		print("Drive!")

class Boat:
	def __init__(self, brand, model):
		self.brand = brand
		self.model = model

	def move(self):
		print("Sail!")

class Plane:
	def __init__(self, brand, model):
		self.brand = brand
		self.model = model

	def move(self):
		print("Fly!")

car1 = Car("Ford", "Mustang") 		# Create a Car Object
boat1 = Boat("Ibiza", "Touring 20") # Create a Boat Object
plane1 = Plane("Boeing", "747") 	# Create a Plane Object

for x in (car1, boat1, plane1):
	x.move()

# Inheritance Class Polymorphism

class Vehicle:
	def __init__(self, brand, model):
		self.brand = brand
		self.model = model

	def move(self):
		print("Move!")

class Car(Vehicle):
	pass

class Boat(Vehicle):
	def move(self):
		print("Sail!")

class Plane(Vehicle):
	def move(self):
		print("Fly!")

car1 = Car("Ford", "Mustang") 		# Create a Car Object
boat1 = Boat("Ibiza", "Touring 20") # Create a Boat Object
plane1 = Plane("Boeing", "747") 	# Create a Plane Object

for x in (car1, boat1, plane1):
	print(x.brand)
	print(x.model)
	x.move()