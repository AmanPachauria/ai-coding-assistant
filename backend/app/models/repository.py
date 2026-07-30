from datetime import datetime

from sqlalchemy import BigInteger, Column, DateTime, Integer, String, Text

from app.database.database import Base


class Repository(Base):
    __tablename__ = "repositories"

    id = Column(Integer, primary_key=True, index=True)

    github_id = Column(BigInteger, unique=True, nullable=False)

    owner = Column(String, nullable=False)

    name = Column(String, nullable=False)

    description = Column(Text, nullable=True)

    language = Column(String, nullable=True)

    stars = Column(Integer, default=0)

    forks = Column(Integer, default=0)

    default_branch = Column(String, nullable=False)

    clone_url = Column(String, nullable=False)

    status = Column(String, default="PENDING")

    created_at = Column(DateTime, default=datetime.utcnow)