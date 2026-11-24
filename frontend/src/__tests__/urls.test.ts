import { describe, expect, it } from "vitest";
import { safeHttpUrl } from "../api/urls";

describe("safeHttpUrl", () => {
  it("allows https URLs", () => {
    expect(safeHttpUrl("https://www.fih.hockey/rules")).toMatch(/^https:\/\//);
  });

  it("rejects javascript schemes", () => {
    expect(safeHttpUrl("javascript:alert(1)")).toBeNull();
  });

  it("rejects empty and invalid", () => {
    expect(safeHttpUrl(null)).toBeNull();
    expect(safeHttpUrl("not a url")).toBeNull();
  });
});
