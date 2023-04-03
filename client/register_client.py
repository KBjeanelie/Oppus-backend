import requests

endpoint = "http://127.0.0.1:8000/api/user/register-client/"

response= requests.post(endpoint, json={
    "email":"test@gmail.com",
    "username":"test",
    'tel':'064838870',
    "password":"test"})
print(response.json)