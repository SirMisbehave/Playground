"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_iterators.asp
"""

# Iterators

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Iterate Through String Object

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Looping Through an Iterator

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
	print("Looped Item:", x)

# Looping Through a String Object Iterable

mystr = "banana"

for x in mystr:
	print("Looped Item String Object:", x)

# Create an Iterator

class MyNumbers:
	def __iter__(self):
		self.a = 1
		return self

	def __next__(self):
		x = self.a
		self.a += 1
		return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# StopIteration

class MyNumbers:
	def __iter__(self):
		self.a = 1
		return self

	def __next__(self):
		if self.a <= 20:
			x = self.a
			self.a += 1
			return x
		else:
			print("Stopping Iteration")
			raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
	print(x)