# #add 2 nums
def add_numbers():
    num1= int(input("enter the first value:"))
    num2= int(input("enter the second value:"))
    result=num1+num2
    print(result)
add_numbers()

#name multiple times
def show_name():
    for i in range(10):
        print("Rajnandni")
show_name()

def show_name():
    return "Rajnandni"
print(show_name())

# for i in range(10):
#     show_name()

# #area of rectangle
length=float(input("enter the length:"))
width=float(input("entert the width:"))

area= length*width
print(area)