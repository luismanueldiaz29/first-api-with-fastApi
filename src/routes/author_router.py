from typing import List
from fastapi import APIRouter
import fastapi as _fastapi
import schemas.author as _schemas

import sqlalchemy.orm as _orm
import services.author_service as _services

author_route = APIRouter()

@author_route.post("/api/authors/", response_model=_schemas.Author)
async def create_cotact(
    author:_schemas.CreateAuthor,
    db:_orm.Session = _fastapi.Depends(_services.get_db)
):
    return await _services.create_authors(author=author, db=db)

@author_route.get("/api/authors/", response_model=List[_schemas.Author])
async def get_authors(db:_orm.Session =_fastapi.Depends(_services.get_db)):
    return await _services.get_all_authors(db=db)

@author_route.get("/api/authors/{id}", response_model=_schemas.Author)
async def get_authors(id:str, db:_orm.Session =_fastapi.Depends(_services.get_db)):
    return await _services.get_by_id(id=id, db=db)

@author_route.delete("/api/authors/{id}", response_model=_schemas.Author)
async def get_authors(id:str, db:_orm.Session =_fastapi.Depends(_services.get_db)):
    await _services.delete_by_id(id=id, db=db)
    return 'Item was deleted'