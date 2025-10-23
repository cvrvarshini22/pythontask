# arc_length.py

import math

r = float(input("Enter the radius of the circle: "))
angle = float(input("Enter the angle (in degrees): "))

# Formula: L = 2πr × (angle / 360)
arc_length = 2 * math.pi * r * (angle / 360)

print("Arc length of the circle =", arc_length)

