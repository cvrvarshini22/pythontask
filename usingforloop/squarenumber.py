numbers = [ ]
for i in range(5):
    num = int(input(f"enter number {i+1}: "))
    numbers.append(num)
print("\n square numbers of the numbers:n")
for n in numbers:
    print(f"{n} sqaured is {n**2}")
