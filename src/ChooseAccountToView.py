# Author: Lucas Axberg

from GetData import getAccountFromFile

def displayAccounts():
    """
        Prints the accounts of the current user    
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
        Shows the current user their accounts, asks which they want to view, and returns the selected account
    """

    # Prints users accounts
    displayAccounts()    
    
    # Get input from user
    chosen_account = input("View > ")
    chosen_account = chosen_account.strip()

    return chosen_account

