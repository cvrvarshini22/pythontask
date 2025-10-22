items = [ ]
n = int(input("how many items do you want to enter? "))
for i in range(n):
    item = input(f"enter item {i+1}: ")
    items.append(item)
print("\n Items in reverse orders:")
for i in range(len(items)-1, -1, -1):
    print(items[i])
