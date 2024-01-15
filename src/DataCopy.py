# Author: Lucas Axberg
# Description: ?

import json

def copyDataToTemp(user):
    
    with open("GetData.json", "r", encoding="utf-8") as file:
        data = json.loads(file.read())

    user_accounts_data = data["users"][user]
    formatted_user_data = json.dumps(user_accounts_data)
    
    with open("CurrentUser.json", "w", encoding="utf-8") as temp_file:
        temp_file.write(formatted_user_data)   

copyDataToTemp("User")
