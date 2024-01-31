# Lucas Axberg 
'''Module for finding accounts or info about a specific account'''

from ReadData import readFile

def getAccountFromFile(account="") -> dict:
    '''Returns the information about the account for the specified user. If the account doesn't exist, it returns False.'''

    formatted_data = {}
    
    user_accounts = readFile("CurrentUser.json")

    # Loops through the list of accounts informations
    for account_data in user_accounts:

        # Add account names if no account was specified
        if account == "":
            formatted_data[account_data["account"]] = 1

        # Saves account information if an accounts name matches the specified account
        elif account_data["account"] == account:
            formatted_data = account_data
            break

    return formatted_data
