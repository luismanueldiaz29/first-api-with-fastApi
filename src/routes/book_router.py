from typing import List
from fastapi import APIRouter
import fastapi as _fastapi
import schemas.book as _schemas

import sqlalchemy.orm as _orm
import services.book_service as _services

book_route = APIRouter()

@book_route.post("/api/books/", response_model=_schemas.Book)
async def create_cotact(
    book:_schemas.CreateBook,
    db:_orm.Session = _fastapi.Depends(_services.get_db)
):
    return await _services.create_books(book=book, db=db)

@book_route.get("/api/books/", response_model=List[_schemas.Book])
async def get_books(db:_orm.Session =_fastapi.Depends(_services.get_db)):
    return await _services.get_all_books(db=db)

@book_route.get("/api/books/{id}", response_model=_schemas.Book)
async def get_books(id:str, db:_orm.Session =_fastapi.Depends(_services.get_db)):
    return await _services.get_by_id(id=id, db=db)