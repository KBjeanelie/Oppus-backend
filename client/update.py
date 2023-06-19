import requests

# Endpoint pour la mise à jour du profil de l'employeur
url = "http://10.10.10.20:8000/api/gestion/compte/employeurs/339/"

# Données à mettre à jour
data = {
    "prenom": "Jean-Élie",
    "nom": "KUBEMBULA"
}

# Token d'authentification de l'employeur
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3MjEzMDkzLCJpYXQiOjE2ODcyMDIyOTMsImp0aSI6ImM5MzI3MDM0Nzg3MzQ0OTM5YTYwZTc3ZTgxYzFlNjcwIiwidXNlcl9pZCI6MzM2fQ.yBais7Q2lgh1I23h-JuRVHWn4oiyE_3hAnRTy50tMbI'

# En-tête d'authentification avec le token
headers = {
    "Authorization": f"Bearer {token}"
}

# Envoi de la requête PATCH
response = requests.patch(url, data=data, headers=headers)

# Vérification de la réponse
if response.status_code == 200:
    updated_data = response.json()
    print("Champs mis à jour avec succès :", updated_data)
else:
    print("Erreur lors de la mise à jour :", response.text)
