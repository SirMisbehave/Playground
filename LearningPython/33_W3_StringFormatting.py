"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_string_formatting.asp
"""

# F - Strings

txt = f"The price is 49 dollars."
print(txt)

# Placeholders and Modifiers

price = 59
txt = f"The price is {price} dollars."
print(txt)

# 2 Decimals

price = 59
txt = f"The price is {price:.2f} dollars."
print(txt)

txt = f"The price is {95:.2f} dollars."
print(txt)

# Perform Operations in F-Strings

txt = f"The price is {20 * 59} dollars."
print(txt)

# Add Taxes Before Displaying the Price

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars."
print(txt)

# If Else Statements

price = 49
txt = f"It is very {'Expensive' if price > 50 else 'Cheap'}"
print(txt)

# Execute Functions in F-Strings

fruits = "apples"
txt = f"I love {fruits.upper()}"
print(txt)

# Function that Converts Feet into Meters

def myconverter(x):
	return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude."
print(txt)

# More Modifiers

price = 59000
txt = f"The price is {price:,} dollars."
print(txt)

# String format()

price = 49
txt = "The price is {:.2f} dollars."
print(txt.format(price))

# Multiple Values

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Index Numbers

myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Referencing Same Value More Than Once

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# Named Indexes

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))