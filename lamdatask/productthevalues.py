import math

# Take input from user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
num = int(input("Enter the number to multiply with: "))

# Multiply each number using math.prod concept
result = [math.prod([n, num]) for n in numbers]

# Display result
print("Original list:", numbers)
print("After multiplying by", num, ":", result)
