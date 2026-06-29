# Pokémon Universe

A full-stack Pokémon app: log in, browse a Pokédex, build teams, simulate battles,
and explore analytics. Built as a two-person portfolio project.

- **Torie** — frontend (React), Rust battle engine, animations, Docker
- **Marshall** — database schema, backend logic, analytics, charts
- **Shared** — auth, API integrations, code reviews, testing, deployment

---

## The plan: build ONE thin slice first

Don't build module-by-module. Build the smallest thing that touches the whole stack,
get it working end-to-end, then widen it.

**First slice → "Log in, then browse the Pokédex."**
It exercises the database, auth, the backend API, the PokéAPI integration, and the
React frontend. Every other module reuses this same pattern.

> The Rust battle engine comes LATER. Build the Battle Simulator in Python first,
> get it working, then port the hot loop to Rust as a showcase optimization.

## Build order for the first slice

Each file is a stub with `TODO`s explaining what to write. Tackle them in this order:

1. `backend/app/database.py` — SQLAlchemy engine + session  *(done — read it)*
2. `backend/app/models.py` — `User` + `Pokemon` tables  *(Marshall)*
3. `backend/app/services/pokeapi.py` — fetch a Pokémon from PokéAPI  *(either)*
4. `backend/app/auth.py` + `routers/auth.py` — register + login  *(shared)*
5. `backend/app/routers/pokemon.py` — list + detail endpoints  *(Marshall)*
6. `backend/app/main.py` — wire it together  *(done — read it, then run it)*
7. `frontend/` — login page, then Pokédex page  *(Torie — scaffold below)*

When step 7 shows a list of Pokémon after logging in, the stack is proven.

---

## Day 1: get the backend running

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open http://127.0.0.1:8000/docs — you'll see the interactive API docs and a
working `/health` endpoint. That's your proof the skeleton runs. Now start filling
in the `TODO`s from the build order above.

## Day 1: scaffold the frontend (Torie)

We left this for you to create yourself with Vite:

```bash
npm create vite@latest frontend -- --template react-ts
cd frontend
npm install
npm run dev
```

Then build `src/api/client.ts`, `src/pages/Login.tsx`, and `src/pages/Pokedex.tsx`.

---

## Stack

- **Backend:** FastAPI + SQLAlchemy, **SQLite to start** (swap to Postgres via Docker later)
- **Frontend:** React + Vite + TypeScript
- **Data:** PokéAPI first; add PokeTCG / Weather / AI APIs as stretch goals
- **Later:** Rust battle engine, Docker, CI/CD
