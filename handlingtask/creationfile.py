import os

os.makedirs("C:\\UsersPrograms\\Python\\filehandlingtask", exist_ok=True)
print("Folder created successfully!")

f = open("C:\\UsersPrograms\\Python\\filehandlingtask\\demo.txt", "w")
f.write("Welcome Python students!\nPython is easy to learn!")
f.close()

f = open("C:\\UsersPrograms\\Python\\filehandlingtask\\demo.txt", "r")
print("\nFile content:\n", f.read())
f.close()

