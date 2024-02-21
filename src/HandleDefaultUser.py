import json
import os

from ReadData import readFile
from login import login

def setDefaultUser(args: list):
    data = readFile("UserData.json")

    input()

    if login(args[2], args[3]):
        data["default_user"] = [args[2], args[3]]
        with open(os.path.dirname(os.path.abspath(__file__)) + "/../data/UserData.json", "w", encoding="UTF-8") as f:
            f.write(json.dumps(data))

def getDefaultUser():
    return readFile("UserData.json")["default_user"]
