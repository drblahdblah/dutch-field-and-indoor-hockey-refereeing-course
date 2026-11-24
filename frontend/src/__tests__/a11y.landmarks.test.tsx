import { fireEvent, render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import type { ModuleStub, ProgressOut } from "../api/types";
import { CourseProgressOverview } from "../components/CourseProgressOverview";
import { QuizVizHook } from "../components/ModuleVisual";
import { uiT } from "../i18n/messages";

const modules: ModuleStub[] = [
  {
    id: "mod-a",
    kind: "shared",
    title: { nl: "Intro NL", en: "Intro EN" },
    summary: { nl: "Samenvatting A", en: "Summary A" },
    learning_objectives: [],
    instruction_outline: [],
    content_status: "full",
    sections: [],
    visuals: [],
    interpretation_references: [],
    quiz_id: "quiz-a",
    further_reading: [],
    order: 1,
  },
  {
    id: "mod-b",
    kind: "field",
    title: { nl: "Veld NL", en: "Field EN" },
    summary: { nl: "Samenvatting B", en: "Summary B" },
    learning_objectives: [],
    instruction_outline: [],
    content_status: "full",
    sections: [],
    visuals: [],
    interpretation_references: [],
    quiz_id: "quiz-b",
    further_reading: [],
    order: 2,
  },
];

describe("a11y landmarks and labels", () => {
  it("exposes a course modules navigation landmark", () => {
    render(
      <CourseProgressOverview
        modules={modules}
        progress={[]}
        selectedId="mod-a"
        locale="en"
        hasSession={false}
        onSelectModule={() => undefined}
      />,
    );

    expect(
      screen.getByRole("navigation", { name: /Course modules/i }),
    ).toBeInTheDocument();
    expect(
      screen.getByRole("button", { name: /Intro EN/i }),
    ).toHaveAttribute("aria-current", "page");
  });

  it("labels NL pathway navigation and keeps next-up assistive prefix", () => {
    const progress: ProgressOut[] = [
      {
        module_id: "mod-a",
        status: "completed",
        quiz_score: 1,
        quiz_total: 1,
        last_question_id: null,
        completed_at: "2026-01-01T00:00:00Z",
        updated_at: "2026-01-01T00:00:00Z",
      },
    ];
    const onSelect = vi.fn();

    render(
      <CourseProgressOverview
        modules={modules}
        progress={progress}
        selectedId={null}
        locale="nl"
        hasSession
        onSelectModule={onSelect}
      />,
    );

    expect(
      screen.getByRole("navigation", { name: /Cursusmodules/i }),
    ).toBeInTheDocument();
    fireEvent.click(
      screen.getByRole("button", { name: /Ga naar volgende module:.*Veld NL/i }),
    );
    expect(onSelect).toHaveBeenCalledWith("mod-b");
  });

  it("names quiz visualization hooks for assistive tech", () => {
    render(<QuizVizHook hint="match-pressure" locale="en" correct />);
    expect(
      screen.getByRole("group", { name: /Visualization: match pressure/i }),
    ).toBeInTheDocument();
  });

  it("localizes new chrome strings for skip, languages, and submitting", () => {
    expect(uiT("skipToContent", "nl")).toMatch(/hoofdinhoud/i);
    expect(uiT("skipToContent", "en")).toMatch(/main content/i);
    expect(uiT("langNl", "nl")).toBe("Nederlands");
    expect(uiT("langEn", "en")).toBe("English");
    expect(uiT("submitting", "en")).toMatch(/Submitting/i);
    expect(uiT("opensInNewTab", "nl")).toMatch(/nieuw tabblad/i);
  });
});
