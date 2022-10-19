import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
import os

USER_DB = os.environ.get('POSTGRES_USER')
PASSWORD_DB = os.environ.get('POSTGRES_PASSWORD')
NAME_DB = os.environ.get('POSTGRES_DB')
HOST_DB= os.environ.get('HOST_DB')

DATABASE_URL = f"postgresql://{USER_DB}:{PASSWORD_DB}@{HOST_DB}/{NAME_DB}"

engine = _sql.create_engine(DATABASE_URL) 

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()