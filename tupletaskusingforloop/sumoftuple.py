numbers = tuple(map(int, input("Enter 5 numbers separated by space: ").split()))
total = 0
for num in numbers:
    total += num
print("Sum of tuple elements:", total)
