import requests

url = "http://localhost:8000/api/auth/employeur/get-current-user/"
header = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg0ODc3MTk5LCJpYXQiOjE2ODQ4NzUzOTksImp0aSI6IjRlY2UzYTA0MGRkMTQ2NjA5MTcxYTgzMTQ4YjJhYTE3IiwidXNlcl9pZCI6MzM5fQ.doxsJ6saJ9mnWZyLtARDO5fL4upSC4nvKvwZWERwqgc";
headers = {
    "Authorization" : f"Bearer {header}"
}
responses = requests.get(url, headers=headers)

print(responses.json())
