import type { Locale } from "../../i18n/messages";
import { label } from "./svgLabels";
import {
  PlayerMarker,
  StepBadge,
  UmpireMarker,
} from "./vizPrimitives";

/** Original course art — calm, brief, visible communication after a call. */
export function CalmSignalSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-calm-signal" viewBox="0 0 280 190" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="264" height="174" rx="10" />
      <circle className="viz-glow viz-calm-glow" cx="118" cy="98" r="52" />
      <path
        className="viz-calm-wave viz-calm-wave-a"
        d="M 148 70 Q 188 58 220 52"
        fill="none"
        strokeWidth="2.5"
      />
      <path
        className="viz-calm-wave viz-calm-wave-b"
        d="M 148 98 Q 196 98 228 98"
        fill="none"
        strokeWidth="2.5"
      />
      <path
        className="viz-calm-wave viz-calm-wave-c"
        d="M 148 126 Q 188 138 220 146"
        fill="none"
        strokeWidth="2.5"
      />
      <UmpireMarker x={118} y={104} />
      <PlayerMarker x={232} y={98} className="viz-actor viz-player" />
      <StepBadge x={118} y={104} n={1} />
      <StepBadge x={188} y={58} n={2} />
      <StepBadge x={232} y={98} n={3} />
      <text x="118" y="168" textAnchor="middle" className="viz-label viz-label-fade">
        {label("calm", locale)}
      </text>
      <text x="188" y="42" textAnchor="middle" className="viz-label viz-label-fade">
        {label("brief", locale)}
      </text>
      <text x="232" y="168" textAnchor="middle" className="viz-label viz-label-fade">
        {label("visible", locale)}
      </text>
    </svg>
  );
}

/** Original course art — shared decision frame, different cadence outdoors vs indoors. */
export function ContextSplitSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-context-split" viewBox="0 0 280 190" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="264" height="174" rx="10" />
      <rect className="viz-surface viz-turf viz-split-field" x="22" y="36" width="108" height="118" rx="4" />
      <rect className="viz-surface viz-floor viz-split-indoor" x="150" y="36" width="108" height="118" rx="4" />
      <line className="viz-split-divider" x1="140" y1="28" x2="140" y2="162" strokeWidth="2" />
      <path
        className="viz-split-tempo viz-split-tempo-field"
        d="M 36 128 Q 70 88 118 72"
        fill="none"
        strokeWidth="2.2"
      />
      <path
        className="viz-split-tempo viz-split-tempo-indoor"
        d="M 164 128 Q 190 70 244 52"
        fill="none"
        strokeWidth="2.2"
      />
      <circle className="viz-ball-travel viz-ball-split-a" cx="36" cy="128" r="4.5" />
      <circle className="viz-ball-travel viz-ball-split-b" cx="164" cy="128" r="4.5" />
      <UmpireMarker x={76} y={150} />
      <UmpireMarker x={204} y={150} />
      <text x="76" y="28" textAnchor="middle" className="viz-label viz-label-fade">
        {label("field", locale)}
      </text>
      <text x="204" y="28" textAnchor="middle" className="viz-label viz-label-fade">
        {label("indoor", locale)}
      </text>
      <text x="76" y="176" textAnchor="middle" className="viz-label viz-label-fade">
        {label("space", locale)}
      </text>
      <text x="204" y="176" textAnchor="middle" className="viz-label viz-label-fade">
        {label("tempo", locale)}
      </text>
    </svg>
  );
}

/** Original course art — posture, scan, voice as professional presence. */
export function PresenceArcSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-presence-arc" viewBox="0 0 280 190" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="264" height="174" rx="10" />
      <circle className="viz-glow viz-presence-glow" cx="140" cy="108" r="62" />
      <path
        className="viz-presence-ring"
        d="M 70 128 A 72 52 0 0 1 210 128"
        fill="none"
        strokeWidth="2.5"
      />
      <path
        className="viz-presence-sweep"
        d="M 88 118 A 58 40 0 0 1 192 118"
        fill="none"
        strokeWidth="1.5"
      />
      <UmpireMarker x={140} y={118} />
      <StepBadge x={88} y={118} n={1} />
      <StepBadge x={140} y={72} n={2} />
      <StepBadge x={192} y={118} n={3} />
      <circle className="viz-node viz-node-a" cx={88} cy={118} r="6" />
      <circle className="viz-node viz-node-b" cx={140} cy={72} r="6" />
      <circle className="viz-node viz-node-c" cx={192} cy={118} r="6" />
      <text x="88" y="148" textAnchor="middle" className="viz-label viz-label-fade">
        {label("posture", locale)}
      </text>
      <text x="140" y="58" textAnchor="middle" className="viz-label viz-label-fade">
        {label("scan", locale)}
      </text>
      <text x="192" y="148" textAnchor="middle" className="viz-label viz-label-fade">
        {label("voice", locale)}
      </text>
      <text x="140" y="176" textAnchor="middle" className="viz-label viz-label-fade">
        {label("presence", locale)}
      </text>
    </svg>
  );
}
