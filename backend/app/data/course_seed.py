"""Bilingual course outline: one full module + remaining stubs.

Do NOT invent copyrighted FIH/KNHB rule text or illustrations.
Attribution hooks and official-source links only.
"""

from app.data.module_intro_role import INTRO_MODULE, INTRO_QUIZ
from app.schemas import (
    Attribution,
    CourseOutline,
    FurtherReading,
    LocalizedText,
    ModuleStub,
    Quiz,
    QuizFeedback,
    QuizOption,
    QuizQuestion,
)

KNHB_RULES_NOTE = LocalizedText(
    nl=(
        "Verwijs altijd naar de officiële FIH-regels en KNHB-interpretaties. "
        "Deze cursus bevat geen overgenomen auteursrechtelijk beschermde "
        "regeltekst of KNHB-illustraties. Plaatshouders voor EN-vertaling "
        "van KNHB-interpretaties volgen later."
    ),
    en=(
        "Always refer to the official FIH Rules and KNHB interpretations. "
        "This course does not reproduce copyrighted rule text or KNHB "
        "illustrations. Placeholders for EN translation of KNHB "
        "interpretations will follow later."
    ),
)

OFFICIAL_ATTRIBUTIONS: list[Attribution] = [
    Attribution(
        source_name="FIH Rules of Hockey",
        source_url="https://www.fih.hockey/inside-fih/our-official-documents/rules-of-hockey",
        note=LocalizedText(
            nl="Officiële FIH Rules of Hockey — bron voor veldhockeyregels.",
            en="Official FIH Rules of Hockey — source for outdoor hockey rules.",
        ),
        knhb_illustration_placeholder=False,
        translation_needed=False,
    ),
    Attribution(
        source_name="FIH Indoor Hockey Rules",
        source_url="https://www.fih.hockey/inside-fih/our-official-documents/rules-of-hockey",
        note=LocalizedText(
            nl="Officiële FIH Indoor Hockey Rules — bron voor zaalhockeyregels.",
            en="Official FIH Indoor Hockey Rules — source for indoor hockey rules.",
        ),
        knhb_illustration_placeholder=False,
        translation_needed=False,
    ),
    Attribution(
        source_name="KNHB — regels & interpretaties",
        source_url="https://www.knhb.nl/",
        note=LocalizedText(
            nl=(
                "[PLACEHOLDER] Link naar KNHB-interpretaties / scheidsrechtersmateriaal. "
                "Geen KNHB-illustraties inbegrepen. EN-vertaling van interpretaties: TODO."
            ),
            en=(
                "[PLACEHOLDER] Link to KNHB interpretations / umpire materials. "
                "No KNHB illustrations included. EN translation of interpretations: TODO."
            ),
        ),
        knhb_illustration_placeholder=True,
        translation_needed=True,
    ),
]

SAMPLE_QUIZ = Quiz(
    id="quiz-dangerous-play-basics",
    title=LocalizedText(
        nl="Quiz: gevaarlijk spel (basis)",
        en="Quiz: dangerous play (basics)",
    ),
    questions=[
        QuizQuestion(
            id="q1-raised-ball",
            type="multiple_choice",
            prompt=LocalizedText(
                nl=(
                    "Een speler slaat de bal hard omhoog in de richting van een "
                    "tegenstander op korte afstand. Wat is de beste eerste "
                    "overweging voor de scheidsrechter?"
                ),
                en=(
                    "A player hits the ball hard and raised toward an opponent "
                    "at close range. What is the umpire’s best first consideration?"
                ),
            ),
            options=[
                QuizOption(
                    id="a",
                    text=LocalizedText(
                        nl="Altijd direct een groene kaart geven.",
                        en="Always award a green card immediately.",
                    ),
                ),
                QuizOption(
                    id="b",
                    text=LocalizedText(
                        nl=(
                            "Beoordelen of de actie gevaarlijk is (richting, "
                            "afstand, snelheid) en passend fluiten/sanctioneren."
                        ),
                        en=(
                            "Assess whether the action is dangerous (direction, "
                            "distance, speed) and whistle/sanction appropriately."
                        ),
                    ),
                ),
                QuizOption(
                    id="c",
                    text=LocalizedText(
                        nl="Alleen fluiten als de bal daadwerkelijk iemand raakt.",
                        en="Only whistle if the ball actually hits someone.",
                    ),
                ),
                QuizOption(
                    id="d",
                    text=LocalizedText(
                        nl="Speel doorlaten; omhoog spelen is altijd toegestaan.",
                        en="Play on; raising the ball is always allowed.",
                    ),
                ),
            ],
            correct_option_id="b",
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Juist. Gevaarlijk spel hangt af van context: richting, "
                        "afstand en snelheid. Consulteer FIH-regels/KNHB-"
                        "interpretaties voor de actuele standaard."
                    ),
                    en=(
                        "Correct. Dangerous play depends on context: direction, "
                        "distance and speed. Consult FIH rules / KNHB "
                        "interpretations for the current standard."
                    ),
                ),
                visualization_hint="timeline: raise → proximity → risk assessment",
            ),
            feedback_incorrect={
                "a": QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Niet altijd. Kaarten zijn situationeel; eerst "
                            "beoordelen of (en hoe) de actie gevaarlijk was."
                        ),
                        en=(
                            "Not always. Cards are situational; first assess "
                            "whether (and how) the action was dangerous."
                        ),
                    ),
                    visualization_hint="decision-tree: danger → advantage → card level",
                ),
                "c": QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Onjuist. Gevaar kan bestaan zonder contact; "
                            "nabijheid en traject tellen mee."
                        ),
                        en=(
                            "Incorrect. Danger can exist without contact; "
                            "proximity and trajectory matter."
                        ),
                    ),
                    visualization_hint="ball-path near defender silhouette (stub viz)",
                ),
                "d": QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Onjuist. Omhoog spelen is niet onvoorwaardelijk "
                            "toegestaan wanneer het gevaarlijk is."
                        ),
                        en=(
                            "Incorrect. Raising the ball is not unconditionally "
                            "allowed when it is dangerous."
                        ),
                    ),
                ),
            },
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Bekijk de officiële regels voor gevaarlijk spel.",
                    en="Review the official rules on dangerous play.",
                ),
            ),
        ),
        QuizQuestion(
            id="q2-advantage-keyword",
            type="written",
            prompt=LocalizedText(
                nl=(
                    "Welk Engels sleutelwoord gebruiken scheidsrechters vaak "
                    "wanneer ze een overtreding ‘doorlaten’ ten voordele van "
                    "het aangevallen team? (één woord)"
                ),
                en=(
                    "Which English keyword do umpires often use when allowing "
                    "play to continue after an offence that benefits the "
                    "attacking team? (one word)"
                ),
            ),
            accepted_answers=["advantage", "advantage!"],
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl="Juist — ‘advantage’ (voordeel) is het gangbare signaalwoord.",
                    en="Correct — ‘advantage’ is the common signal word.",
                ),
            ),
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Het verwachte antwoord is ‘advantage’. Zie FIH "
                        "umpire signals / KNHB-materiaal voor gebaren."
                    ),
                    en=(
                        "The expected answer is ‘advantage’. See FIH umpire "
                        "signals / KNHB materials for gestures."
                    ),
                ),
                visualization_hint="umpire arm signal stub — link official chart",
            ),
        ),
    ],
)

INDOOR_QUIZ = Quiz(
    id="quiz-indoor-context-basics",
    title=LocalizedText(
        nl="Quiz: zaalcontext (basis)",
        en="Quiz: indoor context (basics)",
    ),
    questions=[
        QuizQuestion(
            id="q1-indoor-space",
            type="multiple_choice",
            prompt=LocalizedText(
                nl=(
                    "In zaalhockey is de speelruimte kleiner en sneller dan op "
                    "het veld. Wat is de beste eerste aanpassing voor de "
                    "scheidsrechter (pedagogisch kader — geen regelcitaat)?"
                ),
                en=(
                    "Indoor hockey has less space and a faster tempo than outdoor. "
                    "What is the umpire’s best first adjustment (pedagogical "
                    "frame — not a rules quotation)?"
                ),
            ),
            options=[
                QuizOption(
                    id="a",
                    text=LocalizedText(
                        nl="Alles hetzelfde fluiten als op het veld; context telt niet.",
                        en="Whistle exactly as outdoors; context does not matter.",
                    ),
                ),
                QuizOption(
                    id="b",
                    text=LocalizedText(
                        nl=(
                            "Anticiperen: dichter bij het spel blijven, sneller "
                            "scannen op botsingen bij de banden, en eerder "
                            "communiceren."
                        ),
                        en=(
                            "Anticipate: stay closer to play, scan earlier for "
                            "board collisions, and communicate sooner."
                        ),
                    ),
                ),
                QuizOption(
                    id="c",
                    text=LocalizedText(
                        nl="Alleen bij de goal blijven; middenveld negeren.",
                        en="Stay only at the goal; ignore midfield.",
                    ),
                ),
                QuizOption(
                    id="d",
                    text=LocalizedText(
                        nl="Nooit fluiten bij contact met de band.",
                        en="Never whistle for contact with the boards.",
                    ),
                ),
            ],
            correct_option_id="b",
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Juist. Zaal vraagt snellere positionering en scanpatronen. "
                        "Raadpleeg officiële FIH Indoor Rules / KNHB-materiaal "
                        "voor actuele voorschriften — hier alleen een "
                        "besliskader."
                    ),
                    en=(
                        "Correct. Indoor requires faster positioning and scan "
                        "patterns. Consult official FIH Indoor Rules / KNHB "
                        "materials for current prescriptions — this is a "
                        "decision frame only."
                    ),
                ),
                visualization_hint="court scan: boards → mid → circle",
            ),
            feedback_incorrect={
                "a": QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Onjuist. Tempo en ruimte veranderen hoe je kijkt en "
                            "wanneer je communiceert — niet per se de ethiek, "
                            "wel de uitvoering."
                        ),
                        en=(
                            "Incorrect. Tempo and space change how you look and "
                            "when you communicate — not necessarily ethics, but "
                            "execution."
                        ),
                    ),
                ),
                "c": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Onjuist. Het hele veld (zaal) blijft relevant.",
                        en="Incorrect. The whole court remains relevant.",
                    ),
                ),
                "d": QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Onjuist. Bandenspel kan veilig of problematisch zijn; "
                            "context beoordelen. Zie officiële bronnen."
                        ),
                        en=(
                            "Incorrect. Play off the boards can be safe or not; "
                            "assess context. See official sources."
                        ),
                    ),
                ),
            },
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Herlees het zaal-modulekader en link naar FIH Indoor Rules.",
                    en="Revisit the indoor module frame and link to FIH Indoor Rules.",
                ),
            ),
        ),
        QuizQuestion(
            id="q2-indoor-keyword",
            type="written",
            prompt=LocalizedText(
                nl=(
                    "Welk Engels woord gebruikt deze cursus voor zaalhockey "
                    "(het overdekte format)? (één woord)"
                ),
                en=(
                    "Which English word does this course use for hall/covered "
                    "hockey (zaalhockey)? (one word)"
                ),
            ),
            accepted_answers=["indoor"],
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl="Juist — ‘indoor’ (zaalhockey).",
                    en="Correct — ‘indoor’.",
                ),
            ),
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Verwacht antwoord: indoor.",
                    en="Expected answer: indoor.",
                ),
            ),
        ),
    ],
)

MODULES: list[ModuleStub] = [
    INTRO_MODULE,
    ModuleStub(
        id="mod-field-danger",
        kind="field",
        title=LocalizedText(
            nl="Veld: gevaarlijk spel & omhoog spelen",
            en="Field: dangerous play & raised ball",
        ),
        summary=LocalizedText(
            nl="Contextueel beoordelen van gevaar op het veld.",
            en="Contextual assessment of danger on the outdoor pitch.",
        ),
        learning_objectives=[
            LocalizedText(
                nl="Herkennen van factoren die een omhoog gespeelde bal gevaarlijk maken.",
                en="Identify factors that make a raised ball dangerous.",
            ),
        ],
        instruction_outline=[
            LocalizedText(
                nl="[Instructie-stub] Afstand, richting, snelheid — besliskader.",
                en="[Instruction stub] Distance, direction, speed — decision frame.",
            ),
            LocalizedText(
                nl=(
                    "[KNHB-illustratie PLACEHOLDER] Officiële interpretatie/"
                    "illustratie hier linken — geen asset inbegrepen. EN-vertaling TODO."
                ),
                en=(
                    "[KNHB illustration PLACEHOLDER] Link official interpretation/"
                    "illustration here — no asset included. EN translation TODO."
                ),
            ),
        ],
        content_status="stub",
        quiz_id="quiz-dangerous-play-basics",
        further_reading=[
            FurtherReading(
                title=LocalizedText(
                    nl="KNHB interpretaties (placeholder-link)",
                    en="KNHB interpretations (placeholder link)",
                ),
                url="https://www.knhb.nl/",
                attribution=OFFICIAL_ATTRIBUTIONS[2],
            ),
        ],
        order=2,
    ),
    ModuleStub(
        id="mod-indoor-basics",
        kind="indoor",
        title=LocalizedText(
            nl="Zaal: basisverschillen met veld",
            en="Indoor: key differences from outdoor",
        ),
        summary=LocalizedText(
            nl="Snelheid, ruimte en regelaccenten in zaalhockey.",
            en="Pace, space and rule emphases in indoor hockey.",
        ),
        learning_objectives=[
            LocalizedText(
                nl="Noemen van typische zaalverschillen relevant voor scheidsrechters.",
                en="List typical indoor differences relevant to umpires.",
            ),
        ],
        instruction_outline=[
            LocalizedText(
                nl="[Instructie-stub] Bandenspel, lifting, tempo van beslissingen.",
                en="[Instruction stub] Boards, lifting, decision tempo.",
            ),
        ],
        content_status="stub",
        quiz_id="quiz-indoor-context-basics",
        further_reading=[
            FurtherReading(
                title=LocalizedText(
                    nl="FIH Indoor Hockey Rules (officieel)",
                    en="FIH Indoor Hockey Rules (official)",
                ),
                url="https://www.fih.hockey/inside-fih/our-official-documents/rules-of-hockey",
                attribution=OFFICIAL_ATTRIBUTIONS[1],
            ),
        ],
        order=3,
    ),
    ModuleStub(
        id="mod-pathway-hoofdklasse",
        kind="shared",
        title=LocalizedText(
            nl="Pad naar professioneel niveau (o.a. Hoofdklasse)",
            en="Pathway toward professional standard (e.g. Hoofdklasse)",
        ),
        summary=LocalizedText(
            nl="Wat ‘professioneel standaard’ betekent in NL-context (stub).",
            en="What ‘professional standard’ means in the NL context (stub).",
        ),
        learning_objectives=[
            LocalizedText(
                nl="Schetsen van een ontwikkelpad van clubniveau naar topcompetitie.",
                en="Outline a development path from club level toward top competition.",
            ),
        ],
        instruction_outline=[
            LocalizedText(
                nl="[Instructie-stub] Mentoring, video-review, fitness, game management.",
                en="[Instruction stub] Mentoring, video review, fitness, game management.",
            ),
        ],
        content_status="stub",
        quiz_id=None,
        further_reading=[],
        order=4,
    ),
]


def get_course_outline() -> CourseOutline:
    return CourseOutline(
        id="nl-hockey-umpire-v0",
        title=LocalizedText(
            nl="Nederlandse veld- & zaalhockey scheidsrechterscursus",
            en="Dutch field & indoor hockey umpiring course",
        ),
        description=LocalizedText(
            nl=(
                "Eerste volledige module (intro rol) plus verdere stubs; "
                "quiz met feedback en sessievoortgang. "
                + KNHB_RULES_NOTE.nl
            ),
            en=(
                "First full module (intro role) plus further stubs; "
                "quiz with feedback and session progress. "
                + KNHB_RULES_NOTE.en
            ),
        ),
        modules=MODULES,
        quizzes={
            INTRO_QUIZ.id: INTRO_QUIZ,
            SAMPLE_QUIZ.id: SAMPLE_QUIZ,
            INDOOR_QUIZ.id: INDOOR_QUIZ,
        },
        attributions=OFFICIAL_ATTRIBUTIONS,
    )
