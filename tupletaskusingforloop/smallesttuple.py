numbers = tuple(map(int, input("Enter numbers separated by space: ").split()))
smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("The smallest number in the tuple is:", smallest)

