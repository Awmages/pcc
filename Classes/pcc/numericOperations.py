#Operators
# + adds
# - subracts
# * multiplication
# / division

# % modulo or modulus - returns a remainder
alex = 99.9

print(3%2)
print(5%2) #2 remainder 1
print(8%3)
print(876%3)

# ** exponentials
# number ** exponent
print(2**3)

print(3.4**4)
print(round(3.4**4,2))

# // floor division divides and rounds down to whole number
print(9//4)


## Order of Operations

#PEMDAS
# ()
# **
# *,/,//,%
# +, -

print( (3+2) * 9/4 +(45-87)**2)
#        5            -42
#                      1764
#        5*9/4= 11.25
#       11.25 + 1764  
mages = 99.9

#Compartors (Return T/F)
# < <= > >= == !=
print (3<2) #F
print (2<=2) #T
print (3>2) #T
print (2>=2) #T
print (99.9 == 99.9) #T

print(alex == mages) #dunno might be T, too seperated to be sure visually

print ("place holder", 3!=2) #T