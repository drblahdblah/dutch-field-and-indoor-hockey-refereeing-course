"""Session token helpers — capability tokens for progress APIs."""

from __future__ import annotations

import hashlib
import secrets
from datetime import datetime, timedelta, timezone
from typing import Annotated

from fastapi import Cookie, Depends, Header, HTTPException, status
from sqlalchemy.orm import Session

from app.config import settings
from app.database import get_db
from app.models import UserSession

SESSION_TOKEN_BYTES = 32
BEARER_PREFIX = "Bearer "
SESSION_COOKIE_NAME = "course_access_token"


def generate_access_token() -> str:
    return secrets.token_urlsafe(SESSION_TOKEN_BYTES)


def hash_access_token(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


def session_expiry(now: datetime | None = None) -> datetime:
    base = now or datetime.now(timezone.utc)
    return base + timedelta(seconds=settings.session_ttl_seconds)


def extract_bearer_token(authorization: str | None) -> str | None:
    """Return a Bearer token, or None if header absent/non-Bearer.

    Non-Bearer schemes intentionally fall through so a valid cookie can still auth.
    """
    if not authorization:
        return None
    if not authorization.startswith(BEARER_PREFIX):
        return None
    token = authorization[len(BEARER_PREFIX) :].strip()
    return token or None


def resolve_presented_token(
    authorization: str | None,
    cookie_token: str | None,
) -> str:
    bearer = extract_bearer_token(authorization)
    token = bearer or (cookie_token.strip() if cookie_token else None)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing session token (Authorization Bearer or cookie)",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token


def _as_aware(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt


def get_session_for_token(
    token: str,
    db: Session,
) -> UserSession:
    token_hash = hash_access_token(token)
    session = (
        db.query(UserSession)
        .filter(UserSession.token_hash == token_hash)
        .one_or_none()
    )
    if session is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid session token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if session.revoked_at is not None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session revoked",
            headers={"WWW-Authenticate": "Bearer"},
        )
    now = datetime.now(timezone.utc)
    if _as_aware(session.expires_at) <= now:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return session


def require_session(
    authorization: Annotated[str | None, Header()] = None,
    course_access_token: Annotated[str | None, Cookie()] = None,
    db: Session = Depends(get_db),
) -> UserSession:
    token = resolve_presented_token(authorization, course_access_token)
    return get_session_for_token(token, db)


def set_session_cookie(response, access_token: str) -> None:
    response.set_cookie(
        key=SESSION_COOKIE_NAME,
        value=access_token,
        httponly=True,
        secure=settings.cookie_secure_enabled,
        samesite=settings.cookie_samesite_value,
        max_age=settings.session_ttl_seconds,
        path="/api",
    )


def clear_session_cookie(response) -> None:
    response.delete_cookie(
        key=SESSION_COOKIE_NAME,
        path="/api",
        httponly=True,
        secure=settings.cookie_secure_enabled,
        samesite=settings.cookie_samesite_value,
    )
