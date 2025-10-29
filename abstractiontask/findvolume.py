from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def volume(self):
        print("The shape volume is")
        pass

class cylinder(shape):
    def volume(self):
        r = float(input("Enter radius of cylinder: "))
        h = float(input("Enter height of cylinder: "))
        v = 3.14 * r * r * h
        print("Volume of Cylinder is:", v)

class cone(shape):
    def volume(self):
        r = float(input("Enter radius of cone: "))
        h = float(input("Enter height of cone: "))
        v = (1/3) * 3.14 * r * r * h
        print("Volume of Cone is:", v)

class sphere(shape):
    def volume(self):
        r = float(input("Enter radius of sphere: "))
        v = (4/3) * 3.14 * r ** 3
        print("Volume of Sphere is:", v)

a = cylinder()
a.volume()

b = cone()
b.volume()

c = sphere()
c.volume()
