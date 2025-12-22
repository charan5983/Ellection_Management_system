from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP, UniqueConstraint
from app.database import Base

class Vote(Base):
    __tablename__ = "votes"

    vote_id = Column(Integer, primary_key=True)
    voter_id = Column(Integer, ForeignKey("voters.voter_id"))
    election_id = Column(Integer, ForeignKey("elections.election_id"))
    candidate_id = Column(Integer, ForeignKey("candidates.candidate_id"))
    voted_at = Column(TIMESTAMP)

    __table_args__ = (
        UniqueConstraint("voter_id", "election_id", name="one_vote_per_election"),
    )
