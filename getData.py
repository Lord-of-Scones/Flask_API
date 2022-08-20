import requests

response = requests.get("http://127.0.0.1:5001/api/postgres/json")
print(response)

print(response.json().keys())
print(response.json()["people"])

for person in response.json()["people"]:
    print(person["name"] + "     " + person["craft"])
