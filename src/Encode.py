import jwt
import os
import json

PATH = "/../data/UserData.json"

def encodeJSON():
    encoded = ""
    data = ""
    with open(os.path.dirname(os.path.abspath(__file__)) + PATH, encoding="UTF-8") as f:
        data = json.loads(f.read())

    encoded = jwt.encode(data, "secret", algorithm="HS256")

    with open(os.path.dirname(os.path.abspath(__file__)) + PATH, "w", encoding="UTF-8") as f:        
        f.write(encoded)

def decodeJSON():
    decoded = ""
    with open(os.path.dirname(os.path.abspath(__file__)) + PATH, encoding="UTF-8") as f:
        decoded = jwt.decode(f.read(), "secret", algorithms="HS256")

    with open(os.path.dirname(os.path.abspath(__file__)) + PATH, "w", encoding="UTF-8") as f:
        f.write(json.dumps(decoded))
    


encodeJSON()
decodeJSON()
