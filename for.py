#Write a program to print numbers from 1 to 10 using for.
def num():
    for i in range(1,11):
         print(i)   
num()

# #Write a program to print each character of a string
def character():
    for x in "Rajnandni chandra":
        print(x)
character()
   
#Write a program to print all items of a list
def items():
    name=["raju","jai","rishi","tanu"]
    for x in name:
        print(x)
items()

#Write a program to print even numbers from 1 to 20 using for.
def even_num():
    num=int(input("enter the num:"))
    for i in range(2,num+1,2):
        print(i)
even_num()

#Write a program to print odd numbers from 1 to 20 using for.
def odd_num():
    num=int(input("enter the num:"))
    for i in range(1,num+1,2):
        print(i)
odd_num()

#Write a program to find the sum of numbers in a list
def sum_num():
    numbers=[2,3,5,8,5]
    total=0
    for num in numbers:
        total+=num
        print(total)
sum_num()

#Write a program to find the largest number in a list.
def largest():
    number=[45,87,9,17,0,-1]
    largest=number[0]
    for num in number:
        if num >largest:
            largest=num
    print(largest)
largest()

#Write a program to count vowels in a string
def count_vowels():
    V = input("Enter a string: ")
    count = 0

    for ch in V:
        if ch in "aeiouAEIOU":
            print(ch,end=" ")
            count += 1
    print("\nNumber of vowels:", count,)

count_vowels()

#Write a program using nested for loop to print a pattern.
def tringle_pattern():
    row=5
    for i in range(1,row+1):
        for j in range(i):
            print("*",end=" ")
        print()        
tringle_pattern()

#Write a program using break in a for loop.
def break_for():
    fruits=["apple","mango","lichi","chiku"]
    for x in fruits:
        if x ==  "chiku":
            break
        print(x)    
break_for()