import requests

url = "http://localhost:8000/api/gestion/messagerie/"
header = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg0ODgxMzQ2LCJpYXQiOjE2ODQ4Nzk1NDYsImp0aSI6IjM0ODAwYzQxNTY0ZDQ2YzQ5ZjcwNmNmMjA4ODJjYmVkIiwidXNlcl9pZCI6MzM5fQ.90nWY0fNpHaxdJdzx-SR4VhsV95_M0BlNtl813mOFSU";
headers = {
    "Authorization" : f"Bearer {header}"
}
responses = requests.get(url, headers=headers)

print(responses.json())
