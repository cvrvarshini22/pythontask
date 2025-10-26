import math

class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):
    def area(self, r):
        return math.pi * r * r
    def perimeter(self, r):
        return 2 * math.pi * r

class Triangle(Shape):
    def area(self, b, h):
        return 0.5 * b * h
    def perimeter(self, a, b, c):
        return a + b + c

class Square(Shape):
    def area(self, a):
        return a * a
    def perimeter(self, a):
        return 4 * a

# Example
c = Circle()
print("Circle Area:", c.area(5))
print("Circle Perimeter:", c.perimeter(5))

t = Triangle()
print("Triangle Area:", t.area(6, 4))
print("Triangle Perimeter:", t.perimeter(3, 4, 5))

s = Square()
print("Square Area:", s.area(4))
print("Square Perimeter:", s.perimeter(4))
