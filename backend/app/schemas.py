"""Pydantic request/response schemas."""

from datetime import datetime
from typing import Any, Literal, Self

from pydantic import BaseModel, Field, field_validator, model_validator


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


EN_TRANSLATION_SLOT_MARKER = "[EN translation slot]"


class InterpretationReference(BaseModel):
    """Official interpretation pointer — original pedagogy + EN translation slots.

    Never paste copyrighted KNHB/FIH interpretation text or illustrations.
    When ``translation_needed`` is True, ``summary.en`` is an EN slot (not legal
    paraphrase of protected NL materials).
    """

    id: str = Field(min_length=1, max_length=64, pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
    topic: LocalizedText
    scope: Literal["field", "indoor", "shared"]
    summary: LocalizedText
    translation_needed: bool = False
    official_source_url: str = Field(min_length=1, max_length=500)
    official_source_name: str = Field(min_length=1, max_length=200)
    knhb_illustration_placeholder: bool = True
    attribution: Attribution
    visual_id: str | None = Field(
        default=None,
        max_length=64,
        pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$",
    )

    @model_validator(mode="after")
    def validate_translation_slot(self) -> Self:
        if self.translation_needed:
            if EN_TRANSLATION_SLOT_MARKER not in self.summary.en:
                raise ValueError(
                    "translation_needed references require "
                    f"{EN_TRANSLATION_SLOT_MARKER!r} in summary.en"
                )
        return self


class QuizOption(BaseModel):
    id: str = Field(min_length=1, max_length=32)
    text: LocalizedText


class QuizFeedback(BaseModel):
    explanation: LocalizedText
    visualization_hint: str | None = Field(
        default=None,
        description="Room for viz/animations in answer feedback (client may render).",
    )


class QuizQuestion(BaseModel):
    id: str
    type: Literal["multiple_choice", "written"]
    prompt: LocalizedText
    options: list[QuizOption] | None = None
    correct_option_id: str | None = None
    accepted_answers: list[str] | None = Field(
        default=None,
        description="For written questions: accepted answer keys (normalized).",
    )
    feedback_correct: QuizFeedback
    feedback_incorrect: dict[str, QuizFeedback] | None = None
    feedback_incorrect_default: QuizFeedback | None = Field(
        default=None,
        description="Fallback when option-specific feedback is missing.",
    )

    @model_validator(mode="after")
    def validate_question_shape(self) -> Self:
        if self.type == "multiple_choice":
            if not self.options:
                raise ValueError("multiple_choice questions require options")
            option_ids = {opt.id for opt in self.options}
            if not self.correct_option_id or self.correct_option_id not in option_ids:
                raise ValueError("correct_option_id must match one of the options")
        elif self.type == "written":
            if not self.accepted_answers:
                raise ValueError("written questions require accepted_answers")
        return self


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


class VisualPlaceholder(BaseModel):
    """Original CSS/SVG viz or an attributed slot linking to official FIH/KNHB material.

    Never embed copyrighted KNHB illustrations — use official_source_url + note.
    """

    id: str = Field(min_length=1, max_length=64, pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
    kind: Literal["svg_animation", "official_link_slot"]
    title: LocalizedText
    caption: LocalizedText
    animation_key: str | None = Field(
        default=None,
        max_length=64,
        description="Stable key the SPA uses to pick an original animation (svg_animation only).",
    )
    official_source_url: str | None = None
    official_source_name: str | None = None
    knhb_illustration_placeholder: bool = False

    @model_validator(mode="after")
    def validate_visual_kind(self) -> Self:
        if self.kind == "svg_animation" and not self.animation_key:
            raise ValueError("svg_animation visuals require animation_key")
        if self.kind == "official_link_slot" and not self.official_source_url:
            raise ValueError("official_link_slot visuals require official_source_url")
        return self


class LearningSection(BaseModel):
    """Instructional block inside a full module (not a stub outline line)."""

    id: str = Field(min_length=1, max_length=64, pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
    title: LocalizedText
    paragraphs: list[LocalizedText] = Field(min_length=1)
    visual_id: str | None = Field(
        default=None,
        max_length=64,
        pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$",
    )


class ModuleStub(BaseModel):
    id: str
    kind: Literal["field", "indoor", "shared"]
    title: LocalizedText
    summary: LocalizedText
    learning_objectives: list[LocalizedText]
    instruction_outline: list[LocalizedText]
    content_status: Literal["stub", "full"] = Field(
        default="stub",
        description="stub = outline only; full = sections + visuals + learning prose.",
    )
    sections: list[LearningSection] = Field(default_factory=list)
    visuals: list[VisualPlaceholder] = Field(default_factory=list)
    interpretation_references: list[InterpretationReference] = Field(
        default_factory=list,
        description=(
            "Structured FIH/KNHB interpretation pointers with attribution and "
            "EN translation slots (no copyrighted art/text)."
        ),
    )
    quiz_id: str | None = None
    further_reading: list[FurtherReading] = Field(default_factory=list)
    order: int

    @model_validator(mode="after")
    def validate_full_module(self) -> Self:
        visual_ids = {v.id for v in self.visuals}
        for section in self.sections:
            if section.visual_id and section.visual_id not in visual_ids:
                raise ValueError(
                    f"section {section.id} references unknown visual_id {section.visual_id}"
                )
        for ref in self.interpretation_references:
            if ref.visual_id and ref.visual_id not in visual_ids:
                raise ValueError(
                    f"interpretation {ref.id} references unknown visual_id {ref.visual_id}"
                )
        if self.content_status == "full" and not self.sections:
            raise ValueError("full modules require at least one learning section")
        return self


class PracticeScenario(BaseModel):
    """Standalone decision scenario — not a course module lesson."""

    id: str = Field(min_length=1, max_length=64, pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
    kind: Literal["field", "indoor"]
    title: LocalizedText
    situation: LocalizedText
    focus: LocalizedText
    order: int
    visual_key: str = Field(
        min_length=1,
        max_length=64,
        pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$",
        description="SPA animation key for the scenario diagram.",
    )
    quiz: Quiz


class PracticeBank(BaseModel):
    """Practice scenario catalogue (separate flow from module lessons)."""

    id: str
    title: LocalizedText
    description: LocalizedText
    scenarios: list[PracticeScenario]


class PracticeScenarioPublic(BaseModel):
    """Learner-facing scenario — quiz prompts without answer keys."""

    id: str
    kind: Literal["field", "indoor"]
    title: LocalizedText
    situation: LocalizedText
    focus: LocalizedText
    order: int
    visual_key: str
    quiz: QuizPublic


class PracticeBankPublic(BaseModel):
    id: str
    title: LocalizedText
    description: LocalizedText
    scenarios: list[PracticeScenarioPublic]


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
    expires_at: datetime


class SessionCreatedOut(SessionOut):
    """Creation response. access_token is omitted in production (cookie-only)."""

    access_token: str | None = None


class ProgressUpdate(BaseModel):
    """Client may mark instructional progress only — quiz scores come from submit."""

    module_id: str = Field(min_length=1, max_length=64, pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
    status: Literal["not_started", "in_progress"] = "in_progress"


class ProgressOut(BaseModel):
    module_id: str
    status: Literal["not_started", "in_progress", "completed"]
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
