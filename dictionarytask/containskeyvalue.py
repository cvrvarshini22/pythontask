d = { }
count = int(input("enter the count: "))
for i in range(count):
    key = input("enter the key: ")
    value = input("enter the value: ")
    d[key] = value
    print(d)
if key in d:
    print("the value is exist",d[key])
else:
    print("the value is does not exist",d[key])
