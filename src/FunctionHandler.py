#Author: Dennis Forslund

'''Module for handling function calls'''

#For dynamically importing modules
import importlib

def printUserInterface():
    '''Print usable commands'''

    print("Available Commands".center(30))
    print('''------------------------------
> s | save new account
> v | view all accounts
> e | edit an account
> d | delete an account
------------------------------''')

def handleInput(user_input: str):
    '''(user_input: save or view from InputHandler)
    Compares user input to available modules then calls the function in chosen module'''
    
    # Hard coded values, error checking handled in main 
    if user_input in ['save', 's']:
        function = "createAccount"
        module = "AccountCreator"
    else:
        function = "chooseAccount"
        module = "ChooseAccountToView"

    return callFunctionInModule(module, function, [])

def callFunctionInModule(module: str, function: str, args: list = []):
    '''(module: name of module containing function, function: name of function, args: list of arguments to be used with function)
    Call function inside of module with specified args'''

    #Imports module with same name as input
    mod = importlib.import_module(module)

    #Get function from string parameter
    function = getattr(mod, function)

    return (function, args)
