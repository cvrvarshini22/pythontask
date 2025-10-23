# get_list_values.py

def get_list_values():
    lst = []
    n = int(input("Enter number of elements: "))
    for i in range(n):
        num = int(input(f"Enter element {i+1}: "))
        lst.append(num)
    return lst
