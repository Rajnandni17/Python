#take 2 num as i/p & print their sum,diff,* and quotient.
a=int(input("Enter value1:"))
b=int(input("Enter value2:"))

print(a+b)
print(a-b)
print(a*b)
print(a//b)

#take a person's name and age and print a sentence containing both.
name=input("Enter name:")
age=int(input("Enter age:"))

print("Hi my name is",name,"and i am",age,"year old")

#Convert a temperature from Celsius to Fahrenheit 
convert a tem. from celsius to fahrenheit.
celsius=float(input("Enter the celsius value:"))
fahrenheit=(celsius * 9/5)+32

print(fahrenheit)

#given the length and breadth of a rectangle,calculate area and perimeter.
length=float(input("Enter the len:"))
breadth=float(input("Enter the breadth"))

area=length*breadth
perimeter= 2* (length+breadth)

print("Area of rectangle is:",area)
print("perimeter of rectangle is:",perimeter)

#given total marks in 5 sub ,calculate total and percentage.
sub1=float(input("Enter the marks of sub1:"))
sub2=float(input("Enter the marks of sub2:"))
sub3=float(input("Enter the marks of sub3:"))
sub4=float(input("Enter the marks of sub4:"))
sub5=float(input("Enter the marks of sub5:"))

total=sub1 + sub2 + sub3 + sub4 + sub5
percentage=(total/500) * 100

print("Total marks of subjects is:",total)
print("Percentage =",percentage)

#swap 2 variables without using 3rd variable.
a=int(input("Enter 1st value:"))
b=int(input("Enter 2nd value:"))

a,b=b,a
print("After swapping:")
print("a=", a)
print("b=",b)

#given a number ,print its square and cube.
n=int(input("Enter a number:"))

print("Square=", n**2)
print("Cube=", n**3)

#take a num and determine whether it is divisible by both 2 and 3.
n=int(input("Enter number:"))

if n%2==0 and n%3==0:
    print("Divisible")
else:
    print("Not divisible")