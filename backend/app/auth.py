"""Authentication helpers: password hashing + JWT tokens.  ← shared (step 4).

Auth is fiddly and security-sensitive, so here are the pieces you need and
what each should do. Fill in the bodies — the libraries do the hard parts.

Useful docs:
  - passlib (hashing):  https://passlib.readthedocs.io/
  - python-jose (JWT):  https://github.com/mpdavis/python-jose
  - FastAPI security tutorial (THE thing to read):
        https://fastapi.tiangolo.com/tutorial/security/
"""
from passlib.context import CryptContext

# CHANGE THIS and move it to an env var (.env) before you ever deploy.
SECRET_KEY = "dev-only-change-me"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(plain: str) -> str:
    """Return a bcrypt hash of the password."""
    # TODO: return pwd_context.hash(plain)
    raise NotImplementedError


def verify_password(plain: str, hashed: str) -> bool:
    """Check a plain password against a stored hash."""
    # TODO: return pwd_context.verify(plain, hashed)
    raise NotImplementedError


def create_access_token(data: dict) -> str:
    """Encode a signed JWT containing `data` (e.g. {"sub": username}).

    TODO:
      - copy `data`, add an "exp" claim (now + ACCESS_TOKEN_EXPIRE_MINUTES)
      - return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    """
    raise NotImplementedError


# TODO (after the above work): write a get_current_user dependency that reads
# the token from the request, decodes it, and looks the user up in the DB.
# The FastAPI security tutorial linked above walks through this exactly.
