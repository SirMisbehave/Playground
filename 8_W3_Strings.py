"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_strings.asp
"""

# Strings

# 'hello' is the same as "hello"

print('hello')
print("hello")

# Quotes Inside Quotes

print("It's alright.")
print("He is called 'Johnny'.")
print('He is called "Johnny".')

# Assign String to a Variable

a = "Hello"
print(a)

# Multiline Strings - Using Double Quotes

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Multiline Strings = Using Single Quotes

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Strings are Arrays

a = "Hello, World!"
print(a[1])

# Looping Through a String

for x in "banana":
	print(x)

# String Length

a = "Hello, World!"
print(len(a))

# Check String

txt = "The best things in life are free!"

print("free" in txt)

# Check String - If Statement

if "free" in txt:
	print("Yes, 'free' is present.")

# Check If NOT

print("expensive" not in txt)

# Check If NOT - If Statement

if "expensive" not in txt:
	print("No, 'expensive' is NOT present.")

# Slicing Strings

b = "Hello, World!"

print(b[2:5])

# Slice From the Start

print(b[:5])

# Slice To the End

print(b[2:])

# Negative Indexing

print(b[-5:-2])

# Modify Strings

a = "Hello, World!"

print(a.upper()) # Upper Case

print(a.lower()) # Lower Case

# Remove Whitespace

a = " Hello, World! "
print(a.strip())

# Replace String

a = "Hello, World!"
print(a.replace("H", "J"))

# Split String

print(a.split(","))

# String Concatenation

a = "Hello"
b = "World"
c = a + b
print(c)

c = a + " " + b # String Concatenation - Add Space
print(c)

# Format Strings

"""
age = 36
txt = "My name is John, I am " + age # This portion won't work due to differeing data types along with the '+' operator.
print(txt)
"""

# F-Strings

age = 36
txt = f"My name is John, I am {age}"
print(txt)

# Placeholders and Modifiers

price = 59
txt = f"The price is {price} dollars."
print(txt)

txt = f"The price is {price:.2f} dollars." # Display the price with 2 decimals.
print(txt)

txt = f"The price is {20 * 59} dollars."
print(txt)

# Escape Characters

# txt = "We are the so-called "Vikings" from the north." # This will cause an error.
txt = "We are the so-called \"Vikings\" from the north."


# \' 	 - Single Quote
# \\ 	 - Backslash
# \n 	 - New Line
# \r 	 - Carriage Return
# \t 	 - Tab
# \b 	 - Backspace
# \f 	 - Form Feed
# \000 - Octal Value
# \xhh - Hex Value

"""
Strings Methods

All string methods return new values. Original string remains unchanged.
"""

x = "This is a string."

print("capitalize() string method:", x.capitalize()) 			# Converts the first character to upper case.
print("casefold() string method:", x.casefold())				# Converts string into lower case.
print("center() string method:", x.center(20))					# Returns a centered string.
print("count() string method:", x.count("s"))					# Returns the number of times a specified value occurs in a string.
print("encode() string method:", x.encode())					# Returns an encoded version of the string.
print("endswith() string method:", x.endswith("."))				# Returns true if the string ends with the specified value.
print("expandtabs() string method:", x.expandtabs(5))			# Sets the tab size of the string.
print("find() string method:", x.find("is"))					# Searches the string for a specified value and returns the position.
print("format() string method:", x.format())					# Formats specified values in a string.
print("format_map() string method:", x.format_map("T"))			# Formats specified values in a string.
print("index() string method:", x.index("s"))					# Searches the string for a specified value and returns the position of where it was found.
print("isalnum() string method:", x.isalnum())					# Returns True if all characters in the string are alphanumeric.
print("isalpha() string method:", x.isalpha())					# Returns True if all characters in the string are in the alphabet.
print("isascii() string method:", x.isascii())					# Returns True if all characters in the string are ascii characters.
print("isdecimal() string method:", x.isdecimal())				# Returns True if all characters in the string are decimals.
print("isdigit() string method:", x.isdigit())					# Returns True if all characters in the string are digits.
print("isidentifier() string method:", x.isidentifier())		# Returns True if the string is an identifier.
print("islower() string method:", x.lower())					# Returns True if all characters in the string are lower case.
print("isnumeric() string method:", x.isnumeric())				# Returns True if all characters in the string are numeric.
print("isprintable() string method:", x.isprintable())			# Returns True if all characters in the string are printable.
print("isspace() string method:", x.isspace())					# Returns True if all characters in the string are whitespace.
print("istitle() string method:", x.istitle())					# Returns True if the string follows the rules of a title.
print("isupper() string method:", x.isupper())					# Returns True if all characters in the string are upper case.
# print("join() string method:", x.join(("This is"))			# Joins the elements of an iterable to the end of the string.
print("ljust() string method:", x.ljust(5))						# Returns a left justified version of the string.
print("lower() string method:)", x.lower())						# Converts a string into the lower case.
print("lstrip() srting method:", x.lstrip())					# Returns a left trim version of the game.
# print("maketrans() string method:", x.maketrans()) 			# Returns a translation table to be used in translation.
print("partition() string method:", x.partition("is"))			# Returns a tuple where the string is parted into three parts.
print("replace() string method:", x.replace("string", "cat"))	# Returns a string where a specified value is replaced with specific value.
print("rfind() string method:", x.rfind("This"))				# Search the string for specified value and returns the last position.
print("rindex() string method:", x.rindex("h"))					# Search the string for specified value and returns the last position.
print("rjust() string method:", x.rjust(5))						# Returns a right justified version of the string.
print("rpartition() string method:", x.rpartition("is"))		# Returns a tuple where the string is parted into three parts.
print("rsplit() string method:", x.rsplit())					# Splits the string at the specified seperator, and returns a list.
print("rstrip() string method", x.rstrip())						# Returns a right trim version of the string.
print("split() string method:", x.split())						# Splits the string at the specified separator, and returns a list.
print("splitlines() string method:", x.splitlines())			# Splits the string at line breaks and returns a list.
print("startswith() string method:", x.startswith("T"))			# Returns true if the string starts with the specified value.
print("strip() string method:", x.strip())						# Returns a trimmed version of the string.
print("swapcase() string method:", x.swapcase())				# Swaps cases, lower case becomes upper case and vice versa.
print("title() string method:", x.title())						# Converts the first character of each word to upper case.
# print("translate() string method:", x.translate())			# Returns a translated string.
print("upper() string method:", x.upper())						# Converts a string into upper case.
print("zfill() string method:", x.zfill(10))					# Fills the string with a specified number of 0 values at the beginning.