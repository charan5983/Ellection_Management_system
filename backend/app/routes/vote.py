from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime

from app.database import SessionLocal
from app.services.dependencies import get_current_user

from app.models.voter import Voter
from app.models.election import Election, ElectionStatus
from app.models.vote import Vote
from app.models.candidate import Candidate
from app.schemas.vote import VoteCreate

router = APIRouter(prefix="/vote", tags=["Vote"])


# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def cast_vote(
    vote: VoteCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    # 1️⃣ Only voters can vote
    if current_user.role.value != "VOTER":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only voters are allowed to vote"
        )

    # 2️⃣ Fetch voter
    voter = db.query(Voter).filter(
        Voter.user_id == current_user.user_id
    ).first()

    if not voter:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Voter profile not found"
        )

    # 3️⃣ Voter must be approved
    if voter.eligibility_status.value != "APPROVED":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Voter is not approved yet"
        )

    # 4️⃣ Election must be ongoing
    election = db.query(Election).filter(
        Election.status == ElectionStatus.ONGOING
    ).first()

    if not election:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No active election at the moment"
        )

    # 5️⃣ Prevent duplicate voting
    existing_vote = db.query(Vote).filter(
        Vote.voter_id == voter.voter_id,
        Vote.election_id == election.election_id
    ).first()

    if existing_vote:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You have already voted in this election"
        )

    # 6️⃣ Validate candidate belongs to this election
    candidate = db.query(Candidate).filter(
        Candidate.candidate_id == vote.candidate_id,
        Candidate.election_id == election.election_id
    ).first()

    if not candidate:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid candidate for this election"
        )

    # 7️⃣ Insert vote
    new_vote = Vote(
        voter_id=voter.voter_id,
        election_id=election.election_id,
        candidate_id=vote.candidate_id,
        voted_at=datetime.utcnow()
    )

    db.add(new_vote)
    db.commit()
    db.refresh(new_vote)

    return {
        "message": "Vote cast successfully",
        "vote_id": new_vote.vote_id,
        "election_id": election.election_id
    }
