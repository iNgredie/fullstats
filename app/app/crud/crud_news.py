from typing import List

from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from .. import models
from .. import schemas
from app.db.session import get_db


class CRUDNews:
    def __init__(
        self, model: models.News(), session: Session = Depends(get_db)
    ):
        self.model = model
        self.session = session

    def create_with_author(
        self, db: Session, *, obj_in: schemas.NewsCreate, author_id: int
    ) -> models.News:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, author_id=author_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_news_by_author(
        self, db: Session, *, author_id: int, skip: int = 0, limit: int = 100
    ) -> List[models.News]:
        return (
            db.query(self.model)
            .filter(models.News.author_id == author_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_one_news_by_author(
        self, db: Session, *, news_id: int, author_id: int
    ) -> models.News:
        return (
            db.query(self.model)
            .filter(models.News.author_id == author_id, models.News.id == news_id)
            .first()
        )

    def update_news_with_author(
        self, db: Session, *, obj_in: schemas.NewsCreate, news_id: int, author_id: int
    ) -> models.News:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.get_one_news_by_author(db, news_id=news_id, author_id=author_id)
        for field, value in obj_in_data:
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete_news_with_author(
        self, db: Session, *, news_id: int, author_id: int
    ) -> models.News:
        db_obj = self.get_one_news_by_author(db, news_id=news_id, author_id=author_id)
        db.delete(db_obj)
        db.commit()
        return db_obj
