from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.services.dependencies import get_current_user
from app.services.election_lifecycle import update_election_statuses

router = APIRouter(prefix="/elections", tags=["Election Lifecycle"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/sync-status")
def sync_election_status(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    if current_user.role.value != "ADMIN":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )

    result = update_election_statuses(db)
    return {
        "message": "Election statuses synchronized",
        **result
    }
