from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class AccountCreate(BaseModel):
    username: str
    first_name: str
    last_name: str
    password: str
    email: EmailStr
    age: datetime | None = None

class AccountResponse(BaseModel):
    id: UUID
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    age: datetime | None = None

    class Config:
        from_attributes = True