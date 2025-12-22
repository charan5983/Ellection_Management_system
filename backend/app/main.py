from fastapi import FastAPI
from app.database import Base, engine

from app.routes import auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI-Enabled Election Management System")

app.include_router(auth.router)

@app.get("/")
def root():
    return {"status": "Backend running successfully"}

