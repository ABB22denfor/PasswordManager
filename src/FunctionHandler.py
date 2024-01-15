#Dennis
'''Module for handling function calls'''

#For dynamically importing modules
import importlib

#Allowed function calls
functions = ["save", "view", "s", "v"]

#Remove main later
def main():
    printUserInterface()
    handleInput()

def printUserInterface():
    '''Print usable commands'''

    print('''
Available Commands
------------------
> save new password
> view all passwords
------------------''')

def handleInput():
    '''Compares user input to available modules then calls the function in chosen module'''

    function = ""

    #Retry input if no match
    while function not in functions:
        function = input("> ").strip().lower()

    #Error-handling due to modules not fully iplemented
    try:
        callFunctionInModule(function, function, [])
    except ModuleNotFoundError:
        print("MODULENOTFOUND")

def callFunctionInModule(module: str, function: str, args: list):
    '''(module->str, function->str, args->list) Call function inside of module with specified args'''

    #Imports module with same name as input
    mod = importlib.import_module(module)

    print("Getting module" + module + function)

    #Get function from string parameter
    function = getattr(mod, function)

    #Call function with unspecified amount of args
    function(*args)

if __name__ == "__main__":
    main()
