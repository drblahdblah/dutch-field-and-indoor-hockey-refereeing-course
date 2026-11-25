import { fireEvent, render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import type { ModuleStub } from "../api/types";
import { ModuleDetail } from "../components/ModuleDetail";

const fullModule: ModuleStub = {
  id: "mod-intro-role",
  kind: "shared",
  title: { nl: "Intro NL", en: "Intro EN" },
  summary: { nl: "Samenvatting", en: "Summary" },
  learning_objectives: [{ nl: "Doel", en: "Goal" }],
  instruction_outline: [{ nl: "Outline", en: "Outline" }],
  content_status: "full",
  sections: [
    {
      id: "sec-one",
      title: { nl: "Sectie één", en: "Section one" },
      paragraphs: [{ nl: "Paragraaf NL", en: "Paragraph EN" }],
      visual_id: "viz-safety-triangle",
    },
  ],
  visuals: [
    {
      id: "viz-safety-triangle",
      kind: "svg_animation",
      title: { nl: "Driehoek", en: "Triangle" },
      caption: { nl: "Origineel", en: "Original" },
      animation_key: "safety-triangle",
      official_source_url: null,
      official_source_name: null,
      knhb_illustration_placeholder: false,
    },
  ],
  interpretation_references: [],
  quiz_id: "quiz-intro-umpire-role",
  further_reading: [],
  order: 1,
};

describe("ModuleDetail", () => {
  it("renders full module sections and visuals without an inline quiz", () => {
    const onOpenQuiz = vi.fn();
    render(
      <ModuleDetail module={fullModule} locale="en" onOpenQuiz={onOpenQuiz} />,
    );
    expect(screen.getByRole("heading", { name: "Intro EN" })).toBeInTheDocument();
    expect(screen.getByText("Section one")).toBeInTheDocument();
    expect(screen.getByText("Paragraph EN")).toBeInTheDocument();
    expect(screen.getByText("Triangle")).toBeInTheDocument();
    expect(document.querySelector("svg.viz-svg")).toBeTruthy();
    expect(screen.queryByRole("heading", { name: /Quiz/i })).not.toBeInTheDocument();
    fireEvent.click(
      screen.getByRole("button", { name: /Go to the module quiz/i }),
    );
    expect(onOpenQuiz).toHaveBeenCalledTimes(1);
  });

  it("hides the quiz CTA when the module has no quiz", () => {
    render(
      <ModuleDetail
        module={{ ...fullModule, quiz_id: null }}
        locale="nl"
      />,
    );
    expect(
      screen.queryByRole("button", { name: /Ga naar de modulequiz/i }),
    ).not.toBeInTheDocument();
  });

  it("renders interpretation references with translation slots", () => {
    const withRefs: ModuleStub = {
      ...fullModule,
      interpretation_references: [
        {
          id: "interp-demo",
          topic: { nl: "Topic NL", en: "Topic EN" },
          scope: "shared",
          summary: {
            nl: "Samenvatting NL",
            en: "[EN translation slot] TBD",
          },
          translation_needed: true,
          official_source_url: "https://www.knhb.nl/",
          official_source_name: "KNHB",
          knhb_illustration_placeholder: true,
          attribution: {
            source_name: "KNHB",
            source_url: "https://www.knhb.nl/",
            note: { nl: "Attributie NL", en: "Attribution EN" },
            knhb_illustration_placeholder: true,
            translation_needed: true,
          },
          visual_id: "viz-safety-triangle",
        },
      ],
    };
    render(<ModuleDetail module={withRefs} locale="en" />);
    expect(
      screen.getByRole("heading", { name: "Interpretation references" }),
    ).toBeInTheDocument();
    expect(screen.getByRole("heading", { name: "Topic EN" })).toBeInTheDocument();
    expect(screen.getByText("[EN translation slot] TBD")).toBeInTheDocument();
    // knhb placeholder covers EN-TBD; translationNeeded flag is not duplicated.
    expect(
      screen.getByText(/KNHB illustration\/interpretation: placeholder/i),
    ).toBeInTheDocument();
    expect(
      screen.queryByText(/EN translation slot — no authorized legal translation/i),
    ).not.toBeInTheDocument();
    expect(
      screen.getByRole("link", { name: /KNHB.*opens in new tab/i }),
    ).toHaveAttribute("href", "https://www.knhb.nl/");
    const card = document.querySelector('[data-interp-id="interp-demo"]');
    expect(card).toBeTruthy();
    expect(card?.querySelector("svg.viz-svg")).toBeTruthy();
    expect(card?.querySelector(".module-visual.is-compact")).toBeTruthy();
  });

  it("drops unsafe interpretation source URLs", () => {
    const unsafe: ModuleStub = {
      ...fullModule,
      interpretation_references: [
        {
          id: "interp-unsafe",
          topic: { nl: "Onveilig", en: "Unsafe" },
          scope: "field",
          summary: { nl: "NL", en: "[EN translation slot] TBD" },
          translation_needed: true,
          official_source_url: "javascript:alert(1)",
          official_source_name: "BadSource",
          knhb_illustration_placeholder: false,
          attribution: {
            source_name: "BadSource",
            source_url: "javascript:alert(1)",
            note: { nl: "n", en: "n" },
            knhb_illustration_placeholder: false,
            translation_needed: true,
          },
          visual_id: null,
        },
      ],
    };
    render(<ModuleDetail module={unsafe} locale="en" />);
    expect(screen.queryByRole("link", { name: "BadSource" })).not.toBeInTheDocument();
    expect(screen.getByText("BadSource")).toBeInTheDocument();
    expect(
      screen.getByText(/EN translation slot — no authorized legal translation/i),
    ).toBeInTheDocument();
  });
});
