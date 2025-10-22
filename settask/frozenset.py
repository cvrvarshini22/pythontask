
n = int(input("Enter number of elements in the set: "))
s = set()
for i in range(n):
    elem = input(f"Enter element {i+1}: ")
    s.add(elem)


print("Original Set:", s)
fs = frozenset(s)
print("Frozenset:", fs)


print("\nTrying to add an element to frozenset...")
try:
    fs.add("new")
except AttributeError:
    print("Error: Cannot add elements. Frozensets are immutable!")
