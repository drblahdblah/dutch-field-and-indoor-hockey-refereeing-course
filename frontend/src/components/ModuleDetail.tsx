import type { ModuleStub, Quiz } from "../api/types";
import { safeHttpUrl } from "../api/urls";
import { t, uiT, type Locale } from "../i18n/messages";
import { QuizPanel } from "./QuizPanel";

type Props = {
  module: ModuleStub;
  quiz: Quiz | null;
  locale: Locale;
  accessToken: string | null;
  hasSession: boolean;
  onGraded?: () => void;
};

function kindLabel(kind: ModuleStub["kind"], locale: Locale): string {
  if (kind === "field") return uiT("kindField", locale);
  if (kind === "indoor") return uiT("kindIndoor", locale);
  return uiT("kindShared", locale);
}

export function ModuleDetail({
  module,
  quiz,
  locale,
  accessToken,
  hasSession,
  onGraded,
}: Props) {
  return (
    <article className="panel" aria-labelledby="module-heading">
      <p className="module-meta">
        <span className="pill">{kindLabel(module.kind, locale)}</span>
      </p>
      <h2 id="module-heading">{t(module.title, locale)}</h2>
      <p>{t(module.summary, locale)}</p>

      <h3>{locale === "nl" ? "Leerdoelen" : "Learning objectives"}</h3>
      <ul className="objectives">
        {module.learning_objectives.map((obj, i) => (
          <li key={i}>{t(obj, locale)}</li>
        ))}
      </ul>

      <h3>{locale === "nl" ? "Instructie" : "Instruction"}</h3>
      <ul className="instructions">
        {module.instruction_outline.map((line, i) => (
          <li key={i}>{t(line, locale)}</li>
        ))}
      </ul>

      {module.further_reading.length > 0 && (
        <>
          <h3>{uiT("furtherReading", locale)}</h3>
          <ul>
            {module.further_reading.map((item) => {
              const href = safeHttpUrl(item.url);
              return (
                <li key={item.url}>
                  {href ? (
                    <a href={href} target="_blank" rel="noopener noreferrer">
                      {t(item.title, locale)}
                    </a>
                  ) : (
                    <span>{t(item.title, locale)}</span>
                  )}
                  {item.attribution.knhb_illustration_placeholder && (
                    <div className="placeholder-flag">{uiT("knhbPlaceholder", locale)}</div>
                  )}
                </li>
              );
            })}
          </ul>
        </>
      )}

      {quiz && (
        <QuizPanel
          quiz={quiz}
          locale={locale}
          accessToken={accessToken}
          hasSession={hasSession}
          onGraded={onGraded}
        />
      )}
    </article>
  );
}
