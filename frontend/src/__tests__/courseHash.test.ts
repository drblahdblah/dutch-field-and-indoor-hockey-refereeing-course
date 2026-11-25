import { describe, expect, it } from "vitest";
import {
  courseHashFor,
  isKnownModuleId,
  parseCourseHash,
} from "../nav/courseHash";

describe("courseHash", () => {
  it("parses overview hashes", () => {
    expect(parseCourseHash("")).toEqual({ kind: "overview" });
    expect(parseCourseHash("#")).toEqual({ kind: "overview" });
    expect(parseCourseHash("#/")).toEqual({ kind: "overview" });
    expect(parseCourseHash("#/overview")).toEqual({ kind: "overview" });
  });

  it("parses module hashes and round-trips", () => {
    expect(parseCourseHash("#/modules/field-rules")).toEqual({
      kind: "module",
      moduleId: "field-rules",
    });
    expect(parseCourseHash("#modules/indoor%2Frules")).toEqual({
      kind: "module",
      moduleId: "indoor/rules",
    });
    expect(
      courseHashFor({ kind: "module", moduleId: "capstone" }),
    ).toBe("#/modules/capstone");
    expect(courseHashFor({ kind: "overview" })).toBe("#/");
  });

  it("falls back to overview for unknown paths", () => {
    expect(parseCourseHash("#/nope")).toEqual({ kind: "overview" });
    expect(parseCourseHash("#/modules/")).toEqual({ kind: "overview" });
  });

  it("checks known module ids", () => {
    expect(isKnownModuleId("a", ["a", "b"])).toBe(true);
    expect(isKnownModuleId("c", new Set(["a"]))).toBe(false);
  });
});
