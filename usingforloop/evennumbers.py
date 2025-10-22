numbers = [ ]
for i in range(8):
    num = int(input(f"enter number {i+1}: "))
    numbers.append(num)
even_num = 0
for n in numbers:
    if n % 2 == 0:
        even_num += 1
print("\n number of even numbers: ", even_num)
