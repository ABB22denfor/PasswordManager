'''Module for adding a new user account'''
import sys

def main():
    boolean = strToBool(sys.argv[1].strip())
    print(createAccount(boolean))

def strToBool(inputStr):
    return bool(inputStr.lower() == "true")

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

    name = input("Username: \n > ")

    email = input("*Email address: \n > ")

    if wantsUserPassword:
        password = input("*Password: \n > ")
    else:
        #Call createPassword with functionHandler
        pass

    return {"username": name, "email": email, "password": password}



if __name__ == "__main__":
    main()
