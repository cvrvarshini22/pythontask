d = {}
count = int(input("Enter the count: "))
for i in range(count):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    d[key] = value
    print(d)

keys_to_extract = input("Enter keys to extract (separated by space): ").split()
new_dict = {}

for k in keys_to_extract:
    if k in d:
        new_dict[k] = d[k]

print("New dictionary with extracted keys:", new_dict)
