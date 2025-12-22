from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Candidate(Base):
    __tablename__ = "candidates"

    candidate_id = Column(Integer, primary_key=True)
    election_id = Column(Integer, ForeignKey("elections.election_id"))
    name = Column(String(100), nullable=False)
    party = Column(String(100))
    symbol = Column(String(50))
