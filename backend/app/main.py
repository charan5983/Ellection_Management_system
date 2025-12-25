from fastapi import FastAPI
from app.database import Base, engine

from app.routes.results import router as results_router

from app.routes.auth import router as auth_router
from app.routes.voters import router as voters_router
from app.routes.admin import router as admin_router
from app.routes.vote import router as vote_router

from app.routes.winner import router as winner_router

from app.routes.election_lifecycle import router as election_lifecycle_router






# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI-Enabled Election Management System")

# Register routers
app.include_router(auth_router)
app.include_router(voters_router)
app.include_router(admin_router)
app.include_router(vote_router)
app.include_router(results_router)
app.include_router(winner_router)
app.include_router(election_lifecycle_router)


@app.get("/")
def root():
    return {"status": "Backend running successfully"}
