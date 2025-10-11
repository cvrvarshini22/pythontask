rows = int(input("enter the number of rows: "))
for i in range(rows):
    print(" " * (rows - i - 1), end = (" "))
    print("*" * (2 * i + 1))
          
