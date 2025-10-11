n = (int(input("enter the natural number: ")))
sum_number = 0
for number in range(1, n+1):
   print(number)
   sum_number += number
average = sum_number / n
print("the sum is: ",sum_number)
print("the averge is: ",average)
