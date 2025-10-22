def calculator(a, b, op):
    if op == '+':
        print("Result:", a + b)
    elif op == '-':
        print("Result:", a - b)
    elif op == '*':
        print("Result:", a * b)
    elif op == '/':
        if b != 0:
            print("Result:", a / b)
        else:
            print("Division by zero not allowed.")
    else:
        print("Invalid operator")

print("Enter first number:", end=" ")
x = float(input())
print("Enter second number:", end=" ")
y = float(input())
print("Enter operator (+, -, *, /):", end=" ")
o = input()

calculator(x, y, o)
