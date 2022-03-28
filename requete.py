import requests
import json

url = "https://imdb-api.com/en/API/Top250Movies/k_12345678"

reponse = requests.get(url)
contenu = reponse.json()


fileName = "my-data.json"
jsonString = json.loads(contenu.items)

file = open(fileName, "w")
json.dump(jsonString, file)
file.close()