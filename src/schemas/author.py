import datetime as _dt
import pydantic as _pydantic

class _BaseAuthor(_pydantic.BaseModel):
    name:str
    age:int
    gender:str

class Author(_BaseAuthor):
    author_id:int
    class Config:
        orm_mode = True

class CreateAuthor(_BaseAuthor):
    pass