"""Quiz grading endpoints."""

from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.data.course_seed import get_course_outline
from app.database import get_db
from app.models import ModuleProgress, UserSession
from app.schemas import QuizSubmitRequest, QuizSubmitResult
from app.services.quiz_grader import grade_quiz

router = APIRouter(prefix="/api/quizzes", tags=["quizzes"])


@router.post("/{quiz_id}/submit", response_model=QuizSubmitResult)
def submit_quiz(
    quiz_id: str,
    payload: QuizSubmitRequest,
    db: Session = Depends(get_db),
) -> QuizSubmitResult:
    course = get_course_outline()
    quiz = course.quizzes.get(quiz_id)
    if not quiz:
        raise HTTPException(status_code=404, detail=f"Quiz not found: {quiz_id}")

    score, results = grade_quiz(quiz, payload.answers)
    progress_saved = False

    if payload.session_id:
        session = db.get(UserSession, payload.session_id)
        if not session:
            raise HTTPException(status_code=404, detail="Session not found")

        module = next((m for m in course.modules if m.quiz_id == quiz_id), None)
        if module:
            row = (
                db.query(ModuleProgress)
                .filter(
                    ModuleProgress.session_id == payload.session_id,
                    ModuleProgress.module_id == module.id,
                )
                .one_or_none()
            )
            if row is None:
                row = ModuleProgress(
                    session_id=payload.session_id,
                    module_id=module.id,
                )
                db.add(row)
            row.quiz_score = score
            row.quiz_total = len(quiz.questions)
            row.status = "completed" if score == len(quiz.questions) else "in_progress"
            if row.status == "completed":
                row.completed_at = datetime.now(timezone.utc)
            if results:
                row.last_question_id = results[-1].question_id
            session.updated_at = datetime.now(timezone.utc)
            db.commit()
            progress_saved = True

    return QuizSubmitResult(
        quiz_id=quiz_id,
        score=score,
        total=len(quiz.questions),
        results=results,
        progress_saved=progress_saved,
    )
