"""Grade quiz answers and attach bilingual explanations."""

from app.schemas import (
    LocalizedText,
    Quiz,
    QuizAnswerRequest,
    QuizAnswerResult,
    QuizFeedback,
    QuizQuestion,
)


def _normalize_written(value: str) -> str:
    return value.strip().lower().rstrip("!.")


def _pick_incorrect_feedback(question: QuizQuestion, option_id: str | None) -> QuizFeedback:
    if option_id and question.feedback_incorrect and option_id in question.feedback_incorrect:
        return question.feedback_incorrect[option_id]
    if question.feedback_incorrect_default:
        return question.feedback_incorrect_default
    return QuizFeedback(
        explanation=LocalizedText(
            nl="Onjuist. Raadpleeg de officiële regels voor meer context.",
            en="Incorrect. Consult the official rules for more context.",
        )
    )


def grade_question(question: QuizQuestion, answer: QuizAnswerRequest) -> QuizAnswerResult:
    if question.type == "multiple_choice":
        selected = answer.selected_option_id
        correct = selected is not None and selected == question.correct_option_id
        feedback = question.feedback_correct if correct else _pick_incorrect_feedback(question, selected)
        return QuizAnswerResult(
            question_id=question.id,
            correct=correct,
            explanation=feedback.explanation,
            visualization_hint=feedback.visualization_hint,
            correct_option_id=question.correct_option_id,
        )

    # written
    written = answer.written_answer or ""
    accepted = {_normalize_written(a) for a in (question.accepted_answers or [])}
    correct = _normalize_written(written) in accepted
    feedback = (
        question.feedback_correct
        if correct
        else _pick_incorrect_feedback(question, None)
    )
    return QuizAnswerResult(
        question_id=question.id,
        correct=correct,
        explanation=feedback.explanation,
        visualization_hint=feedback.visualization_hint,
        correct_option_id=None,
    )


def grade_quiz(quiz: Quiz, answers: list[QuizAnswerRequest]) -> tuple[int, list[QuizAnswerResult]]:
    by_id = {a.question_id: a for a in answers}
    results: list[QuizAnswerResult] = []
    score = 0
    for question in quiz.questions:
        answer = by_id.get(question.id) or QuizAnswerRequest(question_id=question.id)
        result = grade_question(question, answer)
        if result.correct:
            score += 1
        results.append(result)
    return score, results
