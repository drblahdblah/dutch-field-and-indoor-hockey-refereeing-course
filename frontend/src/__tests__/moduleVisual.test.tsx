import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import type { VisualPlaceholder } from "../api/types";
import {
  ModuleVisual,
  QuizVizHook,
  animationKeyFromHint,
} from "../components/ModuleVisual";
import { KNOWN_ANIMATION_KEYS } from "../components/visuals/animationKeys";

describe("animationKeyFromHint", () => {
  it("maps known quiz hints to animation keys with exact match only", () => {
    for (const key of KNOWN_ANIMATION_KEYS) {
      expect(animationKeyFromHint(key)).toBe(key);
    }
    expect(animationKeyFromHint(" Danger-Cone ")).toBe("danger-cone");
    expect(animationKeyFromHint(" Field-Attack ")).toBe("field-attack");
    expect(animationKeyFromHint("timeline: raise → proximity")).toBeNull();
    expect(animationKeyFromHint("prefix-safety-triangle")).toBeNull();
    expect(animationKeyFromHint(null)).toBeNull();
    expect(animationKeyFromHint("")).toBeNull();
  });
});

describe("ModuleVisual", () => {
  it("renders original SVG animation with bilingual caption", () => {
    const visual: VisualPlaceholder = {
      id: "viz-safety-triangle",
      kind: "svg_animation",
      title: { nl: "Driehoek", en: "Triangle" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "safety-triangle",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    render(<ModuleVisual visual={visual} locale="en" />);
    expect(screen.getByText("Triangle")).toBeInTheDocument();
    expect(screen.getByText("Original")).toBeInTheDocument();
    expect(document.querySelector("svg.viz-svg")).toBeTruthy();
  });

  it("renders field pitch-zones SVG with localized zone labels", () => {
    const visual: VisualPlaceholder = {
      id: "viz-pitch-zones",
      kind: "svg_animation",
      title: { nl: "Zones", en: "Zones" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "pitch-zones",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    render(<ModuleVisual visual={visual} locale="nl" />);
    expect(screen.getByText("Zones")).toBeInTheDocument();
    const svg = document.querySelector("svg.viz-pitch");
    expect(svg).toBeTruthy();
    expect(svg).toHaveAttribute("aria-hidden", "true");
    expect(svg?.querySelector(".viz-pitch-circle-a")).toHaveAttribute(
      "pathLength",
      "1",
    );
    expect(screen.getByText("helft")).toBeInTheDocument();
    expect(screen.getAllByText("23m")).toHaveLength(2);
    expect(screen.getAllByText("cirkel")).toHaveLength(2);
  });

  it("renders danger-cone and restart-bubble SVGs", () => {
    const cone: VisualPlaceholder = {
      id: "viz-danger-cone",
      kind: "svg_animation",
      title: { nl: "Kegel", en: "Cone" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "danger-cone",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    const { rerender } = render(<ModuleVisual visual={cone} locale="en" />);
    expect(document.querySelector("svg.viz-danger-cone .viz-cone")).toHaveAttribute(
      "pathLength",
      "1",
    );
    expect(screen.getByText("direction")).toBeInTheDocument();
    expect(screen.getByText("distance")).toBeInTheDocument();
    expect(screen.getByText("speed")).toBeInTheDocument();

    const bubble: VisualPlaceholder = {
      id: "viz-restart-bubble",
      kind: "svg_animation",
      title: { nl: "Bubbel", en: "Bubble" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "restart-bubble",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    rerender(<ModuleVisual visual={bubble} locale="nl" />);
    expect(
      document.querySelector("svg.viz-restart-bubble .viz-bubble"),
    ).toHaveAttribute("pathLength", "1");
    expect(screen.getByText("bubbel")).toBeInTheDocument();
    expect(screen.getByText("herstart")).toBeInTheDocument();
  });

  it("renders a complete safety-triangle pathLength for the draw animation", () => {
    const visual: VisualPlaceholder = {
      id: "viz-safety-triangle",
      kind: "svg_animation",
      title: { nl: "Driehoek", en: "Triangle" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "safety-triangle",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    render(<ModuleVisual visual={visual} locale="en" />);
    const tri = document.querySelector("polygon.viz-tri");
    expect(tri).toBeTruthy();
    expect(tri).toHaveAttribute("pathLength", "1");
    expect(screen.getByText("safety")).toBeInTheDocument();
    expect(screen.getByText("fairness")).toBeInTheDocument();
    expect(screen.getByText("flow")).toBeInTheDocument();
  });

  it("renders intro calm-signal, context-split, presence-arc, and call-clarity SVGs", () => {
    const calm: VisualPlaceholder = {
      id: "viz-calm-signal",
      kind: "svg_animation",
      title: { nl: "Calm", en: "Calm" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "calm-signal",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    const { rerender } = render(<ModuleVisual visual={calm} locale="en" />);
    expect(document.querySelector("svg.viz-calm-signal")).toBeTruthy();
    expect(screen.getByText("calm")).toBeInTheDocument();
    expect(screen.getByText("brief")).toBeInTheDocument();
    expect(screen.getByText("visible")).toBeInTheDocument();

    const split: VisualPlaceholder = {
      id: "viz-context-split",
      kind: "svg_animation",
      title: { nl: "Context", en: "Context" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "context-split",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    rerender(<ModuleVisual visual={split} locale="nl" />);
    expect(document.querySelector("svg.viz-context-split")).toBeTruthy();
    expect(screen.getByText("veld")).toBeInTheDocument();
    expect(screen.getByText("zaal")).toBeInTheDocument();

    const presence: VisualPlaceholder = {
      id: "viz-presence-arc",
      kind: "svg_animation",
      title: { nl: "Aanwezigheid", en: "Presence" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "presence-arc",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    rerender(<ModuleVisual visual={presence} locale="en" />);
    expect(document.querySelector("svg.viz-presence-arc")).toBeTruthy();
    expect(screen.getByText("posture")).toBeInTheDocument();
    expect(screen.getByText("presence")).toBeInTheDocument();

    const call: VisualPlaceholder = {
      id: "viz-call-clarity",
      kind: "svg_animation",
      title: { nl: "Leesbaar", en: "Readable" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "call-clarity",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    rerender(<ModuleVisual visual={call} locale="en" />);
    expect(document.querySelector("svg.viz-call-clarity")).toBeTruthy();
    expect(screen.getByText("decide")).toBeInTheDocument();
    expect(screen.getByText("communicate")).toBeInTheDocument();
  });

  it("renders the field advantage-lens SVG", () => {
    const lens: VisualPlaceholder = {
      id: "viz-advantage-lens",
      kind: "svg_animation",
      title: { nl: "Voordeel", en: "Advantage" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "advantage-lens",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    render(<ModuleVisual visual={lens} locale="en" />);
    const svg = document.querySelector("svg.viz-advantage-lens");
    expect(svg).toBeTruthy();
    expect(svg?.querySelector(".viz-advantage-lens-ring")).toHaveAttribute(
      "pathLength",
      "1",
    );
    expect(svg?.querySelector(".viz-advantage-path")).toHaveAttribute(
      "pathLength",
      "1",
    );
    expect(screen.getByText("advantage")).toBeInTheDocument();
    expect(screen.getByText("contest")).toBeInTheDocument();
    expect(screen.getByText("space")).toBeInTheDocument();
  });

  it("renders indoor court-boards, lift-limit, board-play, and tempo-proximity SVGs", () => {
    const court: VisualPlaceholder = {
      id: "viz-court-boards",
      kind: "svg_animation",
      title: { nl: "Zaal", en: "Court" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "court-boards",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    const { rerender } = render(<ModuleVisual visual={court} locale="nl" />);
    const svg = document.querySelector("svg.viz-court");
    expect(svg).toBeTruthy();
    expect(svg).toHaveAttribute("aria-hidden", "true");
    expect(svg?.querySelector(".viz-court-circle-a")).toHaveAttribute(
      "pathLength",
      "1",
    );
    expect(screen.getByText("helft")).toBeInTheDocument();
    expect(screen.getAllByText("banden")).toHaveLength(2);
    expect(screen.getAllByText("cirkel")).toHaveLength(2);

    const lift: VisualPlaceholder = {
      id: "viz-lift-limit",
      kind: "svg_animation",
      title: { nl: "Lift", en: "Lift" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "lift-limit",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    rerender(<ModuleVisual visual={lift} locale="en" />);
    expect(document.querySelector(".viz-lift-arc")).toHaveAttribute(
      "pathLength",
      "1",
    );
    expect(screen.getByText("flat")).toBeInTheDocument();
    expect(screen.getByText("raised")).toBeInTheDocument();

    const board: VisualPlaceholder = {
      id: "viz-board-play",
      kind: "svg_animation",
      title: { nl: "Band", en: "Board" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "board-play",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    rerender(<ModuleVisual visual={board} locale="nl" />);
    expect(document.querySelector(".viz-board-path")).toHaveAttribute(
      "pathLength",
      "1",
    );
    expect(screen.getByText("banden")).toBeInTheDocument();
    expect(screen.getByText("rebound")).toBeInTheDocument();
    expect(screen.getByText("herstel")).toBeInTheDocument();

    const tempo: VisualPlaceholder = {
      id: "viz-tempo-proximity",
      kind: "svg_animation",
      title: { nl: "Tempo", en: "Tempo" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "tempo-proximity",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    rerender(<ModuleVisual visual={tempo} locale="en" />);
    const tempoSvg = document.querySelector("svg.viz-tempo-proximity");
    expect(tempoSvg).toBeTruthy();
    expect(tempoSvg?.querySelector(".viz-tempo-ring")).toHaveAttribute(
      "pathLength",
      "1",
    );
    expect(tempoSvg?.querySelector(".viz-tempo-path")).toHaveAttribute(
      "pathLength",
      "1",
    );
    expect(tempoSvg?.querySelector(".viz-tempo-partner")).toHaveAttribute(
      "pathLength",
      "1",
    );
    expect(screen.getByText("closer")).toBeInTheDocument();
    expect(screen.getByText("tempo")).toBeInTheDocument();
    expect(screen.getByText("partner")).toBeInTheDocument();
    expect(screen.getByText("communicate")).toBeInTheDocument();
  });

  it("renders pathway match-cadence, partner-handoff, consistency-loop, and standard-ladder SVGs", () => {
    const cadence: VisualPlaceholder = {
      id: "viz-match-cadence",
      kind: "svg_animation",
      title: { nl: "Ritme", en: "Cadence" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "match-cadence",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    const { rerender } = render(<ModuleVisual visual={cadence} locale="nl" />);
    const svg = document.querySelector("svg.viz-cadence");
    expect(svg).toBeTruthy();
    expect(svg).toHaveAttribute("aria-hidden", "true");
    expect(svg?.querySelector(".viz-cadence-arrow")).toHaveAttribute(
      "pathLength",
      "1",
    );
    expect(screen.getByText("vóór")).toBeInTheDocument();
    expect(screen.getByText("tijdens")).toBeInTheDocument();
    expect(screen.getByText("ná")).toBeInTheDocument();

    const handoff: VisualPlaceholder = {
      id: "viz-partner-handoff",
      kind: "svg_animation",
      title: { nl: "Overdracht", en: "Handoff" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "partner-handoff",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    rerender(<ModuleVisual visual={handoff} locale="en" />);
    expect(document.querySelector(".viz-handoff-arc")).toHaveAttribute(
      "pathLength",
      "1",
    );
    expect(screen.getByText("lead")).toBeInTheDocument();
    expect(screen.getByText("support")).toBeInTheDocument();
    expect(screen.getByText("handoff")).toBeInTheDocument();

    const loop: VisualPlaceholder = {
      id: "viz-consistency-loop",
      kind: "svg_animation",
      title: { nl: "Lus", en: "Loop" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "consistency-loop",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    rerender(<ModuleVisual visual={loop} locale="nl" />);
    expect(document.querySelector(".viz-consistency-ring")).toHaveAttribute(
      "pathLength",
      "1",
    );
    expect(screen.getByText("observeer")).toBeInTheDocument();
    expect(screen.getByText("besluit")).toBeInTheDocument();
    expect(screen.getByText("communiceer")).toBeInTheDocument();
    expect(screen.getByText("nabespreking")).toBeInTheDocument();

    const ladder: VisualPlaceholder = {
      id: "viz-standard-ladder",
      kind: "svg_animation",
      title: { nl: "Ladder", en: "Ladder" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "standard-ladder",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    rerender(<ModuleVisual visual={ladder} locale="en" />);
    const ladderSvg = document.querySelector("svg.viz-standard-ladder");
    expect(ladderSvg).toBeTruthy();
    expect(ladderSvg?.querySelector(".viz-ladder-rail")).toHaveAttribute(
      "pathLength",
      "1",
    );
    expect(ladderSvg?.querySelector(".viz-ladder-rung")).toHaveAttribute(
      "pathLength",
      "1",
    );
    expect(screen.getByText("club")).toBeInTheDocument();
    expect(screen.getByText("competition")).toBeInTheDocument();
    expect(screen.getByText("top")).toBeInTheDocument();
    expect(screen.getByText("standard")).toBeInTheDocument();
  });

  it("renders official link slot without inventing KNHB art", () => {
    const visual: VisualPlaceholder = {
      id: "viz-knhb-signals-slot",
      kind: "official_link_slot",
      title: { nl: "Gebaren", en: "Signals" },
      caption: { nl: "Plaatshouder", en: "Placeholder" },
      animation_key: null,
      official_source_url: "https://www.knhb.nl/",
      official_source_name: "KNHB",
      knhb_illustration_placeholder: true,
    };
    render(<ModuleVisual visual={visual} locale="nl" />);
    expect(
      screen.getByRole("link", { name: /KNHB.*opent in nieuw tabblad/i }),
    ).toHaveAttribute("href", "https://www.knhb.nl/");
    expect(screen.getByText(/KNHB-illustratie\/interpretatie: plaatshouder/i)).toBeInTheDocument();
  });

  it("renders interpretation-layer animations", () => {
    const stack: VisualPlaceholder = {
      id: "viz-source-stack",
      kind: "svg_animation",
      title: { nl: "Stapel", en: "Stack" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "source-stack",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    const { rerender } = render(<ModuleVisual visual={stack} locale="en" />);
    expect(document.querySelector("svg.viz-source-stack")).toBeTruthy();
    expect(screen.getByText("FIH")).toBeInTheDocument();
    expect(screen.getByText("KNHB")).toBeInTheDocument();
    expect(screen.getByText("club")).toBeInTheDocument();

    const slot: VisualPlaceholder = {
      id: "viz-translation-slot",
      kind: "svg_animation",
      title: { nl: "Slot", en: "Slot" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "translation-slot",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    rerender(<ModuleVisual visual={slot} locale="nl" />);
    expect(document.querySelector("svg.viz-translation-slot")).toBeTruthy();
    expect(screen.getByText("NL")).toBeInTheDocument();
    expect(screen.getByText("EN-slot")).toBeInTheDocument();

    const chain: VisualPlaceholder = {
      id: "viz-attribution-chain",
      kind: "svg_animation",
      title: { nl: "Keten", en: "Chain" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "attribution-chain",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    rerender(<ModuleVisual visual={chain} locale="en" />);
    expect(document.querySelector("svg.viz-attribution-chain")).toBeTruthy();
    expect(screen.getByText("link")).toBeInTheDocument();
    expect(screen.getByText("source")).toBeInTheDocument();
    expect(screen.getByText("placeholder")).toBeInTheDocument();
  });

  it("renders capstone-weave SVG with domain labels", () => {
    const visual: VisualPlaceholder = {
      id: "viz-capstone-weave",
      kind: "svg_animation",
      title: { nl: "Weefsel", en: "Weave" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "capstone-weave",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    render(<ModuleVisual visual={visual} locale="en" />);
    expect(document.querySelector("svg.viz-capstone-weave")).toBeTruthy();
    expect(screen.getByText("field")).toBeInTheDocument();
    expect(screen.getByText("indoor")).toBeInTheDocument();
    expect(screen.getByText("pathway")).toBeInTheDocument();
    expect(screen.getByText("interpretation")).toBeInTheDocument();
  });

  it("renders enriched scenario SVGs for field, indoor, and pathway", () => {
    const attack: VisualPlaceholder = {
      id: "viz-field-attack",
      kind: "svg_animation",
      title: { nl: "Aanval", en: "Attack" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "field-attack",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    const { rerender } = render(<ModuleVisual visual={attack} locale="en" />);
    expect(document.querySelector("svg.viz-field-attack")).toBeTruthy();
    expect(screen.getByText("attack")).toBeInTheDocument();
    expect(screen.getByText("danger")).toBeInTheDocument();

    const rebound: VisualPlaceholder = {
      id: "viz-indoor-rebound",
      kind: "svg_animation",
      title: { nl: "Rebound", en: "Rebound" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "indoor-rebound",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    rerender(<ModuleVisual visual={rebound} locale="nl" />);
    expect(document.querySelector("svg.viz-indoor-rebound")).toBeTruthy();
    expect(screen.getByText("rebound")).toBeInTheDocument();
    expect(screen.getByText("omhoog")).toBeInTheDocument();

    const pressure: VisualPlaceholder = {
      id: "viz-match-pressure",
      kind: "svg_animation",
      title: { nl: "Druk", en: "Pressure" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "match-pressure",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    rerender(<ModuleVisual visual={pressure} locale="en" />);
    expect(document.querySelector("svg.viz-match-pressure")).toBeTruthy();
    expect(screen.getByText("pressure")).toBeInTheDocument();
    expect(screen.getByText("before")).toBeInTheDocument();
  });

  it("renders hard-decision showcase SVGs", () => {
    const frame: VisualPlaceholder = {
      id: "viz-hard-frame",
      kind: "svg_animation",
      title: { nl: "Kader", en: "Frame" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "hard-decision-frame",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    const { rerender } = render(<ModuleVisual visual={frame} locale="en" />);
    expect(document.querySelector("svg.viz-hard-decision-frame")).toBeTruthy();
    expect(document.querySelector(".viz-hard-frame-arc")).toHaveAttribute(
      "pathLength",
      "1",
    );
    expect(screen.getByText("whistle")).toBeInTheDocument();
    expect(screen.getByText("hard read")).toBeInTheDocument();

    const raised: VisualPlaceholder = {
      id: "viz-hard-raised",
      kind: "svg_animation",
      title: { nl: "Omhoog", en: "Raised" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "hard-raised-danger",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    rerender(<ModuleVisual visual={raised} locale="nl" />);
    expect(document.querySelector("svg.viz-hard-raised-danger")).toBeTruthy();
    expect(document.querySelector(".viz-cone")).toHaveAttribute("pathLength", "1");
    expect(document.querySelector(".viz-hard-raised-path")).toHaveAttribute(
      "pathLength",
      "1",
    );
    expect(screen.getByText("veld")).toBeInTheDocument();
    expect(screen.getByText("zaal")).toBeInTheDocument();

    const pressure: VisualPlaceholder = {
      id: "viz-hard-pressure",
      kind: "svg_animation",
      title: { nl: "Druk", en: "Pressure" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "hard-pressure-clear",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    rerender(<ModuleVisual visual={pressure} locale="en" />);
    expect(document.querySelector("svg.viz-hard-pressure-clear")).toBeTruthy();
    expect(document.querySelector(".viz-hard-press-arc")).toHaveAttribute(
      "pathLength",
      "1",
    );
    expect(screen.getByText("possession")).toBeInTheDocument();
    expect(screen.getByText("clear ball")).toBeInTheDocument();

    const contested: VisualPlaceholder = {
      id: "viz-hard-contested",
      kind: "svg_animation",
      title: { nl: "Betwist", en: "Contested" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "hard-contested",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    rerender(<ModuleVisual visual={contested} locale="en" />);
    expect(document.querySelector("svg.viz-hard-contested")).toBeTruthy();
    expect(document.querySelector(".viz-hard-contest-ring")).toHaveAttribute(
      "pathLength",
      "1",
    );
    expect(document.querySelector(".viz-hard-contest-stick-a")).toHaveAttribute(
      "pathLength",
      "1",
    );
    expect(screen.getByText("no bias")).toBeInTheDocument();

    const gk: VisualPlaceholder = {
      id: "viz-hard-gk",
      kind: "svg_animation",
      title: { nl: "Keeper", en: "Keeper" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "hard-gk-dive",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    };
    rerender(<ModuleVisual visual={gk} locale="en" />);
    expect(document.querySelector("svg.viz-hard-gk-dive")).toBeTruthy();
    expect(document.querySelector(".viz-hard-gk-path")).toHaveAttribute(
      "pathLength",
      "1",
    );
    expect(document.querySelector(".viz-pitch-circle")).toHaveAttribute(
      "pathLength",
      "1",
    );
    expect(screen.getByText("keeper")).toBeInTheDocument();
    expect(
      screen.getByText((content) => content.includes("path") && content.includes("timing")),
    ).toBeInTheDocument();
  });

  it("tints QuizVizHook compact visuals by graded outcome", () => {
    const { rerender } = render(
      <QuizVizHook hint="field-attack" locale="en" correct />,
    );
    const ok = document.querySelector(".module-visual.is-ok");
    expect(ok).toBeTruthy();
    expect(ok).toHaveAttribute("data-outcome", "ok");
    expect(document.querySelector("svg.viz-field-attack")).toBeTruthy();

    rerender(<QuizVizHook hint="indoor-rebound" locale="nl" correct={false} />);
    const bad = document.querySelector(".module-visual.is-bad");
    expect(bad).toBeTruthy();
    expect(bad).toHaveAttribute("data-outcome", "bad");
    expect(document.querySelector("svg.viz-indoor-rebound")).toBeTruthy();
  });
});
