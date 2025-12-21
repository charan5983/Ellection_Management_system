from fastapi import FastAPI
from app.database import Base, engine

app = FastAPI(
    title="AI-Enabled Election Management & Voter Registration System"
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def health_check():
    return {"status": "Backend running successfully"}
