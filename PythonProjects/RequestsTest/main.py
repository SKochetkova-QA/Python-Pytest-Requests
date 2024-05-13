import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'd578520967f8fef58c624a910fa813cb'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "Квоока",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

body_change = {
    "pokemon_id": '27187',
    "name": "Binni",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

id = {
    "pokemon_id": '27187'
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

pokemon_id = '27187'
print(pokemon_id)

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = id)
print(response_pokeball.text)