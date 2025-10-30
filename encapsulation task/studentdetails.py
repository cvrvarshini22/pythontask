class Student:
    def __init__(self, name):
        self.__name = name
        self.__grade = [ ]
    def add_grade(self, grade):
        self.__grade.append(grade)
    def get_average(self):
        if len(self.__grade) == 0:
            return 0
        return sum(self.__grade) / len(self.__grade)
    def get_name(self):
        return self.__name
name = input("enter student name: ")
student = Student(name)
n = int(input("enter number of grade: "))
for i in range(n):
    grade = int(input(f"enter grade {i + 1}: "))
    student. add_grade(grade)
print("\n--- Student Details ---")
print("Name: ", student.get_name( ))
print("Average grade: ", student.get_average( ))
