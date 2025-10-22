
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


n = int(input("Enter number of elements in the set: "))
nums = set()
for i in range(n):
    elem = int(input(f"Enter element {i+1}: "))
    nums.add(elem)


print("Original Set:", nums)


prime_nums = {x for x in nums if is_prime(x)}
print("Prime Numbers in Set:", prime_nums)
print("Total Prime Numbers:", len(prime_nums))
