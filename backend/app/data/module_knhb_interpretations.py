"""Full learning module: KNHB interpretation layer (NL + EN structure).

Original pedagogical framing only — links/attribution to FIH/KNHB sources.
No copyrighted KNHB illustrations or verbatim interpretation text.
EN fields marked translation_needed are slots, not invented legal paraphrases.
"""

from app.schemas import (
    EN_TRANSLATION_SLOT_MARKER,
    Attribution,
    FurtherReading,
    InterpretationReference,
    LearningSection,
    LocalizedText,
    ModuleStub,
    Quiz,
    QuizFeedback,
    QuizOption,
    QuizQuestion,
    VisualPlaceholder,
)

FIH_RULES_URL = (
    "https://www.fih.hockey/inside-fih/our-official-documents/rules-of-hockey"
)
KNHB_HOME_URL = "https://www.knhb.nl/"

EN_SLOT = (
    f"{EN_TRANSLATION_SLOT_MARKER} Official KNHB NL interpretation text is not "
    "paraphrased here. Use the linked KNHB/FIH sources; authorized EN "
    "legal translation TBD."
)

KNHB_ATTR = Attribution(
    source_name="KNHB — regels & interpretaties",
    source_url=KNHB_HOME_URL,
    note=LocalizedText(
        nl=(
            "Geen KNHB-illustraties of overgenomen interpretatietekst. "
            "Link naar officiële KNHB-bronnen; EN-vertalingsslot actief."
        ),
        en=(
            "No KNHB illustrations or reproduced interpretation text. "
            "Link to official KNHB sources; EN translation slot active."
        ),
    ),
    knhb_illustration_placeholder=True,
    translation_needed=True,
)

INTERPRETATION_VISUALS: list[VisualPlaceholder] = [
    VisualPlaceholder(
        id="viz-source-stack",
        kind="svg_animation",
        title=LocalizedText(
            nl="Bronnenstapel: FIH → KNHB → club",
            en="Source stack: FIH → KNHB → club",
        ),
        caption=LocalizedText(
            nl=(
                "Originele SVG: internationale regels, nationale interpretatie, "
                "lokale toepassing. Geen KNHB-kunst."
            ),
            en=(
                "Original SVG: international rules, national interpretation, "
                "local application. No KNHB art."
            ),
        ),
        animation_key="source-stack",
    ),
    VisualPlaceholder(
        id="viz-translation-slot",
        kind="svg_animation",
        title=LocalizedText(
            nl="NL-samenvatting + EN-vertalingsslot",
            en="NL summary + EN translation slot",
        ),
        caption=LocalizedText(
            nl=(
                "Originele cursusanimatie: NL-pedagogiek naast een EN-slot. "
                "Geen geclaimde juridische EN-parafrase van KNHB-tekst."
            ),
            en=(
                "Original course animation: NL pedagogy beside an EN slot. "
                "No claimed legal EN paraphrase of KNHB text."
            ),
        ),
        animation_key="translation-slot",
    ),
    VisualPlaceholder(
        id="viz-attribution-chain",
        kind="svg_animation",
        title=LocalizedText(
            nl="Attributieketen: link → bron → plaatshouder",
            en="Attribution chain: link → source → placeholder",
        ),
        caption=LocalizedText(
            nl=(
                "Originele SVG: hoe we officiële bronnen markeren zonder "
                "auteursrechtelijke illustraties te bundelen."
            ),
            en=(
                "Original SVG: how we mark official sources without bundling "
                "copyrighted illustrations."
            ),
        ),
        animation_key="attribution-chain",
    ),
    VisualPlaceholder(
        id="viz-knhb-interpretations-slot",
        kind="official_link_slot",
        title=LocalizedText(
            nl="KNHB-interpretaties (officiële link)",
            en="KNHB interpretations (official link)",
        ),
        caption=LocalizedText(
            nl=(
                "Link naar KNHB-scheidsrechters-/regelmateriaal. Geen "
                "KNHB-illustratie in deze repo. EN-vertaling: slot."
            ),
            en=(
                "Link to KNHB umpire / rules materials. No KNHB illustration "
                "ships in this repo. EN translation: slot."
            ),
        ),
        official_source_url=KNHB_HOME_URL,
        official_source_name="KNHB",
        knhb_illustration_placeholder=True,
    ),
]

INTERPRETATION_REFERENCES: list[InterpretationReference] = [
    InterpretationReference(
        id="interp-fih-knhb-layering",
        topic=LocalizedText(
            nl="FIH-regels ↔ KNHB-interpretaties",
            en="FIH rules ↔ KNHB interpretations",
        ),
        scope="shared",
        summary=LocalizedText(
            nl=(
                "Pedagogisch: FIH levert de internationale regelbasis; KNHB "
                "publiceert interpretaties en opleidingen voor NL-competities. "
                "Deze cursus citeert geen van beide letterlijk — raadpleeg de "
                "gelinkte bronnen voor actuele teksten."
            ),
            en=(
                "Pedagogical: FIH supplies the international rules base; KNHB "
                "publishes interpretations and education for NL competitions. "
                "This course quotes neither verbatim — consult linked sources "
                "for current texts."
            ),
        ),
        translation_needed=False,
        official_source_url=FIH_RULES_URL,
        official_source_name="FIH Rules of Hockey",
        knhb_illustration_placeholder=False,
        attribution=Attribution(
            source_name="FIH Rules of Hockey",
            source_url=FIH_RULES_URL,
            note=LocalizedText(
                nl="Officiële FIH Rules — internationale regelbasis (link).",
                en="Official FIH Rules — international rules base (link).",
            ),
        ),
        visual_id="viz-source-stack",
    ),
    InterpretationReference(
        id="interp-field-advantage",
        topic=LocalizedText(
            nl="Veld: advantage / gevaarlijk spel (raadpleeg KNHB)",
            en="Field: advantage / dangerous play (consult KNHB)",
        ),
        scope="field",
        summary=LocalizedText(
            nl=(
                "Pedagogisch kader: wanneer laat je voordeel doorlopen, en "
                "wanneer grijp je in om veiligheidsredenen? Exacte "
                "KNHB-interpretatietekst hoort bij de bond — hier alleen "
                "het denkmodel plus bronlink."
            ),
            en=EN_SLOT,
        ),
        translation_needed=True,
        official_source_url=KNHB_HOME_URL,
        official_source_name="KNHB",
        knhb_illustration_placeholder=True,
        attribution=KNHB_ATTR,
        visual_id="viz-translation-slot",
    ),
    InterpretationReference(
        id="interp-indoor-lift-boards",
        topic=LocalizedText(
            nl="Zaal: lift & bandenspel (raadpleeg KNHB/FIH Indoor)",
            en="Indoor: lift & board play (consult KNHB/FIH Indoor)",
        ),
        scope="indoor",
        summary=LocalizedText(
            nl=(
                "Pedagogisch kader: zaal vraagt kortere besliscycli rond lift "
                "en banden. Officiële grenzen en uitzonderingen staan in "
                "FIH Indoor / KNHB — niet overgenomen in deze repo."
            ),
            en=EN_SLOT,
        ),
        translation_needed=True,
        official_source_url=KNHB_HOME_URL,
        official_source_name="KNHB",
        knhb_illustration_placeholder=True,
        attribution=KNHB_ATTR,
        visual_id="viz-translation-slot",
    ),
    InterpretationReference(
        id="interp-signals-cards",
        topic=LocalizedText(
            nl="Gebaren & kaarten (officiële kaarten/charts)",
            en="Signals & cards (official charts)",
        ),
        scope="shared",
        summary=LocalizedText(
            nl=(
                "Pedagogisch: oefen communicatie en escalatie in eigen "
                "woorden; officiële gebarenkaarten en card-procedures komen "
                "van FIH/KNHB. Deze cursus bundelt geen KNHB-illustraties."
            ),
            en=EN_SLOT,
        ),
        translation_needed=True,
        official_source_url=KNHB_HOME_URL,
        official_source_name="KNHB",
        knhb_illustration_placeholder=True,
        attribution=KNHB_ATTR,
        visual_id="viz-attribution-chain",
    ),
]

INTERPRETATION_QUIZ = Quiz(
    id="quiz-knhb-interpretations",
    title=LocalizedText(
        nl="Quiz: KNHB-interpretatielaag",
        en="Quiz: KNHB interpretation layer",
    ),
    questions=[
        QuizQuestion(
            id="q1-official-source",
            type="multiple_choice",
            prompt=LocalizedText(
                nl=(
                    "Waar haal je officiële NL-interpretaties vandaan "
                    "(pedagogisch — geen regelcitaat)?"
                ),
                en=(
                    "Where do you get official NL interpretations "
                    "(pedagogical — not a rule quote)?"
                ),
            ),
            options=[
                QuizOption(
                    id="a",
                    text=LocalizedText(
                        nl="Uitsluitend uit deze cursus-repo",
                        en="Only from this course repository",
                    ),
                ),
                QuizOption(
                    id="b",
                    text=LocalizedText(
                        nl="Officiële KNHB-/FIH-bronnen (links)",
                        en="Official KNHB/FIH sources (links)",
                    ),
                ),
                QuizOption(
                    id="c",
                    text=LocalizedText(
                        nl="Willekeurige social-media clips",
                        en="Random social-media clips",
                    ),
                ),
                QuizOption(
                    id="d",
                    text=LocalizedText(
                        nl="Alleen Engelse Wikipedia",
                        en="English Wikipedia only",
                    ),
                ),
            ],
            correct_option_id="b",
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Juist: deze cursus linkt naar KNHB/FIH en levert "
                        "geen auteursrechtelijke interpretatietekst."
                    ),
                    en=(
                        "Correct: this course links to KNHB/FIH and ships no "
                        "copyrighted interpretation text."
                    ),
                ),
                visualization_hint="source-stack",
            ),
            feedback_incorrect={
                "a": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Nee — de repo is pedagogiek + links, geen officiële bron.",
                        en="No — the repo is pedagogy + links, not an official source.",
                    ),
                    visualization_hint="source-stack",
                ),
                "c": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Nee — gebruik officiële KNHB/FIH-kanalen.",
                        en="No — use official KNHB/FIH channels.",
                    ),
                    visualization_hint="attribution-chain",
                ),
                "d": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Nee — Wikipedia is geen officiële bondskanaal.",
                        en="No — Wikipedia is not an official federation channel.",
                    ),
                    visualization_hint="source-stack",
                ),
            },
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Kies de officiële KNHB/FIH-bronnen.",
                    en="Choose the official KNHB/FIH sources.",
                ),
                visualization_hint="source-stack",
            ),
        ),
        QuizQuestion(
            id="q2-no-knhb-art",
            type="multiple_choice",
            prompt=LocalizedText(
                nl="Wat levert deze cursus voor KNHB-illustraties?",
                en="What does this course ship for KNHB illustrations?",
            ),
            options=[
                QuizOption(
                    id="a",
                    text=LocalizedText(
                        nl="Volledige KNHB-gebarenkaarten",
                        en="Full KNHB signal charts",
                    ),
                ),
                QuizOption(
                    id="b",
                    text=LocalizedText(
                        nl="Gescande KNHB-PDF's",
                        en="Scanned KNHB PDFs",
                    ),
                ),
                QuizOption(
                    id="c",
                    text=LocalizedText(
                        nl="Alleen link/plaatshouder + attributie",
                        en="Link/placeholder + attribution only",
                    ),
                ),
                QuizOption(
                    id="d",
                    text=LocalizedText(
                        nl="Hertekende officiële kaarten als cursus-IP",
                        en="Redrawn official charts as course IP",
                    ),
                ),
            ],
            correct_option_id="c",
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Juist: plaatshouders, attributie en links — geen "
                        "gebundelde KNHB-kunst."
                    ),
                    en=(
                        "Correct: placeholders, attribution and links — no "
                        "bundled KNHB art."
                    ),
                ),
                visualization_hint="attribution-chain",
            ),
            feedback_incorrect={
                "a": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Nee — officiële kaarten blijven bij KNHB/FIH.",
                        en="No — official charts stay with KNHB/FIH.",
                    ),
                    visualization_hint="attribution-chain",
                ),
                "b": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Nee — we kopiëren geen KNHB-PDF's.",
                        en="No — we do not copy KNHB PDFs.",
                    ),
                    visualization_hint="attribution-chain",
                ),
                "d": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Nee — hertekenen maakt het geen cursusrecht.",
                        en="No — redrawing does not create course rights.",
                    ),
                    visualization_hint="attribution-chain",
                ),
            },
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Antwoord: alleen link/plaatshouder + attributie.",
                    en="Answer: link/placeholder + attribution only.",
                ),
                visualization_hint="attribution-chain",
            ),
        ),
        QuizQuestion(
            id="q3-translation-keyword",
            type="written",
            prompt=LocalizedText(
                nl=(
                    "Welk Engels sleutelwoord hoort bij een open EN-veld "
                    "wanneer de juridische vertaling van NL-interpretaties "
                    "nog ontbreekt? (één woord)"
                ),
                en=(
                    "Which English keyword belongs with an open EN field "
                    "when the legal rendering of NL interpretations is still "
                    "missing? (one word)"
                ),
            ),
            accepted_answers=[
                "translation",
                "slot",
                "placeholder",
                "translation_needed",
            ],
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Juist: translation / slot / placeholder / "
                        "translation_needed — geen verzonnen juridische "
                        "EN-parafrase."
                    ),
                    en=(
                        "Correct: translation / slot / placeholder / "
                        "translation_needed — no invented legal EN "
                        "paraphrase."
                    ),
                ),
                visualization_hint="translation-slot",
            ),
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Verwacht o.a.: translation, slot, placeholder of "
                        "translation_needed."
                    ),
                    en=(
                        "Expected e.g.: translation, slot, placeholder, or "
                        "translation_needed."
                    ),
                ),
                visualization_hint="translation-slot",
            ),
        ),
        QuizQuestion(
            id="q4-attribution-keyword",
            type="written",
            prompt=LocalizedText(
                nl=(
                    "Welk Engels sleutelwoord hoort bij het duidelijk "
                    "vermelden van FIH/KNHB-bronnen? (één woord)"
                ),
                en=(
                    "Which English keyword belongs with clearly crediting "
                    "FIH/KNHB sources? (one word)"
                ),
            ),
            accepted_answers=["attribution"],
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl="Juist: attribution — bronnaam, URL en notitie.",
                    en="Correct: attribution — source name, URL and note.",
                ),
                visualization_hint="attribution-chain",
            ),
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Verwacht antwoord: attribution.",
                    en="Expected answer: attribution.",
                ),
                visualization_hint=None,
            ),
        ),
    ],
)

INTERPRETATION_MODULE = ModuleStub(
    id="mod-knhb-interpretations",
    kind="shared",
    title=LocalizedText(
        nl="KNHB-interpretatielaag (bronnen & vertaalslots)",
        en="KNHB interpretation layer (sources & translation slots)",
    ),
    summary=LocalizedText(
        nl=(
            "Volledige module: hoe FIH-regels en KNHB-interpretaties samenhangen, "
            "met attributie, officiële links, EN-vertalingsslots en originele "
            "visuals — zonder auteursrechtelijke KNHB-kunst of -tekst."
        ),
        en=(
            "Full module: how FIH rules and KNHB interpretations relate, with "
            "attribution, official links, EN translation slots and original "
            "visuals — without copyrighted KNHB art or text."
        ),
    ),
    learning_objectives=[
        LocalizedText(
            nl="FIH-regelbasis vs KNHB-interpretatie in eigen woorden scheiden.",
            en="Separate FIH rules base vs KNHB interpretation in your own words.",
        ),
        LocalizedText(
            nl="Officiële bronlinks en attributievelden herkennen.",
            en="Recognize official source links and attribution fields.",
        ),
        LocalizedText(
            nl="EN-vertalingsslots gebruiken zonder juridische parafrase te verzinnen.",
            en="Use EN translation slots without inventing legal paraphrase.",
        ),
        LocalizedText(
            nl="Weten dat deze cursus geen KNHB-illustraties bundelt.",
            en="Know that this course does not bundle KNHB illustrations.",
        ),
    ],
    instruction_outline=[
        LocalizedText(
            nl="Bronnenstapel: FIH → KNHB → club.",
            en="Source stack: FIH → KNHB → club.",
        ),
        LocalizedText(
            nl="Interpretatiereferenties met NL-samenvatting + EN-slot.",
            en="Interpretation references with NL summary + EN slot.",
        ),
        LocalizedText(
            nl="Attributieketen en plaatshouders.",
            en="Attribution chain and placeholders.",
        ),
        LocalizedText(
            nl="Quiz over bronnen en vertaalslots.",
            en="Quiz on sources and translation slots.",
        ),
    ],
    content_status="full",
    sections=[
        LearningSection(
            id="sec-interp-why",
            title=LocalizedText(
                nl="Waarom een interpretatielaag",
                en="Why an interpretation layer",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Na veld-, zaal- en pathway-modules blijft één "
                        "vraag open: waar vind je de officiële NL-toelichting "
                        "zonder auteursrecht te schenden? Deze laag is het "
                        "antwoord — structuur, links en slots, geen "
                        "overgenomen KNHB-PDF."
                    ),
                    en=(
                        "After field, indoor and pathway modules, one "
                        "question remains: where do you find official NL "
                        "guidance without infringing copyright? This layer "
                        "is the answer — structure, links and slots, no "
                        "reproduced KNHB PDF."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Alles hier is oorspronkelijke pedagogiek of een "
                        "duidelijke plaatshouder. Officiële teksten blijven "
                        "bij FIH/KNHB."
                    ),
                    en=(
                        "Everything here is original pedagogy or a clear "
                        "placeholder. Official texts stay with FIH/KNHB."
                    ),
                ),
            ],
        ),
        LearningSection(
            id="sec-source-stack",
            title=LocalizedText(
                nl="Bronnenstapel: FIH → KNHB → club",
                en="Source stack: FIH → KNHB → club",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Denk in drie lagen: FIH (internationale regels), "
                        "KNHB (nationale interpretatie/opleiding), club "
                        "(lokale procedures). Misverstand: deze cursus "
                        "vervangt geen van die lagen."
                    ),
                    en=(
                        "Think in three layers: FIH (international rules), "
                        "KNHB (national interpretation/education), club "
                        "(local procedures). Misconception: this course "
                        "replaces none of those layers."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Bij twijfel: open de officiële link, check de "
                        "datum, en noteer attributie — niet ‘ik las het "
                        "ergens in de cursus’."
                    ),
                    en=(
                        "When unsure: open the official link, check the "
                        "date, and note attribution — not ‘I saw it "
                        "somewhere in the course’."
                    ),
                ),
            ],
            visual_id="viz-source-stack",
        ),
        LearningSection(
            id="sec-translation-slots",
            title=LocalizedText(
                nl="NL-samenvattingen & EN-vertalingsslots",
                en="NL summaries & EN translation slots",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Elke interpretatiereferentie heeft een NL "
                        "pedagogische samenvatting (oorspronkelijke "
                        "cursustekst) en, waar nodig, een EN-slot "
                        "gemarkeerd met translation_needed. We verzinnen "
                        "geen juridische EN-parafrase van beschermde "
                        "KNHB-tekst."
                    ),
                    en=(
                        "Each interpretation reference has an NL "
                        "pedagogical summary (original course prose) and, "
                        "where needed, an EN slot marked translation_needed. "
                        "We do not invent legal EN paraphrase of protected "
                        "KNHB text."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "In de UI zie je bij EN-slots een "
                        "plaatshoudervlag. Vul later alleen geautoriseerde "
                        "vertalingen in."
                    ),
                    en=(
                        "In the UI, EN slots show a placeholder flag. Fill "
                        "later only with authorized translations."
                    ),
                ),
            ],
            visual_id="viz-translation-slot",
        ),
        LearningSection(
            id="sec-attribution-practice",
            title=LocalizedText(
                nl="Attributie in de praktijk",
                en="Attribution in practice",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Elke officiële pointer draagt: bronnaam, URL, "
                        "tweetalige notitie, en vlaggen "
                        "(knhb_illustration_placeholder / "
                        "translation_needed). Dat houdt de grens met MIT "
                        "software vs FIH/KNHB-materiaal helder."
                    ),
                    en=(
                        "Every official pointer carries: source name, URL, "
                        "bilingual note, and flags "
                        "(knhb_illustration_placeholder / "
                        "translation_needed). That keeps the boundary "
                        "between MIT software and FIH/KNHB material clear."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Gebruik de KNHB-plaatshouder hieronder voor de "
                        "actuele bondspagina — controleer altijd of de "
                        "URL nog klopt."
                    ),
                    en=(
                        "Use the KNHB placeholder below for the current "
                        "federation page — always verify the URL still "
                        "holds."
                    ),
                ),
            ],
            visual_id="viz-attribution-chain",
        ),
        LearningSection(
            id="sec-official-knhb-slot",
            title=LocalizedText(
                nl="Officiële KNHB-link (plaatshouder)",
                en="Official KNHB link (placeholder)",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Concrete interpretatiedocumenten, gebarenkaarten "
                        "en opleidings-PDF's staan bij de KNHB. Deze module "
                        "levert alleen de link-slot en het "
                        "raadpleegkader."
                    ),
                    en=(
                        "Concrete interpretation documents, signal charts "
                        "and education PDFs live with the KNHB. This module "
                        "only ships the link slot and the consultation "
                        "frame."
                    ),
                ),
            ],
            visual_id="viz-knhb-interpretations-slot",
        ),
        LearningSection(
            id="sec-interp-practice-next",
            title=LocalizedText(
                nl="Oefenen en verder",
                en="Practice and next steps",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Maak de quiz hieronder. Sla voortgang op via je "
                        "cursussessie. Herhaal veld-/zaalmodules met de "
                        "interpretatiereferenties ernaast; houd FIH- en "
                        "KNHB-tabbladen open voor echte wedstrijdvragen."
                    ),
                    en=(
                        "Take the quiz below. Save progress via your course "
                        "session. Revisit field/indoor modules with the "
                        "interpretation references beside you; keep FIH "
                        "and KNHB tabs open for real match questions."
                    ),
                ),
            ],
        ),
    ],
    visuals=INTERPRETATION_VISUALS,
    interpretation_references=INTERPRETATION_REFERENCES,
    quiz_id=INTERPRETATION_QUIZ.id,
    further_reading=[
        FurtherReading(
            title=LocalizedText(
                nl="FIH Rules of Hockey (officieel)",
                en="FIH Rules of Hockey (official)",
            ),
            url=FIH_RULES_URL,
            attribution=Attribution(
                source_name="FIH Rules of Hockey",
                source_url=FIH_RULES_URL,
                note=LocalizedText(
                    nl="Officiële FIH Rules of Hockey — internationale regelbasis.",
                    en="Official FIH Rules of Hockey — international rules base.",
                ),
            ),
        ),
        FurtherReading(
            title=LocalizedText(
                nl="KNHB — regels & interpretaties (link/plaatshouder)",
                en="KNHB — rules & interpretations (link/placeholder)",
            ),
            url=KNHB_HOME_URL,
            attribution=KNHB_ATTR,
        ),
    ],
    order=7,
)
