import requests

endpoint = "http://localhost:8000/api/auth/worker/register/"

response= requests.post(endpoint, json={
    "email":"worker.cg@gmail.com",
    "username":"worker.cg",
    'metier': 65,
    "password":"azerty"})

print(response.text)