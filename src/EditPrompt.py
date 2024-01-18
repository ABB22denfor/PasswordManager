# Author: Lucas Axberg

import os
from GetData import getAccountFromFile


def editPrompt(account):

    # Stores the account dictionary to a variable
    acc = getAccountFromFile(account)

    while True:

        os.system("cls" if os.name == "nt" else "clear")

        # Prints the account information
        for key in acc:
            print(f"{key.title()}: {acc[key]}")
        print("---------------------")

        # Takes user input and formats it
        print("Select a field to edit:")    
        field_to_change = input("Edit > ").strip().lower()

        # Breaks loop if input is correct
        if field_to_change in acc.keys():
            break

        # Returne false if user wants to exit
        if field_to_change == "exit":
            return False
        

    print("---------------------")
    new_value = input(f"Change {field_to_change} to: ")
    
    return [field_to_change, new_value]
