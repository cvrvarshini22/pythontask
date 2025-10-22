def even_numbers(*a):
    print("Even numbers are:")
    for n in a:
        if n % 2 == 0:
            print(n, end=" ")

n = int(input("Enter number of elements: "))
nums = []
count = 1
for i in range(n):
    print("Enter number", count, end=": ")
    num = int(input())
    nums.append(num)
    count = count + 1

even_numbers(*nums)
