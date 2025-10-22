s1 = input("enter numbers separated by spaces: ")
s2 = [int(num) for num in s1.split( )]
s2.sort( )
print("sorted list in ascending order: ",s2)
