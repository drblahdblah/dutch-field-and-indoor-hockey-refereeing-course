import type { PracticeScenario } from "../api/types";
import { quizVizTitle, t, uiT, type Locale } from "../i18n/messages";
import { ModuleVisual } from "./ModuleVisual";
import { QuizPanel } from "./QuizPanel";

type Props = {
  scenario: PracticeScenario;
  scenarioIndex: number;
  scenarioTotal: number;
  nextScenario: PracticeScenario | null;
  locale: Locale;
  accessToken: string | null;
  hasSession: boolean;
  onBackToBank: () => void;
  onOpenNext: (scenarioId: string) => void;
  onGraded?: () => void;
};

export function PracticeScenarioDetail({
  scenario,
  scenarioIndex,
  scenarioTotal,
  nextScenario,
  locale,
  accessToken,
  hasSession,
  onBackToBank,
  onOpenNext,
  onGraded,
}: Props) {
  const vizTitle = quizVizTitle(scenario.visual_key);

  return (
    <div className="practice-scenario-detail">
      <nav className="module-view-nav" aria-label={uiT("practiceNav", locale)}>
        <button type="button" className="btn btn-back" onClick={onBackToBank}>
          ← {uiT("backToPractice", locale)}
        </button>
        <p className="module-step muted" aria-live="polite">
          {uiT("practiceStep", locale)
            .replace("{current}", String(scenarioIndex + 1))
            .replace("{total}", String(scenarioTotal))}
        </p>
      </nav>

      <article className="panel">
        <p className="pill">
          {scenario.kind === "field"
            ? uiT("kindField", locale)
            : uiT("kindIndoor", locale)}
        </p>
        <h2 id="practice-scenario-heading" tabIndex={-1}>
          {t(scenario.title, locale)}
        </h2>
        <p className="muted">
          <strong>{uiT("practiceFocus", locale)}:</strong>{" "}
          {t(scenario.focus, locale)}
        </p>
        <h3>{uiT("practiceSituation", locale)}</h3>
        <p>{t(scenario.situation, locale)}</p>
        <ModuleVisual
          visual={{
            id: `scenario-viz-${scenario.id}`,
            kind: "svg_animation",
            title: vizTitle,
            caption: scenario.focus,
            animation_key: scenario.visual_key,
            official_source_url: null,
            official_source_name: null,
            knhb_illustration_placeholder: false,
          }}
          locale={locale}
        />
      </article>

      <QuizPanel
        key={scenario.quiz.id}
        quiz={scenario.quiz}
        locale={locale}
        accessToken={accessToken}
        hasSession={hasSession}
        onGraded={onGraded}
      />

      <div className="module-view-footer">
        <button type="button" className="btn" onClick={onBackToBank}>
          {uiT("backToPractice", locale)}
        </button>
        {nextScenario && (
          <button
            type="button"
            className="btn btn-primary"
            onClick={() => onOpenNext(nextScenario.id)}
          >
            {uiT("goToNextScenario", locale)}: {t(nextScenario.title, locale)}
          </button>
        )}
      </div>
    </div>
  );
}
