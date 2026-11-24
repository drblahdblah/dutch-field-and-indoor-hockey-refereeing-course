import type { Locale } from "../../i18n/messages";
import { label } from "./svgLabels";

/** Field scenario: attack into circle with danger cone overlay. */
export function FieldAttackSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-field-attack" viewBox="0 0 280 180" aria-hidden="true">
      <rect
        className="viz-pitch-outline"
        x="24"
        y="24"
        width="232"
        height="132"
        rx="4"
        fill="none"
        strokeWidth="2.5"
      />
      <line className="viz-pitch-line" x1="140" y1="24" x2="140" y2="156" strokeWidth="2" />
      <rect className="viz-pitch-band" x="208" y="24" width="48" height="132" />
      <path
        className="viz-pitch-circle"
        d="M 208 56 A 40 40 0 0 0 208 124"
        fill="none"
        strokeWidth="2"
      />
      <polygon
        className="viz-cone-fill"
        points="72,120 230,70 230,130"
      />
      <polygon
        className="viz-cone"
        points="72,120 230,70 230,130"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
      />
      <path
        className="viz-scenario-path"
        d="M 60 120 Q 140 100 220 96"
        fill="none"
        strokeWidth="2.5"
      />
      <circle className="viz-node viz-node-a" cx="60" cy="120" r="7" />
      <circle className="viz-core viz-scenario-focus" cx="220" cy="96" r="9" />
      <circle className="viz-ball-travel viz-ball-attack" cx="60" cy="120" r="5" />
      <text x="60" y="148" textAnchor="middle" className="viz-label viz-label-fade">
        {label("attack", locale)}
      </text>
      <text x="232" y="48" textAnchor="middle" className="viz-label viz-label-fade">
        {label("circle", locale)}
      </text>
      <text x="150" y="88" textAnchor="middle" className="viz-label viz-label-fade">
        {label("danger", locale)}
      </text>
      <text x="140" y="22" textAnchor="middle" className="viz-label viz-label-fade">
        {label("field", locale)}
      </text>
    </svg>
  );
}

/** Indoor scenario: board rebound with raised ball risk. */
export function IndoorReboundSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-indoor-rebound" viewBox="0 0 280 180" aria-hidden="true">
      <rect
        className="viz-court-board viz-court-board-left"
        x="18"
        y="28"
        width="12"
        height="124"
        rx="2"
      />
      <rect
        className="viz-court-outline"
        x="30"
        y="28"
        width="220"
        height="124"
        rx="3"
        fill="none"
        strokeWidth="2.5"
      />
      <line className="viz-court-line" x1="140" y1="28" x2="140" y2="152" strokeWidth="2" />
      <path
        className="viz-scenario-path"
        d="M 220 130 L 42 90 L 170 48"
        fill="none"
        strokeWidth="2.5"
      />
      <path
        className="viz-lift-arc"
        d="M 120 90 Q 150 55 170 48"
        fill="none"
        strokeWidth="2"
      />
      <circle className="viz-node viz-node-a" cx="220" cy="130" r="7" />
      <circle className="viz-core viz-board-impact" cx="42" cy="90" r="9" />
      <circle className="viz-node viz-node-b viz-lift-raised" cx="170" cy="48" r="7" />
      <circle className="viz-ball-travel viz-ball-indoor" cx="220" cy="130" r="5" />
      <text x="220" y="154" textAnchor="middle" className="viz-label viz-label-fade">
        {label("ball", locale)}
      </text>
      <text x="34" y="24" textAnchor="start" className="viz-label viz-label-fade">
        {label("boards", locale)}
      </text>
      <text x="178" y="40" textAnchor="start" className="viz-label viz-label-fade">
        {label("raised", locale)}
      </text>
      <text x="120" y="118" textAnchor="middle" className="viz-label viz-label-fade">
        {label("rebound", locale)}
      </text>
      <text x="140" y="22" textAnchor="middle" className="viz-label viz-label-fade">
        {label("indoor", locale)}
      </text>
    </svg>
  );
}

/** Pathway scenario: match cadence with rising pressure. */
export function MatchPressureSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-match-pressure" viewBox="0 0 280 180" aria-hidden="true">
      <line className="viz-cadence-rail" x1="40" y1="120" x2="240" y2="120" strokeWidth="2.5" />
      <rect className="viz-pressure-bar viz-pressure-a" x="52" y="88" width="18" height="32" rx="3" />
      <rect className="viz-pressure-bar viz-pressure-b" x="126" y="64" width="18" height="56" rx="3" />
      <rect className="viz-pressure-bar viz-pressure-c" x="200" y="40" width="18" height="80" rx="3" />
      <circle className="viz-node viz-node-a viz-cadence-node" cx="61" cy="120" r="9" />
      <circle className="viz-node viz-node-b viz-cadence-node" cx="135" cy="120" r="9" />
      <circle className="viz-node viz-node-c viz-cadence-node" cx="209" cy="120" r="9" />
      <path
        className="viz-scenario-path"
        d="M 61 120 L 135 120 L 209 120"
        fill="none"
        strokeWidth="1.5"
      />
      <circle className="viz-ball-travel viz-ball-pressure" cx="61" cy="120" r="4" />
      <text x="61" y="148" textAnchor="middle" className="viz-label viz-label-fade">
        {label("before", locale)}
      </text>
      <text x="135" y="148" textAnchor="middle" className="viz-label viz-label-fade">
        {label("during", locale)}
      </text>
      <text x="209" y="148" textAnchor="middle" className="viz-label viz-label-fade">
        {label("after", locale)}
      </text>
      <text x="140" y="28" textAnchor="middle" className="viz-label viz-label-fade">
        {label("pressure", locale)}
      </text>
      <text x="140" y="172" textAnchor="middle" className="viz-label viz-label-fade">
        {label("pathway", locale)}
      </text>
    </svg>
  );
}
