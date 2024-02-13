# Lysander

from ReadData import readFile
from WriteData import writeFile
from DataCopy import copyDataToTemp
from ChooseAccountToView import displayAccounts
from PrintInfo import removeLines

def deleteAccount(user: str, account_input: str, data: dict) -> dict:
    '''Deletes the account from the dictionary'''

    # Looks through the dictionary and deletes the inputted account
    for i in range(len(data)):
        if data['users'][user][i]['account'] == account_input:
            del data['users'][user][i]
            break
    else:
        print("Account does not exist")
        input("Press enter to continue...")
        return False
    
    return data


def deleteAccountFunction(user: str):
    '''Uses account input and data from UserData.json to delete it and save changes'''

    # Loops through while there is an account to delete
    while displayAccounts() != 0:
        # Gets data and input and deletes that input from data
        oldData = readFile("UserData.json")
        account_input = input("What account would you want to delete? > ")
        newData = deleteAccount(user, account_input, oldData)
        if not newData:
            removeLines(3)
            continue

        # Saves the data
        answer = input(f"Are you sure you want to delete {account_input}? (y/n) > ")
        if answer.lower().strip() == "y":
            writeFile("UserData.json", newData)
            copyDataToTemp(user)