# Password Generator Project
# Python Program

import random
import string

def generate_password(length):
    # Characters to use in password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate random password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password


# User Input
try:
    length = int(input("Enter the desired password length: "))

    if length <= 0:
        print("Please enter a positive number.")
    else:
        # Generate Password
        password = generate_password(length)

        # Display Password
        print("\nGenerated Password:")
        print(password)

except ValueError:
    print("Invalid input! Please enter a number.")
