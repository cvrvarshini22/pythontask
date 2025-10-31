try:
    a = int(input("enter the first number: "))
    b = int(input("enter the second number: "))

    result = a + b
    print("result is:", result)

except TypeError:
    print("TypeError: enter valid number")

except ValueError:
    print("ValueError: please enter the valid number")

finally:
    print("this program has executed successfully")

