"""Database engine and session factory (Energy Database container, SQLite)."""
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from src.backend.app.config import settings

engine = create_engine(settings.database_url, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    """Base class for the ORM models in models.py."""


def get_session():
    """FastAPI dependency that yields a DB session and always closes it."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
