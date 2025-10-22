numbers = tuple(map(int, input("Enter numbers separated by space: ").split()))
product = 1

for num in numbers:
    product *= num

print("The product of all elements is:", product)
