import requests

endpoint = "http://127.0.0.1:8000/api/user/login/"

response= requests.post(endpoint, json={"email":"test@gmail.com", "password":"test"})
print(response.json)