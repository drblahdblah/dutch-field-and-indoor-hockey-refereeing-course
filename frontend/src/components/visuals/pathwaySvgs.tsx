import type { Locale } from "../../i18n/messages";
import { label } from "./svgLabels";
import { StepBadge, UmpireMarker } from "./vizPrimitives";

export function MatchCadenceSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-cadence" viewBox="0 0 280 170" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="264" height="154" rx="10" />
      <line className="viz-cadence-rail" x1="40" y1="90" x2="240" y2="90" strokeWidth="2.5" />
      <circle className="viz-node viz-node-a viz-cadence-node" cx="56" cy="90" r="10" />
      <circle className="viz-node viz-node-b viz-cadence-node" cx="140" cy="90" r="10" />
      <circle className="viz-node viz-node-c viz-cadence-node" cx="224" cy="90" r="10" />
      <path className="viz-cadence-arrow" d="M 72 90 L 122 90" fill="none" strokeWidth="2" />
      <path
        className="viz-cadence-arrow viz-cadence-arrow-b"
        d="M 158 90 L 206 90"
        fill="none"
        strokeWidth="2"
      />
      <circle className="viz-ball-travel viz-ball-cadence" cx="56" cy="90" r="4" />
      <StepBadge x={56} y={90} n={1} />
      <StepBadge x={140} y={90} n={2} />
      <StepBadge x={224} y={90} n={3} />
      <UmpireMarker x={140} y={128} />
      <text x="56" y="58" textAnchor="middle" className="viz-label viz-label-fade">
        {label("before", locale)}
      </text>
      <text x="140" y="58" textAnchor="middle" className="viz-label viz-label-fade">
        {label("during", locale)}
      </text>
      <text x="224" y="58" textAnchor="middle" className="viz-label viz-label-fade">
        {label("after", locale)}
      </text>
    </svg>
  );
}

export function PartnerHandoffSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg" viewBox="0 0 280 180" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="264" height="164" rx="10" />
      <circle className="viz-glow" cx="140" cy="90" r="62" />
      <circle className="viz-node viz-node-a viz-handoff-a" cx="78" cy="90" r="14" />
      <circle className="viz-node viz-node-b viz-handoff-b" cx="202" cy="90" r="14" />
      <path
        className="viz-handoff-arc"
        d="M 98 78 Q 140 40 182 78"
        fill="none"
        strokeWidth="2.5"
      />
      <path
        className="viz-handoff-arc viz-handoff-arc-b"
        d="M 182 102 Q 140 138 98 102"
        fill="none"
        strokeWidth="2.5"
      />
      <circle className="viz-ball-travel viz-ball-handoff" cx="98" cy="78" r="4" />
      <UmpireMarker x={78} y={96} className="viz-actor viz-umpire viz-umpire-lead" />
      <UmpireMarker x={202} y={96} className="viz-actor viz-umpire viz-umpire-support" />
      <StepBadge x={140} y={48} n={1} />
      <text x="78" y="52" textAnchor="middle" className="viz-label viz-label-fade">
        {label("lead", locale)}
      </text>
      <text x="202" y="52" textAnchor="middle" className="viz-label viz-label-fade">
        {label("support", locale)}
      </text>
      <text x="140" y="164" textAnchor="middle" className="viz-label viz-label-fade">
        {label("handoff", locale)}
      </text>
    </svg>
  );
}

export function ConsistencyLoopSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg" viewBox="0 0 280 190" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="264" height="174" rx="10" />
      <circle className="viz-glow" cx="140" cy="95" r="66" />
      <circle
        className="viz-consistency-ring"
        cx="140"
        cy="95"
        r="54"
        fill="none"
        strokeWidth="2.5"
      />
      <g className="viz-consistency-dot">
        <circle cx="140" cy="41" r="7" />
      </g>
      <circle cx="140" cy="95" r="10" className="viz-core" />
      <UmpireMarker x={140} y={101} />
      <StepBadge x={140} y={41} n={1} />
      <StepBadge x={194} y={95} n={2} />
      <StepBadge x={140} y={149} n={3} />
      <StepBadge x={86} y={95} n={4} />
      <text x="140" y="26" textAnchor="middle" className="viz-label viz-label-fade">
        {label("observe", locale)}
      </text>
      <text x="218" y="99" textAnchor="start" className="viz-label viz-label-fade">
        {label("decide", locale)}
      </text>
      <text x="140" y="172" textAnchor="middle" className="viz-label viz-label-fade">
        {label("communicate", locale)}
      </text>
      <text x="28" y="99" textAnchor="start" className="viz-label viz-label-fade">
        {label("review", locale)}
      </text>
    </svg>
  );
}

export function SourceStackSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-source-stack" viewBox="0 0 280 190" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="264" height="174" rx="10" />
      <rect
        className="viz-stack-layer viz-stack-a"
        x="56"
        y="36"
        width="168"
        height="38"
        rx="6"
        fill="none"
        strokeWidth="2.5"
      />
      <rect
        className="viz-stack-layer viz-stack-b"
        x="56"
        y="84"
        width="168"
        height="38"
        rx="6"
        fill="none"
        strokeWidth="2.5"
      />
      <rect
        className="viz-stack-layer viz-stack-c"
        x="56"
        y="132"
        width="168"
        height="38"
        rx="6"
        fill="none"
        strokeWidth="2.5"
      />
      <path
        className="viz-stack-flow"
        d="M 140 74 L 140 84 M 140 122 L 140 132"
        fill="none"
        strokeWidth="2"
      />
      <StepBadge x={40} y={55} n={1} />
      <StepBadge x={40} y={103} n={2} />
      <StepBadge x={40} y={151} n={3} />
      <text x="140" y="60" textAnchor="middle" className="viz-label viz-label-fade">
        {label("fih", locale)}
      </text>
      <text x="140" y="108" textAnchor="middle" className="viz-label viz-label-fade">
        {label("knhb", locale)}
      </text>
      <text x="140" y="156" textAnchor="middle" className="viz-label viz-label-fade">
        {label("club", locale)}
      </text>
    </svg>
  );
}

export function TranslationSlotSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-translation-slot" viewBox="0 0 280 170" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="264" height="154" rx="10" />
      <rect
        className="viz-nl-box"
        x="32"
        y="44"
        width="100"
        height="84"
        rx="8"
        fill="none"
        strokeWidth="2.5"
      />
      <rect
        className="viz-en-slot"
        x="148"
        y="44"
        width="100"
        height="84"
        rx="8"
        fill="none"
        strokeWidth="2.5"
      />
      <text x="82" y="34" textAnchor="middle" className="viz-label viz-label-fade">
        {label("nlBox", locale)}
      </text>
      <text x="198" y="34" textAnchor="middle" className="viz-label viz-label-fade">
        {label("enSlot", locale)}
      </text>
      <path className="viz-slot-arrow" d="M 138 86 L 158 86" fill="none" strokeWidth="2" />
      <circle className="viz-ball-travel viz-ball-slot" cx="138" cy="86" r="4" />
      <StepBadge x={140} y={86} n={1} />
    </svg>
  );
}

export function AttributionChainSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-attribution-chain" viewBox="0 0 280 170" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="264" height="154" rx="10" />
      <circle className="viz-node viz-node-a viz-attr-node" cx="56" cy="86" r="12" />
      <circle className="viz-node viz-node-b viz-attr-node" cx="140" cy="86" r="12" />
      <circle className="viz-node viz-node-c viz-attr-node" cx="224" cy="86" r="12" />
      <path className="viz-attr-link" d="M 72 86 L 122 86" fill="none" strokeWidth="2.5" />
      <path
        className="viz-attr-link viz-attr-link-b"
        d="M 158 86 L 208 86"
        fill="none"
        strokeWidth="2.5"
      />
      <circle className="viz-ball-travel viz-ball-attr" cx="72" cy="86" r="4" />
      <StepBadge x={56} y={86} n={1} />
      <StepBadge x={140} y={86} n={2} />
      <StepBadge x={224} y={86} n={3} />
      <text x="56" y="56" textAnchor="middle" className="viz-label viz-label-fade">
        {label("link", locale)}
      </text>
      <text x="140" y="56" textAnchor="middle" className="viz-label viz-label-fade">
        {label("source", locale)}
      </text>
      <text x="224" y="56" textAnchor="middle" className="viz-label viz-label-fade">
        {label("placeholder", locale)}
      </text>
    </svg>
  );
}

export function CapstoneWeaveSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-capstone-weave" viewBox="0 0 280 200" aria-hidden="true">
      <rect className="viz-canvas" x="8" y="8" width="264" height="184" rx="10" />
      <circle className="viz-glow" cx="140" cy="100" r="74" />
      <circle className="viz-node viz-node-a viz-weave-node" cx="78" cy="56" r="12" />
      <circle className="viz-node viz-node-b viz-weave-node" cx="202" cy="56" r="12" />
      <circle className="viz-node viz-node-c viz-weave-node" cx="78" cy="144" r="12" />
      <circle className="viz-core viz-weave-core" cx="202" cy="144" r="12" />
      <path className="viz-weave-link" d="M 90 56 L 190 56" fill="none" strokeWidth="2" />
      <path className="viz-weave-link viz-weave-link-b" d="M 78 68 L 78 132" fill="none" strokeWidth="2" />
      <path className="viz-weave-link viz-weave-link-c" d="M 202 68 L 202 132" fill="none" strokeWidth="2" />
      <path className="viz-weave-link viz-weave-link-d" d="M 90 144 L 190 144" fill="none" strokeWidth="2" />
      <path className="viz-weave-diag" d="M 90 64 L 190 136" fill="none" strokeWidth="1.5" />
      <circle className="viz-ball-travel viz-ball-weave" cx="90" cy="56" r="4" />
      <UmpireMarker x={140} y={100} />
      <StepBadge x={78} y={56} n={1} />
      <StepBadge x={202} y={56} n={2} />
      <StepBadge x={78} y={144} n={3} />
      <StepBadge x={202} y={144} n={4} />
      <text x="78" y="36" textAnchor="middle" className="viz-label viz-label-fade">
        {label("field", locale)}
      </text>
      <text x="202" y="36" textAnchor="middle" className="viz-label viz-label-fade">
        {label("indoor", locale)}
      </text>
      <text x="78" y="176" textAnchor="middle" className="viz-label viz-label-fade">
        {label("pathway", locale)}
      </text>
      <text x="202" y="176" textAnchor="middle" className="viz-label viz-label-fade">
        {label("interp", locale)}
      </text>
    </svg>
  );
}
