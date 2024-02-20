import jwt
import os
import json


def encodeJSON(path: str):
    encoded = ""
    data = ""
    with open(os.path.dirname(os.path.abspath(__file__)) + path, encoding="UTF-8") as f:
        data = json.loads(f.read())

    encoded = jwt.encode(data, "secret", algorithm="HS256")

    with open(os.path.dirname(os.path.abspath(__file__)) + path, "w", encoding="UTF-8") as f:        
        f.write(encoded)

def decodeJSON(path: str):
    decoded = ""
    with open(os.path.dirname(os.path.abspath(__file__)) + path, encoding="UTF-8") as f:
        decoded = jwt.decode(f.read(), "secret", algorithms="HS256")

    with open(os.path.dirname(os.path.abspath(__file__)) + path, "w", encoding="UTF-8") as f:
        f.write(json.dumps(decoded))
