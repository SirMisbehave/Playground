"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_file_open.asp
"""

# Open a File on the Server

f = open("demofile.txt", "r")
print(f.read())

# Read Only Parts of the File

print(f.read(5))

# Read Lines

print(f.readline())

# Read Two Lines

print(f.readline())
print(f.readline())

# Loop Through the File Line by Line

f = open("demofile.txt", "r")

for x in f:
	print(x)

# Close Files

f = open("demofile.txt", "r")
print(f.readline())
f.close()