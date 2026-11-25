/** Shared original SVG markers for instructional diagrams (not KNHB art). */

type Point = { x: number; y: number };

/** Simple stick-figure umpire (whistle ring). */
export function UmpireMarker({
  x,
  y,
  className = "viz-actor viz-umpire",
}: Point & { className?: string }) {
  return (
    <g className={className} transform={`translate(${x} ${y})`}>
      <circle className="viz-actor-head" cx="0" cy="-10" r="5" />
      <path className="viz-actor-body" d="M 0 -5 L 0 8 M -7 0 L 7 0 M -6 18 L 0 8 L 6 18" />
      <circle className="viz-umpire-badge" cx="8" cy="-8" r="3" />
    </g>
  );
}

/** Simple stick-figure player. */
export function PlayerMarker({
  x,
  y,
  className = "viz-actor viz-player",
}: Point & { className?: string }) {
  return (
    <g className={className} transform={`translate(${x} ${y})`}>
      <circle className="viz-actor-head" cx="0" cy="-9" r="4.5" />
      <path className="viz-actor-body" d="M 0 -4 L 0 7 M -6 1 L 6 1 M -5 16 L 0 7 L 5 16" />
    </g>
  );
}

/** Numbered callout badge for step-by-step diagrams. */
export function StepBadge({
  x,
  y,
  n,
  className = "viz-step",
}: Point & { n: number; className?: string }) {
  return (
    <g className={className} transform={`translate(${x} ${y})`}>
      <circle className="viz-step-disc" r="9" />
      <text className="viz-step-num" textAnchor="middle" dominantBaseline="central">
        {n}
      </text>
    </g>
  );
}

/** Hockey ball (solid). */
export function BallMarker({
  x,
  y,
  className = "viz-ball-mark",
  r = 5,
}: Point & { className?: string; r?: number }) {
  return <circle className={className} cx={x} cy={y} r={r} />;
}
