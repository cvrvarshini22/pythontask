
matrix = []
print("Enter 2x2 matrix elements:")
for i in range(2):
    row = []
    for j in range(2):
        num = int(input(f"Enter element [{i+1}][{j+1}]: "))
        row.append(num)
    matrix.append(row)
total = 0
for i in range(2):
    for j in range(2):
        total += matrix[i][j]

print("Matrix is:", matrix)
print("Sum of all elements:", total)
