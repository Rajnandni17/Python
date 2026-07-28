def show_name():
    for i in range(10):
        print("Rajnandni")
show_name()


def show_name():
    return "Rajnandni"
print(show_name())

def divide_num():
    num1=int(input("enter the value:"))
    num2=int(input("enter the value:"))
    answer=0
    while num1>0:
        num1=num1-num2
        answer=answer+1
    print(answer)
divide_num()