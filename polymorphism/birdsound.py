class Birds:
    def __init__(self,name):
        self.name = name
    def make_sound(self):
        print("This bird makes a sound")
class parrot(Birds):
    def make_sound(self):
        print("parrot says: Hello!")
class sparrow(Birds):
    def make_sound(self):
        print("sparrow says: chirp chirp!")
bird_name = input("enter bird name: ")
if bird_name.lower( ) == "parrot":
    bird = parrot(bird_name)
elif bird_name.lower( ) == "sparrow":
    bird = sparrow(bird_name)
else:
    bird = Birds(bird_name)
print("\n--- Bird Details ---")
print("bird name:", bird.name)
bird.make_sound( )

        
    
