# sphere_area_volume.py

import math

r = float(input("Enter the radius of the sphere: "))

# Formulas
area = 4 * math.pi * r ** 2
volume = (4 / 3) * math.pi * r ** 3

print("Surface Area of Sphere =", area)
print("Volume of Sphere =", volume)
