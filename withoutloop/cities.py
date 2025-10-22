cities = []
n = int(input("enter the number of city:"))
for i in range(n):
   city = input(f"enter the cities {i+1}:")
   cities.append(city)
print("\n entered cities:")
for city in cities:
    print(city)
