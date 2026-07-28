#calling function
# def fun():
#     print("welcome to home")
# fun()

# #function arguments
# def evenOdd(x):
#     if (x % 2 == 0):
#         return "Even"
#     else:
#         return "Odd"

# print(evenOdd(16))
# print(evenOdd(7))

# #default argument
# def myFun(x,y=50):
#     print("x:",x)
#     print("y:",y)
# myFun(10)

# #keyword arguments
# def student(fname, lname):
#     print(fname, lname)

# student(fname='Geeks', lname='Practice')
# student(lname='Practice', fname='Geeks')

# #positional Arguments
# def nameAge(name, age):
#     print("Hi, I am", name)
#     print("My age is ", age)

# print("Case-1:")
# nameAge("rajnandni", 23)
# print("Case-2:")
# nameAge(23, "rajnandni")

# #function within function
# def f1():
#     s = 'I love panjab'
#     def f2():
#         print(s)
        
#     f2()
# f1()

# #Return Statement

# def sq_value(num):
#     return num**2

# print(sq_value(2))
# print(sq_value(-4))

# #pass by reference and pass by value
# def myFun(x):
#     x[0] = 20

# b = [10, 11, 12, 13]
# myFun(b)
# print(b)

# def myFun2(x):
#     x = 20

# a = 10
# myFun2(a)
# print(a)

#Write a function to print "Hello Python"
def hello_fun():
    print("hello Python")
hello_fun()

#Write a function to add two numbers.
def add_num():
    num1=int(input("enter the value1:"))
    num2=int(input("enter the value2:"))
    print(num1+num2)
add_num()

#Write a function to subtract two numbers
def sub_num():
    num1=int(input("enter value1:"))
    num2=int(input("enter value2:"))
    print(num1-num2)
sub_num()

#Write a function to multiply two numbers.
def multiply_num():
    num1=int(input("enter value1:"))
    num2=int(input("enter value2:"))
    print(num1*num2)
multiply_num()

#Write a function to divide two numbers.
def divide_num():
    num1=int(input("enter the value1:"))
    num2=int(input("enter the value2:"))
    print(num1/num2)
divide_num()

#Write a function to find the square of a number.
def sq_value():
    num=int(input("enter the value1:"))
    print(num**2)
sq_value()

#Write a function to check whether a number is even or odd.
def even_odd():
    num=int(input("enter num:"))
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
even_odd()

#Write a program to find the greatest of two numbers.
def greatest():
    num1=int(input("enter value1:"))
    num2=int(input("enter value2:"))
    if num1>=num2:
        print("greatest")
    else:
        print("not greatest")
greatest()

#Write a function to calculate the area of a rectangle.
def area():
    length=float(input("enter the length:"))
    width=float(input("entert the width:"))
    area= length*width
    print(area)
area()

#Write a function to calculate factorial of a number.
def fact():
    num = int(input("Enter a number: "))
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
        print("Factorial =", fact)
fact()