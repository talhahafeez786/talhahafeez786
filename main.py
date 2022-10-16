from os import O_RANDOM
import typing as TYPE_CHECKING, List 
import fastapi as _fastapi 
import sqlalchemy.orm as _orm
import services as _services
import schemas as _schemas 

if TYPE_CHECKING:
    from sqlalchemy.orm import session

app = _fastapi.FastAPI()

@app.post("/api/contacts/", response_model=_schemas.Contact)
async def create_contact(
    contact: _schemas.CreateContact,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return await _services.create_contact(contact=contact, db=db)
