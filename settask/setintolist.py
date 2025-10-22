n = int(input("How many elements in the set? "))
s = set()
for i in range(n):
    s.add(input("Enter element: "))

lst = list(s)
print("List from Set:", lst)
