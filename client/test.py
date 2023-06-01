import requests

url = "http://10.10.10.20:8000/api/referentiel-btp/travaux/1/by_domaine/"
header = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg0ODgxMzQ2LCJpYXQiOjE2ODQ4Nzk1NDYsImp0aSI6IjM0ODAwYzQxNTY0ZDQ2YzQ5ZjcwNmNmMjA4ODJjYmVkIiwidXNlcl9pZCI6MzM5fQ.90nWY0fNpHaxdJdzx-SR4VhsV95_M0BlNtl813mOFSU";
headers = {
    "Authorization" : f"Bearer {header}"
}
responses = requests.get(url)

print(responses.json())
