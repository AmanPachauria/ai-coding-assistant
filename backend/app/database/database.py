import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

BASE_DIR = Path(__file__).resolve().parents[2]
dotenv_path = BASE_DIR / ".env"

print("Loading .env from:", dotenv_path)

load_dotenv(dotenv_path)

DATABASE_URL = os.getenv("DATABASE_URL")

print("DATABASE_URL =", DATABASE_URL)

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set.")


# Create SQLAlchemy Engine
engine = create_engine(DATABASE_URL)


# Create a Session Factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base class for all database models
Base = declarative_base()