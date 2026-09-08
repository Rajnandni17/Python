#create a simple calculator using an operator(+,-,*,/).
a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if op == "+":
    print("Answer =", a + b)
elif op == "-":
    print("Answer =", a - b)
elif op == "*":
    print("Answer =", a * b)
elif op == "/":
    print("Answer =", a / b)
else:
    print("Invalid operator")

 #Given three sides, check whether they form a valid triangle and, if valid, classify it as equilateral, isosceles or scalene
a=float(input("Enter 1st value:"))
b=float(input("Enter 2nd value:"))
c=float(input("Enter 3rd value:"))

if a + b > c and a + c > b and b + c > a:
    
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Invalid triangle" )