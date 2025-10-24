# A lambda that multiplies two arguments
multiply = lambda x, y: x * y

# Get input from the user
a = float(input("Enter x: "))
b = float(input("Enter y: "))

# Call the lambda and print the result
result = multiply(a, b)
print("Result:", result)
