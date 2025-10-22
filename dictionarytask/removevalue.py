d = {}
count = int(input("Enter the count: "))
for i in range(count):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    d[key] = value
    print(d)

remove_key = input("Enter the key to remove: ")
if remove_key in d:
    del d[remove_key]
    print("Updated dictionary:", d)
else:
    print("Key not found.")
