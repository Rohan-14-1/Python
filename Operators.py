# It can be divided into 6 types:
# 1.	Arithmetic Operators
# 2.	Comparison Operators
# 3.	Logical Operators
# 4.	Assignment Operators
# 5.	Identity Operators
# 6.	Membership Operators
# 7.	Bitwise Operators


#1. Arithmetic operators
a =int(input("enter first number")) + int(input("enter second number"))      #add
b=3-2        #subtract
c=3*2        #multipal
d=8/2        #divided
e=8%3        #reminder
f=13//3       #quotient
g=2**2       #power
print(f"Add: {a}\n subtract: {b}\n multipal: {c}\n divided: {d}\n reminder: {e}\n quotient: {f}\n power: {g}")


# 2.Comparison Operators

# < less than
# > greater than
# = equal to
# !=not equal to
# <= leaa than equalto
# >= greater than equalto

# 3.Logical Operators

a = 3>7 and 3>2     #use of and operator. both are true then only true
print(a)

a = 3>7 or 3>2    # use of OR operator if any one is true then gives true
print(a)

a = 3>7 or 3>2    #use of not just to convert opposite
a = not(a)
print(a)

# 4. Assignment Operators
# = 
# +=
# -=
# *=

# 5. Identity Operators
# Identity operators are used to compare items to see if they are the same object with the same memory address.
#  Types:
# 1.	Is
# 2.	Is not
# Example:
a = 1234
b ="123"                                  
print(a is b)                                               
