# Author: Lucas Axberg
# Description: Shows the user their accounts and asks which to view

from GetData import getAccountFromFile

def displayAccounts():
    """
        Prints the accounts of the specified user    
    """    
    # Call the getAccountFromFile, without an account to get the list of all accounts
    account_names = getAccountFromFile()
    
    # Prints header 
    print("".center(24, "-"))
    print(" YOUR ACCOUNTS: ".center(24, "#"))
    print("".center(24, "-"))

    # Print all account names
    for account in account_names:
        print(f"| {account}")
    print("".center(24, "-"))


def chooseAccount():
    """
        Takes an input of a user and shows that users accounts, then returns a string of the chosen account to view
    """

    displayAccounts()    
    
    # Get input from user
    chosen_account = input("View > ")
    chosen_account = chosen_account.strip()

    return chosen_account

