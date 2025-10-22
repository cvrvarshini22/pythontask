colors = [ ]
for i in range(5):
    color = input(f"enter color {i+1}: ")
    colors.append(color)
color_tuple = tuple(colors)
print("\n the colors you entered are:")
print(color_tuple)

