# #arithemetic operators
a=11
b=2
print("addition:",a+b)
print("subtraction:",a-b)
print("multiplication:",a*b)
print("division:",a/b)
print("floor division:",a//b)
print("modulus:",a%b)

# #comparison operators
a=12
b=11
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)

# #logical operators

a= True
b= False
print(a and b)
print(a or b)
print(not a)

# #ass opera

a=10
b=a
print(b)
b +=a
print(b)
b -=a
print(b)
b *=a
print(b)
b <<=a
print(b)

# #identity opera

a=11
b=12
c=a
print(a is not b)
print(a is c)

# #membership opera
x=55
y=30
my_list=[10,20,30,40,50]

if(x not in my_list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")
if (y in my_list):
    print("y is present in given list")
else:
    print("y is not present in given list")


#ternary operator

a,b=10,20
min = a if a<b else b

print(min)

#precedence operators

expr=10+20*30
print(expr)
name="alex"
age=0

if name=="alex" or name=="john"and age >=2:
    print("hello! welcome.")
else:
    print("good bye!!")

# #associativity opera

# print(55/5*5)
# print(7-5+2)
# print(7- (5+2))
# print(2**3**2)


#Use arithmetic operators on two numbers.
def add():
    a=12
    b=8
    print(a+b)
add()
    
# #Use comparison operators to compare two values.
def name():
    name=input("enter name:")

    if name=="alex":
       print("True")
    else:
        print("False")
name()

#Use logical and to check if a number is between 10 and 100.
def check_num():
    num=int(input("enter value:"))
    
    if num>10 and num<100:
        print("number is btw 10 and 100")
    else:
        print("number is not 10 and 100")
check_num()

#Use logical or to check if a character is a or e.
def check_logic():
    name=str(input("enter the character:"))

    if name== "a" or name== "e":
        print("present")
    else:
        print("not present")
check_logic()

#Use not with a boolean value.
def not_value():
    num=input("enter value:")
    print(not True)
not_value()

