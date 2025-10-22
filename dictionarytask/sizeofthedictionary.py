d = {}
count = int(input("Enter the count: "))
for i in range(count):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    d[key] = value
    print(d)

print("Size of the dictionary:", len(d))
