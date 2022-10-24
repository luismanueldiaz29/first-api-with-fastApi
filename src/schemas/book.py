from schemas.author import Author
import pydantic as _pydantic
from typing import List, Optional

class _BaseBook(_pydantic.BaseModel):
    title: Optional[str] = None
    rating: Optional[str] = None
    author_id: Optional[int] = None

class Book(_BaseBook):
    book_id: Optional[int] = None
    author: Optional[Author] = None
    
    class Config:
        orm_mode = True

class CreateBook(_BaseBook):
    pass