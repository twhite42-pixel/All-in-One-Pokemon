"""Pydantic schemas: define the SHAPE of API requests & responses.

Models (models.py) = how data is stored in the DB.
Schemas (this file) = how data goes in/out of the API as JSON.
Keeping them separate lets you hide fields like hashed_password from responses.
"""
from pydantic import BaseModel


# --- Example for the User flow (finish these during step 4) ---

class UserCreate(BaseModel):
    """Body for POST /auth/register."""
    username: str
    email: str
    password: str  # plain text on the way IN; you hash it before saving.


class UserOut(BaseModel):
    """What you send back about a user — note: NO password field."""
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True  # lets Pydantic read from a SQLAlchemy object


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# TODO (step 5): add a PokemonOut schema mirroring the columns you put in
# models.Pokemon, so the Pokédex endpoint can return clean JSON.
