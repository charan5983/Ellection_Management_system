from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import SessionLocal
from app.models.vote import Vote
from app.models.candidate import Candidate
from app.models.election import Election, ElectionStatus

router = APIRouter(prefix="/winner", tags=["Winner"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def declare_winner(db: Session = Depends(get_db)):
    # 1️⃣ Get completed election
    election = db.query(Election).filter(
        Election.status == ElectionStatus.COMPLETED
    ).first()

    if not election:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Election not completed yet"
        )

    # 2️⃣ Count votes per candidate
    results = (
        db.query(
            Candidate.candidate_id,
            Candidate.name,
            func.count(Vote.vote_id).label("votes")
        )
        .join(Vote, Vote.candidate_id == Candidate.candidate_id)
        .filter(Candidate.election_id == election.election_id)
        .group_by(Candidate.candidate_id, Candidate.name)
        .all()
    )

    if not results:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No votes cast in this election"
        )

    # 3️⃣ Find max votes
    max_votes = max(r.votes for r in results)

    winners = [
        {"candidate_id": r.candidate_id, "name": r.name, "votes": r.votes}
        for r in results if r.votes == max_votes
    ]

    # 4️⃣ Handle tie or single winner
    if len(winners) > 1:
        return {
            "election_id": election.election_id,
            "result": "TIE",
            "winners": winners
        }

    return {
        "election_id": election.election_id,
        "result": "WINNER",
        "winner": winners[0]
    }
