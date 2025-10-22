# without using split function

d = {}
count = int(input("Enter how many names you want to add: "))

names = []
for i in range(count):
    name = input(f"Enter name {i+1}: ")
    names.append(name)

designation = input("Enter default designation: ")
salary = input("Enter default salary: ")

default = {"designation": designation, "salary": salary}

for name in names:
    d[name] = default
    print(d)

print("Final Dictionary with default values:", d)



#with using split function

d = {}
names = input("Enter names separated by space: ").split()
designation = input("Enter default designation: ")
salary = input("Enter default salary: ")

default = {"designation": designation, "salary": salary}
for name in names:
    d[name] = default
    print(d)

print("Final Dictionary with default values:", d)


