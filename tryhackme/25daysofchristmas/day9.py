import requests
import json

BASE_IP = "http://10.10.169.100:3000/"

response = {"value":"s","next":"f"}
flag = ""
while response['next'] != "end":
    flag += response['value']
    url = BASE_IP + response['next']
    res = requests.get(url)
    response = json.loads(res.text)

    print(flag)
