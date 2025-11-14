"""Database connection and session management with SQLite fallback."""

import logging
from typing import Tuple

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import settings

logger = logging.getLogger(__name__)


def _build_engine(database_url: str):
    """Create an SQLAlchemy engine with sensible defaults."""
    connect_args = {"check_same_thread": False} if database_url.startswith("sqlite") else {}
    return create_engine(
        database_url,
        echo=settings.ENVIRONMENT == "development",
        pool_pre_ping=True,
        connect_args=connect_args,
    )


def _init_engine() -> Tuple[Engine, str]:
    """Attempt to connect to the primary DB, falling back to SQLite if needed."""
    primary_url = settings.DATABASE_URL
    fallback_url = settings.SQLITE_FALLBACK_URL

    primary_engine = _build_engine(primary_url)
    try:
        with primary_engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        logger.info("Connected to primary database: %s", primary_url)
        return primary_engine, primary_url
    except OperationalError as exc:
        logger.warning(
            "Primary database unavailable (%s). Falling back to SQLite (%s). Error: %s",
            primary_url,
            fallback_url,
            exc,
        )
        fallback_engine = _build_engine(fallback_url)
        return fallback_engine, fallback_url


# Create database engine (with automatic fallback)
engine, ACTIVE_DATABASE_URL = _init_engine()

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()


def get_db():
    """
    Dependency to get database session
    Usage: db: Session = Depends(get_db)
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
