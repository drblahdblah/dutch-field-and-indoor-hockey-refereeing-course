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
  modules: { nl: "Modules", en: "Modules" },
  quiz: { nl: "Quiz", en: "Quiz" },
  submit: { nl: "Antwoorden indienen", en: "Submit answers" },
  furtherReading: { nl: "Verder lezen", en: "Further reading" },
  attribution: { nl: "Bronnen & attribution", en: "Sources & attribution" },
  progress: { nl: "Voortgang", en: "Progress" },
  language: { nl: "Taal", en: "Language" },
  score: { nl: "Score", en: "Score" },
  correct: { nl: "Juist", en: "Correct" },
  incorrect: { nl: "Onjuist", en: "Incorrect" },
  writtenPlaceholder: { nl: "Typ je antwoord…", en: "Type your answer…" },
  loading: { nl: "Laden…", en: "Loading…" },
  error: { nl: "Er ging iets mis.", en: "Something went wrong." },
  sessionSaved: {
    nl: "Sessie opgeslagen — je kunt later hervatten.",
    en: "Session saved — you can resume later.",
  },
  knhbPlaceholder: {
    nl: "KNHB-illustratie/interpretatie: plaatshouder — link officiële bron; EN-vertaling volgt.",
    en: "KNHB illustration/interpretation: placeholder — link official source; EN translation TBD.",
  },
  licenseNote: {
    nl: "Software: MIT. Officiële FIH/KNHB-regeltekst en illustraties blijven eigendom van hun rechthebbenden — hier alleen links/placeholders.",
    en: "Software: MIT. Official FIH/KNHB rule text and illustrations remain with their rights holders — links/placeholders only here.",
  },
  kindField: { nl: "Veld", en: "Field" },
  kindIndoor: { nl: "Zaal", en: "Indoor" },
  kindShared: { nl: "Algemeen", en: "Shared" },
} as const satisfies Record<string, Localized>;

export type UiKey = keyof typeof ui;

export function uiT(key: UiKey, locale: Locale): string {
  return t(ui[key], locale);
}

export { ui };
