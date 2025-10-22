ele = [ ]
for i in range(5):
    num = int(input(f"enter number {i+1}: "))
    ele.append(num)
num_tuple = tuple(ele)
print("\n First element:", num_tuple[0])
print("\n second element:", num_tuple[-1])
