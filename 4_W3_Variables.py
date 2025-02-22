"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_variables.asp
"""

"""
Variables are containers for storing data values. Ya know? It's funny, until you read a statement like this, you never think about it completely how true it is and how much it makes sense. Guess that's on me for getting into programming without considering (or knowing for that matter) how ADHD I was. Programming never made sense to me in detail, because I was just told the rules, and I remember all of those specific rules only, but never the concept of what it actually was that I was doing. Hence me going through all of this in pure detail so I can be sure to show my 'mental work' and thought process.

Hopefully, if you read the README file and saw that I type everything out by hand? Now it might sense as to why I force myself to do that, even though it slows me down.

Slow is smooth. Smooth is fast.
"""

# Creating Variables

x = 5
y = "John"
print(x)
print(y)

x = 4 		# x is of type int.
x = "Sally" # x is now of type str.
print(x)

# Casting

x = str(3) 		# x will be '3' (As a string).
y = int(3) 		# y will be 3 (As a integer).
z = float(3) 	# z will be 3.0 (As a float point number which is a number as a decimel).

print(x, y, z)

# Get the Type

x = 5
y = "John"
print("x has a type of:", type(x))
print("y has a type of:", type(y))

# Single or Double Quotes? - Apparently, doesn't matter, but they have to be paired correctly with whichever you choose.

x = "John" # Double Quotes
y = 'John' # Single Quotes
print(x, "was assigned to x using double quotes.")
print("This", y, "was assigned to y using single quotes.")

"""
Now this portion is from memory and not in this section. The purpose of allowing both is so that you can use one to output string, but still include the other set of quotes to emphasize or bring attention to a word in the sentence.
"""

# Case Sensitive

a = 4 		# Lower Case
A = "Sally" # Upper Case
print(a, "was assigned to 'a' as an integer and", A, "was assigned to 'A' as a string.")

# Legal Variable Names

myvar = "John"
print("myvar -", myvar)

my_var = "John"
print("my_var -", my_var)

_my_var = "John"
print("_my_var -", _my_var)

myVar = "John"
print("myVar -", myVar)

MYVAR = "John"
print("MYVAR -", MYVAR)

myvar2 = "John"
print("myvar2 -", myvar2)

# Illegal Variable Names

# 2myvar = "John" # This doesn't work because you can't start a variable with a number.
# my-var = "John" # This doesn't work because you can't use a hyphen.
# my var = "John" # This doesn't work because you can't have a space.

# Multi Word Variable Names - Camel Case

myVariableName = "John" # Camel case being the humps that the capitalisation creates, starting with lower case on the first word.
print("myVariableName is", myVariableName)

# Multi Word Variable Names - Pascal Case

MyVariableName = "John" # Pascal case being each word in the multi word variable having capitalisation.
print("MyVariableName is", myVariableName)

# Multi Word Variable Names - Snake Case

my_variables_name = "John" # Snake case being the swirling shape of a snake created by underscores between each word.
print("my_variables_name is", my_variables_name)

# Many Values to Multiple Variables

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables

x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables

x = "Python is awesome."
print(x) # print() function that we've been using this whole time to output variables, but we're only now getting talking about it. Lol.

# Comma Separated Multi Variable Output

x = "Python"
y = "is"
z = "awesome."
print(x, y, z) # Oh look, I managed to remember this one by memory from somewhere and have been using this too.

# Using the '+' Operator to Output Multiple Variables

x = "Python " 	# Notice the space after 'Python' on this line.
y = "is " 		# Notice the space after 'is' on this line.
z = "awesome."
print(x + y + z)

# '+' Operator Output Without Spaces in the String Variables

x = "Python"
y = "is"
z = "awesome."
print(x + y + z)

# '+' as a Mathematical Operator When Used With Integers

x = 5
y = 10
print("x + y =", x + y)

"""
print() Function Error When Using '+' Operator Between Integer and String

x = 5
y = "John"
print(x + y)

"""

# Output Multiple Variables With Different Data Types Using Commas

x = 5
y = "John"
print("Out of x and y respectively is '", x, y, "'")

# Global Variables

x = "awesome." # x is set globally, as in outside of the function where it will be used/called.

def myfunc():
	print("Python is " + x)

myfunc()

# Use Local Variable to Illustrate Updating the Global Variable

x = "awesome." # x set globally.

def myfunc():
	x = "fantastic." # x set local to function.
	print("x called inside the function: Python is " + x)

myfunc()

print("x called outside of the function: Python is " + x)

# Global Keyword

def myfunc():
	global x # x set locally using 'global' keyword which means it gets set as if set outside the function.
	x = "fantastic."

myfunc()
print("Python is " + x)

# Set Global Variable & Update Variable with 'global' Keyword

x = "awesome." # x set globally.

def myfunc():
	global x # x set locally using 'global' keyword which would update the globally set x.
	x = "fantastic."

myfunc()
print("Python is " + x)