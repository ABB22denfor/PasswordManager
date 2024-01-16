'''Module for adding a new user account'''
import sys
import os
#Remove main and sys when done!
def main():
    boolean = strToBool(sys.argv[1].strip())
    print(createAccount(boolean))

def strToBool(inputStr: str) -> bool:
    return bool(inputStr.lower() == "true" or inputStr.lower() == "y")

def printUI():

    print('''
WELCOME TO ACCOUNT CREATOR 3000!
--------------------------------
(*required)
''')

def createAccount(wantsUserPassword: bool) -> dict:
    '''(wantsUserPassword: bool) -> dict, Create a new account with name, email and password'''

    printUI()

    password = ""

    #What is the account for? (e.g. Youtube, Spotify, Facebook)
    accountType = input("*Application / Website: \n > ")

    name = input("*Username: \n > ")

    email = input(" Email address: \n > ")

    if wantsUserPassword:
        password = input("*Password: \n > ")
    else:
        #Call createPassword with functionHandler
        pass

    return printAccount({"username": name, "password": password, "email": email, "account": accountType})


def printAccount(account: dict) -> dict:
    "(account: dict) -> dict, Print account details and ask user if they want to save that account"
    print(f'''
--------------------------------
Account Details:
- Username: {account["username"]}
- Email: {account["email"]}
- Password: {account["password"]}
- For: {account["account"]}
--------------------------------''')

    if not strToBool(input("Do you want to save this account? (y/n) \n > ")):
        os.system('cls' if os.name == 'nt' else 'clear')
        #Ask if want to generate password or make themselves
        #Change parameter to corresponding input
        return createAccount(True)

    return account


if __name__ == "__main__":
    main()
