import requests

response = requests.get(url="http://localhost:5040/animals")

print(response.status_code)
print(response.json())
print(response.headers)
