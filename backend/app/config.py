"""Application settings — no secrets required for v0 defaults."""

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="COURSE_", env_file=".env", extra="ignore")

    app_name: str = "Dutch Field & Indoor Hockey Umpiring Course"
    database_url: str = f"sqlite:///{Path(__file__).resolve().parent.parent / 'data' / 'course.db'}"
    cors_origins: str = "http://localhost:5173,http://127.0.0.1:5173,http://localhost:3000"
    default_locale: str = "nl"

    @property
    def cors_origin_list(self) -> list[str]:
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]


settings = Settings()
