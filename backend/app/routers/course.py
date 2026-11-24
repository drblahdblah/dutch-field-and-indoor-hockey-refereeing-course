"""Course outline and quiz metadata endpoints."""

from fastapi import APIRouter, HTTPException

from app.data.course_seed import get_course_outline
from app.quiz_public import public_quizzes, to_public_quiz
from app.schemas import CourseOutlinePublic, ModuleStub, QuizPublic

router = APIRouter(prefix="/api/course", tags=["course"])


@router.get("", response_model=CourseOutlinePublic)
def read_course() -> CourseOutlinePublic:
    course = get_course_outline()
    return CourseOutlinePublic(
        id=course.id,
        title=course.title,
        description=course.description,
        modules=course.modules,
        quizzes=public_quizzes(course.quizzes),
        attributions=course.attributions,
    )


@router.get("/modules/{module_id}", response_model=ModuleStub)
def read_module(module_id: str) -> ModuleStub:
    course = get_course_outline()
    for module in course.modules:
        if module.id == module_id:
            return module
    raise HTTPException(status_code=404, detail=f"Module not found: {module_id}")


@router.get("/quizzes/{quiz_id}", response_model=QuizPublic)
def read_quiz(quiz_id: str) -> QuizPublic:
    """Return quiz prompts without answers or feedback (graded via submit)."""
    course = get_course_outline()
    quiz = course.quizzes.get(quiz_id)
    if not quiz:
        raise HTTPException(status_code=404, detail=f"Quiz not found: {quiz_id}")
    return to_public_quiz(quiz)
