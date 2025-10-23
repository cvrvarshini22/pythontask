# combination_without_inbuilt.py

# Function to calculate factorial manually
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

# Take user inputs
n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))

# Formula for combination nCr
nCr = factorial(n) / (factorial(r) * factorial(n - r))

# Output
print("\nCombination (nCr) =", nCr)
