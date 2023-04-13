import requests
import json

url = 'http://localhost:8000/api/messagerie/new_messages/'  # remplacer par l'URL de votre serveur

data = {
    'sender': 1,  # remplacer par l'ID de l'utilisateur qui envoie le message
    'recipient': 2,  # remplacer par l'ID de l'utilisateur destinataire
    'content': 'Bonjour, comment ça va?'  # contenu du message
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.status_code)
print(response)
