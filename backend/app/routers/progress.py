"""Session + module progress persistence (bearer-token gated)."""

import secrets
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.data.course_seed import get_course_outline
from app.database import get_db
from app.models import ModuleProgress, UserSession
from app.schemas import (
    ProgressOut,
    ProgressUpdate,
    SessionCreate,
    SessionCreatedOut,
    SessionOut,
    SessionProgressOut,
)
from app.security import generate_access_token, hash_access_token, require_session

router = APIRouter(prefix="/api/progress", tags=["progress"])


def _session_out(session: UserSession) -> SessionOut:
    return SessionOut(
        id=session.id,
        display_name=session.display_name,
        locale=session.locale,
        created_at=session.created_at,
        updated_at=session.updated_at,
    )


def _progress_out(row: ModuleProgress) -> ProgressOut:
    return ProgressOut(
        module_id=row.module_id,
        status=row.status,
        quiz_score=row.quiz_score,
        quiz_total=row.quiz_total,
        last_question_id=row.last_question_id,
        completed_at=row.completed_at,
        updated_at=row.updated_at,
    )


def _known_module_ids() -> set[str]:
    return {m.id for m in get_course_outline().modules}


@router.post("/sessions", response_model=SessionCreatedOut, status_code=201)
def create_session(payload: SessionCreate, db: Session = Depends(get_db)) -> SessionCreatedOut:
    access_token = generate_access_token()
    session = UserSession(
        id=secrets.token_urlsafe(16),
        token_hash=hash_access_token(access_token),
        display_name=payload.display_name,
        locale=payload.locale or "nl",
    )
    db.add(session)
    db.commit()
    db.refresh(session)
    base = _session_out(session)
    return SessionCreatedOut(**base.model_dump(), access_token=access_token)


@router.get("/session", response_model=SessionProgressOut)
def get_session_progress(
    session: UserSession = Depends(require_session),
) -> SessionProgressOut:
    return SessionProgressOut(
        session=_session_out(session),
        progress=[_progress_out(p) for p in session.progress],
    )


@router.put("/session", response_model=ProgressOut)
def upsert_progress(
    payload: ProgressUpdate,
    session: UserSession = Depends(require_session),
    db: Session = Depends(get_db),
) -> ProgressOut:
    if payload.module_id not in _known_module_ids():
        raise HTTPException(status_code=400, detail=f"Unknown module_id: {payload.module_id}")

    row = (
        db.query(ModuleProgress)
        .filter(
            ModuleProgress.session_id == session.id,
            ModuleProgress.module_id == payload.module_id,
        )
        .one_or_none()
    )
    if row is None:
        row = ModuleProgress(session_id=session.id, module_id=payload.module_id)
        db.add(row)

    row.status = payload.status
    if payload.quiz_score is not None:
        row.quiz_score = payload.quiz_score
    if payload.quiz_total is not None:
        row.quiz_total = payload.quiz_total
    if payload.last_question_id is not None:
        row.last_question_id = payload.last_question_id
    if payload.status == "completed":
        row.completed_at = datetime.now(timezone.utc)
    session.updated_at = datetime.now(timezone.utc)

    db.commit()
    db.refresh(row)
    return _progress_out(row)
