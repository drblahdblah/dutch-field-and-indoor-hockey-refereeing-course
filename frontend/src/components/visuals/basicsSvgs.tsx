import type { Locale } from "../../i18n/messages";
import { label } from "./svgLabels";
import {
  BallMarker,
  PlayerMarker,
  StepBadge,
  UmpireMarker,
} from "./vizPrimitives";

/** Push / slap / hit as three stroke styles. */
export function HitTypesSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-hit-types" viewBox="0 0 300 190" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="284" height="174" rx="10" />
      <path
        className="viz-hit-arc viz-hit-push"
        d="M 40 130 Q 70 100 100 130"
        fill="none"
        strokeWidth="2.5"
        pathLength={1}
      />
      <path
        className="viz-hit-arc viz-hit-slap"
        d="M 120 130 Q 150 70 180 130"
        fill="none"
        strokeWidth="2.5"
        pathLength={1}
      />
      <path
        className="viz-hit-arc viz-hit-full"
        d="M 200 130 Q 230 50 260 130"
        fill="none"
        strokeWidth="2.5"
        pathLength={1}
      />
      <BallMarker x={70} y={112} className="viz-ball-travel viz-ball-hit-a" r={4} />
      <BallMarker x={150} y={96} className="viz-ball-travel viz-ball-hit-b" r={4} />
      <BallMarker x={230} y={84} className="viz-ball-travel viz-ball-hit-c" r={4} />
      <StepBadge x={70} y={130} n={1} />
      <StepBadge x={150} y={130} n={2} />
      <StepBadge x={230} y={130} n={3} />
      <text x="70" y="158" textAnchor="middle" className="viz-label viz-label-fade">
        {label("push", locale)}
      </text>
      <text x="150" y="158" textAnchor="middle" className="viz-label viz-label-fade">
        {label("slap", locale)}
      </text>
      <text x="230" y="158" textAnchor="middle" className="viz-label viz-label-fade">
        {label("hit", locale)}
      </text>
      <text x="150" y="36" textAnchor="middle" className="viz-label viz-caption">
        {label("strokeTypes", locale)}
      </text>
    </svg>
  );
}

/** Stick / body / shadow (third-man) obstruction. */
export function ObstructionTypesSvg({ locale }: { locale: Locale }) {
  return (
    <svg
      className="viz-svg viz-obstruction-types"
      viewBox="0 0 300 200"
      aria-hidden="true"
    >
      <rect className="viz-canvas" x="8" y="8" width="284" height="184" rx="10" />
      <PlayerMarker x={70} y={90} className="viz-actor viz-player viz-attacker" />
      <PlayerMarker x={110} y={90} className="viz-actor viz-player viz-defender" />
      <path
        className="viz-scenario-path"
        d="M 70 100 L 110 100"
        fill="none"
        strokeWidth="2"
        pathLength={1}
      />
      <text x="90" y="58" textAnchor="middle" className="viz-label viz-label-fade">
        {label("stickObs", locale)}
      </text>
      <PlayerMarker x={150} y={140} className="viz-actor viz-player viz-attacker" />
      <PlayerMarker x={190} y={140} className="viz-actor viz-player viz-defender" />
      <circle className="viz-bubble-glow" cx="170" cy="140" r="28" fill="none" strokeWidth="2" />
      <text x="170" y="178" textAnchor="middle" className="viz-label viz-label-fade">
        {label("bodyObs", locale)}
      </text>
      <PlayerMarker x={230} y={70} className="viz-actor viz-player viz-attacker" />
      <PlayerMarker x={250} y={100} className="viz-actor viz-player viz-defender" />
      <PlayerMarker x={210} y={100} className="viz-actor viz-player viz-defender" />
      <path
        className="viz-hard-press-arc"
        d="M 230 78 Q 250 100 230 120"
        fill="none"
        strokeWidth="2"
        pathLength={1}
      />
      <text x="240" y="48" textAnchor="middle" className="viz-label viz-label-fade">
        {label("shadowObs", locale)}
      </text>
      <UmpireMarker x={150} y={60} />
    </svg>
  );
}

/** Penalty corner setup sketch. */
export function PenaltyCornerSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-penalty-corner" viewBox="0 0 300 200" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="284" height="184" rx="10" />
      <rect className="viz-surface viz-turf" x="40" y="36" width="220" height="136" rx="4" />
      <rect className="viz-pitch-band" x="200" y="36" width="60" height="136" />
      <path
        className="viz-pitch-circle"
        d="M 200 68 A 40 40 0 0 0 200 140"
        fill="none"
        strokeWidth="2"
        pathLength={1}
      />
      <BallMarker x={70} y={108} className="viz-ball-travel viz-ball-pc" r={4} />
      <PlayerMarker x={70} y={90} className="viz-actor viz-player viz-attacker" />
      <PlayerMarker x={230} y={100} className="viz-actor viz-player viz-gk" />
      <PlayerMarker x={210} y={70} className="viz-actor viz-player viz-defender" />
      <PlayerMarker x={160} y={120} className="viz-actor viz-player viz-attacker" />
      <UmpireMarker x={120} y={150} />
      <StepBadge x={70} y={108} n={1} />
      <StepBadge x={160} y={120} n={2} />
      <StepBadge x={230} y={100} n={3} />
      <text x="150" y="28" textAnchor="middle" className="viz-label viz-caption">
        {label("penaltyCorner", locale)}
      </text>
    </svg>
  );
}

/** Penalty stroke: one attacker vs keeper. */
export function PenaltyStrokeSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-penalty-stroke" viewBox="0 0 300 180" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="284" height="164" rx="10" />
      <rect className="viz-surface viz-turf" x="50" y="40" width="200" height="100" rx="4" />
      <line className="viz-pitch-line" x1="220" y1="40" x2="220" y2="140" strokeWidth="3" />
      <BallMarker x={150} y={90} className="viz-core viz-scenario-focus" r={5} />
      <PlayerMarker x={150} y={72} className="viz-actor viz-player viz-attacker" />
      <PlayerMarker x={230} y={90} className="viz-actor viz-player viz-gk" />
      <UmpireMarker x={90} y={120} />
      <path
        className="viz-scenario-path"
        d="M 150 90 L 220 90"
        fill="none"
        strokeWidth="2.5"
        pathLength={1}
      />
      <text x="150" y="30" textAnchor="middle" className="viz-label viz-caption">
        {label("penaltyStroke", locale)}
      </text>
    </svg>
  );
}

/** Green / yellow / red card ladder. */
export function CardLadderSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-card-ladder" viewBox="0 0 300 180" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="284" height="164" rx="10" />
      <rect className="viz-card viz-card-green" x="48" y="60" width="50" height="70" rx="4" />
      <rect className="viz-card viz-card-yellow" x="125" y="50" width="50" height="80" rx="4" />
      <rect className="viz-card viz-card-red" x="202" y="40" width="50" height="90" rx="4" />
      <path
        className="viz-ladder-rail"
        d="M 73 140 L 227 140"
        fill="none"
        strokeWidth="2"
        pathLength={1}
      />
      <StepBadge x={73} y={140} n={1} />
      <StepBadge x={150} y={140} n={2} />
      <StepBadge x={227} y={140} n={3} />
      <text x="73" y="48" textAnchor="middle" className="viz-label viz-label-fade">
        {label("greenCard", locale)}
      </text>
      <text x="150" y="38" textAnchor="middle" className="viz-label viz-label-fade">
        {label("yellowCard", locale)}
      </text>
      <text x="227" y="28" textAnchor="middle" className="viz-label viz-label-fade">
        {label("redCard", locale)}
      </text>
      <UmpireMarker x={150} y={100} />
    </svg>
  );
}

/** Match start: toss / sides / ball. */
export function MatchStartSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-match-start" viewBox="0 0 300 190" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="284" height="174" rx="10" />
      <circle className="viz-glow" cx="150" cy="90" r="54" />
      <path
        className="viz-hard-frame-arc"
        d="M 90 110 Q 150 40 210 110"
        fill="none"
        strokeWidth="2.5"
        pathLength={1}
      />
      <UmpireMarker x={150} y={100} />
      <PlayerMarker x={90} y={120} className="viz-actor viz-player viz-attacker" />
      <PlayerMarker x={210} y={120} className="viz-actor viz-player viz-defender" />
      <StepBadge x={90} y={70} n={1} />
      <StepBadge x={150} y={50} n={2} />
      <StepBadge x={210} y={70} n={3} />
      <text x="90" y="158" textAnchor="middle" className="viz-label viz-label-fade">
        {label("countPlayers", locale)}
      </text>
      <text x="150" y="36" textAnchor="middle" className="viz-label viz-label-fade">
        {label("toss", locale)}
      </text>
      <text x="210" y="158" textAnchor="middle" className="viz-label viz-label-fade">
        {label("chooseSide", locale)}
      </text>
    </svg>
  );
}

/** Umpire positioning: lead / support halves. */
export function UmpirePositionSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-umpire-position" viewBox="0 0 300 180" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="284" height="164" rx="10" />
      <rect className="viz-surface viz-turf" x="30" y="36" width="240" height="110" rx="4" />
      <line className="viz-pitch-line" x1="150" y1="36" x2="150" y2="146" strokeWidth="2" />
      <UmpireMarker x={90} y={120} className="viz-actor viz-umpire viz-umpire-lead" />
      <UmpireMarker x={210} y={120} className="viz-actor viz-umpire viz-umpire-support" />
      <BallMarker x={100} y={80} className="viz-ball-travel viz-ball-pos" r={4} />
      <path
        className="viz-scenario-path"
        d="M 60 80 L 140 80"
        fill="none"
        strokeWidth="2"
        pathLength={1}
      />
      <text x="90" y="58" textAnchor="middle" className="viz-label viz-label-fade">
        {label("lead", locale)}
      </text>
      <text x="210" y="58" textAnchor="middle" className="viz-label viz-label-fade">
        {label("support", locale)}
      </text>
      <text x="150" y="168" textAnchor="middle" className="viz-label viz-caption">
        {label("positioning", locale)}
      </text>
    </svg>
  );
}

/** Goalkeeper limits sketch. */
export function GkLimitsSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-gk-limits" viewBox="0 0 300 190" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="284" height="174" rx="10" />
      <rect className="viz-surface viz-turf" x="40" y="40" width="220" height="110" rx="4" />
      <path
        className="viz-pitch-circle"
        d="M 200 60 A 40 40 0 0 0 200 130"
        fill="none"
        strokeWidth="2"
        pathLength={1}
      />
      <PlayerMarker x={230} y={90} className="viz-actor viz-player viz-gk" />
      <circle
        className="viz-bubble-glow"
        cx="230"
        cy="95"
        r="36"
        fill="none"
        strokeWidth="2"
        pathLength={1}
      />
      <PlayerMarker x={120} y={90} className="viz-actor viz-player viz-attacker" />
      <UmpireMarker x={80} y={130} />
      <text x="230" y="48" textAnchor="middle" className="viz-label viz-label-fade">
        {label("keeper", locale)}
      </text>
      <text x="150" y="168" textAnchor="middle" className="viz-label viz-caption">
        {label("circle", locale)} · {label("gkRights", locale)}
      </text>
    </svg>
  );
}
