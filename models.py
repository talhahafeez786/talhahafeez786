from ast import Index
import datetime as _dt
import email
from email.policy import default
from enum import unique
from operator import index
import sqlalchemy as _sql

import database as _database

class Contact(_database.Base):
    __tablaname__ = "Contacts"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    first_name = _sql.Column(_sql.String, index=True)
    last_name = _sql.Column(_sql.String, index=True)
    email = _sql.Column(_sql.String, index=True, unique=True)
    phone_number = _sql.Column(_sql.String, index=True, unique=True)
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    
