# Author: Lucas Axberg

import os
from PrintInfo import removeLines

def editPrompt(acc):
    """
        Shows the user the information of an account, asks them which field they want to change, and returns the field + new value
    """

    while True:

        # Takes user input and formats it
        print("Select a field to edit:")    
        field_to_change = input("Edit > ").strip().lower()

        # Breaks loop if input is correct
        if field_to_change in acc.keys():
            break

        # Returne false if user wants to exit
        if field_to_change == "exit":
            return False
        print(f"Selected field {field_to_change} doesn't exist ")
        input("Press enter to continue...")
        removeLines(4)

    print("---------------------")
    new_value = input(f"Change {field_to_change} to: ")
    
    return [field_to_change, new_value]

