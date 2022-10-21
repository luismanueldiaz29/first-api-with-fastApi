from typing import TYPE_CHECKING,List
import fastapi as _fastapi
from fastapi.middleware.cors import CORSMiddleware
from routes.author_router import author_route

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

app.include_router(author_route)