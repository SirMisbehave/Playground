"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_file_write.asp
"""

# Write to an Existing File

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

# Open and Read the File After the Appending

f = open("demofile2.txt", "r")
print(f.read())

# Overwrite Content

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# Open and Read the File After the Overwriting

f = open("demofile3.txt", "r")
print(f.read())

# Create a New File

f = open("myfile.txt", "x") # New Empty File Created
f = open("myfile.txt" ,"w") # Create New File If It Does Not Exist