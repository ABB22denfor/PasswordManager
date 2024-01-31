# Author: Lucas Axberg

from ReadData import readFile
from WriteData import writeFile
import json
import os

def copyDataToTemp(user):
    """
        Copies the accounts and their information for a selected user to a temporary file used by other functions
    """

    # Reads the main file
    data = readFile("UserData.json")
    
    # Copies the users accounts data and formats it to a string
    try:
        user_accounts_data = data["users"][user]
    except KeyError:
        user_accounts_data = []

    # Writes the formatted string to the temp file
    writeFile("CurrentUser.json", user_accounts_data)
        

