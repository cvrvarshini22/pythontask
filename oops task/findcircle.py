import math

class Circle:
    def area(self, r):
        return math.pi * r * r

    def perimeter(self, r):
        return 2 * math.pi * r

# Example
c = Circle()
r = float(input("Enter radius of circle: "))
print("Area of Circle:", c.area(r))
print("Perimeter of Circle:", c.perimeter(r))
