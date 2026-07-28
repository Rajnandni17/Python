#Print "Hello World" using Python.
print("hello world")

def hello():
    print("hello world")
hello()

#Print your name and age in one line.
def one_line():
    name=input("enter name")
    age=input("enter age")
    print(name,age)
one_line()

#Print three words separated by commas using sep.
def words():
    w1=input("enter name:")
    w2=input("enter place:")
    w3=input("enter car:")

    print(w1,",",w2,",",w3)
words()

#Print two statements on the same line using end.
def same_line():
    print("raj", end="")
    print("nandni")
same_line()

#Print the result of 10 + 20.
x=10
y=20
z= x + y
print(z)


def add():
    x=10
    y=20
    z=x + y
    print(z)
add()