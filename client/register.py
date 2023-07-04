import requests

endpoint = "http://127.0.0.1:8000/api/auth/employeur/get-current-user/"

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NzkxMjY0LCJpYXQiOjE2ODc3ODA0NjQsImp0aSI6IjY5YWY4ZjYwNjk5MDRiNzE4MjEzMzc4N2MwYWEyZjY1IiwidXNlcl9pZCI6MzUxfQ.641xa8aHAg6WYeU4fuBSOZrE5LPZYn689a6yAEFWJ_M"
# response= requests.post(endpoint, json={
#     "email":"elijahwalter2018@gmail.com",
#     "password":"azerty"})
head = {
    "Authorization" : f"Bearer {token}"
}
response = requests.get(endpoint, headers=head)
print(response.text)