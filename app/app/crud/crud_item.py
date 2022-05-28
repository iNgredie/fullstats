from typing import List

from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from .. import models
from .. import schemas
from app.db.session import get_db


class CRUDNews:

    def __init__(
        self,
        model: models.News(),
        session: Session = Depends(get_db),
    ):
        self.model = model
        self.session = session

    def create_with_owner(
        self, db: Session, *, obj_in: schemas.NewsCreate, owner_id: int
    ) -> models.News:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, author_id: int, skip: int = 0, limit: int = 100
    ) -> List[models.News]:
        return (
            db.query(self.model)
            .filter(models.News.owner_id == author_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

