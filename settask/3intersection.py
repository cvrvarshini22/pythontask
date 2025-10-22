s1 =input("enter the numbers in first set separated by space:").split()
s2 = input("enter the numbers in second set separated by space:").split()
s3 = input("enter the numbers in third set separated by space:").split()
set1 = set(s1)
set2 = set(s2)
set3 = set(s3)
common = set1.intersection(set2)
common1 = set2.intersection(set3)
common2 = set3.intersection(set1)
if common:
    print("yes, there is common set:",common)
else:
    print("no,common set not found")
