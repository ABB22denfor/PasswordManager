# Lysander

from DataCopy import copyDataToTemp
import os
import json


def getCurrentData(path):
    '''Gets the current data'''

    current_data = open(path + "/CurrentUser.json")
    current_data_list = json.loads(current_data.read())
    current_data.close()

    return current_data_list

def getUserData(path):
    '''Gets the data from UserData'''

    user_data = open(path + "/UserData.json")
    user_data_list = json.loads(user_data.read())
    user_data.close()

    return user_data_list

def saveData(path, new_data):
    '''Saves the data'''

    user_data = open(path + "/UserData.json", "w")
    user_data.write(json.dumps(new_data))
    user_data.close()

    


def writeData(new_data, user):
    '''Get the current data and add the new data to it and then add the current data to UserData.json'''

    path = os.path.dirname(os.path.abspath(__file__))

    current_data_list = getCurrentData(path)
    current_data_list.append(new_data)
    
    try:
        user_data_list = getUserData(path)
        user_data_list["users"][user] = current_data_list

        saveData(path, user_data_list)

        copyDataToTemp(user)
    except KeyError:
        return False



new_data = {"username": "test", "password": "test", "account": "test"}
user = "Hej"

writeData(new_data, user)