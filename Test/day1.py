#Given a person's age,decide whether they are eligible to vote.
age=int(input("Enter the age:"))

if age>=18:
    print("Eligible")
else:
    print("Not eligible")
    
#Given a num, decide whether it is even/odd.
num=int(input("Enter the num:"))

if num%2==0:
    print("Even")
else:
    print("Odd")
    
#Given 2 num, find the larger num.
a=int(input("Enter num1:"))
b=int(input("Enter num2:"))

if a>b:
    print("Larger:",a)
else:
    print("Larger:",b)

#Given 3 num, find the largest num.
a=int(input("Enter the num1:"))
b=int(input("Enter the num2:"))
c=int(input("Enter the num3:"))

if a>b and a>c:
    print("Largest A:",a)
elif b>a and b>c:
    print("Largest B:",b)
elif c>a and c>b:
    print("Largest C:",c)
else:
    print("All equal")

#Given marks out of 100 , decide Pass/ Fail using 40 as the passing marks.
marks=int(input("Enter marks:"))

if marks>=40:
    print("Pass")
else:
    print("Fail")

#Write the manual step for checking whether a num is divisible by 3 and 5.
num=int(input("Enter the num:"))

if num%3==0 and num%5==0:
    print("Divisible")
else:
    print("Not Divisible")