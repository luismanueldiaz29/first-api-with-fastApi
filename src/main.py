from typing import TYPE_CHECKING,List
import fastapi as _fastapi
import schemas.author as _schemas

import sqlalchemy.orm as _orm
import services.service as _services
from fastapi.middleware.cors import CORSMiddleware

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

app = _fastapi.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/authors/", response_model=_schemas.Author)
async def create_cotact(
    author:_schemas.CreateAuthor,
    db:_orm.Session = _fastapi.Depends(_services.get_db)
):
    return await _services.create_authors(author=author, db=db)

@app.get("/api/authors/", response_model=List[_schemas.Author])
async def get_authors(db:_orm.Session =_fastapi.Depends(_services.get_db)):
    return await _services.get_all_authors(db=db)