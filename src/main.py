# Imports modules
import os
import time

from login import login
from PrintInfo import printHeader, removeLines
from Signup import signup
from DataCopy import copyDataToTemp
from InputHandler import getInput
from FunctionHandler import printUserInterface

# Main code
os.system("cls" if os.name == "nt" else "clear")

printHeader()

print("Availible commands:".center(30))
print("".center(30, "-"))
print("> Signup\n> Login")
print("".center(30, "-"))

mode = input("Select > ")
removeLines(6)


while True:
    if mode == "login":
        print("Login".center(30) + "\n" + "".center(30, "-"))
        username_input = input("Username > ").strip()
        password_input = input("Password > ").strip()

        if username_input == "" and password_input == "":
            removeLines(2)
            print("Would you like to signup or exit?")
            mode = input("Select > ")
            removeLines(4)
            continue
            
        if login(username_input, password_input):
            break
        
        input("Username or password doesn't match\nPress enter to continue...")
        removeLines(6)
        
    elif mode == "signup":
        print("Signup".center(30) + "\n" + "".center(30, "-"))
        signup()
        input("Press enter to continue...")
        removeLines(7)
        mode = "login"

    elif mode == "exit":
        print("Goodbye")
        time.sleep(0.5)
        os.system("cls" if os.name == "nt" else "clear")
        exit()
        

    
user = username_input

copyDataToTemp(user)

removeLines(4)

while True:
    printUserInterface()
    func = getInput()
    if func in ["save", "view", "s", "v"]:
        break
    input("Command doesn't exist\nPress enter to continue...")
    removeLines(4)

removeLines(7)

