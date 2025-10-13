a =float(input("enter first value: "))
b =float(input("enter second value: "))
c = float(input("enter the third value: "))
if (a > b and a < c) or (a> c and a < b):
    median = a
elif (b > a and b < c) or (b > c and b < a):
    median = b
else:
    median = c
print("the median is ", median)
