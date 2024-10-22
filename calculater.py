# Simple Calculator

def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    num1 = float(input("Pehla number daalein: "))
    operation = input("Operation daalein (+, -, *, /): ")
    num2 = float(input("Dusra number daalein: "))

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error! Zero se divide nahi kar sakte."
    else:
        return "Invalid operation!"

    return f"Result: {result}"

# Calculator ko run karein
print(calculator())
