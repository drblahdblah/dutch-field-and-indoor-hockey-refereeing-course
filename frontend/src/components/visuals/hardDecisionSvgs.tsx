import type { Locale } from "../../i18n/messages";
import { label } from "./svgLabels";
import {
  BallMarker,
  PlayerMarker,
  StepBadge,
  UmpireMarker,
} from "./vizPrimitives";

/** Decision frame: read → weigh → whistle. */
export function HardDecisionFrameSvg({ locale }: { locale: Locale }) {
  return (
    <svg
      className="viz-svg viz-hard-decision-frame"
      viewBox="0 0 300 190"
      aria-hidden="true"
    >
      <rect className="viz-canvas" x="8" y="8" width="284" height="174" rx="10" />
      <circle className="viz-glow" cx="150" cy="95" r="70" />
      <path
        className="viz-hard-frame-arc"
        d="M 70 120 Q 150 40 230 120"
        fill="none"
        strokeWidth="2.5"
        pathLength={1}
      />
      <circle className="viz-node viz-node-a" cx="70" cy="120" r="11" />
      <circle className="viz-node viz-node-b" cx="150" cy="58" r="11" />
      <circle className="viz-node viz-node-c" cx="230" cy="120" r="11" />
      <BallMarker x={150} y={58} className="viz-ball-travel viz-ball-hard-frame" r={4} />
      <StepBadge x={70} y={120} n={1} />
      <StepBadge x={150} y={58} n={2} />
      <StepBadge x={230} y={120} n={3} />
      <UmpireMarker x={150} y={148} />
      <text x="70" y="152" textAnchor="middle" className="viz-label viz-label-fade">
        {label("observe", locale)}
      </text>
      <text x="150" y="36" textAnchor="middle" className="viz-label viz-label-fade">
        {label("decide", locale)}
      </text>
      <text x="230" y="152" textAnchor="middle" className="viz-label viz-label-fade">
        {label("whistle", locale)}
      </text>
      <text x="150" y="178" textAnchor="middle" className="viz-label viz-caption">
        {label("hardRead", locale)}
      </text>
    </svg>
  );
}

/** Raised / dangerous ball — field cone + indoor lift contrast. */
export function HardRaisedDangerSvg({ locale }: { locale: Locale }) {
  return (
    <svg
      className="viz-svg viz-hard-raised-danger"
      viewBox="0 0 300 200"
      aria-hidden="true"
    >
      <rect className="viz-canvas" x="8" y="8" width="284" height="184" rx="10" />
      {/* Field half */}
      <rect className="viz-surface viz-turf" x="20" y="40" width="126" height="120" rx="4" />
      <polygon className="viz-cone-fill" points="40,140 130,70 130,130" />
      <polygon
        className="viz-cone"
        points="40,140 130,70 130,130"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        pathLength={1}
      />
      <path
        className="viz-scenario-path viz-hard-raised-path"
        d="M 40 140 Q 90 90 128 96"
        fill="none"
        strokeWidth="2.5"
        pathLength={1}
      />
      <BallMarker x={40} y={140} className="viz-ball-travel viz-ball-hard-raised" />
      <PlayerMarker x={40} y={124} className="viz-actor viz-player viz-attacker" />
      <PlayerMarker x={118} y={88} className="viz-actor viz-player viz-defender" />
      <text x="83" y="34" textAnchor="middle" className="viz-label viz-label-fade">
        {label("field", locale)}
      </text>
      {/* Indoor half */}
      <rect className="viz-surface viz-floor" x="154" y="40" width="126" height="120" rx="4" />
      <line className="viz-pitch-line" x1="160" y1="52" x2="274" y2="52" strokeWidth="3" />
      <line className="viz-pitch-line" x1="160" y1="148" x2="274" y2="148" strokeWidth="3" />
      <path
        className="viz-lift-arc"
        d="M 176 130 Q 210 70 250 100"
        fill="none"
        strokeWidth="2"
        pathLength={1}
      />
      <line
        className="viz-lift-limit-line"
        x1="168"
        y1="78"
        x2="268"
        y2="78"
        strokeWidth="1.5"
      />
      <BallMarker x={176} y={130} className="viz-ball-travel viz-ball-hard-raised-in" r={4} />
      <PlayerMarker x={176} y={114} className="viz-actor viz-player viz-attacker" />
      <PlayerMarker x={248} y={96} className="viz-actor viz-player viz-defender" />
      <text x="217" y="34" textAnchor="middle" className="viz-label viz-label-fade">
        {label("indoor", locale)}
      </text>
      <UmpireMarker x={150} y={178} />
      <StepBadge x={40} y={140} n={1} />
      <StepBadge x={210} y={70} n={2} />
      <StepBadge x={250} y={100} n={3} />
      <text x="150" y="188" textAnchor="middle" className="viz-label viz-caption">
        {label("direction", locale)} · {label("distance", locale)} · {label("speed", locale)}
      </text>
    </svg>
  );
}

/** Two defenders pressing clear possession. */
export function HardPressureClearSvg({ locale }: { locale: Locale }) {
  return (
    <svg
      className="viz-svg viz-hard-pressure-clear"
      viewBox="0 0 300 200"
      aria-hidden="true"
    >
      <rect className="viz-canvas" x="8" y="8" width="284" height="184" rx="10" />
      <rect className="viz-surface viz-turf" x="28" y="36" width="244" height="136" rx="4" />
      <circle className="viz-glow viz-hard-possess-glow" cx="120" cy="108" r="36" />
      <path
        className="viz-scenario-path"
        d="M 70 120 L 120 108"
        fill="none"
        strokeWidth="2.5"
        pathLength={1}
      />
      <path
        className="viz-hard-press-arc"
        d="M 190 70 Q 160 100 190 140"
        fill="none"
        strokeWidth="2"
        pathLength={1}
      />
      <BallMarker x={120} y={108} className="viz-ball-travel viz-ball-hard-pressure" r={5} />
      <PlayerMarker x={120} y={90} className="viz-actor viz-player viz-attacker" />
      <PlayerMarker x={190} y={70} className="viz-actor viz-player viz-defender" />
      <PlayerMarker x={190} y={140} className="viz-actor viz-player viz-defender" />
      <UmpireMarker x={70} y={150} />
      <StepBadge x={120} y={108} n={1} />
      <StepBadge x={190} y={70} n={2} />
      <StepBadge x={190} y={140} n={3} />
      <text x="120" y="58" textAnchor="middle" className="viz-label viz-label-fade">
        {label("possession", locale)}
      </text>
      <text x="220" y="58" textAnchor="middle" className="viz-label viz-label-fade">
        {label("pressure", locale)}
      </text>
      <text x="150" y="188" textAnchor="middle" className="viz-label viz-caption">
        {label("clearBall", locale)}
      </text>
    </svg>
  );
}

/** Contested / unclear possession. */
export function HardContestedSvg({ locale }: { locale: Locale }) {
  return (
    <svg
      className="viz-svg viz-hard-contested"
      viewBox="0 0 300 200"
      aria-hidden="true"
    >
      <rect className="viz-canvas" x="8" y="8" width="284" height="184" rx="10" />
      <rect className="viz-surface viz-turf" x="28" y="36" width="244" height="136" rx="4" />
      <circle
        className="viz-bubble-glow viz-hard-contest-ring"
        cx="150"
        cy="110"
        r="42"
        fill="none"
        strokeWidth="2"
        pathLength={1}
      />
      <path
        className="viz-hard-contest-stick-a"
        d="M 110 88 L 150 110"
        fill="none"
        strokeWidth="2.5"
        pathLength={1}
      />
      <path
        className="viz-hard-contest-stick-b"
        d="M 190 88 L 150 110"
        fill="none"
        strokeWidth="2.5"
        pathLength={1}
      />
      <BallMarker x={150} y={110} className="viz-ball-travel viz-ball-hard-contested" r={5} />
      <PlayerMarker x={110} y={80} className="viz-actor viz-player viz-attacker" />
      <PlayerMarker x={190} y={80} className="viz-actor viz-player viz-defender" />
      <UmpireMarker x={150} y={158} />
      <StepBadge x={150} y={110} n={1} />
      <StepBadge x={110} y={80} n={2} />
      <StepBadge x={190} y={80} n={3} />
      <text x="150" y="52" textAnchor="middle" className="viz-label viz-label-fade">
        {label("contest", locale)}
      </text>
      <text x="70" y="120" textAnchor="middle" className="viz-label viz-label-fade">
        {label("unclear", locale)}
      </text>
      <text x="230" y="120" textAnchor="middle" className="viz-label viz-label-fade">
        {label("noBias", locale)}
      </text>
      <text x="150" y="188" textAnchor="middle" className="viz-label viz-caption">
        {label("waitControl", locale)}
      </text>
    </svg>
  );
}

/** Goalkeeper slide / dive — field space vs indoor boards. */
export function HardGkDiveSvg({ locale }: { locale: Locale }) {
  return (
    <svg
      className="viz-svg viz-hard-gk-dive"
      viewBox="0 0 300 200"
      aria-hidden="true"
    >
      <rect className="viz-canvas" x="8" y="8" width="284" height="184" rx="10" />
      <rect className="viz-surface viz-turf" x="28" y="36" width="244" height="136" rx="4" />
      <rect className="viz-pitch-band" x="220" y="36" width="52" height="136" />
      <path
        className="viz-pitch-circle"
        d="M 220 68 A 40 40 0 0 0 220 140"
        fill="none"
        strokeWidth="2"
        pathLength={1}
      />
      {/* Keeper dive path */}
      <path
        className="viz-hard-gk-path"
        d="M 248 108 Q 200 130 150 118"
        fill="none"
        strokeWidth="2.5"
        pathLength={1}
      />
      {/* Attacker run-in */}
      <path
        className="viz-scenario-path"
        d="M 70 90 L 150 110"
        fill="none"
        strokeWidth="2"
        pathLength={1}
      />
      {/* Indoor board hint at bottom edge of band */}
      <line
        className="viz-pitch-line viz-hard-board-hint"
        x1="28"
        y1="168"
        x2="272"
        y2="168"
        strokeWidth="3"
      />
      <BallMarker x={150} y={118} className="viz-ball-travel viz-ball-hard-gk" r={4} />
      <PlayerMarker x={248} y={100} className="viz-actor viz-player viz-gk" />
      <PlayerMarker x={70} y={74} className="viz-actor viz-player viz-attacker" />
      <UmpireMarker x={110} y={150} />
      <StepBadge x={248} y={108} n={1} />
      <StepBadge x={200} y={128} n={2} />
      <StepBadge x={150} y={118} n={3} />
      <text x="248" y="58" textAnchor="middle" className="viz-label viz-label-fade">
        {label("keeper", locale)}
      </text>
      <text x="70" y="58" textAnchor="middle" className="viz-label viz-label-fade">
        {label("attack", locale)}
      </text>
      <text x="150" y="188" textAnchor="middle" className="viz-label viz-caption">
        {label("path", locale)} → {label("timing", locale)} → {label("contact", locale)}
      </text>
    </svg>
  );
}
