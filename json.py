import requests
import json

jsonTestUrl = "https://jsonplaceholder.typicode.com/users"

resp = requests.get(jsonTestUrl)
jsonStr = resp.text

x = json.loads(jsonStr)

print(x)
