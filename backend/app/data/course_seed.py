"""Minimal bilingual course outline + sample quiz (v0 stubs).

Do NOT invent copyrighted FIH/KNHB rule text or illustrations.
Attribution hooks and official-source links only.
"""

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

MODULES: list[ModuleStub] = [
    ModuleStub(
        id="mod-intro-role",
        kind="shared",
        title=LocalizedText(
            nl="Introductie: rol van de scheidsrechter",
            en="Introduction: the umpire’s role",
        ),
        summary=LocalizedText(
            nl="Veiligheid, consistentie en communicatie als basis.",
            en="Safety, consistency and communication as foundations.",
        ),
        learning_objectives=[
            LocalizedText(
                nl="Beschrijven van de primaire verantwoordelijkheden van de scheidsrechter.",
                en="Describe the umpire’s primary responsibilities.",
            ),
            LocalizedText(
                nl="Onderscheiden van veld- en zaalhockeycontext op hoog niveau.",
                en="Distinguish field vs indoor context at a high level.",
            ),
        ],
        instruction_outline=[
            LocalizedText(
                nl="[Instructie-stub] Positionering, blikrichting, teamwork met collega.",
                en="[Instruction stub] Positioning, scanning, teamwork with partner.",
            ),
            LocalizedText(
                nl="[Instructie-stub] Communicatie met spelers en coaches.",
                en="[Instruction stub] Communicating with players and coaches.",
            ),
        ],
        quiz_id=None,
        further_reading=[
            FurtherReading(
                title=LocalizedText(
                    nl="FIH Rules of Hockey (officieel)",
                    en="FIH Rules of Hockey (official)",
                ),
                url="https://www.fih.hockey/inside-fih/our-official-documents/rules-of-hockey",
                attribution=OFFICIAL_ATTRIBUTIONS[0],
            ),
        ],
        order=1,
    ),
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
        quiz_id=None,
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
                "v0-scaffold: modules, quiz met feedback, voortgang. "
                + KNHB_RULES_NOTE.nl
            ),
            en=(
                "v0 scaffold: modules, quiz with feedback, progress. "
                + KNHB_RULES_NOTE.en
            ),
        ),
        modules=MODULES,
        quizzes={SAMPLE_QUIZ.id: SAMPLE_QUIZ},
        attributions=OFFICIAL_ATTRIBUTIONS,
    )
