
numbers = tuple(map(int, input("Enter 6 numbers separated by space: ").split()))
print("Even numbers in the tuple:")
for num in numbers:
    if num % 2 == 0:
        print(num)
