import requests

endpoint = "http://localhost:8000/api/auth/login/"

response= requests.post(endpoint, json={
    "email":"walter@gmail.com",
    "password":"azerty"})

print(response.text)