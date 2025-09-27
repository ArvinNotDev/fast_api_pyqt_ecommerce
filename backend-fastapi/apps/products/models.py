from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.orm import validates, relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone
import uuid
from utils.validators import validate_price, validate_seller
from apps.accounts.models import Account

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String(60), nullable=False)
    description = Column(String(255), nullable=True)
    seller = relationship("Account", backref="products")
    price = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc),
                        onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    @validates("price")
    def price_validator(self, key, value):
        return validate_price(value)

    @validates("seller")
    def seller_validator(self, key, value):
        return validate_seller(self, key, value)