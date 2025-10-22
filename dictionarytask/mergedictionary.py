print("\n dict 1 ")
dict1 = { }
count = int(input("enter the count: "))
for i in range(count):
    key = input("enter the key: ")
    value = input("enter the value: ")
    dict1[key] = value
    print(dict1)
print("\n dict 2")
dict2 = { }
count = int(input("enter the count: "))
for i in range(count):
    key = input("enter the key: ")
    value = input("enter the value: ")
    dict2[key] = value
    print(dict2)
dict1.update(dict2)
print(dict1)
