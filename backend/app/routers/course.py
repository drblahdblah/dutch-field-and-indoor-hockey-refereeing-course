"""Course outline and quiz metadata endpoints."""

from fastapi import APIRouter, HTTPException

from app.data.course_seed import get_course_outline
from app.schemas import CourseOutline, ModuleStub, Quiz, QuizFeedback, LocalizedText

router = APIRouter(prefix="/api/course", tags=["course"])

_EMPTY_FEEDBACK = QuizFeedback(
    explanation=LocalizedText(nl="", en=""),
    visualization_hint=None,
)


@router.get("", response_model=CourseOutline)
def read_course() -> CourseOutline:
    return get_course_outline()


@router.get("/modules/{module_id}", response_model=ModuleStub)
def read_module(module_id: str) -> ModuleStub:
    course = get_course_outline()
    for module in course.modules:
        if module.id == module_id:
            return module
    raise HTTPException(status_code=404, detail=f"Module not found: {module_id}")


@router.get("/quizzes/{quiz_id}", response_model=Quiz)
def read_quiz(quiz_id: str) -> Quiz:
    """Return quiz prompts without answers or feedback (graded via submit)."""
    course = get_course_outline()
    quiz = course.quizzes.get(quiz_id)
    if not quiz:
        raise HTTPException(status_code=404, detail=f"Quiz not found: {quiz_id}")

    stripped = [
        q.model_copy(
            update={
                "correct_option_id": None,
                "accepted_answers": None,
                "feedback_correct": _EMPTY_FEEDBACK,
                "feedback_incorrect": None,
                "feedback_incorrect_default": None,
            }
        )
        for q in quiz.questions
    ]
    return quiz.model_copy(update={"questions": stripped})
