import type { Locale } from "../../i18n/messages";
import { label } from "./svgLabels";
import {
  BallMarker,
  PlayerMarker,
  StepBadge,
  UmpireMarker,
} from "./vizPrimitives";

export function SafetyTriangleSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg" viewBox="0 0 280 190" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="264" height="174" rx="10" />
      <circle className="viz-glow" cx="140" cy="100" r="68" />
      <polygon
        className="viz-tri"
        points="140,28 238,162 42,162"
        fill="none"
        stroke="currentColor"
        strokeWidth="2.5"
      />
      <path
        className="viz-hint-path"
        d="M 140 42 L 222 152 M 140 42 L 58 152 M 58 152 L 222 152"
        fill="none"
        strokeWidth="1"
      />
      <circle className="viz-node viz-node-a" cx="140" cy="36" r="8" />
      <circle className="viz-node viz-node-b" cx="228" cy="154" r="8" />
      <circle className="viz-node viz-node-c" cx="52" cy="154" r="8" />
      <StepBadge x={140} y={36} n={1} />
      <StepBadge x={228} y={154} n={2} />
      <StepBadge x={52} y={154} n={3} />
      <UmpireMarker x={140} y={108} />
      <text x="140" y="62" textAnchor="middle" className="viz-label viz-label-fade">
        {label("safety", locale)}
      </text>
      <text x="210" y="148" textAnchor="middle" className="viz-label viz-label-fade">
        {label("flow", locale)}
      </text>
      <text x="70" y="148" textAnchor="middle" className="viz-label viz-label-fade">
        {label("fairness", locale)}
      </text>
      <text x="140" y="178" textAnchor="middle" className="viz-label viz-caption">
        {label("umpire", locale)}
      </text>
    </svg>
  );
}

export function ScanCycleSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg" viewBox="0 0 280 180" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="264" height="164" rx="10" />
      <circle className="viz-glow" cx="140" cy="90" r="70" />
      <circle className="viz-orbit" cx="140" cy="90" r="58" fill="none" strokeWidth="2" />
      <g className="viz-orbit-dot">
        <circle cx="140" cy="32" r="7" />
      </g>
      <g className="viz-orbit-dot viz-orbit-dot-b">
        <circle cx="198" cy="90" r="4" />
      </g>
      <circle cx="140" cy="90" r="11" className="viz-core" />
      <UmpireMarker x={140} y={96} />
      <StepBadge x={140} y={32} n={1} />
      <StepBadge x={198} y={90} n={2} />
      <StepBadge x={140} y={148} n={3} />
      <StepBadge x={82} y={90} n={4} />
      <text x="140" y="20" textAnchor="middle" className="viz-label viz-label-fade">
        {label("ball", locale)}
      </text>
      <text x="220" y="94" textAnchor="start" className="viz-label viz-label-fade">
        {label("contest", locale)}
      </text>
      <text x="140" y="168" textAnchor="middle" className="viz-label viz-label-fade">
        {label("periphery", locale)}
      </text>
      <text x="28" y="94" textAnchor="start" className="viz-label viz-label-fade">
        {label("partner", locale)}
      </text>
    </svg>
  );
}

export function PitchZonesSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-pitch" viewBox="0 0 280 180" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="264" height="164" rx="10" />
      <rect className="viz-surface viz-turf" x="28" y="28" width="224" height="124" rx="4" />
      <rect
        className="viz-pitch-outline"
        x="28"
        y="28"
        width="224"
        height="124"
        rx="4"
        fill="none"
        strokeWidth="2.5"
      />
      <line className="viz-pitch-line" x1="140" y1="28" x2="140" y2="152" strokeWidth="2" />
      <rect className="viz-pitch-band" x="28" y="28" width="46" height="124" />
      <rect className="viz-pitch-band" x="206" y="28" width="46" height="124" />
      <path
        className="viz-pitch-circle viz-pitch-circle-a"
        d="M 74 56 A 34 34 0 0 1 74 124"
        fill="none"
        strokeWidth="2"
      />
      <path
        className="viz-pitch-circle viz-pitch-circle-b"
        d="M 206 56 A 34 34 0 0 0 206 124"
        fill="none"
        strokeWidth="2"
      />
      <circle className="viz-ball-travel viz-ball-pitch" cx="110" cy="90" r="5" />
      <UmpireMarker x={140} y={90} />
      <PlayerMarker x={70} y={90} className="viz-actor viz-player viz-player-a" />
      <PlayerMarker x={210} y={90} className="viz-actor viz-player viz-player-b" />
      <text x="140" y="22" textAnchor="middle" className="viz-label viz-label-fade">
        {label("half", locale)}
      </text>
      <text x="51" y="48" textAnchor="middle" className="viz-label viz-label-fade">
        {label("band23", locale)}
      </text>
      <text x="229" y="48" textAnchor="middle" className="viz-label viz-label-fade">
        {label("band23", locale)}
      </text>
      <text x="58" y="96" textAnchor="middle" className="viz-label viz-label-fade">
        {label("circle", locale)}
      </text>
      <text x="222" y="96" textAnchor="middle" className="viz-label viz-label-fade">
        {label("circle", locale)}
      </text>
    </svg>
  );
}

export function DangerConeSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg" viewBox="0 0 280 190" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="264" height="174" rx="10" />
      <polygon className="viz-cone-fill" points="56,150 220,52 220,150" />
      <polygon
        className="viz-cone"
        points="56,150 220,52 220,150"
        fill="none"
        stroke="currentColor"
        strokeWidth="2.5"
      />
      <circle className="viz-node viz-node-a" cx="56" cy="150" r="7" />
      <circle className="viz-node viz-node-b" cx="220" cy="52" r="7" />
      <circle className="viz-node viz-node-c" cx="220" cy="150" r="7" />
      <circle className="viz-ball-travel viz-ball-cone" cx="56" cy="150" r="5" />
      <UmpireMarker x={96} y={118} />
      <PlayerMarker x={190} y={100} />
      <StepBadge x={56} y={150} n={1} />
      <StepBadge x={220} y={52} n={2} />
      <StepBadge x={220} y={150} n={3} />
      <text x="44" y="172" textAnchor="start" className="viz-label viz-label-fade">
        {label("ball", locale)}
      </text>
      <text x="214" y="40" textAnchor="end" className="viz-label viz-label-fade">
        {label("direction", locale)}
      </text>
      <text x="214" y="172" textAnchor="end" className="viz-label viz-label-fade">
        {label("distance", locale)}
      </text>
      <text x="142" y="116" textAnchor="middle" className="viz-label viz-label-fade">
        {label("speed", locale)}
      </text>
    </svg>
  );
}

export function RestartBubbleSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg" viewBox="0 0 260 180" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="244" height="164" rx="10" />
      <circle className="viz-glow viz-bubble-glow" cx="130" cy="90" r="60" />
      <circle
        className="viz-bubble"
        cx="130"
        cy="90"
        r="54"
        fill="none"
        strokeWidth="2.5"
      />
      <circle className="viz-core viz-bubble-core" cx="130" cy="90" r="10" />
      <BallMarker x={130} y={90} className="viz-ball-mark" />
      <circle className="viz-node viz-node-a" cx="130" cy="36" r="6" />
      <circle className="viz-node viz-node-b" cx="184" cy="120" r="6" />
      <circle className="viz-node viz-node-c" cx="76" cy="120" r="6" />
      <PlayerMarker x={76} y={120} className="viz-actor viz-player viz-player-a" />
      <PlayerMarker x={184} y={120} className="viz-actor viz-player viz-player-b" />
      <UmpireMarker x={130} y={148} />
      <text x="130" y="24" textAnchor="middle" className="viz-label viz-label-fade">
        {label("bubble", locale)}
      </text>
      <text x="130" y="172" textAnchor="middle" className="viz-label viz-label-fade">
        {label("restart", locale)}
      </text>
    </svg>
  );
}

export function CourtBoardsSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-court" viewBox="0 0 280 180" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="264" height="164" rx="10" />
      <rect
        className="viz-court-board viz-court-board-left"
        x="22"
        y="28"
        width="12"
        height="124"
        rx="2"
      />
      <rect
        className="viz-court-board viz-court-board-right"
        x="246"
        y="28"
        width="12"
        height="124"
        rx="2"
      />
      <rect className="viz-surface viz-floor" x="34" y="28" width="212" height="124" rx="3" />
      <rect
        className="viz-court-outline"
        x="34"
        y="28"
        width="212"
        height="124"
        rx="3"
        fill="none"
        strokeWidth="2.5"
      />
      <line className="viz-court-line" x1="140" y1="28" x2="140" y2="152" strokeWidth="2" />
      <path
        className="viz-court-circle viz-court-circle-a"
        d="M 60 56 A 30 30 0 0 1 60 124"
        fill="none"
        strokeWidth="2"
      />
      <path
        className="viz-court-circle viz-court-circle-b"
        d="M 220 56 A 30 30 0 0 0 220 124"
        fill="none"
        strokeWidth="2"
      />
      <circle className="viz-ball-travel viz-ball-court" cx="90" cy="90" r="5" />
      <UmpireMarker x={140} y={90} />
      <text x="140" y="22" textAnchor="middle" className="viz-label viz-label-fade">
        {label("half", locale)}
      </text>
      <text x="48" y="48" textAnchor="middle" className="viz-label viz-label-fade">
        {label("boards", locale)}
      </text>
      <text x="232" y="48" textAnchor="middle" className="viz-label viz-label-fade">
        {label("boards", locale)}
      </text>
      <text x="54" y="96" textAnchor="middle" className="viz-label viz-label-fade">
        {label("circle", locale)}
      </text>
      <text x="226" y="96" textAnchor="middle" className="viz-label viz-label-fade">
        {label("circle", locale)}
      </text>
    </svg>
  );
}

export function LiftLimitSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg" viewBox="0 0 280 190" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="264" height="174" rx="10" />
      <line className="viz-lift-ground" x1="40" y1="140" x2="240" y2="140" strokeWidth="2.5" />
      <line className="viz-lift-limit-line" x1="40" y1="78" x2="240" y2="78" strokeWidth="1.5" />
      <circle className="viz-node viz-node-a viz-lift-flat" cx="96" cy="140" r="8" />
      <path
        className="viz-lift-arc"
        d="M 150 140 Q 188 78 230 56"
        fill="none"
        strokeWidth="2.5"
      />
      <circle className="viz-node viz-node-b viz-lift-raised" cx="230" cy="56" r="8" />
      <circle className="viz-ball-travel viz-ball-lift" cx="150" cy="140" r="5" />
      <UmpireMarker x={130} y={156} />
      <PlayerMarker x={96} y={122} />
      <StepBadge x={96} y={140} n={1} />
      <StepBadge x={230} y={56} n={2} />
      <text x="96" y="172" textAnchor="middle" className="viz-label viz-label-fade">
        {label("flat", locale)}
      </text>
      <text x="230" y="42" textAnchor="end" className="viz-label viz-label-fade">
        {label("raised", locale)}
      </text>
      <text x="150" y="112" textAnchor="middle" className="viz-label viz-label-fade">
        {label("ball", locale)}
      </text>
      <text x="48" y="72" textAnchor="start" className="viz-label viz-label-fade">
        {label("height", locale)}
      </text>
    </svg>
  );
}

export function BoardPlaySvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg" viewBox="0 0 280 180" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="264" height="164" rx="10" />
      <rect className="viz-surface viz-floor" x="48" y="28" width="200" height="124" rx="3" />
      <rect className="viz-court-board" x="36" y="28" width="12" height="124" rx="2" />
      <path
        className="viz-board-path"
        d="M 210 130 L 54 90 L 170 44"
        fill="none"
        strokeWidth="2.5"
      />
      <circle className="viz-node viz-node-a" cx="210" cy="130" r="7" />
      <circle className="viz-core viz-board-impact" cx="54" cy="90" r="9" />
      <circle className="viz-node viz-node-b" cx="170" cy="44" r="7" />
      <circle className="viz-ball-travel viz-ball-board" cx="210" cy="130" r="5" />
      <UmpireMarker x={120} y={120} />
      <StepBadge x={210} y={130} n={1} />
      <StepBadge x={54} y={90} n={2} />
      <StepBadge x={170} y={44} n={3} />
      <text x="210" y="154" textAnchor="middle" className="viz-label viz-label-fade">
        {label("ball", locale)}
      </text>
      <text x="28" y="94" textAnchor="start" className="viz-label viz-label-fade">
        {label("boards", locale)}
      </text>
      <text x="178" y="34" textAnchor="start" className="viz-label viz-label-fade">
        {label("rebound", locale)}
      </text>
      <text x="140" y="118" textAnchor="middle" className="viz-label viz-label-fade">
        {label("recovery", locale)}
      </text>
    </svg>
  );
}
