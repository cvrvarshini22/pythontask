# get_dict_values.py

def get_dict_values():
    d = {}
    count = int(input("Enter number of key-value pairs: "))
    for i in range(count):
        key = input("Enter key: ")
        value = int(input("Enter value: "))
        d[key] = value
    return d
