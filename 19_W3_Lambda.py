"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_lambda.asp
"""

"""
Syntax

lambda arguments : expression
"""

# Example - Add 10 to argument 'a', and return the result.

x = lambda a : a + 10
print("Lambda Function:", x(5))

# Lambda functions can take any number of arguments.

# Multiply argument 'a' with argument 'b' and return the result.

x = lambda a, b : a * b
print("Multi-Argument Lambda Function:", x(5, 6))

# Summarize argument 'a', 'b' and 'c' and return the result.

x = lambda a, b, c : a + b + c
print("Summarise Argument Lambda Function:", x(5, 6, 2))

# Lambda Functions as Return Arguments

def myfunc(n):
	return lambda a : a * n

# Doubler Function

def myfunc(n):
	return lambda a : a * n

mydoubler = myfunc(2)
print("Doubler Lambda Function:", mydoubler(11))

# Tripler Function

def myfunc(n):
	return lambda a : a * n

mytripler = myfunc(3)
print("Tripler Lambda Function:", mytripler(11))