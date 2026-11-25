import { useEffect, useLayoutEffect, useRef, useState } from "react";
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
import { CourseProgressOverview } from "./components/CourseProgressOverview";
import { ModuleDetail } from "./components/ModuleDetail";
import { t, uiT, type Locale } from "./i18n/messages";
import {
  courseHashFor,
  isKnownModuleId,
  parseCourseHash,
  type CourseView,
} from "./nav/courseHash";

function readViewFromLocation(): CourseView {
  if (typeof window === "undefined") return { kind: "overview" };
  return parseCourseHash(window.location.hash);
}

function focusById(id: string) {
  const el = document.getElementById(id);
  if (el && "focus" in el) {
    (el as HTMLElement).focus();
  }
}

export default function App() {
  const [locale, setLocale] = useState<Locale>("nl");
  const [course, setCourse] = useState<CourseOutline | null>(null);
  const [accessToken, setAccessToken] = useState<string | null>(() =>
    getStoredAccessToken(),
  );
  const [hasSession, setHasSession] = useState<boolean>(() => hasStoredSessionFlag());
  const [progress, setProgress] = useState<ProgressOut[]>([]);
  const [view, setView] = useState<CourseView>(() => readViewFromLocation());
  const [quiz, setQuiz] = useState<Quiz | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);
  const progressGenRef = useRef(0);
  const lastModuleIdRef = useRef<string | null>(null);

  const selectedId = view.kind === "module" ? view.moduleId : null;

  function navigate(next: CourseView, replace = false) {
    setView(next);
    const hash = courseHashFor(next);
    if (typeof window === "undefined") return;
    if (replace) {
      window.history.replaceState(null, "", hash);
    } else if (window.location.hash !== hash) {
      window.location.hash = hash;
    }
  }

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
    function onHashChange() {
      setView(readViewFromLocation());
    }
    window.addEventListener("hashchange", onHashChange);
    return () => window.removeEventListener("hashchange", onHashChange);
  }, []);

  useEffect(() => {
    if (!course || view.kind !== "module") return;
    const ids = course.modules.map((m) => m.id);
    if (!isKnownModuleId(view.moduleId, ids)) {
      setView({ kind: "overview" });
      window.history.replaceState(null, "", courseHashFor({ kind: "overview" }));
    }
  }, [course, view]);

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

  function orderedModules() {
    return course
      ? [...course.modules].sort((a, b) => a.order - b.order)
      : [];
  }

  async function startOrResume() {
    setError(null);
    try {
      const modules = orderedModules();
      if (hasSession) {
        const latest = await refreshProgress(accessToken);
        const firstIncomplete =
          modules.find(
            (m) =>
              latest.find((p) => p.module_id === m.id)?.status !== "completed",
          ) ?? modules[0];
        if (firstIncomplete) {
          await openModule(firstIncomplete.id);
        }
        return;
      }
      const session = await api.createSession(undefined, locale);
      storeAccessToken(session.access_token);
      setAccessToken(session.access_token);
      setHasSession(true);
      setProgress([]);
      if (modules[0]) {
        await openModule(modules[0].id, {
          token: session.access_token,
          trackProgress: true,
        });
      }
    } catch (err) {
      handleApiFailure(err);
    }
  }

  async function openModule(
    moduleId: string,
    opts?: { token?: string | null; trackProgress?: boolean },
  ) {
    navigate({ kind: "module", moduleId });
    const token = opts?.token ?? accessToken;
    const track = opts?.trackProgress ?? hasSession;
    if (!track) return;
    const gen = ++progressGenRef.current;
    try {
      await api.updateProgress(
        { module_id: moduleId, status: "in_progress" },
        token,
      );
      if (gen !== progressGenRef.current) return;
      const data = await api.getProgress(token);
      if (gen !== progressGenRef.current) return;
      setProgress(data.progress);
      setHasSession(true);
    } catch (err) {
      if (gen !== progressGenRef.current) return;
      handleApiFailure(err);
    }
  }

  function backToCourse() {
    navigate({ kind: "overview" });
  }

  async function endSession() {
    setError(null);
    try {
      if (hasSession) {
        await api.revokeSession(accessToken);
      }
    } catch (err) {
      if (!(err instanceof ApiError && err.isUnauthorized)) {
        setError(uiT("error", locale));
      }
    } finally {
      clearAccessToken();
      setAccessToken(null);
      setHasSession(false);
      setProgress([]);
      setQuiz(null);
      navigate({ kind: "overview" }, true);
    }
  }

  const modules = orderedModules();
  const selected = modules.find((m) => m.id === selectedId) ?? null;
  const selectedIndex = selected
    ? modules.findIndex((m) => m.id === selected.id)
    : -1;
  const nextModule =
    selectedIndex >= 0 && selectedIndex < modules.length - 1
      ? modules[selectedIndex + 1]
      : null;
  const showingModule = view.kind === "module" && selected != null;

  useLayoutEffect(() => {
    if (loading || !course) return;
    if (showingModule && selectedId) {
      lastModuleIdRef.current = selectedId;
      focusById("module-heading");
      return;
    }
    if (lastModuleIdRef.current) {
      lastModuleIdRef.current = null;
      focusById("course-progress-heading");
    }
  }, [showingModule, selectedId, loading, course]);

  return (
    <div className="app">
      <a className="skip-link" href="#main-content">
        {uiT("skipToContent", locale)}
      </a>
      <header className="topbar">
        <div>
          <h1 className="brand">{uiT("brand", locale)}</h1>
          <p className="tagline">{uiT("tagline", locale)}</p>
        </div>
        <div className="lang-switch" role="group" aria-label={uiT("language", locale)}>
          <button
            type="button"
            aria-pressed={locale === "nl"}
            aria-label={uiT("langNl", locale)}
            onClick={() => setLocale("nl")}
          >
            NL
          </button>
          <button
            type="button"
            aria-pressed={locale === "en"}
            aria-label={uiT("langEn", locale)}
            onClick={() => setLocale("en")}
          >
            EN
          </button>
        </div>
      </header>

      <main id="main-content" tabIndex={-1} aria-label={uiT("mainContent", locale)}>
        {loading && <p className="muted">{uiT("loading", locale)}</p>}
        {error && (
          <p className="error" role="alert">
            {error}
          </p>
        )}

        {course && !showingModule && (
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

            <CourseProgressOverview
              modules={course.modules}
              progress={progress}
              selectedId={null}
              locale={locale}
              hasSession={hasSession}
              onSelectModule={(id) => {
                void openModule(id);
              }}
            />

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
                            <span className="sr-only"> {uiT("opensInNewTab", locale)}</span>
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

        {course && showingModule && selected && (
          <div className="module-view">
            <nav
              className="module-view-nav"
              aria-label={uiT("moduleChrome", locale)}
            >
              <button
                type="button"
                className="btn btn-back"
                onClick={backToCourse}
              >
                ← {uiT("backToCourse", locale)}
              </button>
              <p className="module-step muted" aria-live="polite">
                {uiT("moduleStep", locale)
                  .replace("{current}", String(selectedIndex + 1))
                  .replace("{total}", String(modules.length))}
              </p>
              {hasSession && (
                <button className="btn" type="button" onClick={endSession}>
                  {uiT("endSession", locale)}
                </button>
              )}
            </nav>

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

            <div className="module-view-footer">
              {nextModule && (
                <button
                  type="button"
                  className="btn btn-primary"
                  onClick={() => {
                    void openModule(nextModule.id);
                  }}
                >
                  {uiT("goToNextModule", locale)}: {t(nextModule.title, locale)}
                </button>
              )}
            </div>
          </div>
        )}
      </main>
    </div>
  );
}
