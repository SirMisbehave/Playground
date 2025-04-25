"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_modules.asp
"""

# Dates

import datetime

x = datetime.datetime.now()
print("Date Time:", x)

# Date Output

print("Date Output Year:", x.year)
print("Date Output Day:", x.strftime("%A"))

# Creating Date Objects

x = datetime.datetime(2020, 5, 17)
print("Creating Date Objects:", x)

# strftime() Method

x = datetime.datetime(2018, 6, 1)
print("strftime():", x.strftime("%B"))

"""
Legal format Code

Directive 	Description 							Example
%a 			Weekday, Short Version 					- Wed
%A 			Weekday, Full Version 					- Wendesday
%w 			Weekday as a Number 0-6, 0 is Sunday 	- 3
%d 			Day of Month 01-31						- 31
%b 			Month Nane, Short Version				- Dec
%B 			Month Name, Full Version				- December
%m 			Month as a Number 01-12 				- 12
%y 			Year, Short Version, With Century 		- 18
%Y 			Year, Full Version 						- 2018
%H 			Hour 00-23 								- 17
%I 			Hour 00-12 								- 05
%p 			AM/PM 									- PM
%M 			Minute 00-59 							- 41
%S 			Second 00-59 							- 08
%f 			Microsecond 0000000-999999 				- 548513
%z 			UTC Offset 								- +0100
%Z 			Timezone 								- CST
%j 			Day Number of Year 001-366 				- 365
%U 			Week Number of Year,					- 52
			Sunday as the First Day of Week,
			00-53
%W 			Week Number of Year, 					- 52
			Monday as the First Day of Week,
			00-53
%C 			Century 								- 20
%x 			Local Version of Date 					- 12/31/18
%X 			Local Version of Time 					- 17:41:00
%% 			A % Character 							- %
%G 			ISO 8601 Year 							- 2018
%u 			ISO 8601 Weekday (1 - 7) 				- 1
"""