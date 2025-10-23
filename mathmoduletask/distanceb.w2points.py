# distance_between_points.py

import math

# Input from user
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Distance formula
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Output
print("\nDistance between two points = ", distance)
