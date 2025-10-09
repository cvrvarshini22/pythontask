a = int(input("enter the value of a: ")) 
b = int(input("enter the value of b:"))
print("select a operation")
print("1.add")
print("2.sub")
print("3.multiplication")
print("4.division")
operation=input("select a operation")
if operation == ("1"):
    print(a+b)
elif operation == ("2"):
    print(a-b)
elif operation ==("3"):
    print(a*b)
elif operation ==("4"):
    print(a/b)
else:
    print("invalid operation")
