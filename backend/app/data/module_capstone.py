"""Full learning module: bilingual capstone assessment.

Original pedagogical scenarios only — mixes field, indoor, pathway and
interpretation themes. No copyrighted FIH/KNHB rule text or illustrations.
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

CAPSTONE_VISUALS: list[VisualPlaceholder] = [
    VisualPlaceholder(
        id="viz-capstone-weave",
        kind="svg_animation",
        title=LocalizedText(
            nl="Capstone-weefsel: veld · zaal · pad · interpretatie",
            en="Capstone weave: field · indoor · pathway · interpretation",
        ),
        caption=LocalizedText(
            nl=(
                "Originele SVG: vier cursusdomeinen die in één "
                "eindtoets samenkomen. Geen KNHB-kunst."
            ),
            en=(
                "Original SVG: four course domains meeting in one "
                "capstone. No KNHB art."
            ),
        ),
        animation_key="capstone-weave",
    ),
    VisualPlaceholder(
        id="viz-scenario-field",
        kind="svg_animation",
        title=LocalizedText(
            nl="Veldscenario: zones & gevaar",
            en="Field scenario: zones & danger",
        ),
        caption=LocalizedText(
            nl="Originele cursusvisual voor veldscenario's in de capstone.",
            en="Original course visual for field scenarios in the capstone.",
        ),
        animation_key="field-attack",
    ),
    VisualPlaceholder(
        id="viz-scenario-indoor",
        kind="svg_animation",
        title=LocalizedText(
            nl="Zaalscenario: lift & banden",
            en="Indoor scenario: lift & boards",
        ),
        caption=LocalizedText(
            nl="Originele cursusvisual voor zaalscenario's in de capstone.",
            en="Original course visual for indoor scenarios in the capstone.",
        ),
        animation_key="indoor-rebound",
    ),
    VisualPlaceholder(
        id="viz-scenario-pathway",
        kind="svg_animation",
        title=LocalizedText(
            nl="Pathway-scenario: oplopende wedstrijddruk",
            en="Pathway scenario: rising match pressure",
        ),
        caption=LocalizedText(
            nl="Originele cursusvisual voor professioneel matchmanagement.",
            en="Original course visual for professional match management.",
        ),
        animation_key="match-pressure",
    ),
    VisualPlaceholder(
        id="viz-scenario-interp",
        kind="svg_animation",
        title=LocalizedText(
            nl="Interpretatiescenario: bronnenstapel",
            en="Interpretation scenario: source stack",
        ),
        caption=LocalizedText(
            nl="Originele SVG: FIH → KNHB → club in de eindtoets.",
            en="Original SVG: FIH → KNHB → club in the capstone.",
        ),
        animation_key="source-stack",
    ),
    VisualPlaceholder(
        id="viz-capstone-knhb-slot",
        kind="official_link_slot",
        title=LocalizedText(
            nl="KNHB-bronnen (officiële link)",
            en="KNHB sources (official link)",
        ),
        caption=LocalizedText(
            nl=(
                "Link naar KNHB-materiaal voor echte wedstrijdvragen. "
                "Geen KNHB-illustratie in deze repo."
            ),
            en=(
                "Link to KNHB materials for real match questions. "
                "No KNHB illustration ships in this repo."
            ),
        ),
        official_source_url=KNHB_HOME_URL,
        official_source_name="KNHB",
        knhb_illustration_placeholder=True,
    ),
]

CAPSTONE_REFERENCES: list[InterpretationReference] = [
    InterpretationReference(
        id="interp-capstone-cross-check",
        topic=LocalizedText(
            nl="Capstone: cross-check FIH ↔ KNHB",
            en="Capstone: cross-check FIH ↔ KNHB",
        ),
        scope="shared",
        summary=LocalizedText(
            nl=(
                "Pedagogisch: bij twijfel in de eindtoets open je de "
                "officiële FIH/KNHB-tab — niet alleen cursusgeheugen. "
                "Deze cursus citeert geen letterlijke interpretatietekst."
            ),
            en=EN_SLOT,
        ),
        translation_needed=True,
        official_source_url=KNHB_HOME_URL,
        official_source_name="KNHB",
        knhb_illustration_placeholder=True,
        attribution=KNHB_ATTR,
        visual_id="viz-scenario-interp",
    ),
]

CAPSTONE_QUIZ = Quiz(
    id="quiz-capstone-assessment",
    title=LocalizedText(
        nl="Capstone-toets (veld · zaal · pad · interpretatie)",
        en="Capstone assessment (field · indoor · pathway · interpretation)",
    ),
    questions=[
        QuizQuestion(
            id="q1-field-danger-priority",
            type="multiple_choice",
            prompt=LocalizedText(
                nl=(
                    "Veldscenario: een aanval richting cirkel, bal hoog en "
                    "dicht bij een verdediger. Wat is je eerste prioriteit "
                    "(pedagogisch — geen regelcitaat)?"
                ),
                en=(
                    "Field scenario: an attack toward the circle, ball "
                    "raised and close to a defender. What is your first "
                    "priority (pedagogical — not a rule quote)?"
                ),
            ),
            options=[
                QuizOption(
                    id="a",
                    text=LocalizedText(
                        nl="Eerst de flow laten doorlopen, veiligheid later",
                        en="Protect flow first, safety later",
                    ),
                ),
                QuizOption(
                    id="b",
                    text=LocalizedText(
                        nl="Veiligheid eerst; grijp in bij gevaarlijk spel",
                        en="Safety first; intervene on dangerous play",
                    ),
                ),
                QuizOption(
                    id="c",
                    text=LocalizedText(
                        nl="Alleen wachten tot de coach klaagt",
                        en="Only wait until a coach complains",
                    ),
                ),
                QuizOption(
                    id="d",
                    text=LocalizedText(
                        nl="Altijd voordeel geven, ongeacht risico",
                        en="Always play advantage, regardless of risk",
                    ),
                ),
            ],
            correct_option_id="b",
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Juist: veiligheid gaat vóór flow en voordeel. "
                        "Gevaarlijk spel vraagt om ingrijpen."
                    ),
                    en=(
                        "Correct: safety comes before flow and advantage. "
                        "Dangerous play calls for intervention."
                    ),
                ),
                visualization_hint="field-attack",
            ),
            feedback_incorrect={
                "a": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Nee — flow mag veiligheid niet overrulen.",
                        en="No — flow must not override safety.",
                    ),
                    visualization_hint="field-attack",
                ),
                "c": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Nee — jij bewaakt veiligheid, niet de coach.",
                        en="No — you own safety, not the coach.",
                    ),
                    visualization_hint="safety-triangle",
                ),
                "d": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Nee — voordeel stopt bij gevaar.",
                        en="No — advantage stops when danger appears.",
                    ),
                    visualization_hint="field-attack",
                ),
            },
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Kies veiligheid eerst bij gevaarlijk spel.",
                    en="Choose safety first on dangerous play.",
                ),
                visualization_hint="field-attack",
            ),
        ),
        QuizQuestion(
            id="q2-indoor-lift-boards",
            type="multiple_choice",
            prompt=LocalizedText(
                nl=(
                    "Zaalscenario: snelle rebound van de band, bal komt "
                    "omhoog in een krappe ruimte. Wat past het best bij "
                    "zaalhockey-denken (pedagogisch)?"
                ),
                en=(
                    "Indoor scenario: quick rebound off the boards, ball "
                    "rises in a tight space. What best fits indoor "
                    "thinking (pedagogical)?"
                ),
            ),
            options=[
                QuizOption(
                    id="a",
                    text=LocalizedText(
                        nl="Behandel het exact als een veldstrafhoek",
                        en="Treat it exactly like an outdoor penalty corner",
                    ),
                ),
                QuizOption(
                    id="b",
                    text=LocalizedText(
                        nl="Negeer lift — zaal heeft geen hoogtegrenzen",
                        en="Ignore lift — indoor has no height concerns",
                    ),
                ),
                QuizOption(
                    id="c",
                    text=LocalizedText(
                        nl=(
                            "Korte besliscyclus: lift/veiligheid + "
                            "bandenspel meewegen"
                        ),
                        en=(
                            "Short decision cycle: weigh lift/safety + "
                            "board play"
                        ),
                    ),
                ),
                QuizOption(
                    id="d",
                    text=LocalizedText(
                        nl="Altijd fluiten zodra de bal de band raakt",
                        en="Always blow when the ball hits the boards",
                    ),
                ),
            ],
            correct_option_id="c",
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Juist: zaal vraagt snellere cycli rond lift, "
                        "veiligheid en bandenrebound — niet veldlogica "
                        "kopiëren."
                    ),
                    en=(
                        "Correct: indoor needs faster cycles around lift, "
                        "safety and board rebound — do not copy outdoor "
                        "logic."
                    ),
                ),
                visualization_hint="indoor-rebound",
            ),
            feedback_incorrect={
                "a": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Nee — zaal ≠ veld; context verschilt.",
                        en="No — indoor ≠ outdoor; context differs.",
                    ),
                    visualization_hint="indoor-rebound",
                ),
                "b": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Nee — lift blijft een veiligheidsfactor.",
                        en="No — lift remains a safety factor.",
                    ),
                    visualization_hint="indoor-rebound",
                ),
                "d": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Nee — bandcontact is normaal in zaal.",
                        en="No — board contact is normal indoors.",
                    ),
                    visualization_hint="indoor-rebound",
                ),
            },
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Kies de korte besliscyclus met lift + banden.",
                    en="Choose the short cycle with lift + boards.",
                ),
                visualization_hint="indoor-rebound",
            ),
        ),
        QuizQuestion(
            id="q3-pathway-management",
            type="multiple_choice",
            prompt=LocalizedText(
                nl=(
                    "Pathway-scenario: Hoofdklasse-tempo, emoties stijgen. "
                    "Welke houding past bij professioneel matchmanagement?"
                ),
                en=(
                    "Pathway scenario: Hoofdklasse tempo, emotions rise. "
                    "Which stance fits professional match management?"
                ),
            ),
            options=[
                QuizOption(
                    id="a",
                    text=LocalizedText(
                        nl="Alleen vóór de wedstrijd voorbereiden, daarna improviseren",
                        en="Prepare only before the match, then improvise",
                    ),
                ),
                QuizOption(
                    id="b",
                    text=LocalizedText(
                        nl="Alleen ná afloop reflecteren; tijdens negeren",
                        en="Only reflect afterward; ignore during play",
                    ),
                ),
                QuizOption(
                    id="c",
                    text=LocalizedText(
                        nl=(
                            "Vóór / tijdens / ná: voorbereiden, sturen, "
                            "nabespreken"
                        ),
                        en=(
                            "Before / during / after: prepare, manage, "
                            "debrief"
                        ),
                    ),
                ),
                QuizOption(
                    id="d",
                    text=LocalizedText(
                        nl="Laat je partner alle communicatie doen",
                        en="Let your partner handle all communication",
                    ),
                ),
            ],
            correct_option_id="c",
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Juist: professioneel ritme dekt vóór, tijdens én "
                        "ná — niet één moment."
                    ),
                    en=(
                        "Correct: professional cadence covers before, "
                        "during and after — not a single moment."
                    ),
                ),
                visualization_hint="match-pressure",
            ),
            feedback_incorrect={
                "a": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Nee — management loopt door tijdens de match.",
                        en="No — management continues during the match.",
                    ),
                    visualization_hint="match-pressure",
                ),
                "b": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Nee — nabespreken alleen is te laat.",
                        en="No — debrief alone is too late.",
                    ),
                    visualization_hint="consistency-loop",
                ),
                "d": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Nee — partners delen lead/support, niet alles afschuiven.",
                        en="No — partners share lead/support, not dump everything.",
                    ),
                    visualization_hint="partner-handoff",
                ),
            },
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Kies vóór / tijdens / ná als managementritme.",
                    en="Choose before / during / after as the management rhythm.",
                ),
                visualization_hint="match-pressure",
            ),
        ),
        QuizQuestion(
            id="q4-interpretation-source",
            type="multiple_choice",
            prompt=LocalizedText(
                nl=(
                    "Interpretatiescenario: je twijfelt over een NL "
                    "toelichting. Waar haal je de officiële bron "
                    "(pedagogisch)?"
                ),
                en=(
                    "Interpretation scenario: you doubt an NL clarification. "
                    "Where do you get the official source (pedagogical)?"
                ),
            ),
            options=[
                QuizOption(
                    id="a",
                    text=LocalizedText(
                        nl="Alleen uit deze cursus-repo",
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
                        nl="Willekeurige highlight-reels",
                        en="Random highlight reels",
                    ),
                ),
                QuizOption(
                    id="d",
                    text=LocalizedText(
                        nl="Alleen Engelse fansites",
                        en="English fansites only",
                    ),
                ),
            ],
            correct_option_id="b",
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Juist: de cursus linkt naar KNHB/FIH; die zijn de "
                        "officiële bron, niet de repo."
                    ),
                    en=(
                        "Correct: the course links to KNHB/FIH; those are "
                        "the official sources, not the repo."
                    ),
                ),
                visualization_hint="source-stack",
            ),
            feedback_incorrect={
                "a": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Nee — de repo is pedagogiek + links.",
                        en="No — the repo is pedagogy + links.",
                    ),
                    visualization_hint="source-stack",
                ),
                "c": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Nee — highlights zijn geen officiële bron.",
                        en="No — highlights are not an official source.",
                    ),
                    visualization_hint="attribution-chain",
                ),
                "d": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Nee — gebruik KNHB/FIH-kanalen.",
                        en="No — use KNHB/FIH channels.",
                    ),
                    visualization_hint="source-stack",
                ),
            },
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Kies officiële KNHB-/FIH-bronnen.",
                    en="Choose official KNHB/FIH sources.",
                ),
                visualization_hint="source-stack",
            ),
        ),
        QuizQuestion(
            id="q5-safety-keyword",
            type="written",
            prompt=LocalizedText(
                nl=(
                    "Welk Engels sleutelwoord hoort bij de hoogste prioriteit "
                    "over veld én zaal heen? (één woord)"
                ),
                en=(
                    "Which English keyword belongs with the highest priority "
                    "across field and indoor? (one word)"
                ),
            ),
            accepted_answers=["safety"],
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl="Juist: safety — overal de eerste filter.",
                    en="Correct: safety — the first filter everywhere.",
                ),
                visualization_hint="safety-triangle",
            ),
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Verwacht antwoord: safety.",
                    en="Expected answer: safety.",
                ),
                visualization_hint="safety-triangle",
            ),
        ),
        QuizQuestion(
            id="q6-capstone-keyword",
            type="written",
            prompt=LocalizedText(
                nl=(
                    "Welk Engels sleutelwoord beschrijft deze "
                    "eindtoets die veld, zaal, pad en interpretatie "
                    "samenbindt? (één woord)"
                ),
                en=(
                    "Which English keyword describes this final assessment "
                    "binding field, indoor, pathway and interpretation? "
                    "(one word)"
                ),
            ),
            accepted_answers=["capstone", "synthesis", "integration"],
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Juist: capstone / synthesis / integration — "
                        "domeinen weven tot één toets."
                    ),
                    en=(
                        "Correct: capstone / synthesis / integration — "
                        "domains weave into one assessment."
                    ),
                ),
                visualization_hint="capstone-weave",
            ),
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Verwacht o.a.: capstone, synthesis of "
                        "integration."
                    ),
                    en=(
                        "Expected e.g.: capstone, synthesis, or "
                        "integration."
                    ),
                ),
                visualization_hint="capstone-weave",
            ),
        ),
    ],
)

CAPSTONE_MODULE = ModuleStub(
    id="mod-capstone-assessment",
    kind="shared",
    title=LocalizedText(
        nl="Capstone-toets: veld · zaal · pad · interpretatie",
        en="Capstone assessment: field · indoor · pathway · interpretation",
    ),
    summary=LocalizedText(
        nl=(
            "Eindtoets die scenario's uit veld- en zaalregels, het "
            "professionele pad en de KNHB-interpretatielaag combineert — "
            "met MC + geschreven vragen, feedback en visuals."
        ),
        en=(
            "Final assessment combining scenarios from field and indoor "
            "rules, the professional pathway and the KNHB interpretation "
            "layer — with MC + written items, feedback and visuals."
        ),
    ),
    learning_objectives=[
        LocalizedText(
            nl="Veldveiligheid en voordeel in een scenario prioriteren.",
            en="Prioritize field safety and advantage in a scenario.",
        ),
        LocalizedText(
            nl="Zaal-specifieke lift-/bandenlogica toepassen.",
            en="Apply indoor-specific lift/board logic.",
        ),
        LocalizedText(
            nl="Professioneel matchmanagement (vóór/tijdens/ná) herkennen.",
            en="Recognize professional match management (before/during/after).",
        ),
        LocalizedText(
            nl="Officiële FIH/KNHB-bronnen boven cursusgeheugen zetten.",
            en="Put official FIH/KNHB sources above course memory alone.",
        ),
        LocalizedText(
            nl="Domeinen (veld/zaal/pad/interpretatie) tot één oordeel weven.",
            en="Weave domains (field/indoor/pathway/interpretation) into one judgment.",
        ),
    ],
    instruction_outline=[
        LocalizedText(
            nl="Herhaal de vier eerdere modules kort.",
            en="Briefly revisit the four prior modules.",
        ),
        LocalizedText(
            nl="Lees de scenario's; gebruik visuals als denkankers.",
            en="Read the scenarios; use visuals as thinking anchors.",
        ),
        LocalizedText(
            nl="Maak de gemengde MC + geschreven toets.",
            en="Take the mixed MC + written assessment.",
        ),
        LocalizedText(
            nl="Sla voortgang op via je sessie.",
            en="Save progress via your session.",
        ),
    ],
    content_status="full",
    sections=[
        LearningSection(
            id="sec-capstone-purpose",
            title=LocalizedText(
                nl="Waarom een capstone",
                en="Why a capstone",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Losse modules oefenen deelvaardigheden. De "
                        "capstone vraagt je om veld, zaal, professioneel "
                        "pad én interpretatiebronnen in één "
                        "beslismoment te combineren — zoals in een "
                        "echte wedstrijdweek."
                    ),
                    en=(
                        "Separate modules practice part-skills. The "
                        "capstone asks you to combine field, indoor, "
                        "professional pathway and interpretation sources "
                        "in one decision moment — as in a real match week."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Alles hier blijft oorspronkelijke pedagogiek of "
                        "een plaatshouder. Officiële FIH/KNHB-teksten "
                        "staan bij de bond."
                    ),
                    en=(
                        "Everything here remains original pedagogy or a "
                        "placeholder. Official FIH/KNHB texts live with "
                        "the federations."
                    ),
                ),
            ],
            visual_id="viz-capstone-weave",
        ),
        LearningSection(
            id="sec-capstone-field",
            title=LocalizedText(
                nl="Veldanker: veiligheid in de cirkelzone",
                en="Field anchor: safety near the circle",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Denk terug aan zones, gevaarlijke richting en "
                        "voordeel. Capstone-scenario's testen of "
                        "veiligheid jouw eerste filter blijft."
                    ),
                    en=(
                        "Recall zones, dangerous direction and advantage. "
                        "Capstone scenarios test whether safety stays "
                        "your first filter."
                    ),
                ),
            ],
            visual_id="viz-scenario-field",
        ),
        LearningSection(
            id="sec-capstone-indoor",
            title=LocalizedText(
                nl="Zaalanker: lift & banden onder tempo",
                en="Indoor anchor: lift & boards under tempo",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Zaal verkort je besliscyclus. Lift, rebound van "
                        "de band en krappe ruimte vragen om scherp "
                        "onderscheid met veldlogica."
                    ),
                    en=(
                        "Indoor shortens your decision cycle. Lift, board "
                        "rebound and tight space demand a sharp split "
                        "from outdoor logic."
                    ),
                ),
            ],
            visual_id="viz-scenario-indoor",
        ),
        LearningSection(
            id="sec-capstone-pathway",
            title=LocalizedText(
                nl="Padanker: ritme vóór / tijdens / ná",
                en="Pathway anchor: cadence before / during / after",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Professioneel niveau is niet alleen regels kennen: "
                        "het is matchmanagement, partnerhandoff en "
                        "consistente communicatie."
                    ),
                    en=(
                        "Professional level is not only knowing rules: it "
                        "is match management, partner handoff and "
                        "consistent communication."
                    ),
                ),
            ],
            visual_id="viz-scenario-pathway",
        ),
        LearningSection(
            id="sec-capstone-interp",
            title=LocalizedText(
                nl="Interpretatieanker: bronnen boven geheugen",
                en="Interpretation anchor: sources over memory",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Bij twijfel: FIH → KNHB → club. De cursus "
                        "vervangt geen officiële interpretatie; gebruik "
                        "links en attributie."
                    ),
                    en=(
                        "When unsure: FIH → KNHB → club. The course does "
                        "not replace official interpretation; use links "
                        "and attribution."
                    ),
                ),
            ],
            visual_id="viz-scenario-interp",
        ),
        LearningSection(
            id="sec-capstone-practice",
            title=LocalizedText(
                nl="Toetsen en voortgang",
                en="Assess and progress",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Maak de gemengde toets hieronder (MC + "
                        "geschreven). Perfecte score markeert de module "
                        "voltooid via je sessie. Heropen eerdere modules "
                        "via het voortgangsoverzicht als iets hapert."
                    ),
                    en=(
                        "Take the mixed assessment below (MC + written). "
                        "A perfect score marks the module complete via "
                        "your session. Reopen earlier modules from the "
                        "progress overview if something sticks."
                    ),
                ),
            ],
            visual_id="viz-capstone-knhb-slot",
        ),
    ],
    visuals=CAPSTONE_VISUALS,
    interpretation_references=CAPSTONE_REFERENCES,
    quiz_id=CAPSTONE_QUIZ.id,
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
