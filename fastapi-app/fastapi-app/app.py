from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import User
from schemas import UserCreate, UserOut

app = FastAPI()

# Create tables automatically on startup for demo (migrations later)
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "FastAPI + PostgreSQL via Docker Compose is live!"}

@app.post("/users", response_model=UserOut, status_code=201)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    user = User(name=payload.name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get("/users", response_model=List[UserOut])
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()

