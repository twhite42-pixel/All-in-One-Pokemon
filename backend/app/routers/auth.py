"""Auth routes: register + login.  ← shared (step 4).

Wire these up after you've filled in app/auth.py. When done, mount this router
in main.py with:  app.include_router(auth.router)
"""
from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])


# TODO: POST /auth/register
#   - takes a schemas.UserCreate
#   - hash the password (auth.hash_password)
#   - save a models.User to the DB (use the get_db dependency)
#   - return a schemas.UserOut
#
# @router.post("/register", response_model=UserOut)
# def register(payload: UserCreate, db: Session = Depends(get_db)):
#     ...


# TODO: POST /auth/login
#   - look up the user, verify the password (auth.verify_password)
#   - if good, return a Token from auth.create_access_token({"sub": user.username})
#   - if bad, raise HTTPException(status_code=401)
