"""Database configuration and session management.

This module provides a SQLAlchemy engine and session factory.  It uses
a synchronous engine for simplicity; if you wish to adopt async sessions,
replace ``create_engine`` with ``create_async_engine`` and adjust usages
accordingly.
"""
from __future__ import annotations

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://bidbrief:change_me@db:5432/bidbrief",
)

# Create the engine.  The echo flag may be toggled for debugging SQL queries.
engine = create_engine(DATABASE_URL, echo=False)

# Base class for models to inherit from.
Base = declarative_base()

# Session factory; use SessionLocal() to get a new session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)