
def is_perfect(n):
    if n < 2:
        return False
    sum_div = 0
    for i in range(1, n):
        if n % i == 0:
            sum_div += i
    return sum_div == n

n = int(input("Enter number of elements in the set: "))
nums = set()
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    nums.add(num)
    print("\nOriginal Set:", nums)


perfect_nums = set()
for num in nums:
    if is_perfect(num):
        perfect_nums.add(num)
print("Perfect Numbers in the Set:", perfect_nums)
