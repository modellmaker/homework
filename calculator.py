print("Hi, I'm Your BASIC calculator")

num1 = input("Enter the first number: ")
while True:
    try:
        num1 = int(num1)
    except ValueError:
        print(num1, "not a number.")
        num1 = input("Enter the first number: ")
    else:
        break

num2 = input("Enter the second number: ")

while True:
    try:
        num2 = int(num2)
    except ValueError:
        print(num2, "not a number.")
        num2 = input("Enter the second number: ")
    else:
        break


operation = input("Enter the operand: ")

if operation == "+":
    print("Result: ", num1 + num2)
elif operation == "-":
    print("Result: ", num1 - num2)
elif operation == "*":
    print("Result: ", num1 * num2)
elif operation == "/":
    print("Result: ", num1 / num2)
else:
    print("You didn't provide the right operand.")
