from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.voter import Voter
from app.services.dependencies import get_db, require_admin

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.put("/approve-voter/{voter_id}")
def approve_voter(
    voter_id: int,
    db: Session = Depends(get_db),
    admin = Depends(require_admin)
):
    voter = db.query(Voter).filter(Voter.voter_id == voter_id).first()
    if not voter:
        raise HTTPException(status_code=404, detail="Voter not found")

    voter.eligibility_status = "APPROVED"
    db.commit()
    return {"message": "Voter approved successfully"}
