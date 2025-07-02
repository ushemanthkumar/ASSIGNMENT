# Get numbers 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Get operator 
operator = input("Enter operator (+, -, *, /): ")

# Perform calculation 
if operator == '+':
    print("Result:", num1 + num2)
elif operator == '-':
    print("Result:", num1 - num2)
elif operator == '*':
    print("Result:", num1 * num2)
elif operator == '/':
    if num2 == 0:
        print("❌ Any number divided by zero is undefined.")
    else:
        print("Result:", num1 / num2)
else:
    print("❌ Invalid operator. Use +, -, *, or /.")