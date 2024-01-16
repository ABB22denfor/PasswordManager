'''Module for adding a new user account'''
import sys
#Remove main and sys when done!
def main():
    boolean = strToBool(sys.argv[1].strip())
    newAccount = createAccount(boolean)
    printAccount(newAccount)

#Remove when done
def strToBool(inputStr):
    return bool(inputStr.lower() == "true" or inputStr.lower() == "y")

def printUI():

    print('''
WELCOME TO ACCOUNT CREATOR 3000!
--------------------------------
(*required)
''')

def createAccount(wantsUserPassword: bool):
    '''(wantsUserPassword->bool) Create a new account with name, email and password'''

    printUI()

    password = ""

    #What is the account for? (e.g. Youtube, Spotify, Facebook)
    accountType = input("*Account for: \n > ")

    name = input("*Username: \n > ")

    email = input("Email address: \n > ")

    if wantsUserPassword:
        password = input("*Password: \n > ")
    else:
        #Call createPassword with functionHandler
        pass

    return {"username": name, "email": email, "password": password, "account": accountType}

def printAccount(account):
    print(f'''
---------------------------------
Account Details:
- Username: {account["username"]}
- Email: {account["email"]}
- Password: {account["password"]}
- For: {account["account"]}
---------------------------------''')

    if not strToBool(input("Do you want to save this account? (y/n) \n > ")):
        #Ask if want to generate password or make themselves
        #Change parameter to corresponding input
        createAccount(True)
    else:
        print(account)


if __name__ == "__main__":
    main()
