"""SQLAlchemy engine and session helpers."""

from collections.abc import Generator
from pathlib import Path

from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.config import settings


class Base(DeclarativeBase):
    pass


def _ensure_sqlite_dir(url: str) -> None:
    if url.startswith("sqlite:///"):
        db_path = Path(url.removeprefix("sqlite:///"))
        db_path.parent.mkdir(parents=True, exist_ok=True)


_ensure_sqlite_dir(settings.database_url)

connect_args = {"check_same_thread": False} if settings.database_url.startswith("sqlite") else {}
engine = create_engine(settings.database_url, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def _sqlite_column_names(table: str) -> set[str]:
    inspector = inspect(engine)
    if table not in inspector.get_table_names():
        return set()
    return {col["name"] for col in inspector.get_columns(table)}


def _migrate_sqlite_schema() -> None:
    """Lightweight SQLite migrations for local v0 (no Alembic yet)."""
    if not settings.database_url.startswith("sqlite"):
        return
    columns = _sqlite_column_names("user_sessions")
    if not columns:
        return

    with engine.begin() as conn:
        if "token_hash" not in columns:
            conn.execute(text("ALTER TABLE user_sessions ADD COLUMN token_hash VARCHAR(64)"))
            conn.execute(text("DELETE FROM module_progress"))
            conn.execute(text("DELETE FROM user_sessions"))
            conn.execute(
                text(
                    "CREATE UNIQUE INDEX IF NOT EXISTS "
                    "ix_user_sessions_token_hash ON user_sessions (token_hash)"
                )
            )
            columns = _sqlite_column_names("user_sessions")

        if "expires_at" not in columns:
            conn.execute(text("ALTER TABLE user_sessions ADD COLUMN expires_at DATETIME"))
            # Existing rows: expire immediately so clients must re-auth.
            conn.execute(
                text(
                    "UPDATE user_sessions SET expires_at = CURRENT_TIMESTAMP "
                    "WHERE expires_at IS NULL"
                )
            )

        if "revoked_at" not in columns:
            conn.execute(text("ALTER TABLE user_sessions ADD COLUMN revoked_at DATETIME"))


def init_db() -> None:
    from app import models  # noqa: F401

    Base.metadata.create_all(bind=engine)
    _migrate_sqlite_schema()
