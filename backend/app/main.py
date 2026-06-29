"""FastAPI app entry point.

Run it from the backend/ directory with:
    uvicorn app.main:app --reload

Then visit http://127.0.0.1:8000/docs for the interactive API docs.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine

# Create tables on startup. (Fine for development. For real migrations later,
# look into Alembic — but don't worry about that yet.)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Pokémon Universe API")

# Let the React dev server (http://localhost:5173) call this API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    """Sanity-check endpoint. If this returns ok, your skeleton runs."""
    return {"status": "ok"}


# TODO (step 4 & 5): once you've written the routers, mount them here, e.g.
#   from app.routers import auth, pokemon
#   app.include_router(auth.router)
#   app.include_router(pokemon.router)
