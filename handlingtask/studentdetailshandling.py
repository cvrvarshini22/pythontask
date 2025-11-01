# student_file_handling.py

def store_student_details():
    f = open("students.txt", "a")  # append mode
    n = int(input("Enter number of students: "))
    for i in range(n):
        print(f"\nEnter details for student {i+1}:")
        name = input("Enter name: ")
        mobile = input("Enter mobile: ")
        age = input("Enter age: ")
        mail = input("Enter mail: ")
        f.write(f"{name},{mobile},{age},{mail}\n")
    f.close()
    print("\n Student details stored successfully!\n")


def retrieve_student_details():
    try:
        f = open("students.txt", "r")
        print("\n Student Details:\n")
        for line in f:
            name, mobile, age, mail = line.strip().split(",")
            print(f"Name: {name}, Mobile: {mobile}, Age: {age}, Mail: {mail}")
        f.close()
    except FileNotFoundError:
        print("\n No student data found! Please store details first.\n")


def count_students():
    try:
        f = open("students.txt", "r")
        count = sum(1 for _ in f)
        f.close()
        print("\n Total number of students:", count, "\n")
    except FileNotFoundError:
        print("\n No student data found! Please store details first.\n")


def students_age_greater_25():
    try:
        f = open("students.txt", "r")
        print("\n Students with age greater than 25:\n")
        found = False
        for line in f:
            name, mobile, age, mail = line.strip().split(",")
            if int(age) > 25:
                print(name)
                found = True
        f.close()
        if not found:
            print("No students found with age greater than 25.")
    except FileNotFoundError:
        print("\n No student data found! Please store details first.\n")


def students_name_starts_with_A():
    try:
        f = open("students.txt", "r")
        print("\n Students whose name starts with 'A':\n")
        found = False
        for line in f:
            name, mobile, age, mail = line.strip().split(",")
            if name.startswith("A") or name.startswith("a"):
                print(name)
                found = True
        f.close()
        if not found:
            print("No students found whose name starts with 'A'.")
    except FileNotFoundError:
        print("\n No student data found! Please store details first.\n")


# ---------------- Main Menu ----------------
while True:
    print("""
========== Student File Handling System ==========
1. Store Student Details
2. Retrieve Student Details
3. Count Number of Students
4. Students Age Greater Than 25
5. Students Name Starts With 'A'
6. Exit
==================================================
""")
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        store_student_details()
    elif choice == '2':
        retrieve_student_details()
    elif choice == '3':
        count_students()
    elif choice == '4':
        students_age_greater_25()
    elif choice == '5':
        students_name_starts_with_A()
    elif choice == '6':
        print("\n Exiting program. Goodbye!")
        break
    else:
        print("\n Invalid choice! Please enter a number between 1 and 6.\n")
