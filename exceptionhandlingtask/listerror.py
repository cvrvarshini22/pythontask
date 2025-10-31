try:
    n = int(input("enter the number of elements in the list: "))
    my_list = []

    for i in range(n):
        element = int(input(f"enter element {i+1}: "))
        my_list.append(element)

    print("List:", my_list)

    value = int(input("enter the value to search: "))

    if value not in my_list:
        raise ValueError("value not found in the list")
    else:
        print("value found in the list:", value)

except ValueError as e:
    print("ValueError:", e)

finally:
    print("this program has executed successfully")

