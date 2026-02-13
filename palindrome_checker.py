# Task 5: Palindrome Checker

# take input from user
text = input("Enter a word: ")

# create empty variable to store reversed word
reverse_text = ""

# reverse the word using loop
for char in text:
    reverse_text = char + reverse_text

# check if original and reversed are same
if text == reverse_text:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
