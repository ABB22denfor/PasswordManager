# Imports modules
import os

from login import login
from PrintInfo import printHeader, removeLines
from Signup import signup
from DataCopy import copyDataToTemp
from InputHandler import getInput
from FunctionHandler import printUserInterface

# Main code
os.system("cls" if os.name == "nt" else "clear")

printHeader()
print("login/signup")
print("".center(30, "-"))

mode = input("select >")
removeLines(3)


while True:
    if mode == "login":
        print("login".center(30) + "\n" + "".center(30, "-"))
        username_input = input("Username > ")
        password_input = input("Password > ")

        if login(username_input, password_input):
            break
        
        input("Username or password doesn't match\nPress enter to continue...")
        removeLines(6)
        
    elif mode == "signup":
        print("signup".center(30) + "\n" + "".center(30, "-"))
        signup()
        input("Press enter to continue...")
        removeLines(7)
        mode = "login"
    
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

