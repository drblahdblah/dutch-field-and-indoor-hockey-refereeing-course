/** Hash routes for course overview vs module detail (no router dependency). */

export type CourseView =
  | { kind: "overview" }
  | { kind: "module"; moduleId: string };

const MODULE_RE = /^\/?modules\/([^/?#]+)\/?$/i;

export function parseCourseHash(hash: string): CourseView {
  const raw = hash.replace(/^#/, "").trim();
  if (!raw || raw === "/" || raw === "/overview") {
    return { kind: "overview" };
  }
  const match = raw.match(MODULE_RE);
  if (match?.[1]) {
    try {
      return { kind: "module", moduleId: decodeURIComponent(match[1]) };
    } catch {
      return { kind: "overview" };
    }
  }
  return { kind: "overview" };
}

export function courseHashFor(view: CourseView): string {
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
