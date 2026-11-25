import type { VisualPlaceholder } from "../api/types";
import { safeHttpUrl } from "../api/urls";
import {
  quizVizTitle,
  t,
  ui,
  uiT,
  type Locale,
} from "../i18n/messages";
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
      <strong className="module-visual-title">{t(visual.title, locale)}</strong>

      {visual.kind === "svg_animation" && pickAnimation(visual.animation_key, locale)}

      {visual.kind === "official_link_slot" && (
        <div className="official-slot">
          <p className="placeholder-flag">{uiT("knhbPlaceholder", locale)}</p>
          {href && (
            <a href={href} target="_blank" rel="noopener noreferrer">
              {visual.official_source_name ?? href}
              <span className="sr-only"> {uiT("opensInNewTab", locale)}</span>
            </a>
          )}
        </div>
      )}

      <figcaption className="module-visual-situation">
        <p>{t(visual.caption, locale)}</p>
      </figcaption>
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

export function QuizVizHook({ hint, locale, correct }: HintProps) {
  const key = animationKeyFromHint(hint);
  if (key) {
    const title = quizVizTitle(key);
    const stubVisual: VisualPlaceholder = {
      id: `hint-${key}`,
      kind: "svg_animation",
      title,
      caption: ui.quizVizCaption,
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
        role="group"
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
