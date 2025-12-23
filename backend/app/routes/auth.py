from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.user import UserRole

from app.schemas.user import UserCreate, UserLogin, Token
from app.models.user import User
from app.services.hashing import hash_password, verify_password
from app.services.auth import create_access_token
from app.services.dependencies import get_db
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=dict)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(
        (User.username == user.username) | (User.email == user.email)
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hash_password(user.password),
        role=UserRole(user.role)
    )
    db.add(new_user)
    db.commit()
    return {"message": "User registered successfully"}

@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    db_user = db.query(User).filter(User.username == form_data.username).first()
    if not db_user or not verify_password(form_data.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(
        {"sub": db_user.username, "role": db_user.role.value}
    )
    return {"access_token": token, "token_type": "bearer"}
