"""Bilingual course outline: full modules + remaining stubs.

Do NOT invent copyrighted FIH/KNHB rule text or illustrations.
Attribution hooks and official-source links only.
"""

from app.data.module_field_rules import FIELD_MODULE, FIELD_QUIZ
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
    FIELD_MODULE,
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
                "Volledige modules (intro rol + veld kernregels) plus verdere "
                "stubs; quiz met feedback en sessievoortgang. "
                + KNHB_RULES_NOTE.nl
            ),
            en=(
                "Full modules (intro role + field core rules) plus further "
                "stubs; quiz with feedback and session progress. "
                + KNHB_RULES_NOTE.en
            ),
        ),
        modules=MODULES,
        quizzes={
            INTRO_QUIZ.id: INTRO_QUIZ,
            FIELD_QUIZ.id: FIELD_QUIZ,
            INDOOR_QUIZ.id: INDOOR_QUIZ,
        },
        attributions=OFFICIAL_ATTRIBUTIONS,
    )
