import type { ModuleStub, Quiz, VisualPlaceholder } from "../api/types";
import { safeHttpUrl } from "../api/urls";
import { t, uiT, type Locale } from "../i18n/messages";
import { ModuleVisual } from "./ModuleVisual";
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

function visualMap(module: ModuleStub): Record<string, VisualPlaceholder> {
  return Object.fromEntries(module.visuals.map((v) => [v.id, v]));
}

export function ModuleDetail({
  module,
  quiz,
  locale,
  accessToken,
  hasSession,
  onGraded,
}: Props) {
  const isFull = module.content_status === "full";
  const byVisualId = visualMap(module);
  const matchedQuiz =
    quiz && module.quiz_id && quiz.id === module.quiz_id ? quiz : null;

  return (
    <article className="panel" aria-labelledby="module-heading">
      <p className="module-meta">
        <span className="pill">{kindLabel(module.kind, locale)}</span>
        <span className={`pill content-${module.content_status}`}>
          {isFull ? uiT("contentFull", locale) : uiT("contentStub", locale)}
        </span>
      </p>
      <h2 id="module-heading">{t(module.title, locale)}</h2>
      <p>{t(module.summary, locale)}</p>

      <h3>{uiT("learningObjectives", locale)}</h3>
      <ul className="objectives">
        {module.learning_objectives.map((obj, i) => (
          <li key={i}>{t(obj, locale)}</li>
        ))}
      </ul>

      {isFull && module.sections.length > 0 ? (
        <div className="learning-sections">
          <h3>{uiT("learningContent", locale)}</h3>
          {module.sections.map((section) => {
            const visual = section.visual_id
              ? byVisualId[section.visual_id]
              : undefined;
            return (
              <section
                key={section.id}
                className="learning-section"
                aria-labelledby={`section-${section.id}`}
              >
                <h4 id={`section-${section.id}`}>{t(section.title, locale)}</h4>
                {section.paragraphs.map((para, i) => (
                  <p key={i}>{t(para, locale)}</p>
                ))}
                {visual && <ModuleVisual visual={visual} locale={locale} />}
              </section>
            );
          })}
        </div>
      ) : (
        <>
          <h3>{uiT("instruction", locale)}</h3>
          <ul className="instructions">
            {module.instruction_outline.map((line, i) => (
              <li key={i}>{t(line, locale)}</li>
            ))}
          </ul>
        </>
      )}

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

      {matchedQuiz && (
        <QuizPanel
          key={matchedQuiz.id}
          quiz={matchedQuiz}
          locale={locale}
          accessToken={accessToken}
          hasSession={hasSession}
          onGraded={onGraded}
        />
      )}
    </article>
  );
}
