import datetime as _dt
import pydantic as _pydantic
from typing import List, Optional

class _BaseAuthor(_pydantic.BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None

class Author(_BaseAuthor):
    author_id: Optional[int] = None
    
    class Config:
        orm_mode = True

class CreateAuthor(_BaseAuthor):
    pass