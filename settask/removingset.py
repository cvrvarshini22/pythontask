
n = int(input("Enter number of elements in the set: "))
my_set = set()
for i in range(n):
    elem = input(f"Enter element {i+1}: ")
    my_set.add(elem)

print("Original Set:", my_set)
my_set.clear()

print("After removing all elements:", my_set)
