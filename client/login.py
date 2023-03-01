import requests

endpoint = "http://127.0.0.1:8000/api/user/login/"

response= requests.post(endpoint, json={"email":"walter@gmail.com", "password":"azerty"})
print(response.json)