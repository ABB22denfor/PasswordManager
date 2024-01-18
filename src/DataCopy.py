# Author: Lucas Axberg
# Description: ?

import json
import os

def copyDataToTemp(user):

    absolute_path = os.path.dirname(os.path.abspath(__file__)) 
    
    with open(absolute_path + "/UserData.json", "r", encoding="utf-8") as file:
        data = json.loads(file.read())

    user_accounts_data = data["users"][user]
    formatted_user_data = json.dumps(user_accounts_data)
    
    with open(absolute_path + "/CurrentUser.json", "w", encoding="utf-8") as temp_file:
        temp_file.write(formatted_user_data)   

