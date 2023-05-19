import requests

endpoint = "http://localhost:8000/api/auth/worker/register/"

response= requests.post(endpoint, json={
    "email":"worker@gmail.com",
    "username":"worker II",
    'metier': 80,
    "password":"azerty"})

print(response.text)