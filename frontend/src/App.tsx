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
import type {
  CourseOutline,
  PracticeBank as PracticeBankData,
  ProgressOut,
  Quiz,
} from "./api/types";
import { CourseProgressOverview } from "./components/CourseProgressOverview";
import { ModuleDetail } from "./components/ModuleDetail";
import { PracticeBank } from "./components/PracticeBank";
import { PracticeScenarioDetail } from "./components/PracticeScenarioDetail";
import { QuizPanel } from "./components/QuizPanel";
import { t, uiT, type Locale } from "./i18n/messages";
import {
  courseHashFor,
  isKnownModuleId,
  isKnownScenarioId,
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
  const [practiceBank, setPracticeBank] = useState<PracticeBankData | null>(null);
  const [accessToken, setAccessToken] = useState<string | null>(() =>
    getStoredAccessToken(),
  );
  const [hasSession, setHasSession] = useState<boolean>(() => hasStoredSessionFlag());
  const [progress, setProgress] = useState<ProgressOut[]>([]);
  const [view, setView] = useState<CourseView>(() => readViewFromLocation());
  const [quiz, setQuiz] = useState<Quiz | null>(null);
  const [quizLoadError, setQuizLoadError] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);
  const progressGenRef = useRef(0);
  const lastModuleIdRef = useRef<string | null>(null);
  const lastScenarioIdRef = useRef<string | null>(null);

  const selectedId =
    view.kind === "module" || view.kind === "module-quiz"
      ? view.moduleId
      : null;
  const selectedScenarioId =
    view.kind === "practice-scenario" ? view.scenarioId : null;

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
        const [outline, bank] = await Promise.all([api.course(), api.practice()]);
        if (cancelled) return;
        setCourse(outline);
        setPracticeBank(bank);
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
    if (!course) return;
    if (view.kind !== "module" && view.kind !== "module-quiz") return;
    const ids = course.modules.map((m) => m.id);
    if (!isKnownModuleId(view.moduleId, ids)) {
      setView({ kind: "overview" });
      window.history.replaceState(null, "", courseHashFor({ kind: "overview" }));
      return;
    }
    if (view.kind === "module-quiz") {
      const mod = course.modules.find((m) => m.id === view.moduleId);
      if (!mod?.quiz_id) {
        const lesson: CourseView = { kind: "module", moduleId: view.moduleId };
        setView(lesson);
        window.history.replaceState(null, "", courseHashFor(lesson));
      }
    }
  }, [course, view]);

  useEffect(() => {
    if (!practiceBank || view.kind !== "practice-scenario") return;
    const ids = practiceBank.scenarios.map((s) => s.id);
    if (!isKnownScenarioId(view.scenarioId, ids)) {
      setView({ kind: "practice" });
      window.history.replaceState(null, "", courseHashFor({ kind: "practice" }));
    }
  }, [practiceBank, view]);

  useEffect(() => {
    setQuiz(null);
    setQuizLoadError(false);
    if (view.kind !== "module-quiz") return;
    const module = course?.modules.find((m) => m.id === view.moduleId);
    if (!module?.quiz_id) return;
    const quizId = module.quiz_id;
    let cancelled = false;
    (async () => {
      try {
        const q = await api.quiz(quizId);
        if (!cancelled) {
          setQuiz(q);
          setQuizLoadError(false);
        }
      } catch (err) {
        if (!cancelled) {
          setQuizLoadError(true);
          handleApiFailure(err);
        }
      }
    })();
    return () => {
      cancelled = true;
    };
  }, [view, course]);

  function orderedModules() {
    return course
      ? [...course.modules].sort((a, b) => a.order - b.order)
      : [];
  }

  function orderedScenarios() {
    return practiceBank
      ? [...practiceBank.scenarios].sort((a, b) => a.order - b.order)
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

  async function trackProgressId(
    progressId: string,
    token?: string | null,
  ) {
    const gen = ++progressGenRef.current;
    try {
      await api.updateProgress(
        { module_id: progressId, status: "in_progress" },
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

  async function openModule(
    moduleId: string,
    opts?: { token?: string | null; trackProgress?: boolean },
  ) {
    navigate({ kind: "module", moduleId });
    const token = opts?.token ?? accessToken;
    const track = opts?.trackProgress ?? hasSession;
    if (!track) return;
    await trackProgressId(moduleId, token);
  }

  async function openScenario(
    scenarioId: string,
    opts?: { token?: string | null; trackProgress?: boolean },
  ) {
    navigate({ kind: "practice-scenario", scenarioId });
    const token = opts?.token ?? accessToken;
    const track = opts?.trackProgress ?? hasSession;
    if (!track) return;
    await trackProgressId(scenarioId, token);
  }

  function openModuleQuiz(moduleId: string) {
    navigate({ kind: "module-quiz", moduleId });
  }

  function backToLesson(moduleId: string) {
    navigate({ kind: "module", moduleId });
  }

  function backToCourse() {
    navigate({ kind: "overview" });
  }

  function openPracticeBank() {
    navigate({ kind: "practice" });
  }

  function backToPractice() {
    navigate({ kind: "practice" });
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
      setQuizLoadError(false);
      navigate({ kind: "overview" }, true);
    }
  }

  const modules = orderedModules();
  const scenarios = orderedScenarios();
  const selected = modules.find((m) => m.id === selectedId) ?? null;
  const selectedIndex = selected
    ? modules.findIndex((m) => m.id === selected.id)
    : -1;
  const nextModule =
    selectedIndex >= 0 && selectedIndex < modules.length - 1
      ? modules[selectedIndex + 1]
      : null;
  const selectedScenario =
    scenarios.find((s) => s.id === selectedScenarioId) ?? null;
  const selectedScenarioIndex = selectedScenario
    ? scenarios.findIndex((s) => s.id === selectedScenario.id)
    : -1;
  const nextScenario =
    selectedScenarioIndex >= 0 && selectedScenarioIndex < scenarios.length - 1
      ? scenarios[selectedScenarioIndex + 1]
      : null;

  const showingModule = view.kind === "module" && selected != null;
  const showingModuleQuiz = view.kind === "module-quiz" && selected != null;
  const showingPracticeBank = view.kind === "practice" && practiceBank != null;
  const showingPracticeScenario =
    view.kind === "practice-scenario" && selectedScenario != null;
  const showingOverview =
    Boolean(course) &&
    !showingModule &&
    !showingModuleQuiz &&
    !showingPracticeBank &&
    !showingPracticeScenario;
  const matchedQuiz =
    showingModuleQuiz &&
    quiz &&
    selected?.quiz_id &&
    quiz.id === selected.quiz_id
      ? quiz
      : null;

  useLayoutEffect(() => {
    if (loading || !course) return;
    if (showingModuleQuiz && selectedId) {
      lastModuleIdRef.current = selectedId;
      focusById(matchedQuiz ? "quiz-heading" : "quiz-view-heading");
      return;
    }
    if (showingModule && selectedId) {
      lastModuleIdRef.current = selectedId;
      focusById("module-heading");
      return;
    }
    if (showingPracticeScenario && selectedScenarioId) {
      lastScenarioIdRef.current = selectedScenarioId;
      focusById("practice-scenario-heading");
      return;
    }
    if (showingPracticeBank) {
      if (lastScenarioIdRef.current) {
        lastScenarioIdRef.current = null;
        focusById("practice-bank-heading");
      }
      return;
    }
    if (lastModuleIdRef.current || lastScenarioIdRef.current) {
      lastModuleIdRef.current = null;
      lastScenarioIdRef.current = null;
      focusById("course-progress-heading");
    }
  }, [
    showingModule,
    showingModuleQuiz,
    matchedQuiz,
    showingPracticeBank,
    showingPracticeScenario,
    selectedId,
    selectedScenarioId,
    loading,
    course,
  ]);

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

        {showingOverview && course && (
          <>
            <p className="muted">{t(course.description, locale)}</p>
            <div className="hero-actions">
              <button className="btn btn-primary" type="button" onClick={startOrResume}>
                {hasSession ? uiT("resume", locale) : uiT("start", locale)}
              </button>
              <button className="btn" type="button" onClick={openPracticeBank}>
                {uiT("openPracticeBank", locale)}
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
              locale={locale}
              onOpenQuiz={
                selected.quiz_id
                  ? () => openModuleQuiz(selected.id)
                  : undefined
              }
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

        {course && showingModuleQuiz && selected && (
          <div className="module-view quiz-view">
            <nav
              className="module-view-nav"
              aria-label={uiT("quizChrome", locale)}
            >
              <button
                type="button"
                className="btn btn-back"
                onClick={() => backToLesson(selected.id)}
              >
                ← {uiT("backToLesson", locale)}
              </button>
              <p className="module-step muted" aria-live="polite">
                {t(selected.title, locale)}
              </p>
              {hasSession && (
                <button className="btn" type="button" onClick={endSession}>
                  {uiT("endSession", locale)}
                </button>
              )}
            </nav>

            {matchedQuiz ? (
              <QuizPanel
                key={matchedQuiz.id}
                quiz={matchedQuiz}
                locale={locale}
                accessToken={accessToken}
                hasSession={hasSession}
                onGraded={() => {
                  void refreshProgress(accessToken).catch((err) =>
                    handleApiFailure(err),
                  );
                }}
              />
            ) : quizLoadError ? (
              <p id="quiz-view-heading" className="error" role="alert" tabIndex={-1}>
                {uiT("quizLoadFailed", locale)}
              </p>
            ) : (
              <p id="quiz-view-heading" className="muted" tabIndex={-1}>
                {uiT("quizLoading", locale)}
              </p>
            )}

            <div className="module-view-footer">
              <button
                type="button"
                className="btn"
                onClick={() => backToLesson(selected.id)}
              >
                ← {uiT("backToLesson", locale)}
              </button>
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

        {showingPracticeBank && practiceBank && (
          <PracticeBank
            scenarios={practiceBank.scenarios}
            progress={progress}
            locale={locale}
            hasSession={hasSession}
            onSelectScenario={(id) => {
              void openScenario(id);
            }}
            onBackToCourse={backToCourse}
          />
        )}

        {showingPracticeScenario && selectedScenario && (
          <PracticeScenarioDetail
            scenario={selectedScenario}
            scenarioIndex={selectedScenarioIndex}
            scenarioTotal={scenarios.length}
            nextScenario={nextScenario}
            locale={locale}
            accessToken={accessToken}
            hasSession={hasSession}
            onBackToBank={backToPractice}
            onOpenNext={(id) => {
              void openScenario(id);
            }}
            onGraded={() => {
              void refreshProgress(accessToken).catch((err) => handleApiFailure(err));
            }}
          />
        )}
      </main>
    </div>
  );
}
