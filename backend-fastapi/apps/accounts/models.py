from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates
import uuid
from datetime import datetime, timezone
from utils.validators import validate_and_hash_password, validate_email, validate_role

Base = declarative_base()

class Account(Base):
    __tablename__ = "accounts"

    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    first_name = Column(String(40), nullable=False)
    last_name = Column(String(40), nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    birth_date = Column(DateTime, nullable=True)
    role = Column(String(10), nullable = False, default="MEMBER")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc),
                        onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    @validates("password")
    def password_validator(self, key, value):
        return validate_and_hash_password(value, self.username)

    @validates("email")
    def email_validator(self, key, value):
        return validate_email(value)

    @validates("role")
    def role_validator(self, key, value):
        return validate_role(value)