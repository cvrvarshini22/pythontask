# Take input from the user
words = input("Enter words separated by space: ").split()

# Find words that have exactly 6 letters
six_letter_words = [word for word in words if len(word) == 6]

# Display the result
print("Words with 6 letters:", six_letter_words)
