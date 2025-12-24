from pydantic import BaseModel

class VoteCreate(BaseModel):
    candidate_id: int
