import type { Locale } from "../../i18n/messages";
import { label } from "./svgLabels";

export function SafetyTriangleSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg" viewBox="0 0 240 180" aria-hidden="true">
      <circle className="viz-glow" cx="120" cy="95" r="62" />
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
      <path
        className="viz-hint-path"
        d="M 120 36 L 200 148 M 120 36 L 40 148 M 40 148 L 200 148"
        fill="none"
        strokeWidth="1"
      />
      <text x="120" y="58" textAnchor="middle" className="viz-label viz-label-fade">
        {label("safety", locale)}
      </text>
      <text x="188" y="148" textAnchor="middle" className="viz-label viz-label-fade">
        {label("flow", locale)}
      </text>
      <text x="52" y="148" textAnchor="middle" className="viz-label viz-label-fade">
        {label("fairness", locale)}
      </text>
    </svg>
  );
}

export function ScanCycleSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg" viewBox="0 0 260 160" aria-hidden="true">
      <circle className="viz-glow" cx="130" cy="80" r="68" />
      <circle className="viz-orbit" cx="130" cy="80" r="58" fill="none" strokeWidth="2" />
      <g className="viz-orbit-dot">
        <circle cx="130" cy="22" r="7" />
      </g>
      <g className="viz-orbit-dot viz-orbit-dot-b">
        <circle cx="188" cy="80" r="4" />
      </g>
      <text x="130" y="14" textAnchor="middle" className="viz-label viz-label-fade">
        {label("ball", locale)}
      </text>
      <text x="210" y="84" textAnchor="start" className="viz-label viz-label-fade">
        {label("contest", locale)}
      </text>
      <text x="130" y="154" textAnchor="middle" className="viz-label viz-label-fade">
        {label("periphery", locale)}
      </text>
      <text x="18" y="84" textAnchor="start" className="viz-label viz-label-fade">
        {label("partner", locale)}
      </text>
      <circle cx="130" cy="80" r="10" className="viz-core" />
    </svg>
  );
}

export function PitchZonesSvg({ locale }: { locale: Locale }) {
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
      <circle className="viz-ball-travel viz-ball-pitch" cx="100" cy="80" r="5" />
      <text x="130" y="12" textAnchor="middle" className="viz-label viz-label-fade">
        {label("half", locale)}
      </text>
      <text x="44" y="36" textAnchor="middle" className="viz-label viz-label-fade">
        {label("band23", locale)}
      </text>
      <text x="216" y="36" textAnchor="middle" className="viz-label viz-label-fade">
        {label("band23", locale)}
      </text>
      <text x="52" y="86" textAnchor="middle" className="viz-label viz-label-fade">
        {label("circle", locale)}
      </text>
      <text x="208" y="86" textAnchor="middle" className="viz-label viz-label-fade">
        {label("circle", locale)}
      </text>
    </svg>
  );
}

export function DangerConeSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg" viewBox="0 0 260 170" aria-hidden="true">
      <polygon
        className="viz-cone-fill"
        points="48,140 200,48 200,140"
      />
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
      <circle className="viz-ball-travel viz-ball-cone" cx="48" cy="140" r="5" />
      <text x="36" y="160" textAnchor="start" className="viz-label viz-label-fade">
        {label("ball", locale)}
      </text>
      <text x="196" y="36" textAnchor="end" className="viz-label viz-label-fade">
        {label("direction", locale)}
      </text>
      <text x="196" y="158" textAnchor="end" className="viz-label viz-label-fade">
        {label("distance", locale)}
      </text>
      <text x="128" y="108" textAnchor="middle" className="viz-label viz-label-fade">
        {label("speed", locale)}
      </text>
    </svg>
  );
}

export function RestartBubbleSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg" viewBox="0 0 240 160" aria-hidden="true">
      <circle className="viz-glow viz-bubble-glow" cx="120" cy="80" r="58" />
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
      <text x="120" y="16" textAnchor="middle" className="viz-label viz-label-fade">
        {label("bubble", locale)}
      </text>
      <text x="120" y="152" textAnchor="middle" className="viz-label viz-label-fade">
        {label("restart", locale)}
      </text>
    </svg>
  );
}

export function CourtBoardsSvg({ locale }: { locale: Locale }) {
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
      <circle className="viz-ball-travel viz-ball-court" cx="80" cy="80" r="5" />
      <text x="130" y="14" textAnchor="middle" className="viz-label viz-label-fade">
        {label("half", locale)}
      </text>
      <text x="42" y="38" textAnchor="middle" className="viz-label viz-label-fade">
        {label("boards", locale)}
      </text>
      <text x="218" y="38" textAnchor="middle" className="viz-label viz-label-fade">
        {label("boards", locale)}
      </text>
      <text x="48" y="86" textAnchor="middle" className="viz-label viz-label-fade">
        {label("circle", locale)}
      </text>
      <text x="212" y="86" textAnchor="middle" className="viz-label viz-label-fade">
        {label("circle", locale)}
      </text>
    </svg>
  );
}

export function LiftLimitSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg" viewBox="0 0 260 170" aria-hidden="true">
      <line className="viz-lift-ground" x1="40" y1="130" x2="220" y2="130" strokeWidth="2.5" />
      <line className="viz-lift-limit-line" x1="40" y1="70" x2="220" y2="70" strokeWidth="1.5" />
      <circle className="viz-node viz-node-a viz-lift-flat" cx="90" cy="130" r="8" />
      <path
        className="viz-lift-arc"
        d="M 150 130 Q 185 70 220 50"
        fill="none"
        strokeWidth="2.5"
      />
      <circle className="viz-node viz-node-b viz-lift-raised" cx="220" cy="50" r="8" />
      <circle className="viz-ball-travel viz-ball-lift" cx="150" cy="130" r="5" />
      <text x="90" y="152" textAnchor="middle" className="viz-label viz-label-fade">
        {label("flat", locale)}
      </text>
      <text x="220" y="36" textAnchor="end" className="viz-label viz-label-fade">
        {label("raised", locale)}
      </text>
      <text x="130" y="100" textAnchor="middle" className="viz-label viz-label-fade">
        {label("ball", locale)}
      </text>
      <text x="48" y="66" textAnchor="start" className="viz-label viz-label-fade">
        {label("height", locale)}
      </text>
    </svg>
  );
}

export function BoardPlaySvg({ locale }: { locale: Locale }) {
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
      <circle className="viz-ball-travel viz-ball-board" cx="200" cy="120" r="5" />
      <text x="200" y="142" textAnchor="middle" className="viz-label viz-label-fade">
        {label("ball", locale)}
      </text>
      <text x="18" y="84" textAnchor="start" className="viz-label viz-label-fade">
        {label("boards", locale)}
      </text>
      <text x="168" y="28" textAnchor="start" className="viz-label viz-label-fade">
        {label("rebound", locale)}
      </text>
      <text x="130" y="108" textAnchor="middle" className="viz-label viz-label-fade">
        {label("recovery", locale)}
      </text>
    </svg>
  );
}
