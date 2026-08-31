#1. Search an element in an array using Linear Search
from array import array

def linear_search():
    arr = array('i', [10, 20, 30, 40, 50])

    key = int(input("Enter element to search: "))

    found = False

    for i in range(len(arr)):
        if arr[i] == key:
            print("Element Found at Index:", i)
            found = True
            break

    if not found:
        print("Element Not Found")

linear_search()

#Count how many times an element appears
def count_occurrence():
    arr = array('i', [10, 20, 30, 20, 40, 20])

    key = int(input("Enter element to count: "))

    count = 0

    for num in arr:
        if num == key:
            count += 1

    print(key, "appears", count, "times")

count_occurrence()

#Check whether an element exists in the array
def element():
    arr=[12,34,66,87,39]

    num=int(input("enter the search  element:"))
    if num in arr:  
        print("found")
    else:
        print("not found")
element()

#Count even and odd numbers.
def Count_even_odd():
    arr = array('i', [22, 68, 73, 99, 3])

    even = 0
    odd = 0

    for num in arr:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    print("Array:", arr)
    print("Even Count:", even)
    print("Odd Count:", odd)

Count_even_odd()


#Print your name, age and city.
name=input("enter your name:")
age=input("enter your age:")
city=input("enter your city:")

print(name)
print(age)
print(city)

#Take two numbers as input and print their sum, difference, product and division.
a=11
b=2

print(a+b)
print(a-b)
print(a*b)
print(a/b)

#Swap two numbers with and without using a third variable.
a=11
b=2

a,b=b,a

print("a=",a)
print("b=",b)

#Check whether a number is positive, negative or zero
def num():
    n=int(input("enter the num:"))

    if(n>0):
        print("positive")
    elif(n<0):
        print("negative")
    else:
        print("zero")
num()

#Check whether a number is even or odd
def check_num():
    n=int(input("enter num:"))

    if n %2==0:
        print("num is even")
    else:
        print("num is odd")
check_num()

#Find the greatest of two numbers.
def greatest():
    n1=int(input("enter the num:"))
    n2=int(input("enter the num:"))
    if n1 > n2:
        print(n1, "is greatest")
    elif n2 > n1:
        print(n2, "is greatest")
    else:
        print("Both numbers are equal")

greatest()

#Check whether a year is a leap year.
def leap_year():
    year = int(input("Enter year: "))
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("Leap year")
    else:
        print("Not a leap year")
leap_year()

#Find the greatest of three numbers
def greatest():
    n1=int(input("enter the num:"))
    n2=int(input("enter the num:"))
    n3=int(input("enter the num:"))
    if n1 > n2 or n1 > n3:
        print(n1, "is greatest")
    elif n2 > n1 or n2 > n3:
        print(n2, "is greatest")
    elif n3 > n1 or n3 > n2:
        print(n3, "is greatest")
    else:
        print("all numbers are equal")
greatest()

#Check whether a number is divisible by both 5 and 11.
def num_divisible():
    num=int(input("enter the num:"))

    if num %5==0 and num %11 ==0:
        print("num is divisible")
    else:
        print("not divisible")
num_divisible()

#Build a basic calculator using conditions
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", a + b)

elif operator == "-":
    print("Result:", a - b)

elif operator == "*":
    print("Result:", a * b)

elif operator == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid operator")

#Calculate the factorial of a number
def fact_num():
    num=int(input("enetr the num:"))
    factorial=1

    for i in range(1,num+1):
        factorial= factorial * i
    print(factorial)
fact_num()


#Print the multiplication table of a number
def fact_num():
    num=int(input("enetr the num:"))

    for i in range(1,11):
        print(num,"*", i,"=", num * i )
fact_num()

#Find the sum of numbers from 1 to n
def sum_num():
    n=int(input("enter the num:"))
    total= 0

    for i in range(1,n+1):
        total= total + i
    print("sum =",total)
sum_num()

#Count the number of digits in an integer.
def count():
    num = int(input("Enter a number: "))
    count =0

    while num > 0:
        count +=1
        num //=10
    print(" number of digits =", count)
count()

#Find the sum of digits of a number.
def sum_digits():
    num = int(input("Enter a number: "))
    total =0
    
    while num > 0:

        digit = num % 10
        total = total + digit
        num //= 10
    print("sum =",  total)
sum_digits()

#Reverse an integer
def reverse():
    num=int(input("enetr the number:"))
    reverse=0

    for i in str(num):
        digit= num %10
        reverse= reverse * 10 + digit
        num //=10
    print("integer =",reverse)
reverse()

#Check whether a number is prime.
def prime_num():
    num=int(input("enter the number:"))
    count=0

    for i in range(1,num +1):
        if num % i ==0:
            count= count +1
    if count == 2:
        print("number is prime.")
    else:
        print("number is not prime.")
prime_num()       

#Check whether a number is a palindrome.
def check_palindrome():
    num = input("Enter a number: ")

    
    if num == num[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
check_palindrome()


#Print all prime numbers within a given range
def prime_num():
    start= int(input("enter start number:"))
    end=int(input("enter end:"))
    
    for num in range(start,end +1):
        if num > 1:
            count=0
            for i in range(1,num +1):
                if num % i ==0:
                    count +=1
            if count == 2:
                print(num)
prime_num()

#Print the Fibonacci sequence up to n terms.
def Fibonacci():
    n=int(input("enter number of terms:"))

    a=0
    b=1

    for i in range(n):
        print(a, end=" ")
    
        c=a+b
        a=b
        b=c
Fibonacci()


