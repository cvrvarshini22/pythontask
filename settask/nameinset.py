

n = int(input("Enter number of names: "))
names = set()
for i in range(n):
    name = input(f"Enter name {i+1}: ")
    names.add(name)


print("Names in the set:", names)

count = 0
for name in names:
    if "ku" in name.lower():
        count += 1

print("Number of names containing 'ku':", count)
