try:
    a = int(input("enter the a value: "))
    b = int(input("enter the b value: "))
    c = a + b
    if a <= 10 and b <= 10:
        raise ValueError("ValueError: enter the valid integer format")
    else:
        print("the result is: ", c)
except ValueError:
    print("ValueError: enter the valid type format")
finally:
    print("the program has been executed successfully")
