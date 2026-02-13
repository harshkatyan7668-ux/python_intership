# Task 1: String Reverse

# take input from the user
text = input("Enter any word: ")

# create empty variable to store reversed string
reverse_text = ""

# use loop to reverse the string
for char in text:
    reverse_text = char + reverse_text

# print the final reversed string
print("Reverse string is:", reverse_text)
