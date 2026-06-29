"""Database setup: SQLAlchemy engine, session, and Base class.

This is boilerplate — you shouldn't need to change much here. The interesting
work is in models.py (defining tables) and the routers (using sessions).
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite lives in a single file next to the backend. Easy for development;
# swap this URL for Postgres later (e.g. when you add Docker).
SQLALCHEMY_DATABASE_URL = "sqlite:///./pokemon.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # check_same_thread is a SQLite-only quirk needed for FastAPI's threading.
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# All ORM models inherit from Base (see models.py).
Base = declarative_base()


def get_db():
    """FastAPI dependency: yields a DB session and always closes it.

    Use it in a route like:  def my_route(db: Session = Depends(get_db)):
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
