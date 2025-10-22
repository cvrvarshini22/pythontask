def count_characters(*a):
    for s in a:
        v = c = sp = 0
        for ch in s:
            if ch.isalpha():
                if ch.lower() in "aeiou":
                    v = v + 1
                else:
                    c = c + 1
            elif not ch.isspace():
                sp = sp + 1
        print("\nString:", s)
        print("Vowels:", v)
        print("Consonants:", c)
        print("Special Characters:", sp)

n = int(input("Enter number of strings: "))
data = []
count = 1
for i in range(n):
    print("Enter string", count, end=": ")
    s = input()
    data.append(s)
    count = count + 1

count_characters(*data)
