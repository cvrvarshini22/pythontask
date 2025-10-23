# armstrongnumber.py
def armstrong(n):
    temp = n
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit ** 3
        n //= 10
    if temp == sum:
        print(temp, "is an Armstrong number")
    else:
        print(temp, "is not an Armstrong number")
