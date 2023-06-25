import requests

endpoint = "http://10.10.10.20:8000/api/auth/login/"

response= requests.post(endpoint, json={
    "email":"elijahwalter2018@gmail.com",
    "password":"azerty"})

print(response.text)