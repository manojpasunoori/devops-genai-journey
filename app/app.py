#Main source code for fast api

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from prometheus_fastapi_instrumentator import Instrumentator
from database import Base, engine, get_db
from models import User

# Create tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "FastAPI + PostgreSQL inside Kubernetes is working!"}

# Enable Prometheus metrics
Instrumentator().instrument(app).expose(app)

@app.post("/users")
def create_user(name: str, db: Session = Depends(get_db)):
    user = User(name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"id": user.id, "name": user.name}

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return [{"id": u.id, "name": u.name} for u in users]

