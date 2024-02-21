from HandleDefaultUser import getDefaultUser, setDefaultUser
from FunctionHandler import callFunctionInModule
from GetData import getAccountFromFile
from PrintInfo import printAccountInfo
from DataCopy import copyDataToTemp
from ReadData import readFile

def handleArgs(args: list = []):
    
    try:
        if args[1] == "-u":
            pass
        user_info = getDefaultUser()
    except KeyError:
        return print("ERROR: Default User Not Set. passman -u <username> <password> to set defaults")

    copyDataToTemp(user_info[0])

    match args[1]:
        case "-v":
            viewAccount(args[2:])
        case "-c":
            print("Create")
        case "-e":
            print("Edit")
        case "-d":
            print("Delete")
        case "-u":
            setDefaultUser(args)
        case _:
            return 1
    return 0

def viewAccount(args: list):
    data = readFile("CurrentUser.json")
    chosen_account = args[0]

    if chosen_account not in getAccountFromFile():
        print(f"Account '{chosen_account}' doesn't exist.")
        return
    for account in data:
        if chosen_account == account["account"]:
            printAccountInfo(account)
