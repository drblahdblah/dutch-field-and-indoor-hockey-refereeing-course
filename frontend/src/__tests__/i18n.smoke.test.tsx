import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { t, uiT } from "../i18n/messages";

function BrandSmoke({ locale }: { locale: "nl" | "en" }) {
  return (
    <div>
      <h1>{uiT("brand", locale)}</h1>
      <p>{t({ nl: "Hallo", en: "Hello" }, locale)}</p>
    </div>
  );
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
});
