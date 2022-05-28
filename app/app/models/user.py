from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class User(Base):
    """User."""

    id = Column(Integer, primary_key=True)
    email = Column(String(length=255), unique=True)
    username = Column(String(length=255), unique=True)
    password_hash = Column(String(length=255))
