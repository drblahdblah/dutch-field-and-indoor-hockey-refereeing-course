/** Hash routes for course overview, modules, and module quizzes (no router dependency). */

export type CourseView =
  | { kind: "overview" }
  | { kind: "module"; moduleId: string }
  | { kind: "module-quiz"; moduleId: string };

const MODULE_QUIZ_RE = /^\/?modules\/([^/?#]+)\/quiz\/?$/i;
const MODULE_RE = /^\/?modules\/([^/?#]+)\/?$/i;

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
