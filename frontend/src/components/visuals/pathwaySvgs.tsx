import type { Locale } from "../../i18n/messages";
import { label } from "./svgLabels";

export function MatchCadenceSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-cadence" viewBox="0 0 260 160" aria-hidden="true">
      <line className="viz-cadence-rail" x1="36" y1="80" x2="224" y2="80" strokeWidth="2.5" />
      <circle className="viz-node viz-node-a viz-cadence-node" cx="52" cy="80" r="10" />
      <circle className="viz-node viz-node-b viz-cadence-node" cx="130" cy="80" r="10" />
      <circle className="viz-node viz-node-c viz-cadence-node" cx="208" cy="80" r="10" />
      <path
        className="viz-cadence-arrow"
        d="M 68 80 L 112 80"
        fill="none"
        strokeWidth="2"
      />
      <path
        className="viz-cadence-arrow viz-cadence-arrow-b"
        d="M 148 80 L 190 80"
        fill="none"
        strokeWidth="2"
      />
      <circle className="viz-ball-travel viz-ball-cadence" cx="52" cy="80" r="4" />
      <text x="52" y="52" textAnchor="middle" className="viz-label viz-label-fade">
        {label("before", locale)}
      </text>
      <text x="130" y="52" textAnchor="middle" className="viz-label viz-label-fade">
        {label("during", locale)}
      </text>
      <text x="208" y="52" textAnchor="middle" className="viz-label viz-label-fade">
        {label("after", locale)}
      </text>
    </svg>
  );
}

export function PartnerHandoffSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg" viewBox="0 0 260 160" aria-hidden="true">
      <circle className="viz-glow" cx="130" cy="80" r="58" />
      <circle className="viz-node viz-node-a viz-handoff-a" cx="70" cy="80" r="14" />
      <circle className="viz-node viz-node-b viz-handoff-b" cx="190" cy="80" r="14" />
      <path
        className="viz-handoff-arc"
        d="M 90 70 Q 130 36 170 70"
        fill="none"
        strokeWidth="2.5"
      />
      <path
        className="viz-handoff-arc viz-handoff-arc-b"
        d="M 170 90 Q 130 124 90 90"
        fill="none"
        strokeWidth="2.5"
      />
      <circle className="viz-ball-travel viz-ball-handoff" cx="90" cy="70" r="4" />
      <text x="70" y="48" textAnchor="middle" className="viz-label viz-label-fade">
        {label("lead", locale)}
      </text>
      <text x="190" y="48" textAnchor="middle" className="viz-label viz-label-fade">
        {label("support", locale)}
      </text>
      <text x="130" y="148" textAnchor="middle" className="viz-label viz-label-fade">
        {label("handoff", locale)}
      </text>
    </svg>
  );
}

export function ConsistencyLoopSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg" viewBox="0 0 260 170" aria-hidden="true">
      <circle className="viz-glow" cx="130" cy="85" r="62" />
      <circle
        className="viz-consistency-ring"
        cx="130"
        cy="85"
        r="52"
        fill="none"
        strokeWidth="2.5"
      />
      <g className="viz-consistency-dot">
        <circle cx="130" cy="33" r="7" />
      </g>
      <text x="130" y="18" textAnchor="middle" className="viz-label viz-label-fade">
        {label("observe", locale)}
      </text>
      <text x="208" y="90" textAnchor="start" className="viz-label viz-label-fade">
        {label("decide", locale)}
      </text>
      <text x="130" y="158" textAnchor="middle" className="viz-label viz-label-fade">
        {label("communicate", locale)}
      </text>
      <text x="18" y="90" textAnchor="start" className="viz-label viz-label-fade">
        {label("review", locale)}
      </text>
      <circle cx="130" cy="85" r="10" className="viz-core" />
    </svg>
  );
}

export function SourceStackSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-source-stack" viewBox="0 0 260 170" aria-hidden="true">
      <rect
        className="viz-stack-layer viz-stack-a"
        x="50"
        y="28"
        width="160"
        height="36"
        rx="6"
        fill="none"
        strokeWidth="2.5"
      />
      <rect
        className="viz-stack-layer viz-stack-b"
        x="50"
        y="72"
        width="160"
        height="36"
        rx="6"
        fill="none"
        strokeWidth="2.5"
      />
      <rect
        className="viz-stack-layer viz-stack-c"
        x="50"
        y="116"
        width="160"
        height="36"
        rx="6"
        fill="none"
        strokeWidth="2.5"
      />
      <path
        className="viz-stack-flow"
        d="M 130 64 L 130 72 M 130 108 L 130 116"
        fill="none"
        strokeWidth="2"
      />
      <text x="130" y="52" textAnchor="middle" className="viz-label viz-label-fade">
        {label("fih", locale)}
      </text>
      <text x="130" y="96" textAnchor="middle" className="viz-label viz-label-fade">
        {label("knhb", locale)}
      </text>
      <text x="130" y="140" textAnchor="middle" className="viz-label viz-label-fade">
        {label("club", locale)}
      </text>
    </svg>
  );
}

export function TranslationSlotSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-translation-slot" viewBox="0 0 260 150" aria-hidden="true">
      <rect
        className="viz-nl-box"
        x="24"
        y="36"
        width="100"
        height="78"
        rx="8"
        fill="none"
        strokeWidth="2.5"
      />
      <rect
        className="viz-en-slot"
        x="136"
        y="36"
        width="100"
        height="78"
        rx="8"
        fill="none"
        strokeWidth="2.5"
      />
      <text x="74" y="28" textAnchor="middle" className="viz-label viz-label-fade">
        {label("nlBox", locale)}
      </text>
      <text x="186" y="28" textAnchor="middle" className="viz-label viz-label-fade">
        {label("enSlot", locale)}
      </text>
      <path
        className="viz-slot-arrow"
        d="M 128 75 L 148 75"
        fill="none"
        strokeWidth="2"
      />
      <circle className="viz-ball-travel viz-ball-slot" cx="128" cy="75" r="4" />
    </svg>
  );
}

export function AttributionChainSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-attribution-chain" viewBox="0 0 260 150" aria-hidden="true">
      <circle className="viz-node viz-node-a viz-attr-node" cx="48" cy="75" r="12" />
      <circle className="viz-node viz-node-b viz-attr-node" cx="130" cy="75" r="12" />
      <circle className="viz-node viz-node-c viz-attr-node" cx="212" cy="75" r="12" />
      <path
        className="viz-attr-link"
        d="M 64 75 L 112 75"
        fill="none"
        strokeWidth="2.5"
      />
      <path
        className="viz-attr-link viz-attr-link-b"
        d="M 146 75 L 194 75"
        fill="none"
        strokeWidth="2.5"
      />
      <circle className="viz-ball-travel viz-ball-attr" cx="64" cy="75" r="4" />
      <text x="48" y="48" textAnchor="middle" className="viz-label viz-label-fade">
        {label("link", locale)}
      </text>
      <text x="130" y="48" textAnchor="middle" className="viz-label viz-label-fade">
        {label("source", locale)}
      </text>
      <text x="212" y="48" textAnchor="middle" className="viz-label viz-label-fade">
        {label("placeholder", locale)}
      </text>
    </svg>
  );
}

export function CapstoneWeaveSvg({ locale }: { locale: Locale }) {
  return (
    <svg className="viz-svg viz-capstone-weave" viewBox="0 0 260 180" aria-hidden="true">
      <circle className="viz-glow" cx="130" cy="90" r="72" />
      <circle className="viz-node viz-node-a viz-weave-node" cx="70" cy="48" r="12" />
      <circle className="viz-node viz-node-b viz-weave-node" cx="190" cy="48" r="12" />
      <circle className="viz-node viz-node-c viz-weave-node" cx="70" cy="132" r="12" />
      <circle className="viz-core viz-weave-core" cx="190" cy="132" r="12" />
      <path className="viz-weave-link" d="M 82 48 L 178 48" fill="none" strokeWidth="2" />
      <path className="viz-weave-link viz-weave-link-b" d="M 70 60 L 70 120" fill="none" strokeWidth="2" />
      <path className="viz-weave-link viz-weave-link-c" d="M 190 60 L 190 120" fill="none" strokeWidth="2" />
      <path className="viz-weave-link viz-weave-link-d" d="M 82 132 L 178 132" fill="none" strokeWidth="2" />
      <path
        className="viz-weave-diag"
        d="M 82 56 L 178 124"
        fill="none"
        strokeWidth="1.5"
      />
      <circle className="viz-ball-travel viz-ball-weave" cx="82" cy="48" r="4" />
      <text x="70" y="28" textAnchor="middle" className="viz-label viz-label-fade">
        {label("field", locale)}
      </text>
      <text x="190" y="28" textAnchor="middle" className="viz-label viz-label-fade">
        {label("indoor", locale)}
      </text>
      <text x="70" y="164" textAnchor="middle" className="viz-label viz-label-fade">
        {label("pathway", locale)}
      </text>
      <text x="190" y="164" textAnchor="middle" className="viz-label viz-label-fade">
        {label("interp", locale)}
      </text>
    </svg>
  );
}
