def perfect_num(*a):
    for n in a:
        s = 0
        for i in range(1, n):
            if n % i == 0:
                s = s + i
        if s == n:
            print(n, "is a Perfect Number")
        else:
            print(n, "is not a Perfect Number")

n = int(input("Enter number of elements: "))
nums = []
count = 1
for i in range(n):
    print("Enter number", count, end=": ")
    num = int(input())
    nums.append(num)
    count = count + 1

perfect_num(*nums)
