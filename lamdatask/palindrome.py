# Take input from the user
words = input("Enter words separated by space: ").split()

# Check each word for palindrome using shorthand if-else
for word in words:
    result = "Palindrome" if word == word[::-1] else "Not Palindrome"
    print(word, "→", result)
