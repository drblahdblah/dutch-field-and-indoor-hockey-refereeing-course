import type { Locale } from "../../i18n/messages";
import { label } from "./svgLabels";
import {
  PlayerMarker,
  StepBadge,
  UmpireMarker,
} from "./vizPrimitives";

/** Field scenario: attack into circle with danger cone overlay. */
export function FieldAttackSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-field-attack" viewBox="0 0 300 200" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="284" height="184" rx="10" />
      <rect className="viz-surface viz-turf" x="28" y="36" width="244" height="136" rx="4" />
      <rect
        className="viz-pitch-outline"
        x="28"
        y="36"
        width="244"
        height="136"
        rx="4"
        fill="none"
        strokeWidth="2.5"
      />
      <line className="viz-pitch-line" x1="150" y1="36" x2="150" y2="172" strokeWidth="2" />
      <rect className="viz-pitch-band" x="226" y="36" width="46" height="136" />
      <path
        className="viz-pitch-circle"
        d="M 226 68 A 40 40 0 0 0 226 140"
        fill="none"
        strokeWidth="2"
      />
      <polygon className="viz-cone-fill" points="78,132 248,78 248,142" />
      <polygon
        className="viz-cone"
        points="78,132 248,78 248,142"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
      />
      <path
        className="viz-scenario-path"
        d="M 70 132 Q 150 112 240 108"
        fill="none"
        strokeWidth="2.5"
      />
      <circle className="viz-node viz-node-a" cx="70" cy="132" r="7" />
      <circle className="viz-core viz-scenario-focus" cx="240" cy="108" r="9" />
      <circle className="viz-ball-travel viz-ball-attack" cx="70" cy="132" r="5" />
      <PlayerMarker x={70} y={116} className="viz-actor viz-player viz-attacker" />
      <PlayerMarker x={210} y={100} className="viz-actor viz-player viz-defender" />
      <UmpireMarker x={120} y={150} />
      <StepBadge x={70} y={132} n={1} />
      <StepBadge x={160} y={108} n={2} />
      <StepBadge x={240} y={108} n={3} />
      <text x="70" y="168" textAnchor="middle" className="viz-label viz-label-fade">
        {label("attack", locale)}
      </text>
      <text x="248" y="58" textAnchor="middle" className="viz-label viz-label-fade">
        {label("circle", locale)}
      </text>
      <text x="160" y="96" textAnchor="middle" className="viz-label viz-label-fade">
        {label("danger", locale)}
      </text>
      <text x="150" y="28" textAnchor="middle" className="viz-label viz-label-fade">
        {label("field", locale)}
      </text>
      <text x="120" y="188" textAnchor="middle" className="viz-label viz-caption">
        {label("umpire", locale)} → {label("scan", locale)}
      </text>
    </svg>
  );
}

/** Indoor scenario: board rebound with raised ball risk. */
export function IndoorReboundSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-indoor-rebound" viewBox="0 0 300 200" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="284" height="184" rx="10" />
      <rect
        className="viz-court-board viz-court-board-left"
        x="24"
        y="40"
        width="14"
        height="128"
        rx="2"
      />
      <rect className="viz-surface viz-floor" x="38" y="40" width="230" height="128" rx="3" />
      <rect
        className="viz-court-outline"
        x="38"
        y="40"
        width="230"
        height="128"
        rx="3"
        fill="none"
        strokeWidth="2.5"
      />
      <line className="viz-court-line" x1="153" y1="40" x2="153" y2="168" strokeWidth="2" />
      <path
        className="viz-scenario-path"
        d="M 230 140 L 52 100 L 180 56"
        fill="none"
        strokeWidth="2.5"
      />
      <path
        className="viz-lift-arc"
        d="M 130 100 Q 160 64 180 56"
        fill="none"
        strokeWidth="2"
      />
      <line className="viz-lift-limit-line" x1="48" y1="72" x2="250" y2="72" strokeWidth="1.5" />
      <circle className="viz-node viz-node-a" cx="230" cy="140" r="7" />
      <circle className="viz-core viz-board-impact" cx="52" cy="100" r="9" />
      <circle className="viz-node viz-node-b viz-lift-raised" cx="180" cy="56" r="7" />
      <circle className="viz-ball-travel viz-ball-indoor" cx="230" cy="140" r="5" />
      <PlayerMarker x={230} y={124} className="viz-actor viz-player viz-attacker" />
      <UmpireMarker x={120} y={140} />
      <StepBadge x={230} y={140} n={1} />
      <StepBadge x={52} y={100} n={2} />
      <StepBadge x={180} y={56} n={3} />
      <text x="230" y="164" textAnchor="middle" className="viz-label viz-label-fade">
        {label("ball", locale)}
      </text>
      <text x="42" y="34" textAnchor="start" className="viz-label viz-label-fade">
        {label("boards", locale)}
      </text>
      <text x="188" y="48" textAnchor="start" className="viz-label viz-label-fade">
        {label("raised", locale)}
      </text>
      <text x="130" y="128" textAnchor="middle" className="viz-label viz-label-fade">
        {label("rebound", locale)}
      </text>
      <text x="150" y="28" textAnchor="middle" className="viz-label viz-label-fade">
        {label("indoor", locale)}
      </text>
      <text x="150" y="188" textAnchor="middle" className="viz-label viz-caption">
        {label("height", locale)} · {label("danger", locale)}
      </text>
    </svg>
  );
}

/** Pathway scenario: match cadence with rising pressure. */
export function MatchPressureSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-match-pressure" viewBox="0 0 300 200" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="284" height="184" rx="10" />
      <line className="viz-cadence-rail" x1="48" y1="128" x2="252" y2="128" strokeWidth="2.5" />
      <rect className="viz-pressure-bar viz-pressure-a" x="60" y="96" width="20" height="32" rx="3" />
      <rect className="viz-pressure-bar viz-pressure-b" x="140" y="70" width="20" height="58" rx="3" />
      <rect className="viz-pressure-bar viz-pressure-c" x="220" y="44" width="20" height="84" rx="3" />
      <circle className="viz-node viz-node-a viz-cadence-node" cx="70" cy="128" r="9" />
      <circle className="viz-node viz-node-b viz-cadence-node" cx="150" cy="128" r="9" />
      <circle className="viz-node viz-node-c viz-cadence-node" cx="230" cy="128" r="9" />
      <path
        className="viz-scenario-path"
        d="M 70 128 L 150 128 L 230 128"
        fill="none"
        strokeWidth="1.5"
      />
      <circle className="viz-ball-travel viz-ball-pressure" cx="70" cy="128" r="4" />
      <UmpireMarker x={150} y={156} />
      <StepBadge x={70} y={128} n={1} />
      <StepBadge x={150} y={128} n={2} />
      <StepBadge x={230} y={128} n={3} />
      <text x="70" y="156" textAnchor="middle" className="viz-label viz-label-fade">
        {label("before", locale)}
      </text>
      <text x="150" y="156" textAnchor="middle" className="viz-label viz-label-fade">
        {label("during", locale)}
      </text>
      <text x="230" y="156" textAnchor="middle" className="viz-label viz-label-fade">
        {label("after", locale)}
      </text>
      <text x="150" y="32" textAnchor="middle" className="viz-label viz-label-fade">
        {label("pressure", locale)}
      </text>
      <text x="150" y="188" textAnchor="middle" className="viz-label viz-label-fade">
        {label("pathway", locale)}
      </text>
    </svg>
  );
}
