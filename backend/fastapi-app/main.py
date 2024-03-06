from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select, delete, update, insert, create_engine
from models import Contact, metadata
from typing import List
from database import DATABASE_URL
from databases import Database
from pydantic import BaseModel


app = FastAPI()
database = Database(DATABASE_URL)
origins = [
    "http://localhost"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    await database.connect()

    # Create an engine for table creation
    engine = create_engine(DATABASE_URL)
    # Create tables
    metadata.create_all(engine)
    # Dispose the engine as it's no longer needed
    engine.dispose()


@app.on_event("shutdown")
async def shutdown_event():
    await database.disconnect()


class ContactForm(BaseModel):
    name: str
    email: str
    message: str


class UpdateContactForm(BaseModel):
    name: str = None
    email: str = None
    message: str = None


class ContactResponse(BaseModel):
    id: int
    name: str
    email: str
    message: str

    class Config:
        orm_mode = True


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/contacts/", response_model=List[ContactResponse])
async def read_contacts(skip: int = 0, limit: int = 100):
    query = select(Contact).offset(skip).limit(limit)
    return await database.fetch_all(query)


@app.post("/contact/")
async def create_contact(contact: ContactForm):
    query = insert(Contact).values(name=contact.name, email=contact.email, message=contact.message)
    last_record_id = await database.execute(query)
    return {**contact.dict(), "id": last_record_id}


@app.delete("/contacts/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact(contact_id: int):
    query = delete(Contact).where(Contact.c.id == contact_id)
    result = await database.execute(query)
    if not result:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"ok": True}


@app.put("/contacts/{contact_id}", response_model=ContactForm)
async def update_contact(contact_id: int, contact: UpdateContactForm):
    query = update(Contact).where(Contact.c.id == contact_id).values(**contact.dict(exclude_unset=True))
    result = await database.execute(query)
    if not result:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {**contact.dict(), "id": contact_id}
