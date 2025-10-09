salary = float(input("enter salary: "))
years = int(input("enter years of service: "))
if years >5:
    bonus = salary * 0.05
else:
    bonus = 0
print("net bonus amount:",bonus)
