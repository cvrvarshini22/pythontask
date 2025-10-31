try:
    a = int(input("enter the first number: "))
    b = int(input("enter the second number: "))
    result = a / b
    print("division result: ", result)
except ZeroDivisionError:
        print("Error: cannot divided by zero")
except ValueError:
        print("Error: please enter the valid number")
finally:
        print("this program has executed sucessfully")
