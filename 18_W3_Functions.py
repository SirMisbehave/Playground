"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_functions.asp
"""

# Create A Function

def my_function():
	print("Hello from a function.")

# Calling A Function

my_function()

# Arguments

def my_function(fname):
	print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Number of Arguments

def my_function(fname, lname):
	print(fname + " " + lname)

my_function("Emil", "Refnes") # Must Supply Both Arguments, Only Including Will Cause Error

# Arbitrary Arguments - *args

def my_function(*kids):
	print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Keyword Arguments

def my_function(child3, child2, child1):
	print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword Arguments - **kwargs

def my_function(**kid):
	print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# Default Parameter Value

def my_function(country = "Norway"):
	print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a List as an Argument

def my_function(food):
	for x in food:
		print("List as an Argument For Loop:", x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Return Values

def my_function(x):
	return 5 * x

print("Return Value for a Function:")
print(my_function(3))
print(my_function(5))
print(my_function(9))

# Pass Statement

def myfunction():
	pass

# Positional-Only Arguments

def my_function(x, /):
	print("Positional-Only Arguments:", x)

my_function(3)
# my_function(x = 3) # This function call will error because the function contains keyword-only arguments.

# Keyword-Only Arguments

def my_function(*, x):
	print("Keyword-Only Arguments:", x)

my_function(x = 3)
# my_function(3) # This will error out because the function contains positional-only argument.

# Combine Positional-Only and Keyword-Only

def my_function(a, b, /, *, c, d):
	print("Combine Positional and Keyword Only Arguments:", a + b + c + d)

my_function(5, 6, c = 7, d = 8) # Any argument before '/, ' are positional-only and any argument after the '*,' are keyword-only.

# Recursion

def tri_recursion(k):
	if(k > 0):
		result = k + tri_recursion(k - 1)
		print(result)
	else:
		result = 0
	return result

print("Recursion Example Results:")
tri_recusion(6)