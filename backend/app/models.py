"""SQL tables (SQLAlchemy ORM models).  ← Marshall starts here (step 2).

Start with just User and Pokemon — enough for the first slice. Add the other
tables (Teams, Favorites, BattleHistory, Achievements, Collections,
DailyChallenges) LATER, once login + Pokédex work end-to-end.

The User model below is a worked example showing the pattern. Use it as a
template to finish the Pokemon model.
"""
from sqlalchemy import Column, Integer, String

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)  # never store plain passwords!
    # TODO: add created_at later if you want (see SQLAlchemy DateTime + func.now()).


class Pokemon(Base):
    __tablename__ = "pokemon"

    id = Column(Integer, primary_key=True, index=True)  # use the PokéAPI id
    name = Column(String, unique=True, index=True, nullable=False)
    # TODO: add the columns you'll actually display in the Pokédex, e.g.:
    #   - sprite_url (String)        the image to show
    #   - types (String)            "fire", "fire/flying", etc. (keep it simple first)
    #   - hp, attack, defense (Integer)   base stats for the radar chart later
    # Decide together with Marshall what the Pokédex card needs, then add it.


# TODO (much later): Team, Favorite, BattleHistory, ...
# These will use relationships (ForeignKey) back to User. Look up
# "SQLAlchemy relationship" when you get there — don't add them yet.
