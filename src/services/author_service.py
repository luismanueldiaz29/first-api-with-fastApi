from json.encoder import INFINITY
from select import select
from typing import TYPE_CHECKING, List

import config.database as _database
import models.author_model as _models
import schemas.author as _schemas

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

async def create_authors(author:_schemas.CreateAuthor, db: "Session"
) -> _schemas.Author:
    author = _models.Author(**author.dict())
    db.add(author)
    db.commit()
    db.refresh(author)
    return _schemas.Author.from_orm(author)

async def get_all_authors(db:"Session")->List[_schemas.Author]:
    authors = db.query(_models.Author).all()
    return list(map(_schemas.Author.from_orm,authors))


async def get_by_id(id: str,  db:"Session"):
    print('Ide -> '+id)
    return db.query(_models.Author).filter(_models.Author.author_id == id).first()


async def delete_by_id(id: str,  db:"Session"):
    authors = db.query(_models.Author).get(id)
    db.delete(authors)
    db.commit()

