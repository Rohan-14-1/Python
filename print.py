#print multiple line in python, we are using triple quotes
print("""Hello, World!
This is a multi-line string in Python.
It can span multiple lines without needing escape characters.""")

#anotherway to print multiple line in python is by using back slaceh \n
print("Hello, World!\nThis is a multi-line string in Python.\nIt can span multiple lines without needing escape characters.")

#Comments in Python:
#  1.single line comment use #. 2.Multiple line comment use ''' '''




# Variables
# .variables are the placeholder, which can store a value. For example:

# Input- A=”hello world”

# Print(a)
a = "hello world"
print(a)

# using f to print two or more than two variable in one line
a="Rohan"
b="Mohan"
print(f"{a} \n {b}")

#USER-INPUT:
#used to take input from user
name = input("Enter your name: ")
print(name)

#use int to take integer input from user
age = int(input("Enter your age: "))
print(age)

#use float to take float input from user
height = float(input("Enter your height in meters: "))  
print(height)

# we can use eval as to solve the equqtion like 2+3=5.
result = eval(input("Enter an expression to evaluate (e.g., 2 + 3): "))
print("The result is:", result)

#TypeCasting and subtyping
# 1. Implicite type conversion
#where python will convert there data type it's self
a=10
b=10.5
print (type(a))
print(type(b))
c=a+b
print(c)
print(type(c))


# 2. Explicit type conversion

a=20
b="Ram"
print(type(a))
print(type(b))
a=str(a)
print(type(a))
c=b+a
print(c)
print(type(c))