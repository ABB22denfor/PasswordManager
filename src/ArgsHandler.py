from HandleDefaultUser import getDefaultUser, setDefaultUser

def handleArgs(args: list = []):
    
    try:
        if args[1] == "-u":
            pass
        default_user = getDefaultUser()
    except KeyError:
        print("ERROR: Default User Not Set. passman -u <username> <password> to set defaults")

    match args[1]:
        case "-v":
            print("View")
        case "-c":
            print("Create")
        case "-e":
            print("Edit")
        case "-d":
            print("Delete")
        case "-u":
            setDefaultUser(args)
        case _:
            return 1
    return 0

