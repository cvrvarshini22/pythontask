s1 =input("enter the numbers in first set separated by space:").split()
s2 = input("enter the numbers in second set separated by space:").split()
set1 = set(s1)
set2 = set(s2)
common = set1.intersection(set2)
if common:
    print("yes, there is common set:",common)
else:
    print("no,common set not found")

