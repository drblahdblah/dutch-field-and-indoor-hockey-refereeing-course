import { fireEvent, render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import type { ModuleStub, ProgressOut } from "../api/types";
import { CourseProgressOverview } from "../components/CourseProgressOverview";

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

describe("CourseProgressOverview", () => {
  it("shows localized progress overview and next-up when session is active", () => {
    const onSelect = vi.fn();
    const progress: ProgressOut[] = [
      {
        module_id: "mod-a",
        status: "completed",
        quiz_score: 4,
        quiz_total: 4,
        last_question_id: null,
        completed_at: "2026-01-01T00:00:00Z",
        updated_at: "2026-01-01T00:00:00Z",
      },
    ];

    render(
      <CourseProgressOverview
        modules={modules}
        progress={progress}
        selectedId="mod-b"
        locale="en"
        hasSession
        onSelectModule={onSelect}
      />,
    );

    expect(
      screen.getByRole("heading", { name: /Course path & progress/i }),
    ).toBeInTheDocument();
    expect(screen.getByText(/1 of 2 modules completed/i)).toBeInTheDocument();
    expect(screen.getByRole("progressbar")).toHaveAttribute("aria-valuenow", "50");
    expect(
      screen.getByText((_, el) => el?.textContent === "Progress: completed"),
    ).toBeInTheDocument();
    expect(
      screen.getByText((_, el) => el?.textContent === "Score: 4/4"),
    ).toBeInTheDocument();
    expect(screen.getAllByText(/Next up/i).length).toBeGreaterThanOrEqual(1);

    fireEvent.click(screen.getByRole("button", { name: /^Field EN$/i }));
    expect(onSelect).toHaveBeenCalledWith("mod-b");
  });

  it("hints to start a session when none exists", () => {
    render(
      <CourseProgressOverview
        modules={modules}
        progress={[]}
        selectedId={null}
        locale="nl"
        hasSession={false}
        onSelectModule={() => undefined}
      />,
    );
    expect(
      screen.getByText(/Start of hervat een sessie om voortgang bij te houden/i),
    ).toBeInTheDocument();
    expect(screen.getAllByText(/Nog niet bijgehouden/i).length).toBe(2);
    expect(screen.queryByText(/niet gestart/i)).not.toBeInTheDocument();
    expect(screen.getByRole("progressbar")).toHaveAttribute("aria-valuenow", "0");
  });

  it("orders modules by order and hides next-up when all complete", () => {
    const shuffled: ModuleStub[] = [modules[1], modules[0]];
    const progress: ProgressOut[] = shuffled.map((m) => ({
      module_id: m.id,
      status: "completed",
      quiz_score: 1,
      quiz_total: 1,
      last_question_id: null,
      completed_at: "2026-01-01T00:00:00Z",
      updated_at: "2026-01-01T00:00:00Z",
    }));

    render(
      <CourseProgressOverview
        modules={shuffled}
        progress={progress}
        selectedId="mod-a"
        locale="en"
        hasSession
        onSelectModule={() => undefined}
      />,
    );

    const titles = screen.getAllByRole("button").map((btn) => btn.textContent);
    const introIdx = titles.findIndex((t) => t?.includes("Intro EN"));
    const fieldIdx = titles.findIndex((t) => t?.includes("Field EN"));
    expect(introIdx).toBeGreaterThanOrEqual(0);
    expect(fieldIdx).toBeGreaterThan(introIdx);
    expect(screen.queryByText(/^Next up$/i)).not.toBeInTheDocument();
    expect(screen.getByText(/2 of 2 modules completed/i)).toBeInTheDocument();
  });
});
