/** Known SPA SVG animation keys — keep in sync with backend seed allowlist. */
export const KNOWN_ANIMATION_KEYS = [
  "safety-triangle",
  "scan-cycle",
  "pitch-zones",
  "danger-cone",
  "restart-bubble",
  "court-boards",
  "lift-limit",
  "board-play",
  "match-cadence",
  "partner-handoff",
  "consistency-loop",
  "source-stack",
  "translation-slot",
  "attribution-chain",
  "capstone-weave",
  "field-attack",
  "indoor-rebound",
  "match-pressure",
  "calm-signal",
  "context-split",
  "presence-arc",
] as const;

export type AnimationKey = (typeof KNOWN_ANIMATION_KEYS)[number];

const KEY_SET = new Set<string>(KNOWN_ANIMATION_KEYS);

export function isAnimationKey(value: string): value is AnimationKey {
  return KEY_SET.has(value);
}
