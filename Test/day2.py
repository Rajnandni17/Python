#check whether a num is +ve,-ve, or 0.
num=int(input("enter the num:"))

if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")

#check whether a num is %by 5.
num=int(input("Enter yhe num:"))

if num%5==0:
    print("Divisible")
else:
    print("Not divisible")
 
#Find the largest of 3 nums.
a=int(input("Enter the value1:"))   
b=int(input("Enter the value2:"))
c=int(input("Enter the value3:"))

if a>b and a>c:
    print("value1 is largest:",a)
elif b>a and b>c:
    print("value2 is largest:",b)
else:
    print("value3 is largest:",c)

#Check whether year is a leap year .
year=int(input("Enter year:"))

if year%400==0 or (year%4==0 and year%100 !=0):
    print("Leap year")
else:
    print("Not leap year")
    
#Given marks, print grade a/b/c/d/f using rules u define clearly.
marks=int(input("enter marks:"))

if marks>90:
    print("A")
elif marks>80:
    print("B")
elif marks>60:
    print("C")
elif marks>40:
    print("D")
else:
    print("F")

#check whether a person is eligible for a discount age>=60 or member=yes.
age= int(input("enter age:"))
is_member=True

if age>=60:
    if is_member:
        print("Eligible for discount")
else:
    print("Not eligible for discount")

#Given 3 sides, decide whether they can form a triangle.
a=int(input("Enter value1:"))
b=int(input("Enter value2:"))
c=int(input("Enter value3:"))

if a+b>c and a+c>b and b+c>a:
    print("Triangle")
else:
    print("Not triangle")

