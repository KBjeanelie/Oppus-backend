import requests

url = "http://10.10.10.20:8000/api/referentiel-btp/travaux/2/"
header = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NzQwNzE3LCJpYXQiOjE2ODc3Mjk5MTcsImp0aSI6IjI4ZTY1NTJkYjAyNjQyNWI5YTZhZmI5MGFiYzE5OGIwIiwidXNlcl9pZCI6MzUxfQ.0XtjzsNDgM6mzEebk6uhsutM7Hy1QCH8hkH8gm4WAz8"

head = {
    "Authorization" : f"Bearer {header}"
}
# Données de l'offre à créer
# data_offre = {
#     'jour': '2023-06-30',
#     'heure': '09:00:00',
#     'description': 'Offre de travail',
#     'lieu': 'Brazzaville',
#     'id_domaine': 6,  # ID du domaine associé à l'offre
#     'id_travaux': 22,  # ID du travail associé à l'offre
# }


responses = requests.get(url)

print(responses.json())
