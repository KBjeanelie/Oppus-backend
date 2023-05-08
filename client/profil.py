import requests

#endpoint = "http://127.0.0.1:8000/api/ref-btp/domaines/"
endpoint = "http://127.0.0.1:8000/api/gest_qual_ouvrier/formations/"
response= requests.get(endpoint)
print(response.text)