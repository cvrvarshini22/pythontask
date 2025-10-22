def find_value_key(**a):
    k = input("Enter key to find value: ")
    if k in a.keys():
        print("Value for", k, "is:", a[k])
    else:
        print("Key not found.")

n = int(input("Enter number of key-value pairs: "))
d = {}
count = 1
for i in range(n):
    print("Enter key", count, end=": ")
    key = input()
    print("Enter value for", key, end=": ")
    val = input()
    d[key] = val
    count = count + 1

find_value_key(**d)
