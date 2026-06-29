"""Client for the PokéAPI (https://pokeapi.co/).  ← step 3, either of you.

This is your "API integration" piece. Keep all external-API logic in here so
the rest of the app just calls clean functions and never knows about HTTP.

PokéAPI is free and needs no key. Try it in your browser first:
    https://pokeapi.co/api/v2/pokemon/pikachu

Be a good citizen: cache results in your own DB (the Pokemon table) so you're
not hammering PokéAPI on every request.
"""
import httpx

BASE_URL = "https://pokeapi.co/api/v2"


async def fetch_pokemon(name_or_id: str) -> dict:
    """Fetch one Pokémon's raw data from PokéAPI.

    TODO:
      - async with httpx.AsyncClient() as client:
            resp = await client.get(f"{BASE_URL}/pokemon/{name_or_id}")
      - resp.raise_for_status()
      - return resp.json()
    Then look at the JSON and decide which fields you actually need
    (name, id, sprites.front_default, types, stats) for your Pokemon model.
    """
    raise NotImplementedError


# TODO (step 5 helper): a function that fetches a Pokémon, maps the big PokéAPI
# JSON down to just your columns, and saves/returns a models.Pokemon row.
