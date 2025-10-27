class School:
    def __init__(self):
        self.name = input("Enter Name: ")
        self.mail = input("Enter Email: ")
        self.mobile = input("Enter Mobile Number: ")
        self.address = input("Enter Address: ")

    def display_school(self):
        print("\n--- School Details ---")
        print("Name       :", self.name)
        print("Email      :", self.mail)
        print("Mobile     :", self.mobile)
        print("Address    :", self.address)


class Staff(School):
    def __init__(self):
        super().__init__()
        self.dept = input("Enter Staff Department: ")

    def display_staff(self):
        print("\n--- Staff Details ---")
        self.display_school()
        print("Staff Department:", self.dept)


class Student(School):
    def __init__(self):
        super().__init__()
        self.std_dept = input("Enter Student Department: ")

    def display_student(self):
        print("\n--- Student Details ---")
        self.display_school()
        print("Student Department:", self.std_dept)


print("Are you Student or Staff?")
choice = input("Enter (student/staff): ")  

if choice == "staff":
    obj = Staff()
    obj.display_staff()

elif choice == "student":
    obj = Student()
    obj.display_student()

else:
    print("Invalid Choice")
