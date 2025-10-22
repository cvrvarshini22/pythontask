def palindrome_check(*a):
    for s in a:
        if s == s[::-1]:
            print(s, "is Palindrome")
        else:
            print(s, "is not Palindrome")

n = int(input("Enter number of strings: "))
words = []
count = 1
for i in range(n):
    print("Enter string", count, end=": ")
    w = input()
    words.append(w)
    count = count + 1

palindrome_check(*words)
