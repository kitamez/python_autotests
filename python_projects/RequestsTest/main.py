import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '4c6a62dfc800ad9fbc0ba8c3cffdbe78'
HEADER = {'Content-type': 'application/json', 'trainer_token': TOKEN}

# Создание покемона и вывод результата
create_pokemon = requests.post (
    url = f'{URL}/pokemons',
    headers = HEADER,
    json = {
        "name": "Паганини",
        "photo_id": 400
        }
)
print(create_pokemon.text)

# Сохранение ID созданного покемона в переменную pokemon_id
POKEMON_ID = create_pokemon.json()["id"]
print(POKEMON_ID)

# Смена имени покемона и вывод результата
rename_pokemon = requests.put (
    url = f'{URL}/pokemons', 
    headers = HEADER, 
    json = {
        "pokemon_id": f"{POKEMON_ID}",
        "name": "Валера",
        "photo_id": 200
    }
)
print(rename_pokemon.text)

# Поймать покемона в покебол и вывести результат
pokeball_pokemon = requests.post (
    url = f'{URL}/trainers/add_pokeball', 
    headers = HEADER, 
    json = {
        "pokemon_id": f"{POKEMON_ID}"
        }
)
print(pokeball_pokemon.text)

'''# Проведение битвы и вывод результата
battle_pokemons = requests.post (
    url = f'{URL}/battle', 
    headers = HEADER, 
    json = {
        "attacking_pokemon": f"{pokemon_id}",
        "defending_pokemon": "?"
        }
)
print(battle_pokemons.text)'''

'''# Отправить покемона в нокаут и вывести результат
knockout_pokemon = requests.post (
    url = f'{URL}/pokemons/knockout', 
    headers = HEADER, 
    json = {
        "pokemon_id": f"{pokemon_id}"
        }
)
print(knockout_pokemon.text)'''
