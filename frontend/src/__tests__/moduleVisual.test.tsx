import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import type { VisualPlaceholder } from "../api/types";
import {
  ModuleVisual,
  animationKeyFromHint,
} from "../components/ModuleVisual";

describe("animationKeyFromHint", () => {
  it("maps known quiz hints to animation keys with exact match only", () => {
    expect(animationKeyFromHint("safety-triangle")).toBe("safety-triangle");
    expect(animationKeyFromHint("scan-cycle")).toBe("scan-cycle");
    expect(animationKeyFromHint("pitch-zones")).toBe("pitch-zones");
    expect(animationKeyFromHint("danger-cone")).toBe("danger-cone");
    expect(animationKeyFromHint("restart-bubble")).toBe("restart-bubble");
    expect(animationKeyFromHint("court-boards")).toBe("court-boards");
    expect(animationKeyFromHint("lift-limit")).toBe("lift-limit");
    expect(animationKeyFromHint("board-play")).toBe("board-play");
    expect(animationKeyFromHint("match-cadence")).toBe("match-cadence");
    expect(animationKeyFromHint("partner-handoff")).toBe("partner-handoff");
    expect(animationKeyFromHint("consistency-loop")).toBe("consistency-loop");
    expect(animationKeyFromHint(" Danger-Cone ")).toBe("danger-cone");
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
    expect(screen.getByText("bubbel")).toBeInTheDocument();
    expect(screen.getByText("herstart")).toBeInTheDocument();
  });

  it("renders indoor court-boards, lift-limit, and board-play SVGs", () => {
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
    expect(screen.getByText("banden")).toBeInTheDocument();
    expect(screen.getByText("rebound")).toBeInTheDocument();
    expect(screen.getByText("herstel")).toBeInTheDocument();
  });

  it("renders pathway match-cadence, partner-handoff, and consistency-loop SVGs", () => {
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
    expect(screen.getByText("observeer")).toBeInTheDocument();
    expect(screen.getByText("besluit")).toBeInTheDocument();
    expect(screen.getByText("communiceer")).toBeInTheDocument();
    expect(screen.getByText("review")).toBeInTheDocument();
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
    expect(screen.getByRole("link", { name: "KNHB" })).toHaveAttribute(
      "href",
      "https://www.knhb.nl/",
    );
    expect(screen.getByText(/KNHB-illustratie\/interpretatie: plaatshouder/i)).toBeInTheDocument();
  });
});
