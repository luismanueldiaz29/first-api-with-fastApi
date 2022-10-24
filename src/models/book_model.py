import sqlalchemy as _sql
import config.database as _database
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Book(_database.Base):
    __tablename__="books"
    book_id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    title = _sql.Column(_sql.String, index=True)
    rating = _sql.Column(_sql.String, index=True)
    created_at = _sql.Column(DateTime(timezone=True), server_default=func.now())
    author_id = _sql.Column(_sql.Integer, ForeignKey('authors.author_id'))
    
    author = relationship('Author')