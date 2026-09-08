#Create variables of type int, float, str, and bool.
def var():
    a=10
    b=33.7
    c="hello"
    d=True

    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
var()


#Create a list, tuple, set, and dictionary.
def data_type():
    name=["raj","rahul","palak","dev"]
    place=("delhi","lko","panjab")
    team={"rcb","psk","mi"}
    student={
        "name": "raj",
        "model":"human",
        "age":22
    }
    print("list:",name)
    print("tuple:",place)
    print("set:",team)
    print("dict:",student)
data_type()


#Check the type of "100" and 100
def check_type():
    num1="100"
    num2=100
    print(type(num1))
    print(type(num2))
check_type()

#Write a program to display the data type of user input.
def display():
    num=int(input("enter the number:"))
    print("num:",num)
    print(type(num))
display()