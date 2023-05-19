import requests

endpoint = "http://localhost:8000/api/auth/employeur/register/"

response= requests.post(endpoint, json={
    "email":"walter@gmail.com",
    "username":"walter II",
    "password":"azerty"})

print(response.text)