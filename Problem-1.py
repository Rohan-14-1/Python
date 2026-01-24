#write a program to display person name, age and adderss in three different line.

name=input("Enter your name : ")
age=int(input("Enter your age: "))
adderess=input("Enter your address: ")
print(f"Name={name}\nage={age}\naddress={adderess}")

#Write the program to swap two variable.
a=10
b=12
a,b=b,a
print(a)
print(b)