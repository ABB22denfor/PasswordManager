# Lucas Axberg | GetData
# Reads data from file/database

import json

def getAccountFromFile(user, account=""):
    """
    Returns the information about the account for the specified user.
    If the account doesn't exist, it returns False.
    """

    # Reads data file and formats the input to a json object
    with open("./GetData.json", "r") as file:
        data = json.loads(file.read())

    # Defines a list for names in case of no account specified
    account_names = []
    
    # Saves the list of dictionaries
    user_accounts = data["users"][user]

    # Saves formatted_data as the specified account if it exists, else sets it to False
    for account_data in user_accounts:
        if account == "":
            account_names.append(account_data["account"])
        elif account_data["account"] == account:
            formatted_data = account_data
            break
    else: 
        formatted_data = False
        
    # Returns datastructure or list of names if account is not specified
    if account == "":
        return account_names
    else:
        return formatted_data
