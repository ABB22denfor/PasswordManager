# Lysander

import string
import random


def generatePassword() -> str:
    '''Creates a string of all letters, symbols and numbers and then picks 16 at random for a new list. Then it makes a string from that list and returns it.'''

    while True:
        # Adds the letters, numbers and symbols to a variable and then choose 16 of them
        random_list = string.ascii_letters + string.digits + "!@#$%^&*"
        generated_password_list = random.choices(random_list,k=16)

        password = ""
        for letter in generated_password_list:
            password += letter

        print(f"New password: {password}")
        answer = input("Do you want to use this password? (y/n) ")

        if answer.lower() == "y":
            break

    return password
