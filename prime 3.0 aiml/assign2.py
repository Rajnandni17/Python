#Write a program that takes as input. Using conditional statements,calculate the final tax rate based on these rules

salary = int(input("Enter your salary: "))

if salary < 30000:
    tax_rate = 5
elif salary <= 70000:
    tax_rate = 15
else:
    tax_rate = 25

print("Final tax rate:", tax_rate, "%")


#Write a function that takes two integers and and prints all even numbers between them (inclusive)
def even(a,b):
    for num in range(a,b+1):
        if num % 2==0:
            print(num)
even(10,20)
    
#Write a function that prints the digits of a number, n
n= int(input("Enter the digits:"))

while n > 0:
    digit= n % 10
    print(digit)
    n=n//10
    
#Write a function to return the count the number of digits in a number,n
n= int(input("Enter the digits:"))
count=0

while n > 0:
    n=n//10
    count +=1
print(count)   

#Write a function to return the sum of digits of a number, n
n= int(input("Enter the digits:"))
total=0

while n > 0:
    digit= n % 10
    total=total+digit
    n=n//10
    
print("sum:",total) 

#Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5

for num in range(1,101):
    if num%3==0 and num%5==0:
        print(num)
