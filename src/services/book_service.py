from json.encoder import INFINITY
from typing import TYPE_CHECKING, List

import config.database as _database
import models.book_model as _models
import schemas.book as _schemas

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

def _add_tables():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def create_books(book:_schemas.CreateBook, db: "Session"
) -> _schemas.Book:
    book = _models.Book(**book.dict())
    db.add(book)
    db.commit()
    db.refresh(book)
    return _schemas.Book.from_orm(book)

async def get_all_books(db:"Session")->List[_schemas.Book]:
    books = db.query(_models.Book).all()
    return list(map(_schemas.Book.from_orm,books))