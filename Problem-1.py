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

#Write a program to convert float in integer
a=float(input("Enter any decimal number"))
a=int(a)
print(a)

#Write a program to take the details from the student for id-card and then print it in different line.
Name = input("Enter your name ")
Age = int(input("Enter your age "))
Class = int(input("Enter your class "))
Section = input("Enter your section ")
Address = input("Enter your address ")
Cont_No = input("Enter your Contact number ")
print("Name : ",Name)
print("Age : ",Age)
print("Class : ",Class)
print("Section : ",Section)
print("Address : ",Address)
print("Contact number : ",Cont_No)

#Write a program to take user input as a integer and then convert it into float
a=int(input ("enter any number"))
a=float(a)
print(a)