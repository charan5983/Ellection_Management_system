from sqlalchemy import Column, Integer, String, Text, DateTime, Enum
from app.database import Base
import enum

class ElectionStatus(enum.Enum):
    UPCOMING = "UPCOMING"
    ONGOING = "ONGOING"
    COMPLETED = "COMPLETED"

class Election(Base):
    __tablename__ = "elections"

    election_id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    status = Column(Enum(ElectionStatus), default=ElectionStatus.UPCOMING)
