"""Pydantic request/response schemas."""

from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, Field, field_validator


class LocalizedText(BaseModel):
    nl: str
    en: str


class Attribution(BaseModel):
    """Hooks for crediting official sources — never invent copyrighted rule text."""

    source_name: str
    source_url: str | None = None
    note: LocalizedText
    knhb_illustration_placeholder: bool = False
    translation_needed: bool = False


class FurtherReading(BaseModel):
    title: LocalizedText
    url: str
    attribution: Attribution


class QuizOption(BaseModel):
    id: str = Field(min_length=1, max_length=32)
    text: LocalizedText


class QuizFeedback(BaseModel):
    explanation: LocalizedText
    """Room for viz/animations in answer feedback (client may render)."""
    visualization_hint: str | None = None


class QuizQuestion(BaseModel):
    id: str
    type: Literal["multiple_choice", "written"]
    prompt: LocalizedText
    options: list[QuizOption] | None = None
    correct_option_id: str | None = None
    """For written questions: accepted answer keys (normalized)."""
    accepted_answers: list[str] | None = None
    feedback_correct: QuizFeedback
    feedback_incorrect: dict[str, QuizFeedback] | None = None
    """Fallback when option-specific feedback is missing."""
    feedback_incorrect_default: QuizFeedback | None = None


class Quiz(BaseModel):
    id: str
    title: LocalizedText
    questions: list[QuizQuestion]


class QuizQuestionPublic(BaseModel):
    """Learner-facing question — no answer keys or feedback payloads."""

    id: str
    type: Literal["multiple_choice", "written"]
    prompt: LocalizedText
    options: list[QuizOption] | None = None


class QuizPublic(BaseModel):
    id: str
    title: LocalizedText
    questions: list[QuizQuestionPublic]


class ModuleStub(BaseModel):
    id: str
    kind: Literal["field", "indoor", "shared"]
    title: LocalizedText
    summary: LocalizedText
    learning_objectives: list[LocalizedText]
    instruction_outline: list[LocalizedText]
    quiz_id: str | None = None
    further_reading: list[FurtherReading] = Field(default_factory=list)
    order: int


class CourseOutline(BaseModel):
    """Internal / seed shape — includes full quizzes with answer keys."""

    id: str
    title: LocalizedText
    description: LocalizedText
    modules: list[ModuleStub]
    quizzes: dict[str, Quiz]
    attributions: list[Attribution]


class CourseOutlinePublic(BaseModel):
    """API course outline — quizzes are stripped of solutions."""

    id: str
    title: LocalizedText
    description: LocalizedText
    modules: list[ModuleStub]
    quizzes: dict[str, QuizPublic]
    attributions: list[Attribution]


class SessionCreate(BaseModel):
    display_name: str | None = Field(default=None, max_length=120)
    locale: str = Field(default="nl", max_length=16)

    @field_validator("display_name")
    @classmethod
    def strip_display_name(cls, value: str | None) -> str | None:
        if value is None:
            return None
        cleaned = value.strip()
        return cleaned or None

    @field_validator("locale")
    @classmethod
    def validate_locale(cls, value: str) -> str:
        normalized = value.strip().lower()
        if normalized not in {"nl", "en"}:
            raise ValueError("locale must be 'nl' or 'en'")
        return normalized


class SessionOut(BaseModel):
    id: str
    display_name: str | None
    locale: str
    created_at: datetime
    updated_at: datetime


class SessionCreatedOut(SessionOut):
    """Returned once at creation — includes the bearer access token."""

    access_token: str


class ProgressUpdate(BaseModel):
    module_id: str = Field(min_length=1, max_length=64, pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
    status: Literal["not_started", "in_progress", "completed"] = "in_progress"
    quiz_score: int | None = Field(default=None, ge=0, le=1000)
    quiz_total: int | None = Field(default=None, ge=0, le=1000)
    last_question_id: str | None = Field(default=None, max_length=64)


class ProgressOut(BaseModel):
    module_id: str
    status: str
    quiz_score: int | None
    quiz_total: int | None
    last_question_id: str | None
    completed_at: datetime | None
    updated_at: datetime


class SessionProgressOut(BaseModel):
    session: SessionOut
    progress: list[ProgressOut]


class QuizAnswerRequest(BaseModel):
    question_id: str = Field(min_length=1, max_length=64)
    selected_option_id: str | None = Field(default=None, max_length=32)
    written_answer: str | None = Field(default=None, max_length=500)


class QuizAnswerResult(BaseModel):
    question_id: str
    correct: bool
    explanation: LocalizedText
    visualization_hint: str | None = None
    """Revealed only after submit grading — never on GET quiz/course paths."""
    correct_option_id: str | None = None


class QuizSubmitRequest(BaseModel):
    answers: list[QuizAnswerRequest] = Field(min_length=1, max_length=100)
    """Optional: when set with a valid bearer token, progress is persisted."""
    save_progress: bool = False


class QuizSubmitResult(BaseModel):
    quiz_id: str
    score: int
    total: int
    results: list[QuizAnswerResult]
    progress_saved: bool = False


class HealthOut(BaseModel):
    status: str
    app: str


class ErrorOut(BaseModel):
    detail: str
    meta: dict[str, Any] | None = None
