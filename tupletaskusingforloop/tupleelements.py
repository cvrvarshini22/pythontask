user_input = input("Enter numbers separated by commas: ")  

# Convert input into a tuple
t = tuple(map(int, user_input.split(',')))

# Print all elements using a loop
print("Tuple elements are:")
for element in t:
    print(element)
