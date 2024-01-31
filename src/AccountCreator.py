#Author: Dennis Forslund

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

    account_type = input("*Application / Website: \n > ")

    name = input("*Username: \n > ")

    email = input(" Email address: \n > ")

    # Check if user wants a generated password or not
    if askPasswordType():
        password = input("*Password: \n > ")
    else:
        password = callFunctionInModule("Generator", "generatePassword", [])[0]()

    return printAccount({"username": name, "password": password,
    "email": email, "account": account_type})


def printAccount(account: dict) -> dict:
    "(account: dictionary of new account) -> dict, Print account details and ask user if they want to save that account"
    print(f'''--------------------------------
Account Details:
- Username: {account["username"]}
- Email: {account["email"]}
- Password: {account["password"]}
- Application: {account["account"]}
--------------------------------''')

    # Start over if user not happy
    if not strToBool(input("Do you want to save this account? (y/n) \n > ")):
        return createAccount()

    return account
