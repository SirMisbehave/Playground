"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_regex.asp
"""

# RegEx Module

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

print("RegEx:", x)

# The findall() Function

txt = "The rain in Spain"
x = re.findall("ai", txt)
print("The findall() Function:", x)

x = re.findall("Portugal", txt)
print("The findall() Function:", x)

# The search() Function

x = re.search("\\s", txt)
print("The first white-space character is located in position:", x.start())

x = re.search("Portugal", txt)
print("The search() Function:", x)

# The split() Function

x = re.split("\\s", txt)
print("The split() Function:", x)

x = re.split("\\s", txt, 1)
print("The split() Function:", x)

# The sub() Function

x = re.sub("\\s", "9", txt)
print("The sub() Function:", x)

x = re.sub("\\s", "9", txt, 2)
print("The sub() Function:", x)

# Search Start and End Position

x = re.search(r"\bS\w+", txt)
print(x.span())
print(x.string)
print(x.group())