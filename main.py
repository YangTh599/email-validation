# Thayer Yang
# 09 DEC 2024
# Email Validation in Python

def validate_username(username):
    if username.isalpha():
        return "Username is valid (letters only)!"
    elif username.isdigit():
        return "Username is valid (digits only)!"
    else:
         return "Invalid username!"

run = True
while run:    
    user = input("Enter a username: ")
    if user == "quit PLEASE":
        run = False
    else:
        print(validate_username(user))
        print()
