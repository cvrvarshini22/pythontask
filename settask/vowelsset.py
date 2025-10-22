
n = int(input("Enter number of names: "))
names = set()
for i in range(n):
    name = input(f"Enter name {i+1}: ")
    names.add(name)


print("\nNames in the set:", names)


vowels = "aeiouAEIOU"


for name in names:
    count = 0
    for ch in name:
        if ch in vowels:
            count += 1
    print(f"Name: {name} --> Vowels: {count}")
