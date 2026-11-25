import type { ComponentType, ReactNode } from "react";
import type { Locale } from "../../i18n/messages";
import type { AnimationKey } from "./animationKeys";
import {
  BoardPlaySvg,
  CourtBoardsSvg,
  DangerConeSvg,
  LiftLimitSvg,
  PitchZonesSvg,
  RestartBubbleSvg,
  SafetyTriangleSvg,
  ScanCycleSvg,
} from "./coreSvgs";
import {
  AttributionChainSvg,
  CapstoneWeaveSvg,
  ConsistencyLoopSvg,
  MatchCadenceSvg,
  PartnerHandoffSvg,
  SourceStackSvg,
  TranslationSlotSvg,
} from "./pathwaySvgs";
import {
  CallClaritySvg,
  CalmSignalSvg,
  ContextSplitSvg,
  PresenceArcSvg,
} from "./introSvgs";
import { AdvantageLensSvg } from "./fieldSvgs";
import {
  FieldAttackSvg,
  IndoorReboundSvg,
  MatchPressureSvg,
} from "./scenarioSvgs";

type SvgProps = { locale: Locale };

const ANIMATIONS = {
  "safety-triangle": SafetyTriangleSvg,
  "scan-cycle": ScanCycleSvg,
  "pitch-zones": PitchZonesSvg,
  "danger-cone": DangerConeSvg,
  "restart-bubble": RestartBubbleSvg,
  "court-boards": CourtBoardsSvg,
  "lift-limit": LiftLimitSvg,
  "board-play": BoardPlaySvg,
  "match-cadence": MatchCadenceSvg,
  "partner-handoff": PartnerHandoffSvg,
  "consistency-loop": ConsistencyLoopSvg,
  "source-stack": SourceStackSvg,
  "translation-slot": TranslationSlotSvg,
  "attribution-chain": AttributionChainSvg,
  "capstone-weave": CapstoneWeaveSvg,
  "field-attack": FieldAttackSvg,
  "indoor-rebound": IndoorReboundSvg,
  "match-pressure": MatchPressureSvg,
  "calm-signal": CalmSignalSvg,
  "context-split": ContextSplitSvg,
  "presence-arc": PresenceArcSvg,
  "call-clarity": CallClaritySvg,
  "advantage-lens": AdvantageLensSvg,
} as const satisfies Record<AnimationKey, ComponentType<SvgProps>>;

export function pickAnimation(
  key: string | null | undefined,
  locale: Locale,
): ReactNode {
  if (key && key in ANIMATIONS) {
    const Svg = ANIMATIONS[key as AnimationKey];
    return <Svg locale={locale} />;
  }
  return (
    <div className="viz-fallback" aria-hidden="true">
      <span className="viz-pulse" />
    </div>
  );
}
