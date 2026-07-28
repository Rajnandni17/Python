#Create a variable name and print it.
name=input("enter name:")
print(name)

def name():
    name=input("enter your name:")
    print(name)
name()

#Create variables name, age, and city.
name=input("name:rajandni")
age=input("age:22")
city=input("city:varindavan")

def user():
    name=input("enter name:")
    age=input("enter age:")
    city=input("enter city:")
    print(name)
    print(age)
    print(city)
user()

#Assign the same value to three variables.
x=10
y=10
z=10
print(x)
print(y)
print(z)

def same_value():
    num1=input("enter value1:")
    num2=input("enter value2:")
    num3=input("enter value3:")
    print(num1)
    print(num2)
    print(num3)
same_value()

#Assign different values to three variables in one line.

x=10
y=20
z=30
print(x,y,z)

def value():
    num1=input("enter value1:")
    num2=input("enter value2:")
    num3=input("enter value3:")
    print(num1,num2,num3)
value()

#Swap values of two variables.
x=12
y=33
temp= x
x=y
y=temp
print("x=",x)
print("y=",y)


def swap():
    a=input("enter value a:")
    b=input("enter value b:")
    a,b=b,a
    print("a=",a)
    print("b=",b)
swap()
