# Author: Lucas Axberg
'''Module for user selection of account'''

from GetData import getAccountFromFile
from PrintInfo import removeLines



def displayAccounts() -> int:
    '''Prints the accounts of the current user'''    

    removeLines(7)
    
    # Call the getAccountFromFile, without an account to get the list of all accounts
    account_names = getAccountFromFile()
    
    # Prints header 
    print("Your accounts:".center(30))
    print("".center(30, "-"))

    # Prints error message and returns 0 if no account exists
    if not account_names:
        print("<NO ACCOUNT FOUND>".center(30))
        print("".center(30, "-"))
        input("Press enter to continue...")
        removeLines(5)
        return 0
    
    # Print all account names and return length of account list
    for account in account_names:
        print(f"* {account}")
    print("".center(30, "-"))
    return len(account_names)



def chooseAccount(msg: str) -> str:
    '''Shows the current user their accounts, asks which they want to view, and returns the selected account'''

    # Prints users accounts
    function_value = displayAccounts() 

    # Returns if no account was found
    if function_value == 0:
        return ""
    
    # Loop while answer is false
    while True:

        # Gets user input
        chosen_account = input(f"{msg} > ")
        chosen_account = chosen_account.strip()

        # Prints error message if account doesn't exist
        if chosen_account not in getAccountFromFile():
            input(f"Account '{chosen_account}' doesn't exist\nPress enter to continue...")
            removeLines(3)
            continue

        # Clear screen and return if answer is correct
        removeLines(4 + function_value)
        return chosen_account

