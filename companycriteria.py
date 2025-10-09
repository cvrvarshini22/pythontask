aptitude_marks = float(input("Enter Aptitude marks: "))
gd_marks = float(input("Enter GD marks: "))
if 390 <= aptitude_marks <= 400:
    salary = 30000
    eligible = True
elif 380 <= aptitude_marks < 390 and aptitude_marks >= 85:
    salary = 28000
    eligible = True
elif 370 <= aptitude_marks < 380 and gd_marks >= 90:
    salary = 25000
    eligible = True
else:
    eligible = False
if eligible:
    print("You are eligible for admission.")
    print("Offered Salary:", salary)
else:
    print("You are not eligible for admission.")
