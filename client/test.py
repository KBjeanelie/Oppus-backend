import requests

url = "http://localhost:8000/api/gestion/offres/reservations/"

responses = requests.get(url)

print(responses.json())
