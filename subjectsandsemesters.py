year = int(input("Enter your year (1 to 4): "))
semester = int(input("Enter your semester (1 or 2): "))

if year == 1 and semester == 1:
    print("Subjects:")
    print("1. English")
    print("2. Maths-I")
    print("3. Physics")
    print("4. Chemistry")
    print("5. Programming")

elif year == 1 and semester == 2:
    print("Subjects:")
    print("1. Maths-II")
    print("2. Environmental Science")
    print("3. C Programming")
    print("4. python")
    print("5. Workshop")

elif year == 2 and semester == 1:
    print("Subjects:")
    print("1. Data Structures")
    print("2. DBMS")
    print("3. OOP")
    print("4. Discrete Math")
    print("5. OS")

elif year == 2 and semester == 2:
    print("Subjects:")
    print("1. Computer Networks")
    print("2. Java")
    print("3. Software Engineering")
    print("4. Microprocessors")
    print("5. Probability")

elif year == 3 and semester == 1:
    print("Subjects:")
    print("1. Web Development")
    print("2. Python")
    print("3. Machine Learning")
    print("4. Statistics")
    print("5. CN Lab")

elif year == 3 and semester == 2:
    print("Subjects:")
    print("1. AI")
    print("2. Big Data")
    print("3. Cloud Computing")
    print("4. Cyber Security")
    print("5. Internship")

elif year == 4 and semester == 1:
    print("Subjects:")
    print("1. Project Work")
    print("2. Deep Learning")
    print("3. DevOps")
    print("4. Research Methodology")
    print("5. Seminar")

elif year == 4 and semester == 2:
    print("Subjects:")
    print("1. Final Project")
    print("2. Viva")
    print("3. Industrial Training")
    print("4. Open Elective")
    print("5. Entrepreneurship")

else:
    print("Invalid input. Please enter a year between 1-4 and semester 1 or 2.")
