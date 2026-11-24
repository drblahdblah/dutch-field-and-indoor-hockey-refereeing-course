import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import type { ModuleStub, Quiz } from "../api/types";
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
  quiz_id: "quiz-intro-umpire-role",
  further_reading: [],
  order: 1,
};

const matchingQuiz: Quiz = {
  id: "quiz-intro-umpire-role",
  title: { nl: "Quiz NL", en: "Quiz EN" },
  questions: [
    {
      id: "q1",
      type: "written",
      prompt: { nl: "Vraag?", en: "Question?" },
      options: null,
    },
  ],
};

const staleQuiz: Quiz = {
  id: "quiz-other",
  title: { nl: "Verkeerde quiz", en: "Wrong quiz" },
  questions: matchingQuiz.questions,
};

describe("ModuleDetail", () => {
  it("renders full module sections and visuals", () => {
    render(
      <ModuleDetail
        module={fullModule}
        quiz={matchingQuiz}
        locale="en"
        accessToken={null}
        hasSession={false}
      />,
    );
    expect(screen.getByRole("heading", { name: "Intro EN" })).toBeInTheDocument();
    expect(screen.getByText("Section one")).toBeInTheDocument();
    expect(screen.getByText("Paragraph EN")).toBeInTheDocument();
    expect(screen.getByText("Triangle")).toBeInTheDocument();
    expect(document.querySelector("svg.viz-svg")).toBeTruthy();
    expect(screen.getByRole("heading", { name: "Quiz EN" })).toBeInTheDocument();
    expect(screen.getByLabelText("Question?")).toBeInTheDocument();
  });

  it("does not render a quiz that belongs to another module", () => {
    render(
      <ModuleDetail
        module={fullModule}
        quiz={staleQuiz}
        locale="nl"
        accessToken={null}
        hasSession={false}
      />,
    );
    expect(screen.queryByText("Verkeerde quiz")).not.toBeInTheDocument();
  });
});
