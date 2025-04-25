"""
Author: 	A2Misbehave
Resource: 	W3 Schools - Python
URL:		https://www.w3schools.com/python/python_operators.asp
"""

# Operators

print(10 + 5)

"""
Arithmetic Operators

+ 	- Addition 			- "x + y"
- 	- Subtraction 		- "x - y"
* 	- Multiplication 	- "x * y"
/ 	- Division 			- "x / y"
% 	- Modulus 			- "x % y"
** 	- Exponentiation 	- "x ** y"
// 	- Floor Division 	- "x // y"

Assignment Operators

= 	- x = 5				Same As 	x = 5
+= 	- x += 3 			Same As 	x = x + 3
-=	- x -= 3 			Same As 	x = x - 3
*= 	- x *= 3 			Same As 	x = x * 3
/= 	- x /= 3 			Same As 	x = x / 3
%= 	- x %= 3 			Same As 	x = x % 3
//=	- x //= 3 			Same As 	x = x // 3
**= - x **= 3 			Same As 	x = x ** 3
&= 	- x &= 3 			Same As 	x = x & 3
|= 	- x |= 3 			Same As 	x = x | 3
^= 	- x ^= 3 			Same As 	x = x ^ 3
>>= - x >>= 3 			Same As 	x = x >> 3
<<= - x <<= 3 			Same As 	x = x << 3
:= 	- print(x := 3) 	Same As 	x = 3
									print(x)

Comparison Operators

== 	- Equal 					- "x == y"
!= 	- Not Equal 				- "x != y"
> 	- Greater Than				- "x > y"
< 	- Less Than 				- "x < y"
>=	- Greater Than or Equal To 	- "x >= y"
<= 	- Less Then or Equal To 	- "x >= y"

Logical Operators

and - Returns True if both statements are true 					- "x < 5 and x < 10"
or 	- Returns True if one of the statements is true 			- "x < 5 or x < 4"
not - Reverse the result, returns False if the result is true 	- "not(x < 5 and x < 10)"

Identity Operators

is 		- Returns True if both variables are the same object 		- "x is y"
is not 	- Returns True if both variables are not the same object 	- "x is not y"

Membership Operators

in 		- Returns True if a sequence with the specified value is present in the object 		- "x in y"
not in 	- REturns True if a sequence with the specified value is not present in the object 	- "x not in y"

Bitwise Operators

& 	- AND 					- Sets each bit to 1 if both bits are 1 											- "x & Y"
| 	- OR  					- Sets each bit to 1 if one of two bits is 1 										- "x | y"
^ 	- XOR 					- Sets each bit to 1 if only one of two bits is 1 									- "x ^ y"
~ 	- NOT 					- Inverts all the bits 																- "~x"
<< 	- Zero Fill Left Shift 	- Shift left by pushing zeros in from the right and let the left most bits fall off - "x << 2"
>>  - Signed Right Shift  	- Shift right by pushing copies of the leftmost bit in from the left, and let the 	- "x >> 2"
							  right most bits fall off							  
"""

# Operator Precedence

print((6 + 3) - (6 + 3)) 	# Parenthese has the highest precedence.

print(100 + 5 * 3) 			# Multiplication has a higher precedence than addition.

"""
Operator Precedence In Order - Descending
() 									- Parentheses
** 									- Exponentiation
+x -x ~x 							- Unary Plus, Unary Minus and Bitwise NOT
* / // % 							- Multiplication, Division, Floor Division and Modulus
+ - 								- Addition and Subtraction
<< >> 								- Bitwise Left and Right Shifts
& 									- Bitwise AND
^ 									- Bitwise XOR
| 									- Bitwise OR
== != > >= < <= is is not in not in - Comparisons, Identity and Memberhsip Operators
not 								- Logical NOT
and 								- AND
or 									- OR
"""

# Addition and Subtraction has the same precendence, therefore it is read left to right.

print(5 + 4 - 7 + 3)