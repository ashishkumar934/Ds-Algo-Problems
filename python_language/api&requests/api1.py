import requests
#response=requests.get("https://randomuser.me/api")
response=requests.get("https://randomuser.me/api")
print(response)
print(response.text)