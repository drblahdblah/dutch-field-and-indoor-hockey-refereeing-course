import { render, screen, waitFor } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";
import App from "../App";

vi.mock("../api/client", () => ({
  api: {
    course: vi.fn(async () => ({
      id: "course",
      title: { nl: "Cursus", en: "Course" },
      description: { nl: "Beschrijving", en: "Description" },
      modules: [],
      attributions: [],
    })),
    getProgress: vi.fn(async () => ({ progress: [] })),
    quiz: vi.fn(),
    createSession: vi.fn(),
    updateProgress: vi.fn(),
    revokeSession: vi.fn(),
    submitQuiz: vi.fn(),
  },
  clearAccessToken: vi.fn(),
  getStoredAccessToken: vi.fn(() => null),
  hasStoredSessionFlag: vi.fn(() => false),
  storeAccessToken: vi.fn(),
}));

describe("App a11y shell", () => {
  beforeEach(() => {
    document.documentElement.lang = "en";
  });

  it("provides skip link, banner, and main landmarks with language labels", async () => {
    render(<App />);

    expect(
      screen.getByRole("link", { name: /Ga naar hoofdinhoud/i }),
    ).toHaveAttribute("href", "#main-content");
    expect(screen.getByRole("banner")).toBeInTheDocument();
    expect(screen.getByRole("main")).toHaveAttribute("id", "main-content");

    await waitFor(() => {
      expect(screen.getByText(/Beschrijving/i)).toBeInTheDocument();
    });

    expect(screen.getByRole("button", { name: /Nederlands/i })).toHaveAttribute(
      "aria-pressed",
      "true",
    );
    expect(screen.getByRole("button", { name: /Engels/i })).toHaveAttribute(
      "aria-pressed",
      "false",
    );
  });
});
