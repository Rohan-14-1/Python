#write a program to display person name, age and adderss in three different line.

name=input("Enter your name : ")
age=int(input("Enter your age: "))
adderess=input("Enter your address: ")
print(f"Name={name}\nage={age}\naddress={adderess}")

#Write the program to swap two variable.

#without using tem veriable
a=10
b=12
a,b=b,a
print(a)
print(b)

#Using tempory variable

a = 12
b = 13
temp = a
a=b
b=temp
print(a)
print(b)

#Write a program to convert float in integer
a = float(input("Enter a number "))
a = int(a)
print(a)
print(type(a))