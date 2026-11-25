import { useState } from "react";
import type { PracticeScenario, ProgressOut } from "../api/types";
import { t, uiT, type Locale } from "../i18n/messages";
import { ModuleVisual } from "./ModuleVisual";

type Filter = "all" | "field" | "indoor";

type Props = {
  scenarios: PracticeScenario[];
  progress: ProgressOut[];
  locale: Locale;
  hasSession: boolean;
  onSelectScenario: (scenarioId: string) => void;
  onBackToCourse: () => void;
};

function normalizeStatus(raw: string | undefined): "not_started" | "in_progress" | "completed" {
  if (raw === "completed" || raw === "in_progress") return raw;
  return "not_started";
}

function kindLabel(kind: PracticeScenario["kind"], locale: Locale): string {
  return kind === "field" ? uiT("kindField", locale) : uiT("kindIndoor", locale);
}

export function PracticeBank({
  scenarios,
  progress,
  locale,
  hasSession,
  onSelectScenario,
  onBackToCourse,
}: Props) {
  const [filter, setFilter] = useState<Filter>("all");
  const headingId = "practice-bank-heading";
  const progressMap = Object.fromEntries(progress.map((p) => [p.module_id, p]));
  const ordered = [...scenarios].sort((a, b) => a.order - b.order);
  const filtered =
    filter === "all" ? ordered : ordered.filter((s) => s.kind === filter);
  const completedCount = ordered.filter(
    (s) => normalizeStatus(progressMap[s.id]?.status) === "completed",
  ).length;

  return (
    <section className="practice-bank" aria-labelledby={headingId}>
      <nav className="module-view-nav" aria-label={uiT("practiceNav", locale)}>
        <button type="button" className="btn btn-back" onClick={onBackToCourse}>
          ← {uiT("backToCourse", locale)}
        </button>
      </nav>

      <h2 id={headingId} className="section-title" tabIndex={-1}>
        {uiT("practiceBank", locale)}
      </h2>
      <p className="muted">{uiT("practiceBankIntro", locale)}</p>

      {hasSession && (
        <p className="muted" aria-live="polite">
          {uiT("practiceProgress", locale)
            .replace("{done}", String(completedCount))
            .replace("{total}", String(ordered.length))}
        </p>
      )}

      <div
        className="practice-filters"
        role="group"
        aria-label={uiT("practiceBank", locale)}
      >
        {(
          [
            ["all", "practiceFilterAll"],
            ["field", "practiceFilterField"],
            ["indoor", "practiceFilterIndoor"],
          ] as const
        ).map(([value, key]) => (
          <button
            key={value}
            type="button"
            className="btn"
            aria-pressed={filter === value}
            onClick={() => setFilter(value)}
          >
            {uiT(key, locale)}
          </button>
        ))}
      </div>

      <ol className="practice-list">
        {filtered.map((scenario) => {
          const row = progressMap[scenario.id];
          const status = normalizeStatus(row?.status);
          const score =
            row?.quiz_score != null && row.quiz_total != null
              ? `${row.quiz_score}/${row.quiz_total}`
              : null;
          return (
            <li key={scenario.id}>
              <article className="practice-card panel">
                <div className="practice-card-head">
                  <span className="pill">{kindLabel(scenario.kind, locale)}</span>
                  {hasSession && (
                    <span className={`status-${status}`}>
                      {status === "completed"
                        ? uiT("statusCompleted", locale)
                        : status === "in_progress"
                          ? uiT("statusInProgress", locale)
                          : uiT("statusNotStarted", locale)}
                      {score ? ` · ${score}` : ""}
                    </span>
                  )}
                </div>
                <h3>{t(scenario.title, locale)}</h3>
                <p className="muted">{t(scenario.focus, locale)}</p>
                <ModuleVisual
                  visual={{
                    id: `preview-${scenario.id}`,
                    kind: "svg_animation",
                    title: scenario.title,
                    caption: scenario.focus,
                    animation_key: scenario.visual_key,
                    official_source_url: null,
                    official_source_name: null,
                    knhb_illustration_placeholder: false,
                  }}
                  locale={locale}
                  compact
                />
                <button
                  type="button"
                  className="btn btn-primary"
                  onClick={() => onSelectScenario(scenario.id)}
                >
                  {uiT("openScenario", locale)}
                </button>
              </article>
            </li>
          );
        })}
      </ol>
    </section>
  );
}
