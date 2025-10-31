import Simple_calc
import date_today

try:
    a = int(input("Enter the A value: "))
    b = int(input("Enter the B value: "))
    print("\n1. Addition  2. Subtraction  3. Multiplication  4. Division")
    choice = int(input("Enter the choice to perform: "))

    date_today.today_date()

    if choice == 1:
        result = Simple_calc.add(a, b)
        print("Addition of two numbers:", result)
    elif choice == 2:
        result = Simple_calc.sub(a, b)
        print("Subtraction of two numbers:", result)
    elif choice == 3:
        result = Simple_calc.mul(a, b)
        print("Multiplication of two numbers:", result)
    elif choice == 4:
        result = Simple_calc.div(a, b)
        print("Division of two numbers:", result)
    else:
        print("Invalid choice!")

except ValueError:
    print("ValueError: Please enter valid numbers.")
except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero.")
else:
    print("No error occurred. Operation completed successfully.")
finally:
    print("This program has executed successfully.")
