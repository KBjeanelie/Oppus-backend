import requests

# URL de base de votre API
base_url = "http://localhost:8000/api/"

# # Endpoint pour l'inscription d'un employeur
# employeur_register_url = base_url + "employeur/register/"

# # Données d'inscription d'un employeur
# employeur_data = {
#     "email": "employeur@example.com",
#     "username": "employeur1",
#     "tel": "123456789",
#     "password": "employeurpassword"
# }

# # Effectuer une requête POST pour l'inscription de l'employeur
# response = requests.post(employeur_register_url, json=employeur_data)
# if response.status_code == 201:
#     print("Inscription de l'employeur réussie!")
# else:
#     print("Échec de l'inscription de l'employeur.")

# # Endpoint pour l'inscription d'un worker
# worker_register_url = base_url + "worker/register/"

# # Données d'inscription d'un worker
# worker_data = {
#     "email": "worker@example.com",
#     "username": "worker1",
#     "tel": "987654321",
#     "password": "workerpassword",
#     "metier": "ouvrier"
# }

# # Effectuer une requête POST pour l'inscription du worker
# response = requests.post(worker_register_url, json=worker_data)
# if response.status_code == 201:
#     print("Inscription du worker réussie!")
# else:
#     print("Échec de l'inscription du worker.")

# Endpoint pour la connexion de l'utilisateur
login_url = base_url + "login/"

# Données de connexion d'un employeur
login_data = {
    "email": "walter@gmail.com",
    "password": "azerty"
}

# Effectuer une requête POST pour la connexion de l'employeur
response = requests.post(login_url, json=login_data)
if response.status_code == 200:
    access_token = response.json()["token"]["access"]
    print("Connexion réussie! Token d'accès : ", access_token)
else:
    print("Échec de la connexion.")
