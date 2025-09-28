from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class ProductCreate(BaseModel):
    name: str
    description: str
    seller_id: UUID
    price: float
    

class ProductResponse(BaseModel):
    id: UUID
    name: str
    description: str
    seller_id: UUID
    price: float
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        from_attributes = True