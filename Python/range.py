# #Print numbers from 0 to 9 using range().
def num_range():
    x=range(10)
    print(x)
    print(list(x))
num_range()

#Print numbers from 1 to 10 using range().
def num_range():
    x=range(1,11)
    print(x)
    print(list(x))
num_range()


# #Print even numbers from 2 to 20 using range().
def num_range():
    x=range(2,21,2)
    print(x)
    print(list(x))
num_range()

# #Print odd numbers from 1 to 19 using range()
def num_range():
    x=range(1,20,2)
    print(x)
    print(list(x))
num_range()

#Print the multiplication table of 5 using range().
def table():
    for i in range(1,11):
        print("5 x",i,"=",5*i)
        i+=1
table()

# #Find the sum of numbers from 1 to 100 using range().
def sum_numbers():
    total = 0

    for i in range(1, 101):
        total += i
    print("Sum =", total)
sum_numbers()


# #Print all numbers divisible by 3 from 1 to 30
def divisible_numbers():

    for i in range(1,31):
        if i % 3==0:
            print(i)
divisible_numbers()

#Print squares of numbers from 1 to 10.
def sqr_value():
    for i in range(1,11):
            print(i,"=",i*i)
sqr_value()

#Print a simple star pattern using range().
def tringle_pattern():
    row=5
    for i in range(1,row+1):
        for j in range(i):
            print("*",end=" ")
        print()        
tringle_pattern()

#Write a program to print factorial of a number using loop
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact = fact * i
print("Factorial =", fact)
