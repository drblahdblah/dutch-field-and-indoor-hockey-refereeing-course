import { useState } from "react";
import { api } from "../api/client";
import { ApiError } from "../api/errors";
import type { Quiz, QuizSubmitResult } from "../api/types";
import { t, uiT, type Locale } from "../i18n/messages";
import { QuizVizHook } from "./ModuleVisual";

type Props = {
  quiz: Quiz;
  locale: Locale;
  accessToken: string | null;
  hasSession: boolean;
  onGraded?: () => void;
};

export function QuizPanel({
  quiz,
  locale,
  accessToken,
  hasSession,
  onGraded,
}: Props) {
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
      // Backend already fail-opens grading when save auth fails (HTTP 200).
      // If the client still sees 401, retry once without progress save so feedback shows.
      let graded: QuizSubmitResult;
      try {
        graded = await api.submitQuiz(quiz.id, answers, {
          saveProgress: hasSession,
          accessToken,
        });
      } catch (firstErr) {
        if (hasSession && firstErr instanceof ApiError && firstErr.isUnauthorized) {
          graded = await api.submitQuiz(quiz.id, answers, {
            saveProgress: false,
            accessToken: null,
          });
        } else {
          throw firstErr;
        }
      }
      setResult(graded);
      onGraded?.();
    } catch {
      setError(uiT("error", locale));
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
        const promptText = t(q.prompt, locale);
        return (
          <div className="question" key={q.id}>
            <p>
              <strong>
                {index + 1}. {promptText}
              </strong>
            </p>
            {q.type === "multiple_choice" && q.options ? (
              <div className="options" role="radiogroup" aria-label={promptText}>
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
                aria-label={promptText}
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
                  <QuizVizHook
                    hint={feedback.visualization_hint}
                    locale={locale}
                    correct={feedback.correct}
                  />
                )}
              </div>
            )}
          </div>
        );
      })}
      <button
        className="btn btn-primary"
        type="button"
        disabled={busy}
        aria-busy={busy || undefined}
        aria-label={busy ? uiT("submitting", locale) : undefined}
        onClick={submit}
      >
        {busy ? uiT("submitting", locale) : uiT("submit", locale)}
      </button>
      {result && (
        <p className="muted">
          {uiT("score", locale)}: {result.score}/{result.total}
        </p>
      )}
      {error && (
        <p className="error" role="alert">
          {error}
        </p>
      )}
    </section>
  );
}
