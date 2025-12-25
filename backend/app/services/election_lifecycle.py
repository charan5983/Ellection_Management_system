from datetime import datetime
from sqlalchemy.orm import Session

from app.models.election import Election, ElectionStatus


def update_election_statuses(db: Session):
    now = datetime.utcnow()

    # UPCOMING → ONGOING
    upcoming = db.query(Election).filter(
        Election.status == ElectionStatus.UPCOMING,
        Election.start_date <= now
    ).all()

    for election in upcoming:
        election.status = ElectionStatus.ONGOING

    # ONGOING → COMPLETED
    ongoing = db.query(Election).filter(
        Election.status == ElectionStatus.ONGOING,
        Election.end_date < now
    ).all()

    for election in ongoing:
        election.status = ElectionStatus.COMPLETED

    if upcoming or ongoing:
        db.commit()

    return {
        "upcoming_to_ongoing": len(upcoming),
        "ongoing_to_completed": len(ongoing)
    }
