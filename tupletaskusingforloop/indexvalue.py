numbers = (100, 200, 300, 400)

for index, value in enumerate(numbers):
    print(f"Index {index} has value {value}")
colors = []

for i in range(5):
    color = input(f"Enter color {i+1}: ")
    colors.append(color)

color_tuple = tuple(colors)

print("Your color tuple is:", color_tuple)


