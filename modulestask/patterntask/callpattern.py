# callpattern.py

from righttriangle import righttriangle
from lefttriangle import lefttriangle
from inverserighttriangle import inverserighttriangle
from inverselefttriangle import inverselefttriangle

print("Choose a pattern:")
print("1. Right Triangle")
print("2. Left Triangle")
print("3. Inverse Right Triangle")
print("4. Inverse Left Triangle")

choice = int(input("Enter your choice (1-4): "))
rows = int(input("Enter number of rows: "))

if choice == 1:
    righttriangle(rows)
elif choice == 2:
    lefttriangle(rows)
elif choice == 3:
    inverserighttriangle(rows)
elif choice == 4:
    inverselefttriangle(rows)
else:
    print("Invalid choice")
