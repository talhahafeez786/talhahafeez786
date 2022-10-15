import datetime as _dt
import email
import pydantic as _pydantic 

class _BaseContact(_pydantic.BaseModel):
    first_name : str
    last_name : str
    email : str
    phone : str


class Contact(_BaseContact):
    id : int
    date_created : _dt.datetime


class CreateContact(_BaseContact):
    pass 

