"""Pokédex routes: list + detail.  ← Marshall (step 5).

Mount in main.py with:  app.include_router(pokemon.router)
"""
from fastapi import APIRouter

router = APIRouter(prefix="/pokemon", tags=["pokemon"])


# TODO: GET /pokemon/{name_or_id}
#   - check your DB first (caching). If missing, call services.pokeapi.fetch_pokemon,
#     map it to a models.Pokemon, save it, then return it as a PokemonOut.
#
# TODO: GET /pokemon  (list)
#   - return the Pokémon you've cached so far (add pagination later).
#
# Build the detail endpoint FIRST — it's what proves the PokéAPI integration
# works. The list endpoint is easy once you have data in the table.
