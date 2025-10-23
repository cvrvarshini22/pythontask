# calllogical.py

from primenumber import prime
from perfectnumber1 import perfect
from armstrongnumber import armstrong

print("Choose an option:")
print("1. Check Prime Number")
print("2. Check Perfect Number")
print("3. Check Armstrong Number")

choice = int(input("Enter your choice (1-3): "))
n = int(input("Enter a number: "))

if choice == 1:
    prime(n)
elif choice == 2:
    perfect(n)
elif choice == 3:
    armstrong(n)
else:
    print("Invalid choice")
