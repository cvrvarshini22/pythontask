quantity = int(input("Enter quantity: "))
price = 100
total = quantity * price

if total > 1000:
    total = total * 0.9  

print("Total cost:", total)
