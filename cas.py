#Convert an integer to a float.
def change_int(float):
    float=float(input("enter value"))
    print(float)
change_int(float)

#Convert a float to an integer
def change_float(int):
    num=float(input("enter value"))
    print(int(num))
change_float(int)

#Convert an integer to a string
def convert_int():
    num=int(input("enter value: "))
    result=str(num)
    print(result)
convert_int()

#Take two numbers as input and add them using casting.
def add():
    a=int(input("enter num1:"))
    b=int(input("enter num:"))
    c=a+b
    print(c)
    print(type(c))
add()

#Convert "25" into an integer and multiply it by 2.
def change_int():
    num=("25")
    num=int(num)
    result=(num)*2
    print("result:",result)
change_int()