# Author: Lucas Axberg

from ReadData import readFile
import json
import os

def copyDataToTemp(user):
    """
        Copies the accounts and their information for a selected user to a temporary file used by other functions
    """

    # Reads the main file
    data = readFile("UserData.json")
    
    # Copies the users accounts data and formats it to a string
    user_accounts_data = data["users"][user]
    formatted_user_data = json.dumps(user_accounts_data)

    # Writes the formatted string to the temp file
    with open(absolute_path + "/CurrentUser.json", "w", encoding="utf-8") as temp_file:
        temp_file.write(formatted_user_data)   

