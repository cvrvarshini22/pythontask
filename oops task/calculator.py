class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Division by zero not allowed"

# Example
c = Calculator()
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", c.add(a, b))
print("Subtraction:", c.sub(a, b))
print("Multiplication:", c.mul(a, b))
print("Division:", c.div(a, b))
