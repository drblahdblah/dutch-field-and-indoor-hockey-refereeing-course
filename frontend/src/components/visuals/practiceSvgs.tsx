import type { Locale } from "../../i18n/messages";
import { label } from "./svgLabels";
import {
  BallMarker,
  PlayerMarker,
  StepBadge,
  UmpireMarker,
} from "./vizPrimitives";

/** Field practice: attack entering the circle with raised path. */
export function PracticeCircleEntrySvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-practice-circle-entry" viewBox="0 0 300 200" aria-hidden="true">
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
      <polygon className="viz-cone-fill" points="90,140 250,84 250,136" />
      <polygon
        className="viz-cone"
        points="90,140 250,84 250,136"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
      />
      <path
        className="viz-scenario-path"
        d="M 78 140 Q 160 100 244 100"
        fill="none"
        strokeWidth="2.5"
      />
      <path
        className="viz-lift-arc"
        d="M 120 128 Q 170 72 220 96"
        fill="none"
        strokeWidth="2"
      />
      <BallMarker x={78} y={140} className="viz-ball-travel viz-ball-practice-a" />
      <PlayerMarker x={78} y={124} className="viz-actor viz-player viz-attacker" />
      <PlayerMarker x={228} y={96} className="viz-actor viz-player viz-defender" />
      <UmpireMarker x={118} y={156} />
      <StepBadge x={78} y={140} n={1} />
      <StepBadge x={170} y={96} n={2} />
      <StepBadge x={244} y={100} n={3} />
      <text x="78" y="172" textAnchor="middle" className="viz-label viz-label-fade">
        {label("attack", locale)}
      </text>
      <text x="248" y="58" textAnchor="middle" className="viz-label viz-label-fade">
        {label("circle", locale)}
      </text>
      <text x="168" y="68" textAnchor="middle" className="viz-label viz-label-fade">
        {label("raised", locale)}
      </text>
      <text x="150" y="28" textAnchor="middle" className="viz-label viz-label-fade">
        {label("field", locale)}
      </text>
      <text x="150" y="188" textAnchor="middle" className="viz-label viz-caption">
        {label("direction", locale)} · {label("distance", locale)} · {label("speed", locale)}
      </text>
    </svg>
  );
}

/** Field practice: free hit near 23m with restart bubble. */
export function PracticeFreehit23Svg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-practice-freehit-23" viewBox="0 0 300 200" aria-hidden="true">
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
      <rect className="viz-pitch-band" x="200" y="36" width="72" height="136" />
      <circle
        className="viz-bubble-glow"
        cx="168"
        cy="108"
        r="36"
        fill="none"
        strokeWidth="2"
      />
      <circle className="viz-core viz-scenario-focus" cx="168" cy="108" r="8" />
      <BallMarker x={168} y={108} className="viz-ball-travel viz-ball-practice-b" r={4} />
      <PlayerMarker x={168} y={90} className="viz-actor viz-player viz-attacker" />
      <PlayerMarker x={210} y={100} className="viz-actor viz-player viz-defender" />
      <PlayerMarker x={214} y={128} className="viz-actor viz-player viz-defender" />
      <UmpireMarker x={120} y={148} />
      <StepBadge x={168} y={108} n={1} />
      <StepBadge x={210} y={100} n={2} />
      <text x="168" y="160" textAnchor="middle" className="viz-label viz-label-fade">
        {label("restart", locale)}
      </text>
      <text x="236" y="58" textAnchor="middle" className="viz-label viz-label-fade">
        {label("band23", locale)}
      </text>
      <text x="120" y="88" textAnchor="middle" className="viz-label viz-label-fade">
        {label("bubble", locale)}
      </text>
      <text x="150" y="28" textAnchor="middle" className="viz-label viz-label-fade">
        {label("field", locale)}
      </text>
      <text x="150" y="188" textAnchor="middle" className="viz-label viz-caption">
        {label("bubble", locale)} → {label("flow", locale)}
      </text>
    </svg>
  );
}

/** Field practice: advantage wave / play-on. */
export function PracticeAdvantageWaveSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-practice-advantage-wave" viewBox="0 0 300 200" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="284" height="184" rx="10" />
      <rect className="viz-surface viz-turf" x="28" y="40" width="244" height="128" rx="4" />
      <rect
        className="viz-pitch-outline"
        x="28"
        y="40"
        width="244"
        height="128"
        rx="4"
        fill="none"
        strokeWidth="2.5"
      />
      <path
        className="viz-scenario-path"
        d="M 60 120 Q 120 100 180 90 T 250 70"
        fill="none"
        strokeWidth="2.5"
      />
      <path
        className="viz-stack-flow"
        d="M 110 132 Q 150 118 190 108"
        fill="none"
        strokeWidth="2"
      />
      <circle className="viz-node viz-node-a" cx="90" cy="118" r="7" />
      <circle className="viz-node viz-node-b" cx="160" cy="96" r="7" />
      <circle className="viz-core viz-scenario-focus" cx="240" cy="74" r="9" />
      <BallMarker x={90} y={118} className="viz-ball-travel viz-ball-practice-c" />
      <PlayerMarker x={90} y={102} className="viz-actor viz-player viz-attacker" />
      <PlayerMarker x={130} y={124} className="viz-actor viz-player viz-defender" />
      <UmpireMarker x={150} y={150} />
      <StepBadge x={90} y={118} n={1} />
      <StepBadge x={160} y={96} n={2} />
      <StepBadge x={240} y={74} n={3} />
      <text x="90" y="148" textAnchor="middle" className="viz-label viz-label-fade">
        {label("contest", locale)}
      </text>
      <text x="190" y="128" textAnchor="middle" className="viz-label viz-label-fade">
        {label("advantage", locale)}
      </text>
      <text x="240" y="58" textAnchor="middle" className="viz-label viz-label-fade">
        {label("flow", locale)}
      </text>
      <text x="150" y="28" textAnchor="middle" className="viz-label viz-label-fade">
        {label("field", locale)}
      </text>
      <text x="150" y="188" textAnchor="middle" className="viz-label viz-caption">
        {label("communicate", locale)} · {label("advantage", locale)}
      </text>
    </svg>
  );
}

/** Indoor practice: board rebound into a raised continuation. */
export function PracticeBoardLiftSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-practice-board-lift" viewBox="0 0 300 200" aria-hidden="true">
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
      <line className="viz-lift-limit-line" x1="48" y1="78" x2="250" y2="78" strokeWidth="1.5" />
      <path
        className="viz-scenario-path"
        d="M 236 144 L 52 108 L 190 58"
        fill="none"
        strokeWidth="2.5"
      />
      <path
        className="viz-lift-arc"
        d="M 110 108 Q 150 60 190 58"
        fill="none"
        strokeWidth="2"
      />
      <circle className="viz-core viz-board-impact" cx="52" cy="108" r="9" />
      <circle className="viz-node viz-node-b viz-lift-raised" cx="190" cy="58" r="7" />
      <BallMarker x={236} y={144} className="viz-ball-travel viz-ball-practice-d" />
      <PlayerMarker x={236} y={128} className="viz-actor viz-player viz-attacker" />
      <PlayerMarker x={178} y={72} className="viz-actor viz-player viz-defender" />
      <UmpireMarker x={120} y={148} />
      <StepBadge x={236} y={144} n={1} />
      <StepBadge x={52} y={108} n={2} />
      <StepBadge x={190} y={58} n={3} />
      <text x="42" y="34" textAnchor="start" className="viz-label viz-label-fade">
        {label("boards", locale)}
      </text>
      <text x="198" y="50" textAnchor="start" className="viz-label viz-label-fade">
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

/** Indoor practice: tight restart with space bubble. */
export function PracticeIndoorRestartSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-practice-indoor-restart" viewBox="0 0 300 200" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="284" height="184" rx="10" />
      <rect
        className="viz-court-board viz-court-board-left"
        x="24"
        y="40"
        width="14"
        height="128"
        rx="2"
      />
      <rect
        className="viz-court-board viz-court-board-right"
        x="262"
        y="40"
        width="14"
        height="128"
        rx="2"
      />
      <rect className="viz-surface viz-floor" x="38" y="40" width="224" height="128" rx="3" />
      <rect
        className="viz-court-outline"
        x="38"
        y="40"
        width="224"
        height="128"
        rx="3"
        fill="none"
        strokeWidth="2.5"
      />
      <circle
        className="viz-bubble-glow"
        cx="150"
        cy="104"
        r="32"
        fill="none"
        strokeWidth="2"
      />
      <circle className="viz-core viz-scenario-focus" cx="150" cy="104" r="8" />
      <BallMarker x={150} y={104} className="viz-ball-travel viz-ball-practice-e" r={4} />
      <PlayerMarker x={150} y={86} className="viz-actor viz-player viz-attacker" />
      <PlayerMarker x={188} y={100} className="viz-actor viz-player viz-defender" />
      <PlayerMarker x={112} y={118} className="viz-actor viz-player viz-defender" />
      <UmpireMarker x={96} y={148} />
      <StepBadge x={150} y={104} n={1} />
      <StepBadge x={188} y={100} n={2} />
      <text x="150" y="154" textAnchor="middle" className="viz-label viz-label-fade">
        {label("restart", locale)}
      </text>
      <text x="110" y="74" textAnchor="middle" className="viz-label viz-label-fade">
        {label("bubble", locale)}
      </text>
      <text x="150" y="28" textAnchor="middle" className="viz-label viz-label-fade">
        {label("indoor", locale)}
      </text>
      <text x="150" y="188" textAnchor="middle" className="viz-label viz-caption">
        {label("space", locale)} → {label("flow", locale)}
      </text>
    </svg>
  );
}

/** Indoor practice: side-board contest. */
export function PracticeSideBoardSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-practice-side-board" viewBox="0 0 300 200" aria-hidden="true">
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
      <path
        className="viz-scenario-path"
        d="M 70 140 L 52 110 L 86 78"
        fill="none"
        strokeWidth="2.5"
      />
      <circle className="viz-core viz-board-impact" cx="52" cy="110" r="9" />
      <BallMarker x={58} y={112} className="viz-ball-travel viz-ball-practice-f" r={4} />
      <PlayerMarker x={78} y={118} className="viz-actor viz-player viz-attacker" />
      <PlayerMarker x={74} y={88} className="viz-actor viz-player viz-defender" />
      <UmpireMarker x={140} y={140} />
      <StepBadge x={52} y={110} n={1} />
      <StepBadge x={78} y={118} n={2} />
      <StepBadge x={74} y={88} n={3} />
      <text x="42" y="34" textAnchor="start" className="viz-label viz-label-fade">
        {label("boards", locale)}
      </text>
      <text x="110" y="108" textAnchor="start" className="viz-label viz-label-fade">
        {label("contest", locale)}
      </text>
      <text x="150" y="28" textAnchor="middle" className="viz-label viz-label-fade">
        {label("indoor", locale)}
      </text>
      <text x="150" y="188" textAnchor="middle" className="viz-label viz-caption">
        {label("safety", locale)} · {label("fairness", locale)}
      </text>
    </svg>
  );
}
