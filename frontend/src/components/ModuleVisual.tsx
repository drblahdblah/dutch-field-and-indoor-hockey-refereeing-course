import type { VisualPlaceholder } from "../api/types";
import { safeHttpUrl } from "../api/urls";
import { t, uiT, type Locale } from "../i18n/messages";

type Props = {
  visual: VisualPlaceholder;
  locale: Locale;
  /** Compact mode for quiz feedback hooks. */
  compact?: boolean;
};

const SVG_LABELS = {
  safety: { nl: "veiligheid", en: "safety" },
  fairness: { nl: "eerlijkheid", en: "fairness" },
  flow: { nl: "flow", en: "flow" },
  ball: { nl: "bal", en: "ball" },
  contest: { nl: "contest", en: "contest" },
  periphery: { nl: "periferie", en: "periphery" },
  partner: { nl: "partner", en: "partner" },
  half: { nl: "helft", en: "half" },
  band23: { nl: "23m", en: "23m" },
  circle: { nl: "cirkel", en: "circle" },
  direction: { nl: "richting", en: "direction" },
  distance: { nl: "afstand", en: "distance" },
  speed: { nl: "snelheid", en: "speed" },
  bubble: { nl: "bubbel", en: "bubble" },
  restart: { nl: "herstart", en: "restart" },
  boards: { nl: "banden", en: "boards" },
  flat: { nl: "plat", en: "flat" },
  raised: { nl: "omhoog", en: "raised" },
  rebound: { nl: "rebound", en: "rebound" },
  recovery: { nl: "herstel", en: "recovery" },
} as const;

function SafetyTriangleSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg" viewBox="0 0 240 180" aria-hidden="true">
      <polygon
        className="viz-tri"
        points="120,18 220,160 20,160"
        fill="none"
        stroke="currentColor"
        strokeWidth="2.5"
      />
      <circle className="viz-node viz-node-a" cx="120" cy="28" r="8" />
      <circle className="viz-node viz-node-b" cx="210" cy="152" r="8" />
      <circle className="viz-node viz-node-c" cx="30" cy="152" r="8" />
      <text x="120" y="58" textAnchor="middle" className="viz-label">
        {t(SVG_LABELS.safety, locale)}
      </text>
      <text x="188" y="148" textAnchor="middle" className="viz-label">
        {t(SVG_LABELS.flow, locale)}
      </text>
      <text x="52" y="148" textAnchor="middle" className="viz-label">
        {t(SVG_LABELS.fairness, locale)}
      </text>
    </svg>
  );
}

function ScanCycleSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg" viewBox="0 0 260 160" aria-hidden="true">
      <circle className="viz-orbit" cx="130" cy="80" r="58" fill="none" strokeWidth="2" />
      <g className="viz-orbit-dot">
        <circle cx="130" cy="22" r="7" />
      </g>
      <text x="130" y="14" textAnchor="middle" className="viz-label">
        {t(SVG_LABELS.ball, locale)}
      </text>
      <text x="210" y="84" textAnchor="start" className="viz-label">
        {t(SVG_LABELS.contest, locale)}
      </text>
      <text x="130" y="154" textAnchor="middle" className="viz-label">
        {t(SVG_LABELS.periphery, locale)}
      </text>
      <text x="18" y="84" textAnchor="start" className="viz-label">
        {t(SVG_LABELS.partner, locale)}
      </text>
      <circle cx="130" cy="80" r="10" className="viz-core" />
    </svg>
  );
}

function PitchZonesSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-pitch" viewBox="0 0 260 160" aria-hidden="true">
      <rect
        className="viz-pitch-outline"
        x="20"
        y="16"
        width="220"
        height="128"
        rx="4"
        fill="none"
        strokeWidth="2.5"
      />
      <line className="viz-pitch-line" x1="130" y1="16" x2="130" y2="144" strokeWidth="2" />
      <rect className="viz-pitch-band" x="20" y="16" width="48" height="128" />
      <rect className="viz-pitch-band" x="192" y="16" width="48" height="128" />
      <path
        className="viz-pitch-circle viz-pitch-circle-a"
        d="M 68 48 A 36 36 0 0 1 68 112"
        fill="none"
        strokeWidth="2"
      />
      <path
        className="viz-pitch-circle viz-pitch-circle-b"
        d="M 192 48 A 36 36 0 0 0 192 112"
        fill="none"
        strokeWidth="2"
      />
      <text x="130" y="12" textAnchor="middle" className="viz-label">
        {t(SVG_LABELS.half, locale)}
      </text>
      <text x="44" y="36" textAnchor="middle" className="viz-label">
        {t(SVG_LABELS.band23, locale)}
      </text>
      <text x="216" y="36" textAnchor="middle" className="viz-label">
        {t(SVG_LABELS.band23, locale)}
      </text>
      <text x="52" y="86" textAnchor="middle" className="viz-label">
        {t(SVG_LABELS.circle, locale)}
      </text>
      <text x="208" y="86" textAnchor="middle" className="viz-label">
        {t(SVG_LABELS.circle, locale)}
      </text>
    </svg>
  );
}

function DangerConeSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg" viewBox="0 0 260 170" aria-hidden="true">
      <polygon
        className="viz-cone"
        points="48,140 200,48 200,140"
        fill="none"
        stroke="currentColor"
        strokeWidth="2.5"
      />
      <circle className="viz-node viz-node-a" cx="48" cy="140" r="7" />
      <circle className="viz-node viz-node-b" cx="200" cy="48" r="7" />
      <circle className="viz-node viz-node-c" cx="200" cy="140" r="7" />
      <text x="36" y="160" textAnchor="start" className="viz-label">
        {t(SVG_LABELS.ball, locale)}
      </text>
      <text x="196" y="36" textAnchor="end" className="viz-label">
        {t(SVG_LABELS.direction, locale)}
      </text>
      <text x="196" y="158" textAnchor="end" className="viz-label">
        {t(SVG_LABELS.distance, locale)}
      </text>
      <text x="128" y="108" textAnchor="middle" className="viz-label">
        {t(SVG_LABELS.speed, locale)}
      </text>
    </svg>
  );
}

function RestartBubbleSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg" viewBox="0 0 240 160" aria-hidden="true">
      <circle
        className="viz-bubble"
        cx="120"
        cy="80"
        r="52"
        fill="none"
        strokeWidth="2.5"
      />
      <circle className="viz-core viz-bubble-core" cx="120" cy="80" r="10" />
      <circle className="viz-node viz-node-a" cx="120" cy="28" r="6" />
      <circle className="viz-node viz-node-b" cx="172" cy="110" r="6" />
      <circle className="viz-node viz-node-c" cx="68" cy="110" r="6" />
      <text x="120" y="16" textAnchor="middle" className="viz-label">
        {t(SVG_LABELS.bubble, locale)}
      </text>
      <text x="120" y="152" textAnchor="middle" className="viz-label">
        {t(SVG_LABELS.restart, locale)}
      </text>
    </svg>
  );
}

function CourtBoardsSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-court" viewBox="0 0 260 160" aria-hidden="true">
      <rect
        className="viz-court-board viz-court-board-left"
        x="12"
        y="16"
        width="10"
        height="128"
        rx="2"
      />
      <rect
        className="viz-court-board viz-court-board-right"
        x="238"
        y="16"
        width="10"
        height="128"
        rx="2"
      />
      <rect
        className="viz-court-outline"
        x="22"
        y="16"
        width="216"
        height="128"
        rx="3"
        fill="none"
        strokeWidth="2.5"
      />
      <line className="viz-court-line" x1="130" y1="16" x2="130" y2="144" strokeWidth="2" />
      <path
        className="viz-court-circle viz-court-circle-a"
        d="M 54 48 A 32 32 0 0 1 54 112"
        fill="none"
        strokeWidth="2"
      />
      <path
        className="viz-court-circle viz-court-circle-b"
        d="M 206 48 A 32 32 0 0 0 206 112"
        fill="none"
        strokeWidth="2"
      />
      <text x="130" y="14" textAnchor="middle" className="viz-label">
        {t(SVG_LABELS.half, locale)}
      </text>
      <text x="42" y="38" textAnchor="middle" className="viz-label">
        {t(SVG_LABELS.boards, locale)}
      </text>
      <text x="218" y="38" textAnchor="middle" className="viz-label">
        {t(SVG_LABELS.boards, locale)}
      </text>
      <text x="48" y="86" textAnchor="middle" className="viz-label">
        {t(SVG_LABELS.circle, locale)}
      </text>
      <text x="212" y="86" textAnchor="middle" className="viz-label">
        {t(SVG_LABELS.circle, locale)}
      </text>
    </svg>
  );
}

function LiftLimitSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg" viewBox="0 0 260 170" aria-hidden="true">
      <line className="viz-lift-ground" x1="40" y1="130" x2="220" y2="130" strokeWidth="2.5" />
      <circle className="viz-node viz-node-a viz-lift-flat" cx="90" cy="130" r="8" />
      <path
        className="viz-lift-arc"
        d="M 150 130 Q 185 70 220 50"
        fill="none"
        strokeWidth="2.5"
      />
      <circle className="viz-node viz-node-b viz-lift-raised" cx="220" cy="50" r="8" />
      <text x="90" y="152" textAnchor="middle" className="viz-label">
        {t(SVG_LABELS.flat, locale)}
      </text>
      <text x="220" y="36" textAnchor="end" className="viz-label">
        {t(SVG_LABELS.raised, locale)}
      </text>
      <text x="130" y="100" textAnchor="middle" className="viz-label">
        {t(SVG_LABELS.ball, locale)}
      </text>
    </svg>
  );
}

function BoardPlaySvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg" viewBox="0 0 260 160" aria-hidden="true">
      <rect className="viz-court-board" x="28" y="24" width="10" height="112" rx="2" />
      <path
        className="viz-board-path"
        d="M 200 120 L 48 80 L 160 40"
        fill="none"
        strokeWidth="2.5"
      />
      <circle className="viz-node viz-node-a" cx="200" cy="120" r="7" />
      <circle className="viz-core viz-board-impact" cx="48" cy="80" r="9" />
      <circle className="viz-node viz-node-b" cx="160" cy="40" r="7" />
      <text x="200" y="142" textAnchor="middle" className="viz-label">
        {t(SVG_LABELS.ball, locale)}
      </text>
      <text x="18" y="84" textAnchor="start" className="viz-label">
        {t(SVG_LABELS.boards, locale)}
      </text>
      <text x="168" y="28" textAnchor="start" className="viz-label">
        {t(SVG_LABELS.rebound, locale)}
      </text>
      <text x="130" y="108" textAnchor="middle" className="viz-label">
        {t(SVG_LABELS.recovery, locale)}
      </text>
    </svg>
  );
}

function pickAnimation(key: string | null | undefined, locale: Locale) {
  if (key === "safety-triangle") return <SafetyTriangleSvg locale={locale} />;
  if (key === "scan-cycle") return <ScanCycleSvg locale={locale} />;
  if (key === "pitch-zones") return <PitchZonesSvg locale={locale} />;
  if (key === "danger-cone") return <DangerConeSvg locale={locale} />;
  if (key === "restart-bubble") return <RestartBubbleSvg locale={locale} />;
  if (key === "court-boards") return <CourtBoardsSvg locale={locale} />;
  if (key === "lift-limit") return <LiftLimitSvg locale={locale} />;
  if (key === "board-play") return <BoardPlaySvg locale={locale} />;
  return (
    <div className="viz-fallback" aria-hidden="true">
      <span className="viz-pulse" />
    </div>
  );
}

export function ModuleVisual({ visual, locale, compact = false }: Props) {
  const href = safeHttpUrl(visual.official_source_url);

  return (
    <figure
      className={`module-visual ${compact ? "is-compact" : ""} ${visual.kind}`}
      data-visual-id={visual.id}
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

const KNOWN_ANIMATION_KEYS = new Set([
  "safety-triangle",
  "scan-cycle",
  "pitch-zones",
  "danger-cone",
  "restart-bubble",
  "court-boards",
  "lift-limit",
  "board-play",
]);

/** Resolve a quiz visualization_hint to a known animation key or null. */
export function animationKeyFromHint(hint: string | null | undefined): string | null {
  if (!hint) return null;
  const normalized = hint.trim().toLowerCase();
  return KNOWN_ANIMATION_KEYS.has(normalized) ? normalized : null;
}

type HintProps = {
  hint: string;
  locale: Locale;
};

export function QuizVizHook({ hint, locale }: HintProps) {
  const key = animationKeyFromHint(hint);
  if (key) {
    const stubVisual: VisualPlaceholder = {
      id: `hint-${key}`,
      kind: "svg_animation",
      title: {
        nl: "Visualisatie",
        en: "Visualization",
      },
      caption: {
        nl: "Cursusanimatie gekoppeld aan deze feedback.",
        en: "Course animation linked to this feedback.",
      },
      animation_key: key,
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    return <ModuleVisual visual={stubVisual} locale={locale} compact />;
  }
  return <span className="viz-hint muted">{uiT("vizUnavailable", locale)}</span>;
}
