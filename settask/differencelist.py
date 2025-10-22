l1 = input("enter the first list separated by spaces:").split()
l2 = input("enter the second list separated by spaces:").split()
set1 = set(l1)
set2 = set(l2)
difference = set1 - set2
difference_set = set(difference)
print("difference between the first and second list is:", difference_set)
