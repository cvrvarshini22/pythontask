from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        print("The shape area is")
        pass

class circle(shape):
    def area(self):
        r = float(input("Enter radius of the circle: "))
        area = 3.14 * r * r
        print("Area of Circle is:", area)

class triangle(shape):
    def area(self):
        base = float(input("Enter base of the triangle: "))
        height = float(input("Enter height of the triangle: "))
        area = 0.5 * base * height
        print("Area of Triangle is:", area)
        
a = circle()
a.area()

b = triangle()
b.area()
