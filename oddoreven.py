num = int(input("enter the number: "))
even_count = 0
odd_count = 0
for i in range(1,101,num):
    if num % 2 == 0:
        even_count += 1
    else:
            odd_count +=1
print("even number count: ", even_count)
print("odd number count: ",odd_count)

