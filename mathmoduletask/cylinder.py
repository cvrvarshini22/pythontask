# cylinder_area_volume.py

import math

r = float(input("Enter the radius of the cylinder: "))
h = float(input("Enter the height of the cylinder: "))

# Formulas
area = (2 * math.pi * r * h) + (2 * math.pi * r ** 2)
volume = math.pi * r ** 2 * h

print("Surface Area of Cylinder =", area)
print("Volume of Cylinder =", volume)
