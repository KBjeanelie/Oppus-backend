import requests

endpoint = "http://127.0.0.1:8000/api/user/profile/"

response= requests.get(endpoint)
print(response.text)