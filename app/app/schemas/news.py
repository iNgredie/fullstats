from enum import Enum

from pydantic import BaseModel


class NewsVote(int, Enum):
    PLUS = 1
    NEUTRAL = 0
    MINUS = -1


class NewsBase(BaseModel):
    article: int
    slug: str
    title: str
    summary: str
    content: str
    views: int
    vote: NewsVote
    rating: int


class News(BaseModel):
    id: int

    class Config:
        orm_mode = True


class NewsCreate(BaseModel):
    ...


class NewsUpdate(BaseModel):
    ...
