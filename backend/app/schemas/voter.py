from pydantic import BaseModel
from typing import Optional
from datetime import date

class VoterCreate(BaseModel):
    full_name: str
    dob: date
    address: str
    id_proof: Optional[str] = None

class VoterResponse(BaseModel):
    voter_id: int
    full_name: str
    eligibility_status: str

    class Config:
        from_attributes = True
