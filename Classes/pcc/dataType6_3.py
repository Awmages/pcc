##Data Types

#there are numerous data types in programming. Each has it's own purpose and functions use one, some, or all data types.

#in VS code each data type is color coded
"strings are this color"

#string in any computer programming language, a string sequence of chars used to represent text
#strings are noted by " or '.

print("The cowboy told barkeep 'there's a snake in my boot' ")

# The stament below has improper opening/closing quotes
# print('The cowboy told barkeep 'there's a snake in my boot' ')

print('The cowboy told barkeep' + "there's a snake in my boot")

# Triple-Double Quote Technique """ """

print(""" The student quoted their teacher saying "my old teacher told us 'don't not use double negatives as my professor was quoted saying 'DON'T DO IT!''" """)

#Integer
#whole number -77832, 0, 938283
#can do math with integers
print(3*245)
print(838-999)

#Floats (floating decimal)
#number with a decimal
# 8.1, -92.765009
#can do math on floats (+,-,/,*,**,sqrt,fact)
print(2.5*3)

#values will start to get rounding errors
print(8.3 * 33)

#NEW FUNCTION TIME
#round(number, numberOfDecimals)
numbers= 8.3 * 33
print(round(numbers,2))

print(round(2.92933,2))

#Boolean
#True or False
print(10>1)
print(2 < 1)

#NEW FUNCTION TIME
#type(arg) arg = string, integer, float, function, anything
#it tells you the type of the arg (i.e., is a string, integer, float)

type(8.3)
print(type(8.3))
print(type('sentece'))

#NEW FUNCTION TIME
#int(value) forces a value into the interger data type
#float(value) forces a value into the float data type

print(int(3.2))
print(int("9"))

print(float('3.2'))
print(int(float('3.2')))
# string "3.2" -> float 3.2 -> int 3