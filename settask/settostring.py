n = int(input("Enter number of elements in the set: "))
user_set = set()

for i in range(n):
    item = input(f"Enter element {i+1}: ")
    user_set.add(item)

set_string = ''.join(user_set)

print("Set:", user_set)
print("String from set:", set_string)
