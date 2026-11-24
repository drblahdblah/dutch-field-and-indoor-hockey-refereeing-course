"""Public quiz views — never expose answer keys on read paths."""

from app.schemas import Quiz, QuizPublic, QuizQuestionPublic


def to_public_quiz(quiz: Quiz) -> QuizPublic:
    """Strip correct answers and feedback from a quiz for GET responses."""
    questions = [
        QuizQuestionPublic(
            id=q.id,
            type=q.type,
            prompt=q.prompt,
            options=q.options,
        )
        for q in quiz.questions
    ]
    return QuizPublic(id=quiz.id, title=quiz.title, questions=questions)


def public_quizzes(quizzes: dict[str, Quiz]) -> dict[str, QuizPublic]:
    return {quiz_id: to_public_quiz(quiz) for quiz_id, quiz in quizzes.items()}
