def cal():
    result = int(input("Enter number: "))

    while True:
        op = input("(+, -, *, /, %, = to exit): ")

        if op == "=":
            print("Final result =", result)
            break

        num = int(input("Enter number: "))

        if op == "+":
            result += num
        elif op == "-":
            result -= num
        elif op == "*":
            result *= num
        elif op == "/":
            result /= num
        elif op == "%":
            result %= num
        else:
            print("Invalid operator")
            continue

        print("=", result)

cal()