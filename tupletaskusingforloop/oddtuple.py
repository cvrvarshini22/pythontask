numbers = tuple(map(int, input("Enter numbers separated by space: ").split()))
odd_count = 0

for num in numbers:
    if num % 2 != 0:
        odd_count += 1

print("Number of odd values in the tuple:", odd_count)
