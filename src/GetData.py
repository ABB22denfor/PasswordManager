# Lucas Axberg | GetData

import os
import json

def getAccountFromFile(account=""):
    """
    Returns the information about the account for the specified user.
    If the account doesn't exist, it returns False.
    """

    absolute_path = os.path.dirname(os.path.abspath(__file__)) 
    
    # Reads data file and formats the input to a json object
    with open(absolute_path + "/CurrentUser.json", "r") as file:
        user_accounts = json.loads(file.read())

    # Defines a list for names in case of no account specified
    account_names = []  

    for account_data in user_accounts:

        # Appends account names if no account was specified
        if account == "":
            account_names.append(account_data["account"])

        # Saves account information if an accounts name matches the specified account
        elif account_data["account"] == account:
            formatted_data = account_data
            break
    # Saves False if no account name matched
    else: 
        formatted_data = False
        
    # Returns datastructure (or list of names if account is not specified)
    if account == "":
        return account_names
    else:
        return formatted_data
