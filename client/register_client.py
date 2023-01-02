import requests

endpoint = "http://127.0.0.1:8000/api/user/register-client/"
data = {
    "email":"test@gmail.com",
    "username":"test",
    "password":"test",
    "password2":"testa",
    "is_client":True}

response= requests.post(endpoint, json={
    "email":"test@gmail.com",
    "username":"test",
    "password":"test"})
print(response.json)