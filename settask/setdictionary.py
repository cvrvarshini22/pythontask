
n = int(input("Enter number of elements: "))
s = set()
for i in range(n):
    s.add(input(f"Enter element {i+1}: "))

d = {value: index for index, value in enumerate(s)}
print("Set:", s)
print("Converted Dictionary:", d)
