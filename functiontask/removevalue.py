def remove_last(**a):
    print("Original Dictionary:", a)
    if a:
        a.popitem()
        print("After Removing Last Key:", a)
    else:
        print("Dictionary is empty.")

n = int(input("Enter number of key-value pairs: "))
d = {}
count = 1
for i in range(n):
    print("Enter key", count, end=": ")
    k = input()
    print("Enter value for", k, end=": ")
    v = input()
    d[k] = v
    count = count + 1

remove_last(**d)
