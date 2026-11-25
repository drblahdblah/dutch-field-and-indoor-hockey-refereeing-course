import type {
  InterpretationReference,
  ModuleStub,
  Quiz,
  VisualPlaceholder,
} from "../api/types";
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

function InterpretationCard({
  refItem,
  visual,
  locale,
}: {
  refItem: InterpretationReference;
  visual: VisualPlaceholder | undefined;
  locale: Locale;
}) {
  const href = safeHttpUrl(refItem.official_source_url);
  return (
    <article
      className="interpretation-card"
      data-interp-id={refItem.id}
      aria-labelledby={`interp-${refItem.id}`}
    >
      <header className="interpretation-card-head">
        <h4 id={`interp-${refItem.id}`}>{t(refItem.topic, locale)}</h4>
        <span className="pill">{kindLabel(refItem.scope, locale)}</span>
      </header>
      <p>{t(refItem.summary, locale)}</p>
      {/* Top-level flags are the UI source of truth (nested attribution mirrors seed). */}
      {refItem.knhb_illustration_placeholder ? (
        <p className="placeholder-flag">{uiT("knhbPlaceholder", locale)}</p>
      ) : (
        refItem.translation_needed && (
          <p className="placeholder-flag">{uiT("translationNeeded", locale)}</p>
        )
      )}
      <p className="interpretation-source">
        <span className="muted">{uiT("officialSource", locale)}: </span>
        {href ? (
          <a href={href} target="_blank" rel="noopener noreferrer">
            {refItem.official_source_name}
            <span className="sr-only"> {uiT("opensInNewTab", locale)}</span>
          </a>
        ) : (
          <span>{refItem.official_source_name}</span>
        )}
      </p>
      <p className="muted attribution-note">{t(refItem.attribution.note, locale)}</p>
      {visual && <ModuleVisual visual={visual} locale={locale} compact />}
    </article>
  );
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
  const refs = module.interpretation_references ?? [];

  return (
    <article className="panel" aria-labelledby="module-heading">
      <p className="module-meta">
        <span className="pill">{kindLabel(module.kind, locale)}</span>
        <span className={`pill content-${module.content_status}`}>
          {isFull ? uiT("contentFull", locale) : uiT("contentStub", locale)}
        </span>
      </p>
      <h2 id="module-heading" tabIndex={-1}>
        {t(module.title, locale)}
      </h2>
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

      {refs.length > 0 && (
        <section
          className="interpretation-refs"
          aria-labelledby="interp-refs-heading"
        >
          <h3 id="interp-refs-heading">{uiT("interpretationRefs", locale)}</h3>
          <div className="interpretation-grid">
            {refs.map((refItem) => (
              <InterpretationCard
                key={refItem.id}
                refItem={refItem}
                visual={
                  refItem.visual_id ? byVisualId[refItem.visual_id] : undefined
                }
                locale={locale}
              />
            ))}
          </div>
        </section>
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
                      <span className="sr-only"> {uiT("opensInNewTab", locale)}</span>
                    </a>
                  ) : (
                    <span>{t(item.title, locale)}</span>
                  )}
                  {item.attribution.knhb_illustration_placeholder && (
                    <div className="placeholder-flag">{uiT("knhbPlaceholder", locale)}</div>
                  )}
                  {item.attribution.translation_needed && (
                    <div className="placeholder-flag">{uiT("translationNeeded", locale)}</div>
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
