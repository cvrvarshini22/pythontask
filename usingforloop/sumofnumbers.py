numbers = [ ]
for i in range(5):
    num = int(input(f"enter the number {i+1}: "))
    numbers.append(num)
total = 0
for n in numbers:
    total += n
print("\n The sum of the number is:", total)
