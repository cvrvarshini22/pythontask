num1 = input("enter first list of numbers separated by commas: ").split(',')
num2 = input("enter second list of numbers separated by commas: ").split(',')
num1 = [int(num) for num in num1]
num2 = [int(num) for num in num2]
for item in num2:
    num1.append(item)
print("The list are: ",num1)
