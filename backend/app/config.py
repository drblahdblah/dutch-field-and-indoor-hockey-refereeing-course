"""Application settings — no secrets required for v0 defaults."""

from pathlib import Path
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="COURSE_", env_file=".env", extra="ignore")

    app_name: str = "Dutch Field & Indoor Hockey Umpiring Course"
    database_url: str = f"sqlite:///{Path(__file__).resolve().parent.parent / 'data' / 'course.db'}"
    cors_origins: str = "http://localhost:5173,http://127.0.0.1:5173,http://localhost:3000"
    default_locale: str = "nl"

    # development | production — drives secure cookie defaults and token exposure.
    environment: Literal["development", "production"] = "development"

    # Session lifetime (also cookie Max-Age). Default 30 days.
    session_ttl_seconds: int = Field(default=60 * 60 * 24 * 30, ge=60, le=60 * 60 * 24 * 365)

    # Cookie flags. Secure defaults on in production; SameSite=none requires Secure.
    cookie_secure: bool | None = None
    cookie_samesite: Literal["lax", "strict", "none"] = "lax"

    # When false (production default), access_token is omitted from JSON — cookie only.
    expose_access_token: bool | None = None

    # Simple in-process rate limits (per client IP). Single-worker only —
    # multi-worker deployments need edge/shared limiting.
    rate_limit_session_create: int = Field(default=30, ge=1, le=10_000)
    rate_limit_quiz_submit: int = Field(default=120, ge=1, le=10_000)
    rate_limit_window_seconds: int = Field(default=60, ge=1, le=3600)

    # When true, derive client IP from X-Forwarded-For (rightmost hop).
    # Keep false unless sitting behind a trusted reverse proxy that strips spoofed XFF.
    trust_proxy: bool = False

    @property
    def cors_origin_list(self) -> list[str]:
        origins = [o.strip() for o in self.cors_origins.split(",") if o.strip()]
        # Never allow wildcard when credentials are enabled.
        return [o for o in origins if o != "*"]

    @property
    def is_production(self) -> bool:
        return self.environment == "production"

    @property
    def cookie_secure_enabled(self) -> bool:
        if self.cookie_secure is not None:
            return self.cookie_secure
        return self.is_production

    @property
    def cookie_samesite_value(self) -> Literal["lax", "strict", "none"]:
        if self.cookie_samesite == "none" and not self.cookie_secure_enabled:
            # Spec: SameSite=None requires Secure — fall back to lax.
            return "lax"
        return self.cookie_samesite

    @property
    def should_expose_access_token(self) -> bool:
        if self.expose_access_token is not None:
            return self.expose_access_token
        return not self.is_production


settings = Settings()
