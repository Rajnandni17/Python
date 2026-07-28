# from array import array

#Print all elements using a for loop.
def arr_forloop():
    num=[100,30,27,78,90]
    for i in num:
        print(i)
arr_forloop()

#Find the sum of all elements.
def sum_ele():
    arr=[30,50,26,78,44]
    total=0
    for i in arr:
        total+=i
    print("sum=",total)
sum_ele()

#Find the largest element.
def largest():
    arr=[44,88,76,21,90]
    largest=arr[0]
    for i in arr:
        if i > largest:
            largest=i
    print("largest=",largest)
largest()

#Find the smallest element
def smallest():
    arr=[44,88,76,21,90]
    smallest=arr[0]
    for i in arr:
        if i < smallest:
            smallest=i
    print("smallest=",smallest)
smallest()

#Count even and odd numbers
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

#Search for an element.
def element():
    arr=[12,34,66,87,39]

    num=int(input("enter the search  element:"))
    if num in arr:
        print("found")
    else:
        print("not found")
element()

#Reverse the array.
def reverse():
    arr=[41,67,32,5,91,11]
    arr.reverse()
    print(arr)
reverse()

# #Sort the array in ascending order
def ascending():
    arr=[89,94,11,2,65,14,33]
    arr.sort()
    print(arr)
ascending()

#Find the second largest element.
def second_largest():
    arr=[44,88,76,21,90]
    largest=second=arr[0]
    for num in arr:
        if num > largest:
            second=largest
            largest=num
        elif num > second and num !=largest:
            second=num
    print(arr)
    print("largest=",largest)
    print(second)
second_largest()

arr = array('i', [10, 20, 30, 40, 50])

base_address = arr.buffer_info()[0]

print("Base Address:", base_address)

arr = array('i', [10, 20, 30, 40, 50])

print("Size of one element:", arr.itemsize, "bytes")
print("Number of elements:", len(arr))
print("Total memory:", arr.itemsize * len(arr), "bytes")

import sys
s="abc"
size=sys.getsizeof(s)
print("Total memory:", size, "bytes")

#Count the frequency of a given element in an array.
def fre_count():
    arr=[12,3,11,2,11,4,11]
    target = 11
    count=0
    for num in arr:
        if num== target:
            count +=1
    print("fre=",count)
fre_count()

#Find the first occurrence of a given element
def first_occu():
    arr=[10,2,6,2,5,2,9,2]
    target= 2

    for i in range(len(arr)):
        if arr[i]==target:
             print("found at index:=",i)
             return
    print("element not found")
first_occu()

#Find the last occurrence of a given element
def last_occu():
    arr=[10,2,6,2,5,2,9,2]
    target= 2

    for i in range(len(arr) -1,-1,-1):
        if arr[i]==target:
             print("last occurrence found at index:=",i)
             return
    print("element not found")
last_occu()

#Insert an element at a given index.
def insert_element():
    arr = [10, 20, 30, 40]
    element = 11
    index = 5

    arr.insert(index, element)

    print(arr)

insert_element()

#Delete an element from a given index.
def insert_element():
    arr = [10, 20, 30, 40]
    index = 3

    arr.pop(index)

    print(arr)

insert_element()

#Remove duplicate elements from an array.
def remove_duplicate():
    arr=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,]
    unique=[]
    
    for num in arr:
        if num not in unique:
            unique.append(num)
    
    print(unique)
remove_duplicate()

# #Merge two sorted arrays into a single sorted array.
def merge_array():
    arr1 = [1,2,3,4,5]
    arr2 = [6,7,8,9]

    arr3 = arr1 + arr2

    arr3.sort()

    print(arr3)
merge_array()

#Move all zero elements to the end of the array while maintaining the order of non-zero elements.
def move_zero():
    arr=[11,0,32,0,56,0,0,23]

    result=[]
    zero_count=0

    for num in arr:
        if num ==0:
            zero_count +=1
        else:
            result.append(num)
    for i in range(zero_count):
        result.append(0)
    print(result)
move_zero()


def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)
print("Sorted array:", my_array)
