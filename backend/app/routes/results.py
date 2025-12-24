from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import SessionLocal
from app.models.vote import Vote
from app.models.candidate import Candidate
from app.models.election import Election, ElectionStatus

router = APIRouter(prefix="/results", tags=["Results"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_results(db: Session = Depends(get_db)):
    # Get completed or ongoing election
    election = db.query(Election).filter(
        Election.status.in_([ElectionStatus.ONGOING, ElectionStatus.COMPLETED])
    ).first()

    if not election:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No election results available"
        )

    results = (
        db.query(
            Candidate.name,
            func.count(Vote.vote_id).label("votes")
        )
        .join(Vote, Vote.candidate_id == Candidate.candidate_id)
        .filter(Candidate.election_id == election.election_id)
        .group_by(Candidate.name)
        .all()
    )

    return {
        "election_id": election.election_id,
        "results": [{"candidate": r.name, "votes": r.votes} for r in results]
    }
