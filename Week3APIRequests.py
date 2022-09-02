
import requests

endpoint = "https://pokeapi.co/api/v2/pokemon/1"

response = requests.get(endpoint)
data = response.json()

with open ('pokemon.txt', 'w') as file:
    for name in data['forms']:
        file.write("Your pokemon name and moves are:" + '\n' + name['name'] + '\n')

with open ('pokemon.txt', 'a') as file:
    for move in data['moves']:
        file.write(move['move']['name'] + '\n')
