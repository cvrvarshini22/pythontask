# distance_with_inbuilt.py

import math

# Input from user
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Using inbuilt function
distance = math.dist([x1, y1], [x2, y2])

print("\nDistance between two points =", distance)
