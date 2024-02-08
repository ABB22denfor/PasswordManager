# Imports modules
import os
import time

from GetData import getAccountFromFile
from login import login
from PrintInfo import printHeader, removeLines
from Signup import signup
from DataCopy import copyDataToTemp
from InputHandler import getInput
from FunctionHandler import printUserInterface, handleInput
from EditPrompt import editPrompt
from EditSavedValues import editSavedValue
from EditSavedValues import editValue
from Writer import writeData

# Global variables
global mode
global user
global save
global view 

def firstStep():
    # Main code
    try:
        global mode
    
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

            if mode == "login" or mode == "signup":
                break

            print(f"Mode <{mode}> is not a valid mode")
            input("Press enter to continue...")
            
            removeLines(8)
            
    except KeyboardInterrupt:
        os.system("cls" if os.name == "nt" else "clear")
        exit()

    removeLines(6)
    secondStep()

def secondStep():
    # LOGIN LOOP
    global mode
    try:
        while True:
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
    
            elif mode == "signup":

                # Print signup header
                print("Signup".center(30) + "\n" + "".center(30, "-"))

                # Call signup wich creates an account and saves it
                signup()

                # Wait for user input, clear the screen and change mode to login
                input("Press enter to continue...")
                removeLines(7)
                mode = "login"


        # Saves username for other functions
        global user
        user = username_input

        # Creates a temporary file with the information on the users accounts
        copyDataToTemp(user)

        # Clears the lines from the login "page"
        removeLines(4)

    except KeyboardInterrupt:
        os.system("cls" if os.name == "nt" else "clear")
        printHeader()       
        firstStep()

    thirdStep()

def thirdStep():
    global mode
    global user
    global save
    global view
    
    # FUNCTION CALL LOOP
    try:
        while True:
            printUserInterface()

            save = ["save", "s"]
            view = ["view", "v"]
    
            func = getInput()
            
            if func in save:
                removeLines(7)
                
            if func not in save and func not in view :
                input("Command doesn't exist\nPress enter to continue...")
                removeLines(9)
                continue
            else:
                break  

    except KeyboardInterrupt:
        os.system("cls" if os.name == "nt" else "clear")
        printHeader()       
        secondStep()

    
    fourthStep(func)
    
def fourthStep(external_func):
    func = external_func

    global user
    global mode
    global view
    global save
        
    try:
        while True:        
            func_and_arg = handleInput(func)
            account_variable = func_and_arg[0](*func_and_arg[1])

            # Runs if selected function is "view"
            if func in view:

                # Stops of no accounts are found
                if not account_variable:
                    continue

                # Gets account information
                data = getAccountFromFile(account_variable)

                # Prints header
                print("Account info:".center(30))
                print("".center(30, "-"))

                # Prints account information
                for i in data:
                    print(f"* {i.title()}: {data[i]}")
                print("".center(30, "-"))

                # Gets user input and clears screen
                edit_answer = input("Do you want to edit this account (y/n) > ")
                
                removeLines(1)
                # If user doesn't want to edit, restart the loop
                if edit_answer != "y":
                    continue
                
                if not editValue(user, data):
                    continue
                
                # Checks if an account has been selected, else restarts the loop
                                
            elif func in save:
                writeData(account_variable, user)

    
          
            thirdStep()
        
    except KeyboardInterrupt:
        os.system("cls" if os.name == "nt" else "clear")
        printHeader()       
        thirdStep()


user = "Jeff"
mode = "login"
firstStep()
