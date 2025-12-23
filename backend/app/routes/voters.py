from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date

from app.schemas.voter import VoterCreate, VoterResponse
from app.models.voter import Voter
from app.services.dependencies import get_db, require_voter

router = APIRouter(prefix="/voters", tags=["Voters"])

@router.post("/register", response_model=VoterResponse)
def register_voter(
    voter: VoterCreate,
    db: Session = Depends(get_db),
    current_user = Depends(require_voter)
):
    existing = db.query(Voter).filter(Voter.user_id == current_user.user_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Voter profile already exists")

    age = date.today().year - voter.dob.year

    new_voter = Voter(
        user_id=current_user.user_id,
        full_name=voter.full_name,
        dob=voter.dob,
        age=age,
        address=voter.address,
        id_proof=voter.id_proof,
        eligibility_status="PENDING"
    )

    db.add(new_voter)
    db.commit()
    db.refresh(new_voter)
    return new_voter
