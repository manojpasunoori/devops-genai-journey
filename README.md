 DevOps + GenAI Journey
Day 1 started at Tue Nov 11 00:23:55 CST 2025

## Day 1 — Automation
- Added focus scripts (bash, executable, tested)

## Day 2 – FastAPI + PostgreSQL + Docker Compose Integration (Completed)

- Built a fully containerized FastAPI backend service.
- Added SQLAlchemy ORM and Pydantic schemas.
- Connected FastAPI ↔ PostgreSQL using Docker internal networking.
- Added database migrations (auto-create tables).
- Implemented POST /users and GET /users API routes.
- Verified persistent storage using named Docker volumes.
- Successfully ran the entire stack using `docker compose up -d`.
- Tested endpoints using curl and Swagger UI at /docs.

Endpoints:
- GET / → Health message
- POST /users → Create user
- GET /users → List users

Stack:
- FastAPI
- Uvicorn server
- PostgreSQL 14
- SQLAlchemy ORM
- Docker
- Docker Compose
- WSL2 Ubuntu

# redeploy test Fri Nov 21 02:18:12 CST 2025
Fri Nov 21 02:22:15 CST 2025
