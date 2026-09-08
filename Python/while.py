#Write a program to print numbers from 1 to 10 using while.
def num_list():
    num=int(input("enter the value:"))

    while num<=10:
        print(num)
        num+=1
num_list()

#Write a program to print numbers from 10 to 1 using while.
def num_list():
    num=int(input("enter the value:"))

    while num>=1:
        print(num)
        num-=1
num_list()

#Write a program to print even numbers from 1 to 20.
def even_num():
    num=int(input("enter the value:"))

    while num<=20:
        if num %2==0:
            print(num)
        num+=1
even_num()

#Write a program to print odd numbers from 1 to 20.
def odd_num():
    num=int(input("enter the value:"))

    while num<=20:
        if num % 2 != 0:
            print(num)
        num+=1
odd_num()

#Write a program to find the sum of numbers from 1 to 10.
def find_sum():
    num=int(input("enter the value:"))

    total=0
    i=1

    while i<=num:
        total +=i
        i += 1
        print(total)
find_sum()


#Write a program to print the multiplication table of a number
def table(n):
    i=1
    while i<=10:
        print(n,"x",i,"=",n*i)
        i+=1
num=int(input("enter the num:"))
table(num)



