n1 = int(input("Enter number of elements in first set (A): "))
A = set()
for i in range(n1):
    elem = input(f"Enter element {i+1} for first set A: ")
    A.add(elem)


n2 = int(input("Enter number of elements in second set (B): "))
B = set()
for i in range(n2):
    elem = input(f"Enter element {i+1} for second set B: ")
    B.add(elem)


if A.issubset(B):
    print("Set A is a subset of Set B")
else:
    print("Set A is NOT a subset of Set B")


print("Set A:", A)
print("Set B:", B)
