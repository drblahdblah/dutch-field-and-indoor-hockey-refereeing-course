export type Locale = "nl" | "en";

export type Localized = { nl: string; en: string };

export function t(text: Localized, locale: Locale): string {
  return text[locale] || text.en || text.nl;
}

const ui = {
  brand: {
    nl: "Hockey Scheidsrechterscursus",
    en: "Hockey Umpiring Course",
  },
  tagline: {
    nl: "Veld & zaal — op weg naar professioneel niveau",
    en: "Field & indoor — toward professional standard",
  },
  start: { nl: "Start cursus", en: "Start course" },
  resume: { nl: "Hervat", en: "Resume" },
  progressOverview: {
    nl: "Cursuspad & voortgang",
    en: "Course path & progress",
  },
  modulesCompleted: {
    nl: "{done} van {total} modules voltooid",
    en: "{done} of {total} modules completed",
  },
  nextUp: { nl: "Volgende", en: "Next up" },
  progressStartHint: {
    nl: "Start of hervat een sessie om voortgang bij te houden.",
    en: "Start or resume a session to track progress.",
  },
  progressIdle: {
    nl: "Nog niet bijgehouden",
    en: "Not tracking yet",
  },
  courseComplete: {
    nl: "Cursuspad voltooid — goed gedaan.",
    en: "Course path complete — well done.",
  },
  jumpToNext: {
    nl: "Ga naar volgende module",
    en: "Go to next module",
  },
  backToCourse: {
    nl: "Terug naar cursusoverzicht",
    en: "Back to course overview",
  },
  openModule: {
    nl: "Open module",
    en: "Open module",
  },
  moduleStep: {
    nl: "Module {current} van {total}",
    en: "Module {current} of {total}",
  },
  goToNextModule: {
    nl: "Volgende module",
    en: "Next module",
  },
  courseOverview: {
    nl: "Cursusoverzicht",
    en: "Course overview",
  },
  statusNotStarted: { nl: "niet gestart", en: "not started" },
  statusInProgress: { nl: "bezig", en: "in progress" },
  statusCompleted: { nl: "voltooid", en: "completed" },
  quiz: { nl: "Quiz", en: "Quiz" },
  submit: { nl: "Antwoorden indienen", en: "Submit answers" },
  furtherReading: { nl: "Verder lezen", en: "Further reading" },
  attribution: { nl: "Bronnen & vermelding", en: "Sources & attribution" },
  progress: { nl: "Voortgang", en: "Progress" },
  language: { nl: "Taal", en: "Language" },
  langNl: { nl: "Nederlands", en: "Dutch" },
  langEn: { nl: "Engels", en: "English" },
  skipToContent: {
    nl: "Ga naar hoofdinhoud",
    en: "Skip to main content",
  },
  courseNav: {
    nl: "Cursusmodules",
    en: "Course modules",
  },
  mainContent: {
    nl: "Hoofdinhoud",
    en: "Main content",
  },
  score: { nl: "Score", en: "Score" },
  correct: { nl: "Juist", en: "Correct" },
  incorrect: { nl: "Onjuist", en: "Incorrect" },
  writtenPlaceholder: { nl: "Typ je antwoord…", en: "Type your answer…" },
  submitting: { nl: "Bezig met indienen…", en: "Submitting…" },
  loading: { nl: "Laden…", en: "Loading…" },
  error: { nl: "Er ging iets mis.", en: "Something went wrong." },
  sessionSaved: {
    nl: "Sessie opgeslagen — je kunt later hervatten.",
    en: "Session saved — you can resume later.",
  },
  endSession: { nl: "Sessie beëindigen", en: "End session" },
  opensInNewTab: {
    nl: "(opent in nieuw tabblad)",
    en: "(opens in new tab)",
  },

  knhbPlaceholder: {
    nl: "KNHB-illustratie/interpretatie: plaatshouder — link officiële bron; EN-vertaling volgt.",
    en: "KNHB illustration/interpretation: placeholder — link official source; EN translation TBD.",
  },
  translationNeeded: {
    nl: "EN-vertalingsslot — geen geautoriseerde juridische vertaling van KNHB-tekst.",
    en: "EN translation slot — no authorized legal translation of KNHB text yet.",
  },
  interpretationRefs: {
    nl: "Interpretatiereferenties",
    en: "Interpretation references",
  },
  officialSource: {
    nl: "Officiële bron",
    en: "Official source",
  },
  licenseNote: {
    nl: "Software: MIT. Officiële FIH/KNHB-regeltekst en illustraties blijven eigendom van hun rechthebbenden — hier alleen links/placeholders.",
    en: "Software: MIT. Official FIH/KNHB rule text and illustrations remain with their rights holders — links/placeholders only here.",
  },
  kindField: { nl: "Veld", en: "Field" },
  kindIndoor: { nl: "Zaal", en: "Indoor" },
  kindShared: { nl: "Algemeen", en: "Shared" },
  contentFull: { nl: "Volledige module", en: "Full module" },
  contentStub: { nl: "Stub", en: "Stub" },
  learningContent: { nl: "Leerstof", en: "Learning content" },
  learningObjectives: { nl: "Leerdoelen", en: "Learning objectives" },
  instruction: { nl: "Instructie", en: "Instruction" },
  vizUnavailable: {
    nl: "Geen gekoppelde visualisatie voor deze feedback.",
    en: "No linked visualization for this feedback.",
  },
  quizVizCaption: {
    nl: "Cursusanimatie gekoppeld aan deze feedback.",
    en: "Course animation linked to this feedback.",
  },
  quizVizFallbackTitle: {
    nl: "Visualisatie",
    en: "Visualization",
  },
} as const satisfies Record<string, Localized>;

/** Localized titles for quiz feedback visualization hooks (animation keys). */
export const QUIZ_VIZ_TITLES = {
  "safety-triangle": {
    nl: "Visualisatie: prioriteitsdriehoek",
    en: "Visualization: priority triangle",
  },
  "scan-cycle": {
    nl: "Visualisatie: scan-cyclus",
    en: "Visualization: scan cycle",
  },
  "pitch-zones": {
    nl: "Visualisatie: veldzones",
    en: "Visualization: pitch zones",
  },
  "danger-cone": {
    nl: "Visualisatie: gevaarskegel",
    en: "Visualization: danger cone",
  },
  "restart-bubble": {
    nl: "Visualisatie: herstartbubbel",
    en: "Visualization: restart bubble",
  },
  "court-boards": {
    nl: "Visualisatie: zaalbanden",
    en: "Visualization: indoor boards",
  },
  "lift-limit": {
    nl: "Visualisatie: liftkader",
    en: "Visualization: lift frame",
  },
  "board-play": {
    nl: "Visualisatie: bandenspel",
    en: "Visualization: board play",
  },
  "match-cadence": {
    nl: "Visualisatie: wedstrijdritme",
    en: "Visualization: match cadence",
  },
  "partner-handoff": {
    nl: "Visualisatie: partneroverdracht",
    en: "Visualization: partner handoff",
  },
  "consistency-loop": {
    nl: "Visualisatie: consistentielus",
    en: "Visualization: consistency loop",
  },
  "source-stack": {
    nl: "Visualisatie: bronnenstapel",
    en: "Visualization: source stack",
  },
  "translation-slot": {
    nl: "Visualisatie: vertalingsslot",
    en: "Visualization: translation slot",
  },
  "attribution-chain": {
    nl: "Visualisatie: attributieketen",
    en: "Visualization: attribution chain",
  },
  "capstone-weave": {
    nl: "Visualisatie: capstone-weefsel",
    en: "Visualization: capstone weave",
  },
  "field-attack": {
    nl: "Visualisatie: veldscenario-aanval",
    en: "Visualization: field attack scenario",
  },
  "indoor-rebound": {
    nl: "Visualisatie: zaalscenario-rebound",
    en: "Visualization: indoor rebound scenario",
  },
  "match-pressure": {
    nl: "Visualisatie: wedstrijddruk",
    en: "Visualization: match pressure",
  },
} as const satisfies Record<string, Localized>;

export type UiKey = keyof typeof ui;

export function uiT(key: UiKey, locale: Locale): string {
  return t(ui[key], locale);
}

export function quizVizTitle(key: string): Localized {
  return (
    QUIZ_VIZ_TITLES[key as keyof typeof QUIZ_VIZ_TITLES] ?? ui.quizVizFallbackTitle
  );
}

export { ui };
