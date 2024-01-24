#Dennis
'''Module for handling function calls'''

#For dynamically importing modules
import importlib

def printUserInterface():
    '''Print usable commands'''

    print('''Available Commands
------------------
> save new password
> view all passwords
------------------''')

def handleInput(user_input: str):
    '''(user_input: str)
    Compares user input to available modules then calls the function in chosen module'''

    if user_input in ['save', 's']:
        function = "createAccount"
        module = "AccountCreator"
    else:
        function = "chooseAccount"
        module = "ChooseAccountToView"

    return callFunctionInModule(module, function, [])

def callFunctionInModule(module: str, function: str, args: list):
    '''(module: str, function: str, args: list)
    Call function inside of module with specified args'''

    #Imports module with same name as input
    mod = importlib.import_module(module)

    #Get function from string parameter
    function = getattr(mod, function)

    return (function, args)
