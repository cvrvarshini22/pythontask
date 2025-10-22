
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


print("First Set (A):", A)
print("Second Set (B):", B)


A.difference_update(B)


print("After removing intersection of 2nd set from 1st set:", A)
