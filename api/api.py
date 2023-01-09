import urllib.request
import json

url= "https://swapi.dev/api/starships/3"

foo = urllib.request.urlopen(url)

uggo = foo.read()

cleanedup = uggo.decode("utf-8")

data = json.loads(cleanedup)

print(data["name"])