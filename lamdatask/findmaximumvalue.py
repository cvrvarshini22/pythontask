# Ask how many numbers the user wants to enter
count = int(input("Enter how many numbers you want: "))

# Create an empty list
numbers = []

# Take numbers one by one
for i in range(count):
    num = int(input("Enter number {}: ".format(i + 1)))
    numbers.append(num)

# Find the maximum value manually
max_value = numbers[0]
for n in numbers:
    if n > max_value:
        max_value = n

# Display the result
print("Numbers entered:", numbers)
print("Maximum value is:", max_value)
