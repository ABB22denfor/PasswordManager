# Lysander

import string
import random


symbols = "!@#$%^&*"

def generatePassword():
    '''Creates a string of all letters, symbols and numbers and then picks 16 at random for a new list. Then it makes a string from that list.'''

    finished = False

    while not finished:

        random_list = string.ascii_letters + string.digits + symbols
        generated_password_list = random.choices(random_list,k=16)

        password = ""
        for letter in generated_password_list:
            password += letter
        
        print(f"New password: {password}")
        answer = input("Do you want to use this password? (y/n) ")

        if answer.lower() == "y":
            finished = True
    
    return password


password = generatePassword()

print(password)