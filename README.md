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
## Auth endpoints

- POST /auth/register — create account
- POST /auth/login — returns JWT token
- GET /users/me — requires Bearer token

## Protected endpoints (require Authorization: Bearer <token>)

- POST /posts
- GET /posts/{id}
- PUT /posts/{id} — only post author
- DELETE /posts/{id} — only post author