print("Hi, I'm Your BASIC calculator")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter the operand: ")

if operation == "+":
    print("Result: ", num1 + num2)
if operation == "-":
    print("Result: ", num1 - num2)
if operation == "*":
    print("Result: ", num1 * num2)
if operation == "/":
    print("Result: ", num1 / num2)
