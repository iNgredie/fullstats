from sqlalchemy import Column, Integer, String, Text, ForeignKey

from app.db.base_class import Base


class News(Base):
    """News."""

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    article = Column(Integer)
    slug = Column(String(length=150), unique=True)
    title = Column(String(length=150))
    summary = Column(String(250))
    content = Column(Text)
    views = Column(Integer, default=0)
    vote = Column(Integer)
    rating = Column(Integer, default=0)
