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
    quiz_id: "quiz-intro-a",
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

const practiceScenarios = [
  {
    id: "practice-field-a",
    kind: "field" as const,
    title: { nl: "Veldscenario NL", en: "Field scenario EN" },
    situation: { nl: "Situatie A", en: "Situation A" },
    focus: { nl: "Focus A", en: "Focus A" },
    order: 1,
    visual_key: "practice-circle-entry",
    quiz: {
      id: "quiz-practice-field-a",
      title: { nl: "Quiz A", en: "Quiz A" },
      questions: [],
    },
  },
  {
    id: "practice-indoor-b",
    kind: "indoor" as const,
    title: { nl: "Zaalscenario NL", en: "Indoor scenario EN" },
    situation: { nl: "Situatie B", en: "Situation B" },
    focus: { nl: "Focus B", en: "Focus B" },
    order: 2,
    visual_key: "practice-board-lift",
    quiz: {
      id: "quiz-practice-indoor-b",
      title: { nl: "Quiz B", en: "Quiz B" },
      questions: [],
    },
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
    practice: vi.fn(async () => ({
      id: "practice",
      title: { nl: "Oefenbank", en: "Practice bank" },
      description: { nl: "Oefen", en: "Practice" },
      scenarios: practiceScenarios,
    })),
    practiceScenario: vi.fn(),
    getProgress: vi.fn(async () => ({ progress: [] })),
    quiz: vi.fn(async () => ({
      id: "quiz-intro-a",
      title: { nl: "Quiz A NL", en: "Quiz A EN" },
      questions: [
        {
          id: "q1",
          type: "written" as const,
          prompt: { nl: "Vraag A?", en: "Question A?" },
          options: null,
        },
      ],
    })),
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
    expect(
      screen.getByRole("navigation", { name: /Modulenavigatie/i }),
    ).toBeInTheDocument();
    expect(
      screen.getByRole("button", { name: /Terug naar cursusoverzicht/i }),
    ).toBeInTheDocument();
    expect(screen.getByText(/Module 1 van 2/i)).toBeInTheDocument();

    await waitFor(() => {
      expect(document.activeElement?.id).toBe("module-heading");
    });

    fireEvent.click(
      screen.getByRole("button", { name: /Terug naar cursusoverzicht/i }),
    );

    await waitFor(() => {
      expect(
        screen.getByRole("navigation", { name: /Cursusmodules/i }),
      ).toBeInTheDocument();
    });
    expect(screen.queryByRole("heading", { name: /Intro NL/i })).not.toBeInTheDocument();
    expect(window.location.hash).toBe("#/");

    await waitFor(() => {
      expect(document.activeElement?.id).toBe("course-progress-heading");
    });
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
    expect(
      screen.getByRole("navigation", { name: /Modulenavigatie/i }),
    ).toBeInTheDocument();
  });

  it("replaces an unknown module hash with the overview", async () => {
    window.location.hash = "#/modules/does-not-exist";
    render(<App />);

    await waitFor(() => {
      expect(
        screen.getByRole("navigation", { name: /Cursusmodules/i }),
      ).toBeInTheDocument();
    });
    expect(window.location.hash).toBe("#/");
  });

  it("advances to the next module from the module footer", async () => {
    window.location.hash = "#/modules/mod-a";
    render(<App />);

    await waitFor(() => {
      expect(screen.getByRole("heading", { name: /Intro NL/i })).toBeInTheDocument();
    });

    fireEvent.click(
      screen.getByRole("button", { name: /Volgende module:.*Veld NL/i }),
    );

    await waitFor(() => {
      expect(screen.getByRole("heading", { name: /Veld NL/i })).toBeInTheDocument();
    });
    expect(window.location.hash).toBe("#/modules/mod-b");
  });

  it("opens the module quiz on a separate route after the lesson CTA", async () => {
    window.location.hash = "#/modules/mod-a";
    render(<App />);

    await waitFor(() => {
      expect(screen.getByRole("heading", { name: /Intro NL/i })).toBeInTheDocument();
    });
    expect(screen.queryByRole("heading", { name: /Quiz A NL/i })).not.toBeInTheDocument();

    fireEvent.click(
      screen.getByRole("button", { name: /Ga naar de modulequiz/i }),
    );

    await waitFor(() => {
      expect(screen.getByRole("heading", { name: /Quiz A NL/i })).toBeInTheDocument();
    });
    expect(window.location.hash).toBe("#/modules/mod-a/quiz");
    expect(screen.queryByRole("heading", { name: /Intro NL/i })).not.toBeInTheDocument();
    expect(screen.getByLabelText(/Vraag A\?/i)).toBeInTheDocument();
    expect(
      screen.getByRole("navigation", { name: /Quiznavigatie/i }),
    ).toBeInTheDocument();

    await waitFor(() => {
      expect(document.activeElement?.id).toBe("quiz-heading");
    });

    fireEvent.click(
      screen.getAllByRole("button", { name: /Terug naar de lesstof/i })[0],
    );

    await waitFor(() => {
      expect(screen.getByRole("heading", { name: /Intro NL/i })).toBeInTheDocument();
    });
    expect(window.location.hash).toBe("#/modules/mod-a");
    expect(screen.queryByRole("heading", { name: /Quiz A NL/i })).not.toBeInTheDocument();
    await waitFor(() => {
      expect(document.activeElement?.id).toBe("module-heading");
    });
  });

  it("opens the practice bank from the overview and a scenario detail", async () => {
    render(<App />);

    await waitFor(() => {
      expect(screen.getByText(/Beschrijving/i)).toBeInTheDocument();
    });

    fireEvent.click(
      screen.getByRole("button", { name: /Open oefenscenario's/i }),
    );

    await waitFor(() => {
      expect(
        screen.getByRole("heading", { name: /Oefenscenario's/i }),
      ).toBeInTheDocument();
    });
    expect(window.location.hash).toBe("#/practice");
    expect(
      screen.getByRole("heading", { name: /Veldscenario NL/i }),
    ).toBeInTheDocument();

    fireEvent.click(
      screen.getAllByRole("button", { name: /Open scenario/i })[0],
    );

    await waitFor(() => {
      expect(
        screen.getByRole("heading", { name: /Veldscenario NL/i }),
      ).toBeInTheDocument();
    });
    expect(window.location.hash).toBe("#/practice/practice-field-a");
    expect(screen.getByText(/Situatie A/i)).toBeInTheDocument();
    expect(screen.getByText(/Scenario 1 van 2/i)).toBeInTheDocument();

    fireEvent.click(
      screen.getAllByRole("button", { name: /Terug naar oefenscenario's/i })[0],
    );

    await waitFor(() => {
      expect(
        screen.getByRole("heading", { name: /Oefenscenario's/i }),
      ).toBeInTheDocument();
    });
    expect(window.location.hash).toBe("#/practice");
  });

  it("deep-links the module quiz hash", async () => {
    window.location.hash = "#/modules/mod-a/quiz";
    render(<App />);

    await waitFor(() => {
      expect(screen.getByRole("heading", { name: /Quiz A NL/i })).toBeInTheDocument();
    });
    expect(window.location.hash).toBe("#/modules/mod-a/quiz");
  });

  it("replaces a quiz hash for a module without a quiz with the lesson", async () => {
    window.location.hash = "#/modules/mod-b/quiz";
    render(<App />);

    await waitFor(() => {
      expect(screen.getByRole("heading", { name: /Veld NL/i })).toBeInTheDocument();
    });
    expect(window.location.hash).toBe("#/modules/mod-b");
    expect(screen.queryByRole("heading", { name: /Quiz/i })).not.toBeInTheDocument();
  });

  it("opens a practice scenario from a deep-link hash", async () => {
    window.location.hash = "#/practice/practice-indoor-b";
    render(<App />);

    await waitFor(() => {
      expect(
        screen.getByRole("heading", { name: /Zaalscenario NL/i }),
      ).toBeInTheDocument();
    });
    expect(screen.getByText(/Situatie B/i)).toBeInTheDocument();
  });

  it("replaces an unknown practice scenario hash with the practice bank", async () => {
    window.location.hash = "#/practice/does-not-exist";
    render(<App />);

    await waitFor(() => {
      expect(
        screen.getByRole("heading", { name: /Oefenscenario's/i }),
      ).toBeInTheDocument();
    });
    expect(window.location.hash).toBe("#/practice");
  });
});
