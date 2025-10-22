          
def find_value(*a):
    v = input("Enter value to find: ")
    if v in a:
        print("Value", v, "found.")
    else:
        print("Value", v, "not found.")

n = int(input("Enter number of elements: "))
items = []
count = 1
for i in range(n):
    print("Enter element", count, end=": ")
    val = input()
    items.append(val)
    count = count + 1

find_value(*items)
