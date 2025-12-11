started at Tue Nov 11 00:23:55 CST 2025
🚀 DevOps + GenAI Engineering Journey

I am currently on a structured 6-month journey to transition into a DevOps + GenAI Engineer, combining cloud infrastructure, automation, MLOps, and AI systems development. This journey emphasizes production-grade tooling, Kubernetes-native design, observability, scalable backend architecture, and end-to-end CI/CD workflows.
I am also actively preparing for the AWS Solutions Architect Certification to strengthen my cloud fundamentals and cloud-native design principles.

🔧 Automation & Developer Productivity

I built a personalized automation system to support deep-work sessions and consistent engineering productivity.
This includes Bash-based focus scripts, timers, and reusable workflows optimized for daily DevOps and AI engineering tasks.
These automation tools run natively inside WSL2 Ubuntu, providing a clean and distraction-free development environment.

🛠️ FastAPI + PostgreSQL + Containerized Backend (Docker)

Designed and deployed a fully containerized backend microservice using FastAPI, integrated with PostgreSQL through Docker Compose.

Core Achievements

Structured a scalable FastAPI project layout

Implemented SQLAlchemy ORM with automatic table creation

Added Pydantic models for clean request/response validation

Configured PostgreSQL with persistent Docker volumes

Verified communication via Docker internal networking

Implemented and tested essential endpoints:

GET / — Health check

POST /users — Insert user

GET /users — Retrieve users

Tested via curl and interactive Swagger UI

Ensured consistent builds using Docker Compose (docker compose up -d)

Technologies Used

FastAPI · Uvicorn · PostgreSQL 14 · SQLAlchemy ORM · Docker · Docker Compose · Python 3.11 · WSL2 Ubuntu

🔁 Redeploy & Regression Stability

Performed multiple rebuilds and redeploy tests to ensure application stability, idempotent behavior, and clean re-creation of containers.
All API endpoints and database interactions were validated after each rebuild cycle.

Migrated backend to Kubernetes (Minikube → EKS)

Built complete CI/CD pipelines using GitHub Actions

Added full observability stack (Prometheus, Loki, Grafana)

Implemented Helm charts, autoscaling (HPA), service mesh

📌 Next Steps in the Journey

Extend into MLOps pipelines using MLflow, DVC, model serving

Integrate GenAI systems using LangChain, vector DBs, orchestration

Deploy end-to-end production-ready cloud environments

Complete AWS Solutions Architect Certification to strengthen cloud-native skills
