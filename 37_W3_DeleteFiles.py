"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_file_remove.asp
"""

# Delete a File

import os

# os.remove("demofile4.txt")

# Check If File Exist

if os.path.exists("demofile4.txt"):
	os.remove("demofile4.txt")
else:
	print("The file does not exist.")

# Delete Folder

# os.rmdir("Folder")