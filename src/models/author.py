
import datetime as _dt
import sqlalchemy as _sql
import config.database as _database

class Author(_database.Base):
    __tablename__="authors"
    author_id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String, index=True)
    age = _sql.Column(_sql.Integer, index=True)
    gender = _sql.Column(_sql.String, index=True)