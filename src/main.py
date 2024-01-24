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

# Main code
os.system("cls" if os.name == "nt" else "clear")

printHeader()

# Prints the availible commands for the first page
print("Availible commands:".center(30))
print("".center(30, "-"))
print("> Signup\n> Login")
print("".center(30, "-"))

# Asks user for input and removes all lines except for header
mode = input("Select > ")
removeLines(6)

# LOGIN LOOP
while True:
    if mode == "login":
        # Prints login header
        print("Login".center(30) + "\n" + "".center(30, "-"))

        # Asks user for username and password
        username_input = input("Username > ").strip()
        password_input = input("Password > ").strip()

        # If both are blank, ask the user if they want to exit or create an account
        if username_input == "" and password_input == "":
            removeLines(2)
            print("Would you like to signup or exit?")
            mode = input("Select > ")
            removeLines(4)
            continue

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

    elif mode == "exit":
        
        # Print goodbye, waits, then clears screen and exit program
        print("Goodbye")
        time.sleep(0.5)
        os.system("cls" if os.name == "nt" else "clear")
        exit()
        


# Saves username for other functions
user = username_input

# Creates a temporary file with the information on the users accounts
copyDataToTemp(user)

# Clears the lines from the login "page"
removeLines(4)

# FUNCTION CALL LOOP
while True:
    printUserInterface()

    save = ["save", "s"]
    view = ["view", "v"]
    
    func = getInput()
    if func not in save and func not in view :
        input("Command doesn't exist\nPress enter to continue...")
        removeLines(4)
        continue
        
    func_and_arg = handleInput(func)
    a = func_and_arg[0](*func_and_arg[1])

    if func in view:
        data = getAccountFromFile(a)
        for i in data:
            print(f"{i.title()}: {data[i]}")

removeLines(7)

