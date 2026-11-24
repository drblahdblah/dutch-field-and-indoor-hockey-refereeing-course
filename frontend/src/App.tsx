import { useEffect, useState } from "react";
import { api } from "./api/client";
import type { CourseOutline, ProgressOut, Quiz } from "./api/types";
import { ModuleDetail } from "./components/ModuleDetail";
import { t, uiT, type Locale } from "./i18n/messages";

const SESSION_KEY = "umpire-course-session-id";

export default function App() {
  const [locale, setLocale] = useState<Locale>("nl");
  const [course, setCourse] = useState<CourseOutline | null>(null);
  const [sessionId, setSessionId] = useState<string | null>(
    () => localStorage.getItem(SESSION_KEY),
  );
  const [progress, setProgress] = useState<ProgressOut[]>([]);
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [quiz, setQuiz] = useState<Quiz | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  async function refreshProgress(id: string) {
    const data = await api.getProgress(id);
    setProgress(data.progress);
  }

  useEffect(() => {
    let cancelled = false;
    (async () => {
      try {
        const outline = await api.course();
        if (cancelled) return;
        setCourse(outline);
        if (sessionId) {
          try {
            await refreshProgress(sessionId);
          } catch {
            localStorage.removeItem(SESSION_KEY);
            setSessionId(null);
          }
        }
      } catch (err) {
        if (!cancelled) {
          setError(err instanceof Error ? err.message : uiT("error", locale));
        }
      } finally {
        if (!cancelled) setLoading(false);
      }
    })();
    return () => {
      cancelled = true;
    };
  }, []);

  useEffect(() => {
    document.documentElement.lang = locale;
  }, [locale]);

  useEffect(() => {
    const module = course?.modules.find((m) => m.id === selectedId);
    if (!module?.quiz_id) {
      setQuiz(null);
      return;
    }
    let cancelled = false;
    (async () => {
      try {
        const q = await api.quiz(module.quiz_id!);
        if (!cancelled) setQuiz(q);
      } catch (err) {
        if (!cancelled) {
          setError(err instanceof Error ? err.message : uiT("error", locale));
        }
      }
    })();
    return () => {
      cancelled = true;
    };
  }, [selectedId, course]);

  async function startOrResume() {
    setError(null);
    try {
      if (sessionId) {
        await refreshProgress(sessionId);
        const firstIncomplete =
          course?.modules.find(
            (m) =>
              progress.find((p) => p.module_id === m.id)?.status !== "completed",
          ) ?? course?.modules[0];
        setSelectedId(firstIncomplete?.id ?? null);
        return;
      }
      const session = await api.createSession(undefined, locale);
      localStorage.setItem(SESSION_KEY, session.id);
      setSessionId(session.id);
      setProgress([]);
      setSelectedId(course?.modules[0]?.id ?? null);
    } catch (err) {
      setError(err instanceof Error ? err.message : uiT("error", locale));
    }
  }

  async function openModule(moduleId: string) {
    setSelectedId(moduleId);
    if (!sessionId) return;
    try {
      await api.updateProgress(sessionId, {
        module_id: moduleId,
        status: "in_progress",
      });
      await refreshProgress(sessionId);
    } catch (err) {
      setError(err instanceof Error ? err.message : uiT("error", locale));
    }
  }

  const selected = course?.modules.find((m) => m.id === selectedId) ?? null;
  const progressMap = Object.fromEntries(progress.map((p) => [p.module_id, p]));

  return (
    <div className="app">
      <header className="topbar">
        <div>
          <h1 className="brand">{uiT("brand", locale)}</h1>
          <p className="tagline">{uiT("tagline", locale)}</p>
        </div>
        <div className="lang-switch" role="group" aria-label={uiT("language", locale)}>
          <button
            type="button"
            aria-pressed={locale === "nl"}
            onClick={() => setLocale("nl")}
          >
            NL
          </button>
          <button
            type="button"
            aria-pressed={locale === "en"}
            onClick={() => setLocale("en")}
          >
            EN
          </button>
        </div>
      </header>

      {loading && <p className="muted">{uiT("loading", locale)}</p>}
      {error && <p className="error">{error}</p>}

      {course && (
        <>
          <p className="muted">{t(course.description, locale)}</p>
          <div className="hero-actions">
            <button className="btn btn-primary" type="button" onClick={startOrResume}>
              {sessionId ? uiT("resume", locale) : uiT("start", locale)}
            </button>
            {sessionId && (
              <span className="muted">{uiT("sessionSaved", locale)}</span>
            )}
          </div>

          <h2 className="section-title">{uiT("modules", locale)}</h2>
          <div className="module-list">
            {course.modules
              .slice()
              .sort((a, b) => a.order - b.order)
              .map((mod) => {
                const status = progressMap[mod.id]?.status ?? "not_started";
                return (
                  <button
                    key={mod.id}
                    type="button"
                    className="module-row"
                    aria-current={selectedId === mod.id}
                    onClick={() => openModule(mod.id)}
                  >
                    <div className="module-meta">
                      <span className="pill">
                        {mod.kind === "field"
                          ? uiT("kindField", locale)
                          : mod.kind === "indoor"
                            ? uiT("kindIndoor", locale)
                            : uiT("kindShared", locale)}
                      </span>
                      <span className={`status-${status}`}>
                        {uiT("progress", locale)}: {status}
                      </span>
                    </div>
                    <strong>{t(mod.title, locale)}</strong>
                    <div className="muted">{t(mod.summary, locale)}</div>
                  </button>
                );
              })}
          </div>

          {selected && (
            <ModuleDetail
              module={selected}
              quiz={quiz}
              locale={locale}
              sessionId={sessionId}
              onGraded={() => sessionId && refreshProgress(sessionId)}
            />
          )}

          <section className="panel" aria-labelledby="attr-heading">
            <h2 id="attr-heading">{uiT("attribution", locale)}</h2>
            <ul className="attribution-list">
              {course.attributions.map((a) => (
                <li key={a.source_name}>
                  <strong>
                    {a.source_url ? (
                      <a href={a.source_url} target="_blank" rel="noreferrer">
                        {a.source_name}
                      </a>
                    ) : (
                      a.source_name
                    )}
                  </strong>
                  <p>{t(a.note, locale)}</p>
                  {a.knhb_illustration_placeholder && (
                    <p className="placeholder-flag">{uiT("knhbPlaceholder", locale)}</p>
                  )}
                </li>
              ))}
            </ul>
          </section>
        </>
      )}
    </div>
  );
}
