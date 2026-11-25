"""FastAPI application entrypoint."""

import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database import init_db
from app.routers import course, practice, progress, quiz
from app.schemas import HealthOut


@asynccontextmanager
async def lifespan(_app: FastAPI):
    await asyncio.to_thread(init_db)
    yield


app = FastAPI(title=settings.app_name, lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type", "Accept"],
)

app.include_router(course.router)
app.include_router(practice.router)
app.include_router(progress.router)
app.include_router(quiz.router)


@app.get("/api/health", response_model=HealthOut)
def health() -> HealthOut:
    return HealthOut(status="ok", app=settings.app_name)
