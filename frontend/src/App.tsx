import { useEffect, useState } from "react";
import {
  api,
  clearAccessToken,
  getStoredAccessToken,
  hasStoredSessionFlag,
  storeAccessToken,
} from "./api/client";
import { ApiError } from "./api/errors";
import { safeHttpUrl } from "./api/urls";
import type { CourseOutline, ProgressOut, Quiz } from "./api/types";
import { ModuleDetail } from "./components/ModuleDetail";
import { t, uiT, type Locale } from "./i18n/messages";

export default function App() {
  const [locale, setLocale] = useState<Locale>("nl");
  const [course, setCourse] = useState<CourseOutline | null>(null);
  const [accessToken, setAccessToken] = useState<string | null>(() =>
    getStoredAccessToken(),
  );
  const [hasSession, setHasSession] = useState<boolean>(() => hasStoredSessionFlag());
  const [progress, setProgress] = useState<ProgressOut[]>([]);
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [quiz, setQuiz] = useState<Quiz | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  function handleApiFailure(err: unknown) {
    if (err instanceof ApiError && err.isUnauthorized) {
      clearAccessToken();
      setAccessToken(null);
      setHasSession(false);
      setProgress([]);
    }
    setError(uiT("error", locale));
  }

  async function refreshProgress(token?: string | null): Promise<ProgressOut[]> {
    const data = await api.getProgress(token);
    setProgress(data.progress);
    setHasSession(true);
    return data.progress;
  }

  useEffect(() => {
    let cancelled = false;
    (async () => {
      try {
        const outline = await api.course();
        if (cancelled) return;
        setCourse(outline);
        try {
          await refreshProgress(accessToken);
        } catch (err) {
          if (err instanceof ApiError && err.isUnauthorized) {
            clearAccessToken();
            if (!cancelled) {
              setAccessToken(null);
              setHasSession(false);
            }
          } else if (!cancelled) {
            // Keep token on transient errors; show safe message.
            setError(uiT("error", locale));
          }
        }
      } catch {
        if (!cancelled) {
          setError(uiT("error", locale));
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
    setQuiz(null);
    const module = course?.modules.find((m) => m.id === selectedId);
    if (!module?.quiz_id) {
      return;
    }
    const quizId = module.quiz_id;
    let cancelled = false;
    (async () => {
      try {
        const q = await api.quiz(quizId);
        if (!cancelled) setQuiz(q);
      } catch (err) {
        if (!cancelled) handleApiFailure(err);
      }
    })();
    return () => {
      cancelled = true;
    };
  }, [selectedId, course]);

  async function startOrResume() {
    setError(null);
    try {
      if (hasSession) {
        const latest = await refreshProgress(accessToken);
        const firstIncomplete =
          course?.modules.find(
            (m) =>
              latest.find((p) => p.module_id === m.id)?.status !== "completed",
          ) ?? course?.modules[0];
        setSelectedId(firstIncomplete?.id ?? null);
        return;
      }
      const session = await api.createSession(undefined, locale);
      // Cookie is primary. Only persist bearer when the API returns one (dev expose).
      storeAccessToken(session.access_token);
      setAccessToken(session.access_token);
      setHasSession(true);
      setProgress([]);
      setSelectedId(course?.modules[0]?.id ?? null);
    } catch (err) {
      handleApiFailure(err);
    }
  }

  async function openModule(moduleId: string) {
    setSelectedId(moduleId);
    if (!hasSession) return;
    try {
      await api.updateProgress(
        { module_id: moduleId, status: "in_progress" },
        accessToken,
      );
      await refreshProgress(accessToken);
    } catch (err) {
      handleApiFailure(err);
    }
  }

  async function endSession() {
    setError(null);
    try {
      if (hasSession) {
        await api.revokeSession(accessToken);
      }
    } catch (err) {
      // Still clear local state even if revoke fails (e.g. already expired).
      if (!(err instanceof ApiError && err.isUnauthorized)) {
        setError(uiT("error", locale));
      }
    } finally {
      clearAccessToken();
      setAccessToken(null);
      setHasSession(false);
      setProgress([]);
      setSelectedId(null);
      setQuiz(null);
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
      {error && <p className="error" role="alert">
        {error}
      </p>}

      {course && (
        <>
          <p className="muted">{t(course.description, locale)}</p>
          <div className="hero-actions">
            <button className="btn btn-primary" type="button" onClick={startOrResume}>
              {hasSession ? uiT("resume", locale) : uiT("start", locale)}
            </button>
            {hasSession && (
              <>
                <button className="btn" type="button" onClick={endSession}>
                  {uiT("endSession", locale)}
                </button>
                <span className="muted">{uiT("sessionSaved", locale)}</span>
              </>
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
              accessToken={accessToken}
              hasSession={hasSession}
              onGraded={() => {
                void refreshProgress(accessToken).catch((err) => handleApiFailure(err));
              }}
            />
          )}

          <section className="panel" aria-labelledby="attr-heading">
            <h2 id="attr-heading">{uiT("attribution", locale)}</h2>
            <p className="muted">{uiT("licenseNote", locale)}</p>
            <ul className="attribution-list">
              {course.attributions.map((a) => {
                const href = safeHttpUrl(a.source_url);
                return (
                  <li key={a.source_name}>
                    <strong>
                      {href ? (
                        <a href={href} target="_blank" rel="noopener noreferrer">
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
                    {a.translation_needed && (
                      <p className="placeholder-flag">{uiT("translationNeeded", locale)}</p>
                    )}
                  </li>
                );
              })}
            </ul>
          </section>
        </>
      )}
    </div>
  );
}
