def calculator(op,a,b):
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "%":
        print(a % b)
    else:
        print("Invalid operator")
while True:
    a=int(input())
    op =input("(+, -, *,/):")
    b=int(input())
    # op =input("(+, -, *,/):")
    calculator(op, a, b)
c=int(input())
op =input("(+, -, *,/):")

calculator(op, a, b,c)


def calculator(op, a=5, b=10):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "%":
        return a % b
    else:
        return "Invalid operator"
def calculator():
    result = int(input())
    
    while True:
        op = input(" (+, -, *, /, %, = to exit): ")

        if op == "=":
            print("Final Result =", result)
            break

        num = int(input())

        if op=="+": result +=num
        elif op=="-":result -=num

        print("=", result)

# calculator()


def cal():
    result=int(input())
    while True:
        op = input(" (+, -, *, /, %, = to exit): ")

        if op=="=":
           print("final result=",result)
           break

        num=int(input())
        if op=="+":result +=num
        elif op=="-":result -=num
        elif op=="*":result *=num
        elif op=="/":result /=num
        else:
            print("Invalid operator")
            continue

        print("=",result)
cal()      