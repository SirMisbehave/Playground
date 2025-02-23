"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_booleans.asp
"""

# Booleans - Them True or False Thangs

print(10 > 9)	# True
print(10 == 9)	# False
print(10 < 9)	# False

# Print a Message Based On Condition

a = 200
b = 33

if b > a:
	print("b is greater then a")
else:
	print("b is not greater than a")

# Evaluate Values and Variables

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15
print(bool(x))
print(bool(y))

"""
Most Values are True

Almost any value is evaluated as True if it has some form of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set and dictionary are True, except empty ones.
"""

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# Some Values are False

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# Objects made from __len__ function returns 0 or False

class myclass():
	def __len__(self):
		return 0

myobj = myclass()
print(bool(myobj))

# Functions can Return a Boolean

def myFunction():
	return True

print(myFunction())

def myFunction():
	return True

if myFunction():
	print("YES!")
else:
	print("NO!")

# Check If An Object Is An Integer or Not

x = 200
print(isinstance(x, int))