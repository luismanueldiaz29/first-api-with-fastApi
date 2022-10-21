import pydantic as _pydantic

class _BaseBook(_pydantic.BaseModel):
    title:str
    rating:str
    author_id:int

class Book(_BaseBook):
    book_id:int
    class Config:
        orm_mode = True

class CreateBook(_BaseBook):
    pass