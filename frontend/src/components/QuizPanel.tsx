import { useState } from "react";
import { api } from "../api/client";
import type { Quiz, QuizSubmitResult } from "../api/types";
import { t, uiT, type Locale } from "../i18n/messages";

type Props = {
  quiz: Quiz;
  locale: Locale;
  sessionId: string | null;
  onGraded?: () => void;
};

export function QuizPanel({ quiz, locale, sessionId, onGraded }: Props) {
  const [selections, setSelections] = useState<Record<string, string>>({});
  const [written, setWritten] = useState<Record<string, string>>({});
  const [result, setResult] = useState<QuizSubmitResult | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  async function submit() {
    setBusy(true);
    setError(null);
    try {
      const answers = quiz.questions.map((q) =>
        q.type === "multiple_choice"
          ? { question_id: q.id, selected_option_id: selections[q.id] }
          : { question_id: q.id, written_answer: written[q.id] ?? "" },
      );
      const graded = await api.submitQuiz(quiz.id, answers, sessionId);
      setResult(graded);
      onGraded?.();
    } catch (err) {
      setError(err instanceof Error ? err.message : uiT("error", locale));
    } finally {
      setBusy(false);
    }
  }

  const byQuestion = Object.fromEntries(
    (result?.results ?? []).map((r) => [r.question_id, r]),
  );

  return (
    <section className="panel" aria-labelledby="quiz-heading">
      <h2 id="quiz-heading">{t(quiz.title, locale)}</h2>
      {quiz.questions.map((q, index) => {
        const feedback = byQuestion[q.id];
        return (
          <div className="question" key={q.id}>
            <p>
              <strong>
                {index + 1}. {t(q.prompt, locale)}
              </strong>
            </p>
            {q.type === "multiple_choice" && q.options ? (
              <div className="options" role="radiogroup" aria-label={t(q.prompt, locale)}>
                {q.options.map((opt) => (
                  <label className="option" key={opt.id}>
                    <input
                      type="radio"
                      name={q.id}
                      value={opt.id}
                      checked={selections[q.id] === opt.id}
                      onChange={() =>
                        setSelections((prev) => ({ ...prev, [q.id]: opt.id }))
                      }
                    />
                    <span>{t(opt.text, locale)}</span>
                  </label>
                ))}
              </div>
            ) : (
              <input
                className="written-input"
                value={written[q.id] ?? ""}
                placeholder={uiT("writtenPlaceholder", locale)}
                onChange={(e) =>
                  setWritten((prev) => ({ ...prev, [q.id]: e.target.value }))
                }
              />
            )}
            {feedback && (
              <div className={`feedback ${feedback.correct ? "ok" : "bad"}`}>
                <strong>
                  {feedback.correct ? uiT("correct", locale) : uiT("incorrect", locale)}
                </strong>
                <p>{t(feedback.explanation, locale)}</p>
                {feedback.visualization_hint && (
                  <span className="viz-hint">
                    viz: {feedback.visualization_hint}
                  </span>
                )}
              </div>
            )}
          </div>
        );
      })}
      <button className="btn btn-primary" type="button" disabled={busy} onClick={submit}>
        {uiT("submit", locale)}
      </button>
      {result && (
        <p className="muted">
          {uiT("score", locale)}: {result.score}/{result.total}
        </p>
      )}
      {error && <p className="error">{error}</p>}
    </section>
  );
}
