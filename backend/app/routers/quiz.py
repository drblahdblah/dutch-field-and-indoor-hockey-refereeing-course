"""Quiz grading endpoints."""

from datetime import datetime, timezone

from fastapi import APIRouter, Cookie, Depends, Header, HTTPException
from sqlalchemy.orm import Session

from app.data.course_seed import get_course_outline
from app.database import get_db
from app.models import ModuleProgress, UserSession
from app.schemas import Quiz, QuizAnswerResult, QuizSubmitRequest, QuizSubmitResult
from app.security import resolve_presented_token, get_session_for_token
from app.services.quiz_grader import grade_quiz

router = APIRouter(prefix="/api/quizzes", tags=["quizzes"])


@router.post("/{quiz_id}/submit", response_model=QuizSubmitResult)
def submit_quiz(
    quiz_id: str,
    payload: QuizSubmitRequest,
    authorization: str | None = Header(default=None),
    course_access_token: str | None = Cookie(default=None),
    db: Session = Depends(get_db),
) -> QuizSubmitResult:
    course = get_course_outline()
    quiz = course.quizzes.get(quiz_id)
    if not quiz:
        raise HTTPException(status_code=404, detail=f"Quiz not found: {quiz_id}")

    known_ids = {q.id for q in quiz.questions}
    for answer in payload.answers:
        if answer.question_id not in known_ids:
            raise HTTPException(
                status_code=400,
                detail=f"Unknown question_id: {answer.question_id}",
            )

    score, results = grade_quiz(quiz, payload.answers)
    progress_saved = False

    if payload.save_progress:
        # Auth failure must not hide graded feedback — save is best-effort.
        try:
            token = resolve_presented_token(authorization, course_access_token)
            session = get_session_for_token(token, db)
            progress_saved = _persist_quiz_progress(db, session, quiz_id, quiz, score, results)
        except HTTPException as exc:
            if exc.status_code != 401:
                raise

    return QuizSubmitResult(
        quiz_id=quiz_id,
        score=score,
        total=len(quiz.questions),
        results=results,
        progress_saved=progress_saved,
    )


def _persist_quiz_progress(
    db: Session,
    session: UserSession,
    quiz_id: str,
    quiz: Quiz,
    score: int,
    results: list[QuizAnswerResult],
) -> bool:
    module = next((m for m in get_course_outline().modules if m.quiz_id == quiz_id), None)
    if not module:
        return False

    row = (
        db.query(ModuleProgress)
        .filter(
            ModuleProgress.session_id == session.id,
            ModuleProgress.module_id == module.id,
        )
        .one_or_none()
    )
    if row is None:
        row = ModuleProgress(session_id=session.id, module_id=module.id)
        db.add(row)

    total = len(quiz.questions)
    previous_score = row.quiz_score or 0
    row.quiz_total = total
    # Keep the best score; never demote an already-completed module.
    row.quiz_score = max(previous_score, score)
    if score == total or row.status == "completed":
        row.status = "completed"
        if row.completed_at is None:
            row.completed_at = datetime.now(timezone.utc)
    else:
        row.status = "in_progress"
    if results:
        row.last_question_id = results[-1].question_id
    session.updated_at = datetime.now(timezone.utc)
    db.commit()
    return True
