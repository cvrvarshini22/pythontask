d1 = { }
n = int(input("enter how many key-value pairs you want: "))
for i in range(n):
    key = int(input("enter the key(number):"))
    value = int(input("enter the value:"))
    d1[key] = value
print("the dictionary is:", d1)
total = sum(d1.keys())
print("sum of all dictionary values:", total)

