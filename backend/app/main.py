from fastapi import FastAPI
from app.database import Base, engine

from app.routes.auth import router as auth_router
from app.routes.voters import router as voters_router
from app.routes.admin import router as admin_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI-Enabled Election Management System")

app.include_router(auth_router)
app.include_router(voters_router)
app.include_router(admin_router)

@app.get("/")
def root():
    return {"status": "Backend running successfully"}
