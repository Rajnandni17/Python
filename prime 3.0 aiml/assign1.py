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

#Evaluate and print the result
x = 10 + 3 * 2 ** 2
print(x)

#Write a program to swap values of two numbers entered by the user.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)

#Ask the user for a temperature in Celsius (string input). Convert it to float ,then calculate and print temperature in Fahrenheit.
celsius=input("Enter temperature in celsius")
celsius= float(celsius)
fahrenheit=(celsius * 9/5)+32
print("Temperature in fahrenheit=", fahrenheit)

#Take the radius (r) as user input and print the area.
radius=int(input("Enter the radius:"))
area= 3.14 * radius ** 2
print("value of area is=",area)

#Ask the user for: Principal (P), Rate (R), Time (T). Convert all to and compute simple interest
P=float(input("Enter p value:"))
R=float(input("Enter r value:"))
T=float(input("enter t value:"))
SI = (P * R * T )/100
print("SI is=",SI)


#Take a decimal number as input (like 45.78 ) and output its: integer part - 45 fractional part - .78
num = float(input("Enter a decimal number: "))

integer= int(num)
fractional= num - integer

print("Integer part =", integer)
print("Fractional part =", fractional)