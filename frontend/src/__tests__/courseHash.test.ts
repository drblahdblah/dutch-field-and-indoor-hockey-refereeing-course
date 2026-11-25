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

  it("falls back to overview for unknown paths", () => {
    expect(parseCourseHash("#/nope")).toEqual({ kind: "overview" });
    expect(parseCourseHash("#/modules/")).toEqual({ kind: "overview" });
  });

  it("checks known module ids", () => {
    expect(isKnownModuleId("a", ["a", "b"])).toBe(true);
    expect(isKnownModuleId("c", new Set(["a"]))).toBe(false);
  });
});
