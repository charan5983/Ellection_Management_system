from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP
from app.database import Base
import enum

class UserRole(enum.Enum):
    ADMIN = "ADMIN"
    VOTER = "VOTER"

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    created_at = Column(TIMESTAMP)
