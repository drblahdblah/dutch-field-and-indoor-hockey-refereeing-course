import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { KNOWN_ANIMATION_KEYS } from "../components/visuals/animationKeys";
import { SVG_LABELS } from "../components/visuals/svgLabels";
import {
  QUIZ_VIZ_TITLES,
  t,
  ui,
  uiT,
  type Localized,
} from "../i18n/messages";

function BrandSmoke({ locale }: { locale: "nl" | "en" }) {
  return (
    <div>
      <h1>{uiT("brand", locale)}</h1>
      <p>{t({ nl: "Hallo", en: "Hello" }, locale)}</p>
    </div>
  );
}

function assertBilingual(entry: Localized, path: string) {
  expect(entry.nl.trim(), `${path}.nl`).not.toBe("");
  expect(entry.en.trim(), `${path}.en`).not.toBe("");
}

describe("i18n smoke", () => {
  it("renders Dutch brand and copy", () => {
    render(<BrandSmoke locale="nl" />);
    expect(screen.getByRole("heading", { name: /Hockey Scheidsrechterscursus/i })).toBeInTheDocument();
    expect(screen.getByText("Hallo")).toBeInTheDocument();
  });

  it("renders English brand and copy", () => {
    render(<BrandSmoke locale="en" />);
    expect(screen.getByRole("heading", { name: /Hockey Umpiring Course/i })).toBeInTheDocument();
    expect(screen.getByText("Hello")).toBeInTheDocument();
  });

  it("covers every UI chrome string in NL and EN", () => {
    for (const key of Object.keys(ui) as (keyof typeof ui)[]) {
      assertBilingual(ui[key], `ui.${key}`);
    }
  });

  it("covers every SVG label in NL and EN", () => {
    for (const key of Object.keys(SVG_LABELS) as (keyof typeof SVG_LABELS)[]) {
      assertBilingual(SVG_LABELS[key], `SVG_LABELS.${key}`);
    }
  });

  it("covers quiz visualization titles for every animation key", () => {
    for (const key of KNOWN_ANIMATION_KEYS) {
      expect(QUIZ_VIZ_TITLES[key], `QUIZ_VIZ_TITLES.${key}`).toBeDefined();
      assertBilingual(QUIZ_VIZ_TITLES[key], `QUIZ_VIZ_TITLES.${key}`);
    }
  });
});
