import requests

endpoint = "http://127.0.0.1:8000/api/ref-btp/domaines/"

response= requests.get(endpoint)
print(response.text)