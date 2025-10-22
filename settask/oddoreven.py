
n = int(input("Enter number of elements in the set: "))

numbers = set()
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.add(num)


print("\nOriginal Set:", numbers)
even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
print("Number of Even Numbers:", len(even_numbers))
print("Number of Odd Numbers:", len(odd_numbers))
