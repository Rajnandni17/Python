# def check_num():
#    num=input("enter value")
#    num=int(num)

#    if num> 0:
#     print("positive")
#    elif num< 0:
#     print("negative")
#    else:
#     print("zero")
# check_num()

#Add two integer numbers
a=13
b=33
z=a+b 
print(z)

def add():
    num1=int(input("value1:"))
    num2=int(input("value2:"))
    result=num1+num2
    print(result)
add()

#Divide two numbers using /(with float value).
a=77
b=7
c=a//b
print(c)

def two_input():
    num1=int(input("enter the value1:"))
    num2=int(input("enter the value2"))
    result=num1/num2
    print(result)
two_input()

#Divide two numbers using //(without float value).
a=99
b=7
c=a//b
print(c)

def two_input():
    num1=int(input("enter the value1:"))
    num2=int(input("enter the value2:"))
    result=num1//num2
    print(result)
two_input()

#Find the remainder using %(remainder).
a=99
b=7
c=a%b
print(c)


def two_input():
    num1=int(input("enter the value1:"))
    num2=int(input("enter the value2:"))
    result=num1%num2
    print(result)
two_input()

#Write a program to calculate the square and cube of a number.
def cal_sqr_cube():
    num=int(input("enter the value:"))

    sqr=num**2
    cube=num**3
    print("sqr=:",sqr)
    print("cube=:",cube)
cal_sqr_cube()                             