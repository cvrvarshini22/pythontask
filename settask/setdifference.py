
n1 = int(input("Enter number of elements in first set: "))
A = set()
for i in range(n1):
    elem = input(f"Enter element {i+1} for first set: ")
    A.add(elem)


n2 = int(input("Enter number of elements in second set: "))
B = set()
for i in range(n2):
    elem = input(f"Enter element {i+1} for second set: ")
    B.add(elem)


difference = A - B


print("First Set:", A)
print("Second Set:", B)
print("Set Difference (A - B):", difference)

