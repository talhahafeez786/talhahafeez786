from lib2to3.pytree import Base
import sqlalchemy as _sql 
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

DATABASE_URL = "postgresql://myuser:Talha123@localhost/python_database"

engine = _sql.create_engine(DATABASE_URL)

Session = _orm.sessionmaker(autocommit=False, autoflush=False,bind=engine) 

Base = _declarative.declarative_base()