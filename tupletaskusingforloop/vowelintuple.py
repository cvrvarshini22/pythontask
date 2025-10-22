letters = tuple(input("Enter letters separated by space: ").split())
vowels = ('a', 'e', 'i', 'o', 'u')
count = 0

for letter in letters:
    if letter.lower() in vowels:
        count += 1

print("Number of vowels:", count)

