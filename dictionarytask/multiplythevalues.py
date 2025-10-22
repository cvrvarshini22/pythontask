d = {}
count = int(input("Enter the count: "))
for i in range(count):
    key = input("Enter the key: ")
    value = int(input("Enter the numeric value: "))
    d[key] = value
    print(d)

result = 1
for v in d.values():
    result *= v
print("Multiplication of all values:", result)
