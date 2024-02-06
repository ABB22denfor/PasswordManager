#Author: Dennis Forslund

'''Module for adding a new user account'''

from FunctionHandler import callFunctionInModule
from Saver import askPasswordType
from PrintInfo import removeLines

def strToBool(input_str: str) -> bool:
    '''Convert y/N input to True or False'''
    return input_str.lower() == "y"

def printHeader():
    print("###Account Creator###".center(30))
    print("".center(30, "-"))


def createAccount() -> dict:
    '''Create a new account with name, email and password'''
    printHeader()

    password = ""

    account_type = input("*Application / Website: \n > ")

    name = input("*Username: \n > ")

    email = input(" Email address: \n > ")

    # Check if user wants a generated password or not
    if askPasswordType():
        password = input("*Password: \n > ")
    else:
        password = callFunctionInModule("Generator", "generatePassword", [])[0]()

    removeLines(11)

    return printAccount({"username": name, "password": password,
    "email": email, "account": account_type})


def printAccount(account: dict) -> dict:
    "(account: dictionary of new account) -> dict, Print account details and ask user if they want to save that account"
    printHeader()
    print(f'''Account Details:
- Username: {account["username"]}
- Email: {account["email"]}
- Password: {account["password"]}
- Application: {account["account"]}
--------------------------------''')

    save_account_input = input("Do you want to save this account (y/n) \n > ")

    removeLines(10)
    # Start over if user not happy
    if not strToBool(save_account_input):
        return createAccount()
    return account
