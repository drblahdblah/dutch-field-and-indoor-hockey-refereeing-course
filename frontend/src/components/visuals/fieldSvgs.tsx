import type { Locale } from "../../i18n/messages";
import { label } from "./svgLabels";
import {
  PlayerMarker,
  StepBadge,
  UmpireMarker,
} from "./vizPrimitives";

/** Original course art — read advantage before whistling when the attack still has space. */
export function AdvantageLensSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-advantage-lens" viewBox="0 0 280 190" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="264" height="174" rx="10" />
      <rect className="viz-surface viz-turf" x="24" y="32" width="232" height="120" rx="4" />
      <rect
        className="viz-pitch-outline"
        x="24"
        y="32"
        width="232"
        height="120"
        rx="4"
        fill="none"
        strokeWidth="2.5"
      />
      <ellipse
        className="viz-advantage-glow"
        cx="168"
        cy="92"
        rx="78"
        ry="48"
      />
      <path
        className="viz-advantage-lens-ring"
        d="M 100 92 A 68 42 0 1 1 236 92 A 68 42 0 1 1 100 92"
        fill="none"
        strokeWidth="2.5"
        pathLength={1}
      />
      <path
        className="viz-advantage-path"
        d="M 52 118 Q 110 96 210 72"
        fill="none"
        strokeWidth="2.5"
        pathLength={1}
      />
      <circle className="viz-ball-travel viz-ball-advantage" cx="52" cy="118" r="5" />
      <PlayerMarker x={52} y={102} className="viz-actor viz-player viz-attacker" />
      <PlayerMarker x={118} y={108} className="viz-actor viz-player viz-defender" />
      <PlayerMarker x={210} y={64} className="viz-actor viz-player viz-attacker" />
      <UmpireMarker x={140} y={148} />
      <StepBadge x={52} y={118} n={1} />
      <StepBadge x={168} y={92} n={2} />
      <StepBadge x={210} y={72} n={3} />
      <circle className="viz-node viz-node-a" cx={52} cy={118} r="6" />
      <circle className="viz-node viz-node-b" cx={168} cy={92} r="6" />
      <circle className="viz-node viz-node-c" cx={210} cy={72} r="6" />
      <text x="52" y="168" textAnchor="middle" className="viz-label viz-label-fade">
        {label("contest", locale)}
      </text>
      <text x="168" y="28" textAnchor="middle" className="viz-label viz-label-fade">
        {label("advantage", locale)}
      </text>
      <text x="220" y="168" textAnchor="middle" className="viz-label viz-label-fade">
        {label("space", locale)}
      </text>
      <text x="140" y="180" textAnchor="middle" className="viz-label viz-caption">
        {label("flow", locale)}
      </text>
    </svg>
  );
}
