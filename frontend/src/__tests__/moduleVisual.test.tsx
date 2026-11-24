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
    expect(animationKeyFromHint("timeline: raise → proximity")).toBeNull();
    expect(animationKeyFromHint("prefix-safety-triangle")).toBeNull();
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
