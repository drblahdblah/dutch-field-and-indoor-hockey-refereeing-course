import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";
import App from "../App";

const modules = [
  {
    id: "mod-a",
    kind: "shared" as const,
    title: { nl: "Intro NL", en: "Intro EN" },
    summary: { nl: "Sam A", en: "Sum A" },
    learning_objectives: [{ nl: "Doel", en: "Goal" }],
    instruction_outline: [],
    content_status: "full" as const,
    sections: [],
    visuals: [],
    interpretation_references: [],
    quiz_id: null,
    further_reading: [],
    order: 1,
  },
  {
    id: "mod-b",
    kind: "field" as const,
    title: { nl: "Veld NL", en: "Field EN" },
    summary: { nl: "Sam B", en: "Sum B" },
    learning_objectives: [{ nl: "Doel B", en: "Goal B" }],
    instruction_outline: [],
    content_status: "full" as const,
    sections: [],
    visuals: [],
    interpretation_references: [],
    quiz_id: null,
    further_reading: [],
    order: 2,
  },
];

vi.mock("../api/client", () => ({
  api: {
    course: vi.fn(async () => ({
      id: "course",
      title: { nl: "Cursus", en: "Course" },
      description: { nl: "Beschrijving", en: "Description" },
      modules,
      attributions: [],
    })),
    getProgress: vi.fn(async () => ({ progress: [] })),
    quiz: vi.fn(),
    createSession: vi.fn(async () => ({
      access_token: null,
      session_id: "s1",
    })),
    updateProgress: vi.fn(async () => ({
      progress: [
        {
          module_id: "mod-a",
          status: "in_progress",
          quiz_score: null,
          quiz_total: null,
          last_question_id: null,
          completed_at: null,
          updated_at: "2026-01-01T00:00:00Z",
        },
      ],
    })),
    revokeSession: vi.fn(),
    submitQuiz: vi.fn(),
  },
  clearAccessToken: vi.fn(),
  getStoredAccessToken: vi.fn(() => null),
  hasStoredSessionFlag: vi.fn(() => false),
  storeAccessToken: vi.fn(),
}));

describe("App course / module navigation", () => {
  beforeEach(() => {
    window.location.hash = "";
    document.documentElement.lang = "nl";
  });

  it("keeps modules off the course overview and opens a dedicated module view", async () => {
    render(<App />);

    await waitFor(() => {
      expect(screen.getByText(/Beschrijving/i)).toBeInTheDocument();
    });

    expect(
      screen.getByRole("navigation", { name: /Cursusmodules/i }),
    ).toBeInTheDocument();
    expect(screen.queryByRole("heading", { name: /Intro NL/i })).not.toBeInTheDocument();

    fireEvent.click(
      screen.getByRole("button", { name: /Ga naar volgende module:.*Intro NL/i }),
    );

    await waitFor(() => {
      expect(screen.getByRole("heading", { name: /Intro NL/i })).toBeInTheDocument();
    });

    expect(window.location.hash).toBe("#/modules/mod-a");
    expect(
      screen.queryByRole("navigation", { name: /Cursusmodules/i }),
    ).not.toBeInTheDocument();
    const backButtons = screen.getAllByRole("button", {
      name: /Terug naar cursusoverzicht/i,
    });
    expect(backButtons.length).toBeGreaterThanOrEqual(1);
    expect(screen.getByText(/Module 1 van 2/i)).toBeInTheDocument();

    fireEvent.click(backButtons[0]!);

    await waitFor(() => {
      expect(
        screen.getByRole("navigation", { name: /Cursusmodules/i }),
      ).toBeInTheDocument();
    });
    expect(screen.queryByRole("heading", { name: /Intro NL/i })).not.toBeInTheDocument();
    expect(window.location.hash).toBe("#/");
  });

  it("opens a module from a deep-link hash", async () => {
    window.location.hash = "#/modules/mod-b";
    render(<App />);

    await waitFor(() => {
      expect(screen.getByRole("heading", { name: /Veld NL/i })).toBeInTheDocument();
    });
    expect(
      screen.queryByRole("navigation", { name: /Cursusmodules/i }),
    ).not.toBeInTheDocument();
  });
});
