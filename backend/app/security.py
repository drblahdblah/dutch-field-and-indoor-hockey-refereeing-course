"""Session token helpers — capability tokens for progress APIs."""

from __future__ import annotations

import hashlib
import hmac
import secrets
from typing import Annotated

from fastapi import Depends, Header, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import UserSession

SESSION_TOKEN_BYTES = 32
BEARER_PREFIX = "Bearer "


def generate_access_token() -> str:
    return secrets.token_urlsafe(SESSION_TOKEN_BYTES)


def hash_access_token(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


def tokens_match(presented: str, stored_hash: str) -> bool:
    return hmac.compare_digest(hash_access_token(presented), stored_hash)


def extract_bearer_token(authorization: str | None) -> str:
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing Authorization bearer token",
            headers={"WWW-Authenticate": "Bearer"},
        )
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
    db: Session = Depends(get_db),
) -> UserSession:
    token = extract_bearer_token(authorization)
    return get_session_for_token(token, db)
