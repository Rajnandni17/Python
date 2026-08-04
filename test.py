#1. Search an element in an array using Linear Search
from array import array

# def linear_search():
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
