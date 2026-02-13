# Task 3: Email Validator

# take email input from user
email = input("Enter your email: ")

# check basic conditions
if "@" in email and "." in email:
    
    # find position of @ and .
    at_position = email.index("@")
    dot_position = email.rindex(".")
    
    # check if dot is after @
    if at_position < dot_position:
        print("Valid email address")
    else:
        print("Invalid email address")

else:
    print("Invalid email address")
