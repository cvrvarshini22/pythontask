# max_number.py

# Input: get numbers from user
numbers = input("Enter numbers separated by spaces: ")

# Convert input string to a list of integers
num_list = [int(n) for n in numbers.split()]

# Find the maximum number using max() function
maximum = max(num_list)

print("The maximum number in the list is:", maximum)
