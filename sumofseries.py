n = int(input("enter number of terms: "))
harmonic_sum = 0.0
print("\n harmonic series is: ")
for i in range (1, n + 1):
        print("1/", i, end= " ")
        harmonic_sum += 1 / i
print("\n\n sum of harmonic series upto", n," term is: ", round(harmonic_sum, 4))
        
