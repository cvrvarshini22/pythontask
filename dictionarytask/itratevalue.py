student = { }
name  = input("enter the name: ")
age = input("enter the age: ")
course = input("enter the course name: ")
student["name"] = name
student["age"] = age
student["course"] = course
print("\n student details: ")
for key, value in student.items( ):
    print(key, ":", value)
