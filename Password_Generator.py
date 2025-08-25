# Random Password Generator using Python

import string
import random

def create_password(length, use_digits=True, use_symbols=True):
    chars = string.ascii_letters  # includes a-z + A-Z

    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    password = "".join(random.choice(chars) for _ in range(length))
    return password

print("=== Strong Password Generator ===")
try:
    length = int(input("How long should the password be? "))
    digits = input("Include numbers? (y/n): ").lower() == 'y'
    symbols = input("Include symbols? (y/n): ").lower() == 'y'

    result = create_password(length, digits, symbols)
    print("Your new password:", result)
except ValueError:
    print("Please enter a valid number.")
