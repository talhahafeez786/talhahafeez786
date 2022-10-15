import database as _database
import models as _models

def _add_tables():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.Session()
    try:
        yield db
    finally: 
        db.close()
        
async def create_contact(contact: _schemas.CreateContact, db: "Session") _schemas.Contact:
    contact = _models.Contact(**contact.dict())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return _schemas.Contact.from_orm(contact)
