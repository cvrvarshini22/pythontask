tup = tuple(map(int, input("Enter elements (repeat allowed): ").split()))

val = int(input("Enter value to check: "))

if val in tup:
    first_index = tup.index(val)
    occurrences = tup.count(val)
    print(f"{val} found at index {first_index} (first occurrence).")
    print(f"Total occurrences: {occurrences}")
else:
    print(f"{val} is NOT in the tuple.")
