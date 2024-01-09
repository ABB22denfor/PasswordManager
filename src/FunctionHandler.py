#Dennis
'''Module for handling function calls'''

#Remove sys when implementation done
import sys

import importlib

functions = ["Save", "View"]

def main():
    printUserInterface()
    handleInput()

#Subject to move
def printUserInterface():
    print('''
Available commands
------------------
> Save new password
> View all passwords
------------------
          ''')

def handleInput():
    '''Compares user input to available modules then calls the function in appropiate module'''

    #Sys.argv is placeholder for InputHandler
    function = sys.argv[1]
    
    #Retry input if no match
    while function not in functions:
        function = input("> ")

    #Error-handling due to modules not fully iplemented
    try:
        #Imports module with same name as input
        module = importlib.import_module(function)
        
        #Run test function inside of said module
        module.test()
    except ModuleNotFoundError:
        pass

main()
