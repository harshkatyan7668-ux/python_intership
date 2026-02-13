# Task 4: Calculator Program

# take first number from user
num1 = float(input("Enter first number: "))

# take second number from user
num2 = float(input("Enter second number: "))

# take operator from user
operator = input("Enter operator (+, -, *, /): ")

# check which operation to perform
if operator == "+":
    result = num1 + num2
    print("Result is:", result)

elif operator == "-":
    result = num1 - num2
    print("Result is:", result)

elif operator == "*":
    result = num1 * num2
    print("Result is:", result)

elif operator == "/":
    result = num1 / num2
    print("Result is:", result)

else:
    print("Invalid operator entered")
