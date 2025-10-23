# count_even_numbers.py

def count_even_numbers(lst):
    count = 0
    for i in lst:
        if i % 2 == 0:
            count += 1
    print("Number of even numbers in the list:", count)
