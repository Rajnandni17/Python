#Write a program to check whether a number is positive.
# def check_num():
#     num=int(input("enter number:"))

#     if num >0:
#         print("positive")
#     else:
#         print("not positive")
# check_num()

#Write a program to check whether a number is negative or positive.
def check_num():
    num=int(input("enter number:"))

    if num >0:
        print("positive")
    elif num<0:
        print("negative")
    else:
        print("zero")
check_num()

#Write a program to check whether a number is even or odd
def check_even_odd():
    num=int(input("enter value:"))

    if num%2==0:
        print("even")
    else:
        print("odd")
check_even_odd()

#Write a program to check whether a person is eligible to vote.
def check_age():
    age=int(input("enter age:"))

    if age>18:
        print("eligible")
    else:
        print("not eligible")
check_age()

#Write a program to find the greatest of two numbers.
def greatest():
    num1=int(input("enter value1:"))
    num2=int(input("enter value2:"))

    if num1>=num2:
        print("greatest")
    else:
        print("not greatest")
greatest()

#Write a program to find the greatest of three numbers.
def greatest():
    num1=int(input("enter value1:"))
    num2=int(input("enter value2:"))
    num3=int(input("enter value2:"))

    if num1>=num2>=num3:
        print("greatest")
    else:
        print("not greatest")
greatest()

#Write a program to check whether a number is divisible by 5.
def check_divisible():
    num=int(input("enter the value:"))

    if num/5:
        print("divisible")
    else:
        print("not divisible")
check_divisible()

#write a program to check whether a student passed or failed.
def check_marks():
    num=int(input("enter the marks:"))

    if num>30:
        print("passed")
    else:
        print("failed")
check_marks()


#Write a program to assign grades based on marks.
def assign_grades():
    num=int(input("enter the marks:"))

    if num>80:
        print("grade A")
    elif num>60:
        print("grade B")
    else:
        print("grade C")
assign_grades()

#Write a program using nested if to check username and password.
  