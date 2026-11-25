import type { Locale } from "../../i18n/messages";
import { label } from "./svgLabels";
import {
  PlayerMarker,
  StepBadge,
  UmpireMarker,
} from "./vizPrimitives";

/** Original course art — stay closer and communicate sooner in tight indoor space. */
export function TempoProximitySvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-tempo-proximity" viewBox="0 0 280 190" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="264" height="174" rx="10" />
      <rect
        className="viz-court-board viz-court-board-left"
        x="22"
        y="36"
        width="10"
        height="112"
        rx="2"
      />
      <rect
        className="viz-court-board viz-court-board-right"
        x="248"
        y="36"
        width="10"
        height="112"
        rx="2"
      />
      <rect className="viz-surface viz-floor" x="32" y="36" width="216" height="112" rx="3" />
      <rect
        className="viz-court-outline"
        x="32"
        y="36"
        width="216"
        height="112"
        rx="3"
        fill="none"
        strokeWidth="2.5"
      />
      <ellipse
        className="viz-tempo-glow"
        cx="140"
        cy="92"
        rx="62"
        ry="40"
      />
      <path
        className="viz-tempo-ring"
        d="M 86 92 A 54 34 0 1 1 194 92 A 54 34 0 1 1 86 92"
        fill="none"
        strokeWidth="2.5"
        pathLength={1}
      />
      <path
        className="viz-tempo-path"
        d="M 70 120 Q 120 88 200 70"
        fill="none"
        strokeWidth="2.5"
        pathLength={1}
      />
      <circle className="viz-ball-travel viz-ball-tempo" cx="70" cy="120" r="5" />
      <PlayerMarker x={70} y={104} className="viz-actor viz-player viz-attacker" />
      <PlayerMarker x={118} y={100} className="viz-actor viz-player viz-defender" />
      <UmpireMarker x={148} y={128} />
      <UmpireMarker x={198} y={64} />
      <path
        className="viz-tempo-partner"
        d="M 148 120 Q 174 86 198 72"
        fill="none"
        strokeWidth="1.75"
        pathLength={1}
      />
      <StepBadge x={70} y={120} n={1} />
      <StepBadge x={140} y={92} n={2} />
      <StepBadge x={198} y={70} n={3} />
      <circle className="viz-node viz-node-a" cx={70} cy={120} r="6" />
      <circle className="viz-node viz-node-b" cx={140} cy={92} r="6" />
      <circle className="viz-node viz-node-c" cx={198} cy={70} r="6" />
      <text x="70" y="168" textAnchor="middle" className="viz-label viz-label-fade">
        {label("closer", locale)}
      </text>
      <text x="140" y="28" textAnchor="middle" className="viz-label viz-label-fade">
        {label("tempo", locale)}
      </text>
      <text x="214" y="168" textAnchor="middle" className="viz-label viz-label-fade">
        {label("partner", locale)}
      </text>
      <text x="140" y="180" textAnchor="middle" className="viz-label viz-caption">
        {label("communicate", locale)}
      </text>
    </svg>
  );
}
