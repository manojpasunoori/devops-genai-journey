from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Gauge

from database import Base, engine, get_db
from models import User

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# --------------------------------------------
# REQUIRED FOR GRAFANA FASTAPI OBSERVABILITY
# --------------------------------------------
APP_NAME = "fastapi-app"

# Creates a metric required by the dashboard
app_info = Gauge(
    "fastapi_app_info",
    "Static information about this FastAPI application",
    ["app_name"]
)

@app.on_event("startup")
def startup_event():
    # Set metric value on startup
    app_info.labels(app_name=APP_NAME).set(1)

# --------------------------------------------
# ROUTES
# --------------------------------------------
@app.get("/")
def root():
    return {"msg": "FastAPI + PostgreSQL inside Kubernetes is working!"}

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

# --------------------------------------------
# PROMETHEUS METRICS (REQUIRED)
# --------------------------------------------
Instrumentator().instrument(app).expose(app)

