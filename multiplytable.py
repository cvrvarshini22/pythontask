num =int(input("\n multiplication limit upto: "))
for i in range (1, num+1):
    for j in range (1,11):
        s = i * j
        print(f"{i} * {j} = {s}" )
    print ( )
