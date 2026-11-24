"""Pydantic request/response schemas."""

from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, Field


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
    id: str
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
    id: str
    title: LocalizedText
    description: LocalizedText
    modules: list[ModuleStub]
    quizzes: dict[str, Quiz]
    attributions: list[Attribution]


class SessionCreate(BaseModel):
    display_name: str | None = None
    locale: str = "nl"


class SessionOut(BaseModel):
    id: str
    display_name: str | None
    locale: str
    created_at: datetime
    updated_at: datetime


class ProgressUpdate(BaseModel):
    module_id: str
    status: Literal["not_started", "in_progress", "completed"] = "in_progress"
    quiz_score: int | None = None
    quiz_total: int | None = None
    last_question_id: str | None = None


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
    question_id: str
    selected_option_id: str | None = None
    written_answer: str | None = None


class QuizAnswerResult(BaseModel):
    question_id: str
    correct: bool
    explanation: LocalizedText
    visualization_hint: str | None = None
    correct_option_id: str | None = None


class QuizSubmitRequest(BaseModel):
    session_id: str | None = None
    answers: list[QuizAnswerRequest]


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
