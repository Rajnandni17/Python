#write a program that asks the user name and age,then prints in like sentence.
name=input("enter the name:")
age=int(input("enter the age:"))

print("hello",name,",","you are",age,"years old!")

#take two nums as a input from user and print their sum, diff,product,and quotient.
a=int(input("enter the val1:"))
b=int(input("enter the val2:"))

sum= a+b 
diff= a-b
product= a*b
quotient= a//b

print(sum)
print(diff)
print(product)
print(quotient)

#Ask the user to enter two integers and one float. Convert them all to floats and print their average.
a=int(input("enter the val1:"))
b=int(input("enter the val2:"))

a=float(a)
b=float(b)

print(a)
print(b)

#The user enters a string containing a number (e.g."45"). Convert it to:• an integer • a float • a string again print all three values with their types
num=input("enter the num:")

integer=int(num)
float=float(num)
string=str(integer)

print(integer, type(integer))
print(float, type(float))
print(string,type(string))