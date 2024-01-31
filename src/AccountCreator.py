#Dennis
'''Module for adding a new user account'''
import os

from FunctionHandler import callFunctionInModule
from Saver import askPasswordType

def strToBool(input_str: str) -> bool:
    '''(input_str: str) Convert y/N input to True or False'''
    return input_str.lower() == "y"


def createAccount() -> dict:
    '''Create a new account with name, email and password'''

    password = ""

    #What is the account for? (e.g. Youtube, Spotify, Facebook)
    account_type = input("*Application / Website: \n > ")

    name = input("*Username: \n > ")

    email = input(" Email address: \n > ")

    if askPasswordType():
        password = input("*Password: \n > ")
    else:
        #Call createPassword with functionHandler
        password = callFunctionInModule("Generator", "generatePassword", [])[0]()

    return printAccount({"username": name, "password": password,
    "email": email, "account": account_type})


def printAccount(account: dict) -> dict:
    "(account: dict) -> dict, Print account details and ask user if they want to save that account"
    print(f'''--------------------------------
Account Details:
- Username: {account["username"]}
- Email: {account["email"]}
- Password: {account["password"]}
- Application: {account["account"]}
--------------------------------''')

    if not strToBool(input("Do you want to save this account? (y/n) \n > ")):
        return createAccount()

    return account
