import requests

url = "https://swapi.dev/api/starships/3"

data = requests.get(url).json()

print(f"I {data['name']}\'d your mom last night")