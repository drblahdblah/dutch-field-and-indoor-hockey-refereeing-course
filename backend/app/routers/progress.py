"""Session + module progress persistence (bearer/cookie gated)."""

import secrets
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Request, Response
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.config import settings
from app.data.course_seed import get_course_outline
from app.data.practice_scenarios import practice_scenario_ids
from app.database import get_db
from app.models import ModuleProgress, UserSession
from app.rate_limit import enforce_session_create_limit
from app.schemas import (
    ProgressOut,
    ProgressUpdate,
    SessionCreate,
    SessionCreatedOut,
    SessionOut,
    SessionProgressOut,
)
from app.security import (
    clear_session_cookie,
    generate_access_token,
    hash_access_token,
    require_session,
    session_expiry,
    set_session_cookie,
)

router = APIRouter(prefix="/api/progress", tags=["progress"])


def _session_out(session: UserSession) -> SessionOut:
    return SessionOut(
        id=session.id,
        display_name=session.display_name,
        locale=session.locale,
        created_at=session.created_at,
        updated_at=session.updated_at,
        expires_at=session.expires_at,
    )


def _progress_out(row: ModuleProgress) -> ProgressOut:
    status = row.status
    if status not in {"not_started", "in_progress", "completed"}:
        status = "in_progress"
    return ProgressOut(
        module_id=row.module_id,
        status=status,  # type: ignore[arg-type]
        quiz_score=row.quiz_score,
        quiz_total=row.quiz_total,
        last_question_id=row.last_question_id,
        completed_at=row.completed_at,
        updated_at=row.updated_at,
    )


def _known_progress_ids() -> set[str]:
    """Course modules plus practice scenario ids (optional practice progress)."""
    return {m.id for m in get_course_outline().modules} | practice_scenario_ids()


@router.post("/sessions", response_model=SessionCreatedOut, status_code=201)
def create_session(
    payload: SessionCreate,
    request: Request,
    response: Response,
    db: Session = Depends(get_db),
) -> SessionCreatedOut:
    enforce_session_create_limit(request)
    access_token = generate_access_token()
    now = datetime.now(timezone.utc)
    session = UserSession(
        id=secrets.token_urlsafe(16),
        token_hash=hash_access_token(access_token),
        display_name=payload.display_name,
        locale=payload.locale or "nl",
        expires_at=session_expiry(now),
    )
    db.add(session)
    db.commit()
    db.refresh(session)
    set_session_cookie(response, access_token)
    base = _session_out(session)
    exposed = access_token if settings.should_expose_access_token else None
    return SessionCreatedOut(**base.model_dump(), access_token=exposed)


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
    if payload.module_id not in _known_progress_ids():
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

    # Never accept client-supplied quiz scores; completion is set by quiz submit only.
    if row.status != "completed":
        row.status = payload.status
    session.updated_at = datetime.now(timezone.utc)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        row = (
            db.query(ModuleProgress)
            .filter(
                ModuleProgress.session_id == session.id,
                ModuleProgress.module_id == payload.module_id,
            )
            .one()
        )
        if row.status != "completed":
            row.status = payload.status
        session.updated_at = datetime.now(timezone.utc)
        db.commit()

    db.refresh(row)
    return _progress_out(row)


@router.delete("/session", status_code=204)
def revoke_session(
    response: Response,
    session: UserSession = Depends(require_session),
    db: Session = Depends(get_db),
) -> None:
    """Revoke the current session and clear the cookie."""
    session.revoked_at = datetime.now(timezone.utc)
    # Rotate hash so the old bearer/cookie cannot be reused even if TTL remains.
    session.token_hash = hash_access_token(generate_access_token())
    session.updated_at = datetime.now(timezone.utc)
    db.commit()
    clear_session_cookie(response)
