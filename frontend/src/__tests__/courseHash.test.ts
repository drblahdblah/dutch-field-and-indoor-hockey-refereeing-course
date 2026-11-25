import { describe, expect, it } from "vitest";
import {
  courseHashFor,
  isKnownModuleId,
  isKnownScenarioId,
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

  it("parses module quiz hashes and prefers /quiz over the lesson path", () => {
    expect(parseCourseHash("#/modules/mod-intro-role/quiz")).toEqual({
      kind: "module-quiz",
      moduleId: "mod-intro-role",
    });
    expect(parseCourseHash("#modules/field%2Frules/quiz")).toEqual({
      kind: "module-quiz",
      moduleId: "field/rules",
    });
    expect(
      courseHashFor({ kind: "module-quiz", moduleId: "mod-intro-role" }),
    ).toBe("#/modules/mod-intro-role/quiz");
  });

  it("parses practice bank and scenario hashes", () => {
    expect(parseCourseHash("#/practice")).toEqual({ kind: "practice" });
    expect(parseCourseHash("#practice")).toEqual({ kind: "practice" });
    expect(parseCourseHash("#/practice/field-raised")).toEqual({
      kind: "practice-scenario",
      scenarioId: "field-raised",
    });
    expect(
      courseHashFor({
        kind: "practice-scenario",
        scenarioId: "practice-field-raised-circle",
      }),
    ).toBe("#/practice/practice-field-raised-circle");
    expect(courseHashFor({ kind: "practice" })).toBe("#/practice");
  });

  it("falls back to overview for unknown paths", () => {
    expect(parseCourseHash("#/nope")).toEqual({ kind: "overview" });
    expect(parseCourseHash("#/modules/")).toEqual({ kind: "overview" });
  });

  it("checks known module and scenario ids", () => {
    expect(isKnownModuleId("a", ["a", "b"])).toBe(true);
    expect(isKnownModuleId("c", new Set(["a"]))).toBe(false);
    expect(isKnownScenarioId("s1", ["s1"])).toBe(true);
    expect(isKnownScenarioId("s2", new Set(["s1"]))).toBe(false);
  });
});
