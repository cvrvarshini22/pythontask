def sum_all(*a):
    print("Sum of numbers:", sum(a))

n = int(input("Enter number of elements: "))
nums = []
count = 1
for i in range(n):
    print("Enter number", count, end=": ")
    num = int(input())
    nums.append(num)
    count = count + 1
sum_all(*nums)

            
    
    
