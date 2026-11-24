import type { VisualPlaceholder } from "../api/types";
import { safeHttpUrl } from "../api/urls";
import { t, uiT, type Locale } from "../i18n/messages";
import { isAnimationKey } from "./visuals/animationKeys";
import { pickAnimation } from "./visuals/pickAnimation";

type Props = {
  visual: VisualPlaceholder;
  locale: Locale;
  /** Compact mode for quiz feedback hooks. */
  compact?: boolean;
  /** Quiz outcome tint for feedback-linked visuals. */
  outcome?: "ok" | "bad" | null;
};

export function ModuleVisual({
  visual,
  locale,
  compact = false,
  outcome = null,
}: Props) {
  const href = safeHttpUrl(visual.official_source_url);
  const toneClass =
    outcome === "ok" ? "is-ok" : outcome === "bad" ? "is-bad" : "";

  return (
    <figure
      className={`module-visual ${compact ? "is-compact" : ""} ${visual.kind} ${toneClass}`.trim()}
      data-visual-id={visual.id}
      data-outcome={outcome ?? undefined}
    >
      <figcaption>
        <strong>{t(visual.title, locale)}</strong>
        <p className="muted">{t(visual.caption, locale)}</p>
      </figcaption>

      {visual.kind === "svg_animation" && pickAnimation(visual.animation_key, locale)}

      {visual.kind === "official_link_slot" && (
        <div className="official-slot">
          <p className="placeholder-flag">{uiT("knhbPlaceholder", locale)}</p>
          {href && (
            <a href={href} target="_blank" rel="noopener noreferrer">
              {visual.official_source_name ?? href}
            </a>
          )}
        </div>
      )}
    </figure>
  );
}

/** Resolve a quiz visualization_hint to a known animation key or null. */
export function animationKeyFromHint(hint: string | null | undefined): string | null {
  if (!hint) return null;
  const normalized = hint.trim().toLowerCase();
  return isAnimationKey(normalized) ? normalized : null;
}

type HintProps = {
  hint: string;
  locale: Locale;
  /** Whether the graded answer was correct — tints the compact viz. */
  correct?: boolean;
};

const QUIZ_VIZ_TITLES: Record<string, { nl: string; en: string }> = {
  "safety-triangle": {
    nl: "Visualisatie: prioriteitsdriehoek",
    en: "Visualization: priority triangle",
  },
  "scan-cycle": {
    nl: "Visualisatie: scan-cyclus",
    en: "Visualization: scan cycle",
  },
  "pitch-zones": {
    nl: "Visualisatie: veldzones",
    en: "Visualization: pitch zones",
  },
  "danger-cone": {
    nl: "Visualisatie: gevaarskegel",
    en: "Visualization: danger cone",
  },
  "restart-bubble": {
    nl: "Visualisatie: herstartbubbel",
    en: "Visualization: restart bubble",
  },
  "court-boards": {
    nl: "Visualisatie: zaalbanden",
    en: "Visualization: indoor boards",
  },
  "lift-limit": {
    nl: "Visualisatie: liftkader",
    en: "Visualization: lift frame",
  },
  "board-play": {
    nl: "Visualisatie: bandenspel",
    en: "Visualization: board play",
  },
  "match-cadence": {
    nl: "Visualisatie: wedstrijdritme",
    en: "Visualization: match cadence",
  },
  "partner-handoff": {
    nl: "Visualisatie: partneroverdracht",
    en: "Visualization: partner handoff",
  },
  "consistency-loop": {
    nl: "Visualisatie: consistentielus",
    en: "Visualization: consistency loop",
  },
  "source-stack": {
    nl: "Visualisatie: bronnenstapel",
    en: "Visualization: source stack",
  },
  "translation-slot": {
    nl: "Visualisatie: vertalingsslot",
    en: "Visualization: translation slot",
  },
  "attribution-chain": {
    nl: "Visualisatie: attributieketen",
    en: "Visualization: attribution chain",
  },
  "capstone-weave": {
    nl: "Visualisatie: capstone-weefsel",
    en: "Visualization: capstone weave",
  },
  "field-attack": {
    nl: "Visualisatie: veldscenario-aanval",
    en: "Visualization: field attack scenario",
  },
  "indoor-rebound": {
    nl: "Visualisatie: zaalscenario-rebound",
    en: "Visualization: indoor rebound scenario",
  },
  "match-pressure": {
    nl: "Visualisatie: wedstrijddruk",
    en: "Visualization: match pressure",
  },
};

export function QuizVizHook({ hint, locale, correct }: HintProps) {
  const key = animationKeyFromHint(hint);
  if (key) {
    const title = QUIZ_VIZ_TITLES[key] ?? {
      nl: "Visualisatie",
      en: "Visualization",
    };
    const stubVisual: VisualPlaceholder = {
      id: `hint-${key}`,
      kind: "svg_animation",
      title,
      caption: {
        nl: "Cursusanimatie gekoppeld aan deze feedback.",
        en: "Course animation linked to this feedback.",
      },
      animation_key: key,
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    const outcome = correct === undefined ? null : correct ? "ok" : "bad";
    return (
      <div
        className="quiz-viz-hook"
        data-quiz-viz={key}
        aria-label={t(title, locale)}
      >
        <ModuleVisual
          visual={stubVisual}
          locale={locale}
          compact
          outcome={outcome}
        />
      </div>
    );
  }
  return <span className="viz-hint muted">{uiT("vizUnavailable", locale)}</span>;
}
