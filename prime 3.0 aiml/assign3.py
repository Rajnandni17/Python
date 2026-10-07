# Ask the user fhttps://github.com/Rajnandni17or a string and check whether it is a palindrome or not.
str=input("enter the string:")
if str==str[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
    
#Given a list of integers compute the average of all numbers in the list
num=[13,54,76,87,12,]

total=sum(num)
count=len(num)

average=total/count

print(" Average =", average)
#Input two lists of integers from the user. Merge them into one list and sort the result.
list1=[1,3,5,8]
list2=[2,4,6,9,3]

list1.extend(list2)
print(list1)


#Given a tuple of integers, create:
#• A tuple of all even numbers
#• A tuple of all odd numbers
num = (13, 54, 76, 87, 12, 9, 20)

even = []
odd = []

for n in num:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

even = tuple(even)
odd = tuple(odd)

print("Even numbers:", even)
print("Odd numbers:", odd)


#Given a list of words:
#words = ["apple", "banana", "kiwi", "cherry", "mango"]
#Create a dictionary that maps each word to its length.
words = ["apple", "banana", "kiwi", "cherry", "mango"]

result = {}

for word in words:
    result[word] = len(word)

print(result)

#Write a program that takes a string from the user and prints the number of spaces in the string
string = input("Enter a string: ")

count = 0

for ch in string:
    if ch == " ":
        count = count + 1

print("Number of spaces:", count)

#Write a program to check whether two lists share no common elements.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

set1 = set(list1)
set2 = set(list2)

common = set1 & set2

if common:
    print("Common elements:", common)
else:
    print("No common elements")