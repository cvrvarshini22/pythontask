from abc import ABC, abstractmethod
class animal(ABC):
    @abstractmethod
    def sound(self):
        print("the animal sound is")
        pass
class lion(animal):
    def sound(self):
        print("the lion is roaring")
class tiger(animal):
    def sound(self):
        print("the tiger is moaning")
a = lion( )
a.sound( )
b = tiger ( )
b.sound( )
