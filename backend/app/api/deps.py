from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

def get_db() -> Generator[Session, None, None]:
    """
    Dependency for FastAPI routes to get a SQLAlchemy session.

    Yields:
        Session: a SQLAlchemy session, closed after the request
    """

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()