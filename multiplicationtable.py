num = int(input("Enter a number: "))
limit = int(input("Enter the limit: "))

print("\nMultiplication table of", num, "up to", limit)

for i in range(1, limit + 1):
    print(num, "x", i, "=", num * i)

