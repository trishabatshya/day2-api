# Day 2 API

FastAPI + PostgreSQL + SQLAlchemy async + Alembic migrations.

## Models
- User (id, username, email)
- Post (id, title, content, price, author_id → FK to users)

## Setup
```bash
uv venv && source .venv/Scripts/activate
uv sync
alembic upgrade head
uvicorn app.main:app --reload
```
