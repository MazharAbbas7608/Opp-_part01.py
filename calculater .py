# simple calculater
num1 = int (input("Enter first number"))
num2 = int (input("Enter second number"))
choice = input("Enter the operation[+ - * / %]")
result = 1
if choice == '+' :
    result = num1 + num2
elif choice == '-' :
    result = num1 - num2
elif choice == '*' :
    result = num1 * num2
elif choice == '/' :
    result = num1 / num2
print (result)


