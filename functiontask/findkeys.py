def find_key(*a):
    k = input("Enter value to find: ")
    if k in a:
        print("Key", k, "found.")
    else:
        print("Key", k, "not found.")

n = int(input("Enter number of elements: "))
items = []
count = 1
for i in range(n):
    print("Enter element", count, end=": ")
    key = input()
    items.append(key)
    count = count + 1

find_key(*items)
