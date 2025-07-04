import math

print("operators: +  -  *  /  sin  cos  tan  cot  sec  cosec")

operator = input("Enter operator: ")

if operator in ['+', '-', '*', '/']:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      
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

elif operator in ['sin', 'cos', 'tan', 'cot', 'sec', 'cosec']:
    angle = float(input("Enter angle in degrees: "))

    if operator == 'sin':
        print("Result:", math.sin(angle))
    elif operator == 'cos':
        print("Result:", math.cos(angle))
    elif operator == 'tan':
        print("Result:", math.tan(angle))
    elif operator == 'cot':
        print("Result:", 1 / math.tan(angle))
    elif operator == 'sec':
        print("Result:", 1 / math.cos(angle))
    elif operator == 'cosec':
        print("Result:", 1 / math.sin(angle))
else:
    print("❌ Invalid operation: ")
