"""Session token helpers — capability tokens for progress APIs."""

from __future__ import annotations

import hashlib
import secrets
from typing import Annotated

from fastapi import Cookie, Depends, Header, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import UserSession

SESSION_TOKEN_BYTES = 32
BEARER_PREFIX = "Bearer "
SESSION_COOKIE_NAME = "course_access_token"


def generate_access_token() -> str:
    return secrets.token_urlsafe(SESSION_TOKEN_BYTES)


def hash_access_token(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


def extract_bearer_token(authorization: str | None) -> str | None:
    if not authorization:
        return None
    if not authorization.startswith(BEARER_PREFIX):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization must use Bearer scheme",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = authorization[len(BEARER_PREFIX) :].strip()
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Empty bearer token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token


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
    return session


def require_session(
    authorization: Annotated[str | None, Header()] = None,
    course_access_token: Annotated[str | None, Cookie()] = None,
    db: Session = Depends(get_db),
) -> UserSession:
    token = resolve_presented_token(authorization, course_access_token)
    return get_session_for_token(token, db)
