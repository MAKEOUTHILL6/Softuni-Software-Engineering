import re


def validator(password):
    is_valid = True
    if not(6 <= len(password) <= 10):
        is_valid = False
        print("Password must be between 6 and 10 characters")
    if not(re.match("^[A-Za-z0-9_-]*$", password)):
        is_valid = False
        print("Password must consist only of letters and digits")
    if not any(char.isdigit() for char in password):
        is_valid = False
        print("Password must have at least 2 digits")

    if is_valid:
        print("Password is valid")


password = input()
validator(password)