#Dennis
'''Module for adding a new user account'''
import sys
import os

from FunctionHandler import callFunctionInModule
from Saver import askPasswordType

#Remove main and sys when done!
def main():
    createAccount()

def strToBool(input_str: str) -> bool:
    return input_str.lower() == "y"

def printUI():

    print('''
WELCOME TO ACCOUNT CREATOR 3000!
--------------------------------
(*required)
''')

def createAccount() -> dict:
    '''(wantsUserPassword: bool) -> dict, Create a new account with name, email and password'''

    printUI()

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
    print(f'''
--------------------------------
Account Details:
- Username: {account["username"]}
- Email: {account["email"]}
- Password: {account["password"]}
- Application: {account["account"]}
--------------------------------''')

    if not strToBool(input("Do you want to save this account? (y/n) \n > ")):
        os.system('cls' if os.name == 'nt' else 'clear')
        #Ask if want to generate password or make themselves
        #Change parameter to corresponding input
        return createAccount()

    return account


if __name__ == "__main__":
    main()
