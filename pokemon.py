import requests
from datetime import date

def get_pokemon_of_the_day(total_pokemon=1010):
    today = date.today()
    day_number = today.toordinal()
    pokemon_id = (day_number % total_pokemon) + 1  # PokeAPI IDs start at 1
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    return response.json()

pokemon = get_pokemon_of_the_day()
print(pokemon["name"], pokemon["id"])