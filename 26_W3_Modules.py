"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_modules.asp
"""

# Use a Module

import mymodule

mymodule.greeting("Jonathan")

# Variables in Module

a = mymodule.person1["age"]
print("Module Person1:", a)

# Re-naming a Module

import mymodule as mx

a = mx.person1["age"]
print("Renamed Module:", a)

# Built-In Modules

import platform

x = platform.system()
print("Platform:", x)

# Using dir() Function

x = dir(platform)
print("dir() Function Platform:", x)