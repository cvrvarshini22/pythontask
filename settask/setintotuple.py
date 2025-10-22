n1 = int(input("How many elements in the set? "))
s = set()
for i in range(n1):
    s.add(input("Enter element: "))

n2 = int(input("How many elements in the tuple? "))
t = []
for i in range(n2):
    t.append(input("Enter element: "))

set_to_tuple = tuple(s)
tuple_to_set = set(t)

print("Set to Tuple:", set_to_tuple)
print("Tuple to Set:", tuple_to_set)
