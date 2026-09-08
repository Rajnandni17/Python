# # Create a boolean variable and print it.
def variable():
    is_student=True
    has_loging= False
    print(is_student)
    print(has_loging)
variable()

# # Compare two numbers and print the boolean result.
def num():
    a=10
    b=20
    print(a>b)
num()

#  Use bool() on 0, 1, and "Hello".
def num():
    num1=bool(0)
    num2=bool(1)
    num3=bool("hello")
    print(num1)
    print(num2)
    print(num3)
num()

#Check if a number is greater than 50.
def greater():
    number=int(input("enter the value:"))
    if number >50:
        print("greater") 
    else:
       print("not greater")
greater()

#Check if a string is empty or not.
def empty():
    num=bool("")
    print(num)
empty()