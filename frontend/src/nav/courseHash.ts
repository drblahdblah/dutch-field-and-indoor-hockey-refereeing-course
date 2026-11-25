/** Hash routes for course overview, modules, module quizzes, and practice bank. */

export type CourseView =
  | { kind: "overview" }
  | { kind: "module"; moduleId: string }
  | { kind: "module-quiz"; moduleId: string }
  | { kind: "practice" }
  | { kind: "practice-scenario"; scenarioId: string };

const MODULE_QUIZ_RE = /^\/?modules\/([^/?#]+)\/quiz\/?$/i;
const MODULE_RE = /^\/?modules\/([^/?#]+)\/?$/i;
const PRACTICE_SCENARIO_RE = /^\/?practice\/([^/?#]+)\/?$/i;

function decodeSegment(raw: string): string | null {
  try {
    return decodeURIComponent(raw);
  } catch {
    return null;
  }
}

export function parseCourseHash(hash: string): CourseView {
  const raw = hash.replace(/^#/, "").trim();
  if (!raw || raw === "/" || raw === "/overview") {
    return { kind: "overview" };
  }
  if (raw === "/practice" || raw === "practice") {
    return { kind: "practice" };
  }
  const practiceMatch = raw.match(PRACTICE_SCENARIO_RE);
  if (practiceMatch?.[1]) {
    const scenarioId = decodeSegment(practiceMatch[1]);
    if (!scenarioId) return { kind: "overview" };
    return { kind: "practice-scenario", scenarioId };
  }
  const quizMatch = raw.match(MODULE_QUIZ_RE);
  if (quizMatch?.[1]) {
    const moduleId = decodeSegment(quizMatch[1]);
    if (!moduleId) return { kind: "overview" };
    return { kind: "module-quiz", moduleId };
  }
  const match = raw.match(MODULE_RE);
  if (match?.[1]) {
    const moduleId = decodeSegment(match[1]);
    if (!moduleId) return { kind: "overview" };
    return { kind: "module", moduleId };
  }
  return { kind: "overview" };
}

export function courseHashFor(view: CourseView): string {
  if (view.kind === "module-quiz") {
    return `#/modules/${encodeURIComponent(view.moduleId)}/quiz`;
  }
  if (view.kind === "module") {
    return `#/modules/${encodeURIComponent(view.moduleId)}`;
  }
  if (view.kind === "practice") {
    return "#/practice";
  }
  if (view.kind === "practice-scenario") {
    return `#/practice/${encodeURIComponent(view.scenarioId)}`;
  }
  return "#/";
}

export function isKnownModuleId(
  moduleId: string,
  knownIds: ReadonlySet<string> | readonly string[],
): boolean {
  return "has" in knownIds
    ? knownIds.has(moduleId)
    : knownIds.includes(moduleId);
}

export function isKnownScenarioId(
  scenarioId: string,
  knownIds: ReadonlySet<string> | readonly string[],
): boolean {
  return "has" in knownIds
    ? knownIds.has(scenarioId)
    : knownIds.includes(scenarioId);
}
