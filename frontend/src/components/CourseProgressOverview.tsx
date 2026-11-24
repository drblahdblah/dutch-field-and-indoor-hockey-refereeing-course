import { useId } from "react";
import type { ModuleStub, ProgressOut } from "../api/types";
import { t, uiT, type Locale } from "../i18n/messages";

export type ProgressStatus = "not_started" | "in_progress" | "completed";

type Props = {
  modules: ModuleStub[];
  progress: ProgressOut[];
  selectedId: string | null;
  locale: Locale;
  hasSession: boolean;
  onSelectModule: (moduleId: string) => void;
};

function normalizeStatus(raw: string | undefined): ProgressStatus {
  if (raw === "completed" || raw === "in_progress") return raw;
  return "not_started";
}

function statusLabel(status: ProgressStatus, locale: Locale): string {
  if (status === "completed") return uiT("statusCompleted", locale);
  if (status === "in_progress") return uiT("statusInProgress", locale);
  return uiT("statusNotStarted", locale);
}

function kindLabel(kind: ModuleStub["kind"], locale: Locale): string {
  if (kind === "field") return uiT("kindField", locale);
  if (kind === "indoor") return uiT("kindIndoor", locale);
  return uiT("kindShared", locale);
}

export function CourseProgressOverview({
  modules,
  progress,
  selectedId,
  locale,
  hasSession,
  onSelectModule,
}: Props) {
  const baseId = useId();
  const headingId = `${baseId}-heading`;
  const summaryId = `${baseId}-summary`;

  const ordered = [...modules].sort((a, b) => a.order - b.order);
  const progressMap = Object.fromEntries(progress.map((p) => [p.module_id, p]));
  const completedCount = ordered.filter(
    (m) => normalizeStatus(progressMap[m.id]?.status) === "completed",
  ).length;
  const total = ordered.length;
  const percent = total === 0 ? 0 : Math.round((completedCount / total) * 100);
  const allComplete = hasSession && total > 0 && completedCount === total;
  const nextUp =
    ordered.find(
      (m) => normalizeStatus(progressMap[m.id]?.status) !== "completed",
    ) ?? null;

  return (
    <section className="course-progress" aria-labelledby={headingId}>
      <div className="course-progress-head">
        <h2 id={headingId} className="section-title">
          {uiT("progressOverview", locale)}
        </h2>
        {hasSession ? (
          <p
            id={summaryId}
            className="course-progress-summary muted"
            aria-live="polite"
          >
            {uiT("modulesCompleted", locale)
              .replace("{done}", String(completedCount))
              .replace("{total}", String(total))}{" "}
            · {percent}%
          </p>
        ) : (
          <p id={summaryId} className="course-progress-summary muted">
            {uiT("progressStartHint", locale)}
          </p>
        )}
      </div>

      <div
        className="progress-track"
        role="progressbar"
        aria-valuemin={0}
        aria-valuemax={100}
        aria-valuenow={hasSession ? percent : 0}
        aria-label={uiT("progressOverview", locale)}
        aria-describedby={summaryId}
      >
        <div
          className="progress-track-fill"
          style={{ width: `${hasSession ? percent : 0}%` }}
        />
      </div>

      {hasSession && nextUp && (
        <p className="next-up">
          <span className="muted">{uiT("nextUp", locale)}: </span>
          <button
            type="button"
            className="linkish"
            onClick={() => onSelectModule(nextUp.id)}
          >
            {t(nextUp.title, locale)}
          </button>
        </p>
      )}

      {allComplete && (
        <p className="course-complete" role="status">
          {uiT("courseComplete", locale)}
        </p>
      )}

      <nav aria-label={uiT("courseNav", locale)}>
        <ol className="module-pathway">
          {ordered.map((mod, index) => {
            const row = progressMap[mod.id];
            const status = normalizeStatus(row?.status);
            const isSelected = selectedId === mod.id;
            const isNext = Boolean(hasSession && nextUp?.id === mod.id);
            const isDone = Boolean(hasSession && status === "completed");
            const score =
              row?.quiz_score != null && row.quiz_total != null
                ? `${row.quiz_score}/${row.quiz_total}`
                : null;

            return (
              <li key={mod.id}>
                <button
                  type="button"
                  className={[
                    "module-row",
                    "pathway-row",
                    isNext ? "is-next" : "",
                    isDone ? "is-done" : "",
                  ]
                    .filter(Boolean)
                    .join(" ")}
                  aria-current={isSelected ? "page" : undefined}
                  onClick={() => onSelectModule(mod.id)}
                >
                  {isNext && (
                    <span className="sr-only">{uiT("jumpToNext", locale)}: </span>
                  )}
                  <span className="pathway-step" aria-hidden="true">
                    {isDone ? "✓" : index + 1}
                  </span>
                  <div className="pathway-body">
                    <div className="module-meta">
                      <span className="pill">{kindLabel(mod.kind, locale)}</span>
                      {hasSession ? (
                        <>
                          <span className={`status-${status}`}>
                            {uiT("progress", locale)}:{" "}
                            {statusLabel(status, locale)}
                          </span>
                          {score && (
                            <span className="quiz-score muted">
                              {uiT("score", locale)}: {score}
                            </span>
                          )}
                          {isNext && (
                            <span className="pill next-pill">
                              {uiT("nextUp", locale)}
                            </span>
                          )}
                        </>
                      ) : (
                        <span className="muted">{uiT("progressIdle", locale)}</span>
                      )}
                    </div>
                    <strong>{t(mod.title, locale)}</strong>
                    <div className="muted">{t(mod.summary, locale)}</div>
                  </div>
                </button>
              </li>
            );
          })}
        </ol>
      </nav>
    </section>
  );
}
