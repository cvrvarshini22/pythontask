num = int(input("enter the number: "))
original = num
digits = len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum +=digit ** digits
    temp = temp // 10
if sum == original:
    print("yes, it is an armstorng number ")
else: print("no, it is an armstrong number")
