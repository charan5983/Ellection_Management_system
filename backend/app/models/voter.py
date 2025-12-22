from sqlalchemy import Column, Integer, String, Date, Text, Enum, ForeignKey, TIMESTAMP
from app.database import Base
import enum

class EligibilityStatus(enum.Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

class Voter(Base):
    __tablename__ = "voters"

    voter_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), unique=True)
    full_name = Column(String(100), nullable=False)
    dob = Column(Date, nullable=False)
    age = Column(Integer, nullable=False)
    address = Column(Text)
    id_proof = Column(String(100))
    eligibility_status = Column(Enum(EligibilityStatus), default=EligibilityStatus.PENDING)
    registered_at = Column(TIMESTAMP)
