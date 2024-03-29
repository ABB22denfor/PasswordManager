# Imports modules
import os
import sys

# Add module folder to path
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))+'/src')

from PrintWelcome import printWelcomeScreen
from GetData import getAccountFromFile
from login import login
from PrintInfo import printHeader, removeLines, printAccountInfo
from Signup import signup
from DataCopy import copyDataToTemp
from InputHandler import getInput
from FunctionHandler import printUserInterface, handleInput, callFunctionInModule
from EditSavedValues import editValue
from Writer import writeData
from Delete import deleteAccountFunction
from CheckFunction import checkFunction
from Encode import encodeJSON, decodeJSON
from jwt.exceptions import DecodeError

# Global variables
global mode
global user

PATH = "/../data/UserData.json"


# Main code

def firstStep():
    '''The first part of the main code'''
    try:
        decodeJSON(PATH)
    except DecodeError:
        pass
        
    try:
        global mode

        # Clears screeen and prints header    
        os.system("cls" if os.name == "nt" else "clear")
        printHeader()

        while True:

            # Prints the availible commands for the first page
            print("Availible commands:".center(30))
            print("".center(30, "-"))
            print("> Signup\n> Login")
            print("".center(30, "-"))

            # Asks user for input and removes all lines except for header
            mode = input("Select > ").lower().strip()

            # Breaks the loop if mode is correct
            if mode == "login" or mode == "signup":
                break

            # Prints error message and restarts loop if mode isn't correct
            print(f"Mode <{mode}> is not a valid mode")
            input("Press enter to continue...")
            removeLines(8)

    # Runs if <ctrl><c> is pressed        
    except KeyboardInterrupt:

        # Clears screen and exits
        os.system("cls" if os.name == "nt" else "clear")
        encodeJSON(PATH)
        exit()

    # Clears screen and runs next part
    removeLines(6)
    secondStep()



def secondStep():
    '''The second part of the main code'''

    # Use global variable "mode"
    global mode

    try:
        while True:

            # Checks if the mode is "login"
            if mode == "login":
                
                # Prints login header
                print("Login".center(30) + "\n" + "".center(30, "-"))

                # Asks user for username and password
                username_input = input("Username > ").strip()
                password_input = input("Password > ").strip()

                # If username and password is correct, exit the loop
                if login(username_input, password_input):
                    break

                # If username or password isnt correct, explain it to user and start over the loop
                input("Username or password doesn't match\nPress enter to continue...")
                removeLines(6)

            # Checks if mode is "signup"    
            elif mode == "signup":

                # Print signup header
                print("Signup".center(30) + "\n" + "".center(30, "-"))

                # Call signup wich creates an account and saves it
                signup()

                # Wait for user input, clear the screen and change mode to login
                input("Press enter to continue...")
                removeLines(7)
                mode = "login"



    # Runs if <ctrl><c> is pressed        
    except KeyboardInterrupt:

        # Clears screen, prints header and calls the previous part of the main code
        os.system("cls" if os.name == "nt" else "clear")
        printHeader()       
        firstStep()


    # Saves username for other functions when loop is done
    global user
    user = username_input

    # Creates a temporary file with the information on the users accounts
    copyDataToTemp(user)

    # Clears the lines from the login "page"
    removeLines(4)

    # Calls the next part of the main code
    thirdStep()



def thirdStep():
    '''The third step of the main code'''

    # Use global variables mode, user  
    global mode
    global user
    
    try:
        while True:

            # Prints the availible functions to the user
            printUserInterface()

            # Saves 2 lists of availible commands to the global variables

            # Calls the input handler and saves the result in a variable
            func = getInput()


            # If the function does not exist, print error message and restart the loop
            if not checkFunction(func):
                input("Command doesn't exist\nPress enter to continue...")
                removeLines(11)
                continue

            # If the function exists, it exits the loop
            else:
                removeLines(9)
                break  


    # Runs if <ctrl><c> is pressed        
    except KeyboardInterrupt:

        # Clears screen, prints header and calls the previous part of the main code
        os.system("cls" if os.name == "nt" else "clear")
        printHeader()       
        secondStep()

    # Calls the next part if the main code
    fourthStep(func)


    
def fourthStep(func):
    '''Fourth step of the main code'''

    # Use global variables user, mode  
    global user
    global mode
        
    try:
        while True:        

            # Runs if selected function is "view"
            if checkFunction(func, 1):
                func_and_args = callFunctionInModule("ChooseAccountToView", "chooseAccount", ["Select an account to view"])
                chosen_account = func_and_args[0](*func_and_args[1])

                # Stops of no accounts are found
                if chosen_account:
    
                    # Get account info and print it
                    account_info = getAccountFromFile(chosen_account)
                    printAccountInfo(account_info)

                    # Wait and clear screen
                    input("Press enter to coninue...")
                    removeLines(8)
                
            # Checks if function is "save" 
            elif checkFunction(func, 2):
                func_and_args = callFunctionInModule("AccountCreator", "createAccount", [])
                account_data = func_and_args[0](*func_and_args[1])

                # Calls the write data accont with the returned informaion
                writeData(account_data, user)
                
            elif checkFunction(func, 3):
                func_and_args = callFunctionInModule("ChooseAccountToView", "chooseAccount", ["Select and account to edit"])
                chosen_account = func_and_args[0](*func_and_args[1])

                if chosen_account:
                    # Gets account information
                    account_info = getAccountFromFile(chosen_account)

                    # Calls edit function
                    func_and_args = callFunctionInModule("EditSavedValues", "editValue", [user, account_info])
                    func_and_args[0](*func_and_args[1])

            elif checkFunction(func, 4):
                func_and_args = callFunctionInModule("Delete", "deleteAccountFunction", [user])
                chosen_account = func_and_args[0](*func_and_args[1])
                                
                
            thirdStep()
          
        
    except KeyboardInterrupt:
        os.system("cls" if os.name == "nt" else "clear")
        printHeader()       
        thirdStep()



printWelcomeScreen()
firstStep()
