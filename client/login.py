import requests
import random


# URL de base de votre API
base_url = "http://192.168.1.74:8000/api/"

# Endpoint pour l'inscription d'un employeur
# employeur_register_url = base_url + "employeur/register/"

# # Données d'inscription d'un employeur
# employeur_data = {
#     "email": "employeur@example.com",
#     "username": "employeur1",
#     "password": "employeurpassword"
# }

# # Effectuer une requête POST pour l'inscription de l'employeur
# response = requests.post(employeur_register_url, json=employeur_data)
# if response.status_code == 201:
#     print("Inscription de l'employeur réussie!")
# else:
#     print("Échec de l'inscription de l'employeur.")

# Endpoint pour l'inscription d'un worker
# worker_register_url = base_url + "worker/register/"

# # Données d'inscription d'un worker
# worker_data = {
#     "email": "worker@example.com",
#     "username": "worker1",
#     "password": "workerpassword",
#     "metier": 35
# }

# # Effectuer une requête POST pour l'inscription du worker
# print(worker_data)
# response = requests.post(worker_register_url, json=worker_data)
# if response.status_code == 201:
#     print("Inscription du worker réussie!")
# else:
#     print("Échec de l'inscription du worker.")

# # Endpoint pour la connexion de l'utilisateur
login_url = "http://localhost:8000/api/auth/login/"

# Données de connexion d'un employeur
login_data = {
    "email": "worker@gmail.com",
    "password": "azerty"
}

# Effectuer une requête POST pour la connexion de l'employeur
response = requests.post(login_url, json=login_data)
if response.status_code == 200:
    access_token = response.json()
    print("Connexion réussie! Token d'accès : ", access_token)
else:
    print(response.json())
    print("Échec de la connexion.")


# # CREATION DE 30 OUVRIER ALÉATOIREMENT
# worker_register_url = base_url + "worker/register/"

# metiers = [35, 36, 37, 38, 39, 40, 45, 59, 60, 43, 100, 89, 80, 65, 55, 51,52, 93, 70, 101]  # Liste des IDs de métiers possibles
# total_ouvriers = 30  # Nombre total d'ouvriers à inscrire

# for i in range(total_ouvriers):
#     worker_data = {
#         "email": f"Ouvrier{i+1}@example.com",
#         "username": f"ouvrier{i+1}",
#         "password": "workerpassword",
#         "metier": random.choice(metiers)
#     }

#     response = requests.post(worker_register_url, json=worker_data)
#     if response.status_code == 201:
#         print(f"Inscription de l'ouvrier {i+1} réussie!")
#     else:
#         print(f"Échec de l'inscription de l'ouvrier {i+1}.")

# url = "http://localhost:8000/api/workers/20"
# response = requests.get(url)
# print(response.text)