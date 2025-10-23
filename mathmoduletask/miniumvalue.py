# min_in_dict.py

# Create an empty dictionary
data = {}

# Get number of key-value pairs
n = int(input("Enter number of items in the dictionary: "))

# Take user input for key-value pairs
for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = int(input(f"Enter value for {key}: "))
    data[key] = value

# Find the minimum value
min_value = min(data.values())

# Find the key(s) corresponding to the minimum value
min_keys = [k for k, v in data.items() if v == min_value]

print("\nDictionary:", data)
print("Minimum value in the dictionary is:", min_value)
print("Key(s) with the minimum value:", min_keys)
