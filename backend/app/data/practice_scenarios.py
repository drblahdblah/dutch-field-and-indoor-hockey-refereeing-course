"""Practice decision scenario bank (field + indoor) — separate from module lessons.

Pedagogical framing only — no reproduced FIH/KNHB copyrighted rule text or art.
"""

from app.schemas import (
    LocalizedText,
    PracticeBank,
    PracticeScenario,
    Quiz,
    QuizFeedback,
    QuizOption,
    QuizQuestion,
)

_FIH_NOTE_NL = (
    "Raadpleeg altijd de officiële FIH-regels en KNHB-interpretaties voor de "
    "actuele standaard — dit is een oefenkader, geen regelcitaat."
)
_FIH_NOTE_EN = (
    "Always consult official FIH rules and KNHB interpretations for the current "
    "standard — this is a practice frame, not a rules quote."
)


def _mc(
    question_id: str,
    prompt: LocalizedText,
    options: list[QuizOption],
    correct: str,
    ok: QuizFeedback,
    bad: dict[str, QuizFeedback],
    default_bad: QuizFeedback,
) -> QuizQuestion:
    return QuizQuestion(
        id=question_id,
        type="multiple_choice",
        prompt=prompt,
        options=options,
        correct_option_id=correct,
        feedback_correct=ok,
        feedback_incorrect=bad,
        feedback_incorrect_default=default_bad,
    )


def _written(
    question_id: str,
    prompt: LocalizedText,
    accepted: list[str],
    ok: QuizFeedback,
    bad: QuizFeedback,
) -> QuizQuestion:
    return QuizQuestion(
        id=question_id,
        type="written",
        prompt=prompt,
        accepted_answers=accepted,
        feedback_correct=ok,
        feedback_incorrect_default=bad,
    )


SCENARIO_FIELD_RAISED = PracticeScenario(
    id="practice-field-raised-circle",
    kind="field",
    title=LocalizedText(
        nl="Veld: omhoog in de cirkelaanloop",
        en="Field: raised ball into the circle approach",
    ),
    situation=LocalizedText(
        nl=(
            "Aanval bouwt op vanuit de 23m. De bal wordt hard en omhoog "
            "gespeeld richting een verdediger die dicht bij de cirkel staat. "
            "Jij leest richting, afstand en snelheid terwijl je partner de "
            "andere helft scant. Wat is je beste eerste besluitlijn?"
        ),
        en=(
            "Attack builds from the 23m. The ball is played hard and raised "
            "toward a defender standing near the circle. You read direction, "
            "distance and speed while your partner scans the other half. What "
            "is your best first decision line?"
        ),
    ),
    focus=LocalizedText(
        nl="Gevaar wegen vóór automatische sanctie",
        en="Weigh danger before an automatic sanction",
    ),
    order=1,
    visual_key="practice-circle-entry",
    quiz=Quiz(
        id="quiz-practice-field-raised-circle",
        title=LocalizedText(
            nl="Oefening: omhoog naar de cirkel",
            en="Practice: raised toward the circle",
        ),
        questions=[
            _mc(
                "q1-first-read",
                LocalizedText(
                    nl="Wat is de beste eerste overweging?",
                    en="What is the best first consideration?",
                ),
                [
                    QuizOption(
                        id="a",
                        text=LocalizedText(
                            nl="Direct groene kaart — omhoog is altijd fout.",
                            en="Green card immediately — raised is always illegal.",
                        ),
                    ),
                    QuizOption(
                        id="b",
                        text=LocalizedText(
                            nl=(
                                "Beoordeel gevaar (richting × afstand × snelheid) "
                                "en fluit/sanctioneer passend."
                            ),
                            en=(
                                "Assess danger (direction × distance × speed) and "
                                "whistle/sanction appropriately."
                            ),
                        ),
                    ),
                    QuizOption(
                        id="c",
                        text=LocalizedText(
                            nl="Alleen fluiten als de bal iemand raakt.",
                            en="Only whistle if the ball hits someone.",
                        ),
                    ),
                    QuizOption(
                        id="d",
                        text=LocalizedText(
                            nl="Speel altijd door voor flow bij een aanval.",
                            en="Always play on for flow during an attack.",
                        ),
                    ),
                ],
                "b",
                QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Juist. Context bepaalt gevaar; kaarten zijn middelen, "
                            "geen reflex. " + _FIH_NOTE_NL
                        ),
                        en=(
                            "Correct. Context defines danger; cards are tools, not "
                            "a reflex. " + _FIH_NOTE_EN
                        ),
                    ),
                    visualization_hint="practice-circle-entry",
                ),
                {
                    "a": QuizFeedback(
                        explanation=LocalizedText(
                            nl="Te snel. Eerst gevaar wegen, dan pas sanctioneren.",
                            en="Too fast. Weigh danger first, then sanction.",
                        ),
                        visualization_hint="practice-circle-entry",
                    ),
                    "c": QuizFeedback(
                        explanation=LocalizedText(
                            nl="Gevaar kan bestaan zonder contact.",
                            en="Danger can exist without contact.",
                        ),
                        visualization_hint="practice-circle-entry",
                    ),
                    "d": QuizFeedback(
                        explanation=LocalizedText(
                            nl="Flow komt na veiligheid en eerlijkheid.",
                            en="Flow comes after safety and fairness.",
                        ),
                        visualization_hint="practice-circle-entry",
                    ),
                },
                QuizFeedback(
                    explanation=LocalizedText(
                        nl="Onjuist. Begin bij gevaarcontext. " + _FIH_NOTE_NL,
                        en="Incorrect. Start with danger context. " + _FIH_NOTE_EN,
                    ),
                    visualization_hint="practice-circle-entry",
                ),
            ),
            _written(
                "q2-danger-axes",
                LocalizedText(
                    nl=(
                        "Welk Engels sleutelwoord noemt één as van de "
                        "gevaar-driehoek in dit cursusmodel? (één woord)"
                    ),
                    en=(
                        "Which English keyword names one axis of the danger "
                        "triangle in this course model? (one word)"
                    ),
                ),
                [
                    "direction",
                    "distance",
                    "speed",
                ],
                QuizFeedback(
                    explanation=LocalizedText(
                        nl="Juist. Die drie assen structureren je scan. " + _FIH_NOTE_NL,
                        en="Correct. Those three axes structure your scan. "
                        + _FIH_NOTE_EN,
                    ),
                    visualization_hint="danger-cone",
                ),
                QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Verwacht: richting, afstand of snelheid "
                            "(direction / distance / speed)."
                        ),
                        en="Expected: direction, distance, or speed.",
                    ),
                    visualization_hint="danger-cone",
                ),
            ),
        ],
    ),
)

SCENARIO_FIELD_RESTART = PracticeScenario(
    id="practice-field-restart-23",
    kind="field",
    title=LocalizedText(
        nl="Veld: herstart bij de 23m",
        en="Field: restart near the 23m",
    ),
    situation=LocalizedText(
        nl=(
            "Vrije slag voor de aanvallende ploeg net buiten de 23m-band. "
            "Tegenstanders staan dichtbij; de aanvallers willen snel doorspelen "
            "richting cirkel. Jij moet het startbeeld leesbaar maken."
        ),
        en=(
            "Free hit for the attacking team just outside the 23m band. "
            "Opponents are tight; attackers want to play quickly toward the "
            "circle. You need a readable starting picture."
        ),
    ),
    focus=LocalizedText(
        nl="Bubbel van ruimte vóór snelle flow",
        en="Space bubble before quick flow",
    ),
    order=2,
    visual_key="practice-freehit-23",
    quiz=Quiz(
        id="quiz-practice-field-restart-23",
        title=LocalizedText(
            nl="Oefening: herstart bij 23m",
            en="Practice: restart near 23m",
        ),
        questions=[
            _mc(
                "q1-bubble-first",
                LocalizedText(
                    nl="Wat check je eerst bij deze herstart?",
                    en="What do you check first at this restart?",
                ),
                [
                    QuizOption(
                        id="a",
                        text=LocalizedText(
                            nl="Of de aanval al in de cirkel staat.",
                            en="Whether the attack is already inside the circle.",
                        ),
                    ),
                    QuizOption(
                        id="b",
                        text=LocalizedText(
                            nl=(
                                "Of er een leesbare ‘bubbel’ van ruimte rond de "
                                "herstartplek is vóór je flow toelaat."
                            ),
                            en=(
                                "Whether there is a readable space ‘bubble’ around "
                                "the restart spot before you allow flow."
                            ),
                        ),
                    ),
                    QuizOption(
                        id="c",
                        text=LocalizedText(
                            nl="Alleen de klok — tempo is belangrijker dan ruimte.",
                            en="Only the clock — tempo matters more than space.",
                        ),
                    ),
                    QuizOption(
                        id="d",
                        text=LocalizedText(
                            nl="Altijd eerst een kaart voor te dicht staan.",
                            en="Always card first for standing too close.",
                        ),
                    ),
                ],
                "b",
                QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Juist. Ruimte → veiligheid → flow. Exacte meters: "
                            "officiële bronnen. " + _FIH_NOTE_NL
                        ),
                        en=(
                            "Correct. Space → safety → flow. Exact metres: official "
                            "sources. " + _FIH_NOTE_EN
                        ),
                    ),
                    visualization_hint="practice-freehit-23",
                ),
                {
                    "a": QuizFeedback(
                        explanation=LocalizedText(
                            nl="Cirkelcontext komt na een veilig startbeeld.",
                            en="Circle context comes after a safe starting picture.",
                        ),
                        visualization_hint="practice-freehit-23",
                    ),
                    "c": QuizFeedback(
                        explanation=LocalizedText(
                            nl="Tempo zonder bubbel maakt het speelbeeld onleesbaar.",
                            en="Tempo without a bubble makes the picture unreadable.",
                        ),
                        visualization_hint="practice-freehit-23",
                    ),
                    "d": QuizFeedback(
                        explanation=LocalizedText(
                            nl="Kaarten zijn middelen; eerst ruimte herstellen.",
                            en="Cards are tools; restore space first.",
                        ),
                        visualization_hint="practice-freehit-23",
                    ),
                },
                QuizFeedback(
                    explanation=LocalizedText(
                        nl="Onjuist. Begin bij de herstartbubbel. " + _FIH_NOTE_NL,
                        en="Incorrect. Start with the restart bubble. " + _FIH_NOTE_EN,
                    ),
                    visualization_hint="practice-freehit-23",
                ),
            ),
            _written(
                "q2-bubble-keyword",
                LocalizedText(
                    nl=(
                        "Welk Engels sleutelwoord gebruikt deze cursus voor de "
                        "ruimte rond een herstart? (één woord)"
                    ),
                    en=(
                        "Which English keyword does this course use for the "
                        "space around a restart? (one word)"
                    ),
                ),
                ["bubble"],
                QuizFeedback(
                    explanation=LocalizedText(
                        nl="Juist. Denk in een leesbare bubbel. " + _FIH_NOTE_NL,
                        en="Correct. Think in a readable bubble. " + _FIH_NOTE_EN,
                    ),
                    visualization_hint="restart-bubble",
                ),
                QuizFeedback(
                    explanation=LocalizedText(
                        nl="Verwacht: bubbel / bubble.",
                        en="Expected: bubble / bubbel.",
                    ),
                    visualization_hint="restart-bubble",
                ),
            ),
        ],
    ),
)

SCENARIO_FIELD_ADVANTAGE = PracticeScenario(
    id="practice-field-advantage",
    kind="field",
    title=LocalizedText(
        nl="Veld: voordeel of fluiten",
        en="Field: advantage or whistle",
    ),
    situation=LocalizedText(
        nl=(
            "Lichte stick-inbreuk middenveld; de bal blijft bij de aanvallende "
            "ploeg die doorstroomt. Geen direct gevaar. Je partner kijkt mee. "
            "Kies de leesbare lijn tussen voordeel en onderbreken."
        ),
        en=(
            "Minor stick infringement midfield; the ball stays with the "
            "attacking team flowing forward. No immediate danger. Your partner "
            "is watching with you. Choose the readable line between advantage "
            "and stopping play."
        ),
    ),
    focus=LocalizedText(
        nl="Voordeel communiceren zonder veiligheid te laten vallen",
        en="Communicate advantage without dropping safety",
    ),
    order=3,
    visual_key="practice-advantage-wave",
    quiz=Quiz(
        id="quiz-practice-field-advantage",
        title=LocalizedText(
            nl="Oefening: voordeel",
            en="Practice: advantage",
        ),
        questions=[
            _mc(
                "q1-advantage-line",
                LocalizedText(
                    nl="Beste aanpak in dit speelbeeld?",
                    en="Best approach in this picture?",
                ),
                [
                    QuizOption(
                        id="a",
                        text=LocalizedText(
                            nl="Altijd direct fluiten — elke inbreuk stoppen.",
                            en="Always whistle immediately — stop every infringement.",
                        ),
                    ),
                    QuizOption(
                        id="b",
                        text=LocalizedText(
                            nl=(
                                "Speel door met duidelijk voordeel-signaal als "
                                "veiligheid en eerlijkheid intact blijven."
                            ),
                            en=(
                                "Play on with a clear advantage signal if safety "
                                "and fairness remain intact."
                            ),
                        ),
                    ),
                    QuizOption(
                        id="c",
                        text=LocalizedText(
                            nl="Negeer de inbreuk stil — geen signaal nodig.",
                            en="Ignore the infringement silently — no signal needed.",
                        ),
                    ),
                    QuizOption(
                        id="d",
                        text=LocalizedText(
                            nl="Direct gele kaart om ‘standaard’ te zetten.",
                            en="Yellow card immediately to ‘set a standard’.",
                        ),
                    ),
                ],
                "b",
                QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Juist. Voordeel is leesbaar management — niet "
                            "onzichtbaar negeren. " + _FIH_NOTE_NL
                        ),
                        en=(
                            "Correct. Advantage is readable management — not "
                            "invisible ignoring. " + _FIH_NOTE_EN
                        ),
                    ),
                    visualization_hint="practice-advantage-wave",
                ),
                {
                    "a": QuizFeedback(
                        explanation=LocalizedText(
                            nl="Te star; flow kan blijven als het speelbeeld schoon is.",
                            en="Too rigid; flow can continue if the picture stays clean.",
                        ),
                        visualization_hint="practice-advantage-wave",
                    ),
                    "c": QuizFeedback(
                        explanation=LocalizedText(
                            nl="Spelers en partner moeten je lijn kunnen lezen.",
                            en="Players and partner must be able to read your line.",
                        ),
                        visualization_hint="practice-advantage-wave",
                    ),
                    "d": QuizFeedback(
                        explanation=LocalizedText(
                            nl="Escalatie zonder noodzaak ondermijnt geloofwaardigheid.",
                            en="Escalation without need undermines credibility.",
                        ),
                        visualization_hint="practice-advantage-wave",
                    ),
                },
                QuizFeedback(
                    explanation=LocalizedText(
                        nl="Onjuist. Zoek leesbaar voordeel. " + _FIH_NOTE_NL,
                        en="Incorrect. Seek readable advantage. " + _FIH_NOTE_EN,
                    ),
                    visualization_hint="practice-advantage-wave",
                ),
            ),
            _written(
                "q2-advantage-keyword",
                LocalizedText(
                    nl=(
                        "Welk Engels sleutelwoord past bij doorspelen met een "
                        "leesbaar signaal? (één woord)"
                    ),
                    en=(
                        "Which English keyword fits playing on with a readable "
                        "signal? (one word)"
                    ),
                ),
                ["advantage"],
                QuizFeedback(
                    explanation=LocalizedText(
                        nl="Juist. " + _FIH_NOTE_NL,
                        en="Correct. " + _FIH_NOTE_EN,
                    ),
                    visualization_hint="practice-advantage-wave",
                ),
                QuizFeedback(
                    explanation=LocalizedText(
                        nl="Verwacht: voordeel / advantage.",
                        en="Expected: advantage / voordeel.",
                    ),
                    visualization_hint="practice-advantage-wave",
                ),
            ),
        ],
    ),
)

SCENARIO_INDOOR_BOARD_LIFT = PracticeScenario(
    id="practice-indoor-board-lift",
    kind="indoor",
    title=LocalizedText(
        nl="Zaal: rebound van de band + lift",
        en="Indoor: board rebound + lift",
    ),
    situation=LocalizedText(
        nl=(
            "Bal komt hard van de zijband terug. De ontvanger speelt door met "
            "een lift die de kniehoogte nadert terwijl een tegenstander dichtbij "
            "staat. Je scant band → pad → hoogte."
        ),
        en=(
            "The ball rebounds hard off the side board. The receiver plays on "
            "with a lift approaching knee height while an opponent is close. "
            "You scan board → path → height."
        ),
    ),
    focus=LocalizedText(
        nl="Hoogte en gevaar na bandenspel",
        en="Height and danger after board play",
    ),
    order=4,
    visual_key="practice-board-lift",
    quiz=Quiz(
        id="quiz-practice-indoor-board-lift",
        title=LocalizedText(
            nl="Oefening: band + lift",
            en="Practice: board + lift",
        ),
        questions=[
            _mc(
                "q1-lift-after-board",
                LocalizedText(
                    nl="Beste eerste beoordeling?",
                    en="Best first assessment?",
                ),
                [
                    QuizOption(
                        id="a",
                        text=LocalizedText(
                            nl="Bandenspel is altijd fout — direct fluiten.",
                            en="Board play is always illegal — whistle immediately.",
                        ),
                    ),
                    QuizOption(
                        id="b",
                        text=LocalizedText(
                            nl=(
                                "Beoordeel of de lift gevaarlijk/te hoog is in "
                                "context (hoogte, nabijheid, richting)."
                            ),
                            en=(
                                "Assess whether the lift is dangerous/too high in "
                                "context (height, proximity, direction)."
                            ),
                        ),
                    ),
                    QuizOption(
                        id="c",
                        text=LocalizedText(
                            nl="Negeer hoogte zolang de bal van de band komt.",
                            en="Ignore height as long as the ball came off the board.",
                        ),
                    ),
                    QuizOption(
                        id="d",
                        text=LocalizedText(
                            nl="Alleen fluiten als de bal de plafond raakt.",
                            en="Only whistle if the ball hits the ceiling.",
                        ),
                    ),
                ],
                "b",
                QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Juist. Bandenspel mag flow geven, maar lift blijft "
                            "een gevaarscan. " + _FIH_NOTE_NL
                        ),
                        en=(
                            "Correct. Board play can create flow, but lift still "
                            "needs a danger scan. " + _FIH_NOTE_EN
                        ),
                    ),
                    visualization_hint="practice-board-lift",
                ),
                {
                    "a": QuizFeedback(
                        explanation=LocalizedText(
                            nl="Bandenspel is inherent aan zaal — context telt.",
                            en="Board play is inherent indoors — context matters.",
                        ),
                        visualization_hint="practice-board-lift",
                    ),
                    "c": QuizFeedback(
                        explanation=LocalizedText(
                            nl="Hoogte en nabijheid blijven relevant na de rebound.",
                            en="Height and proximity stay relevant after the rebound.",
                        ),
                        visualization_hint="practice-board-lift",
                    ),
                    "d": QuizFeedback(
                        explanation=LocalizedText(
                            nl="Gevaar zit lager — bij spelers, niet bij het dak.",
                            en="Danger sits lower — at players, not the roof.",
                        ),
                        visualization_hint="practice-board-lift",
                    ),
                },
                QuizFeedback(
                    explanation=LocalizedText(
                        nl="Onjuist. Scan hoogte na de rebound. " + _FIH_NOTE_NL,
                        en="Incorrect. Scan height after the rebound. " + _FIH_NOTE_EN,
                    ),
                    visualization_hint="practice-board-lift",
                ),
            ),
            _written(
                "q2-height-keyword",
                LocalizedText(
                    nl=(
                        "Welk Engels sleutelwoord hoort bij beoordeling van een "
                        "liftende bal in de zaal? (één woord)"
                    ),
                    en=(
                        "Which English keyword belongs with assessing a lifted "
                        "ball indoors? (one word)"
                    ),
                ),
                ["height"],
                QuizFeedback(
                    explanation=LocalizedText(
                        nl="Juist. " + _FIH_NOTE_NL,
                        en="Correct. " + _FIH_NOTE_EN,
                    ),
                    visualization_hint="lift-limit",
                ),
                QuizFeedback(
                    explanation=LocalizedText(
                        nl="Verwacht: hoogte / height.",
                        en="Expected: height / hoogte.",
                    ),
                    visualization_hint="lift-limit",
                ),
            ),
        ],
    ),
)

SCENARIO_INDOOR_RESTART = PracticeScenario(
    id="practice-indoor-restart",
    kind="indoor",
    title=LocalizedText(
        nl="Zaal: herstart in krappe ruimte",
        en="Indoor: restart in tight space",
    ),
    situation=LocalizedText(
        nl=(
            "Herstart midden op de zaalvloer. Tegenstanders drukken dichtbij de "
            "band. De balbezittende ploeg wil snel zelf doorspelen. Jij hebt "
            "weinig diepte en moet het startbeeld helder houden."
        ),
        en=(
            "Restart mid-court. Opponents press tight near the boards. The team "
            "in possession wants a quick self-play. You have little depth and "
            "must keep the starting picture clear."
        ),
    ),
    focus=LocalizedText(
        nl="Ruimte en leesbaarheid in een krappe zaal",
        en="Space and readability in a tight indoor court",
    ),
    order=5,
    visual_key="practice-indoor-restart",
    quiz=Quiz(
        id="quiz-practice-indoor-restart",
        title=LocalizedText(
            nl="Oefening: zaalherstart",
            en="Practice: indoor restart",
        ),
        questions=[
            _mc(
                "q1-indoor-space",
                LocalizedText(
                    nl="Wat heeft prioriteit bij deze zaalherstart?",
                    en="What takes priority at this indoor restart?",
                ),
                [
                    QuizOption(
                        id="a",
                        text=LocalizedText(
                            nl="Zo snel mogelijk doorspelen — tempo boven alles.",
                            en="Play as fast as possible — tempo above all.",
                        ),
                    ),
                    QuizOption(
                        id="b",
                        text=LocalizedText(
                            nl=(
                                "Eerst een leesbare ruimte/afstand rond de "
                                "herstart, dan pas tempo toestaan."
                            ),
                            en=(
                                "First a readable space/distance around the "
                                "restart, then allow tempo."
                            ),
                        ),
                    ),
                    QuizOption(
                        id="c",
                        text=LocalizedText(
                            nl="Altijd wachten tot beide teams stilstaan.",
                            en="Always wait until both teams are stationary.",
                        ),
                    ),
                    QuizOption(
                        id="d",
                        text=LocalizedText(
                            nl="Direct kaart voor druk zetten bij de band.",
                            en="Card immediately for pressing near the board.",
                        ),
                    ),
                ],
                "b",
                QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Juist. In de zaal is ruimte schaars — maak het "
                            "startbeeld eerst leesbaar. " + _FIH_NOTE_NL
                        ),
                        en=(
                            "Correct. Space is scarce indoors — make the starting "
                            "picture readable first. " + _FIH_NOTE_EN
                        ),
                    ),
                    visualization_hint="practice-indoor-restart",
                ),
                {
                    "a": QuizFeedback(
                        explanation=LocalizedText(
                            nl="Tempo zonder ruimte maakt beslissingen onduidelijk.",
                            en="Tempo without space makes decisions unclear.",
                        ),
                        visualization_hint="practice-indoor-restart",
                    ),
                    "c": QuizFeedback(
                        explanation=LocalizedText(
                            nl="Volledige stilstand is niet altijd nodig — leesbaarheid wel.",
                            en="Full stillness is not always required — readability is.",
                        ),
                        visualization_hint="practice-indoor-restart",
                    ),
                    "d": QuizFeedback(
                        explanation=LocalizedText(
                            nl="Eerst management; kaarten als middelen.",
                            en="Manage first; cards as tools.",
                        ),
                        visualization_hint="practice-indoor-restart",
                    ),
                },
                QuizFeedback(
                    explanation=LocalizedText(
                        nl="Onjuist. Prioriteer leesbare ruimte. " + _FIH_NOTE_NL,
                        en="Incorrect. Prioritise readable space. " + _FIH_NOTE_EN,
                    ),
                    visualization_hint="practice-indoor-restart",
                ),
            ),
            _written(
                "q2-space-keyword",
                LocalizedText(
                    nl=(
                        "Welk Engels sleutelwoord past bij leesbare "
                        "herstartruimte in de zaal? (één woord)"
                    ),
                    en=(
                        "Which English keyword fits readable restart room "
                        "indoors? (one word)"
                    ),
                ),
                ["space"],
                QuizFeedback(
                    explanation=LocalizedText(
                        nl="Juist. " + _FIH_NOTE_NL,
                        en="Correct. " + _FIH_NOTE_EN,
                    ),
                    visualization_hint="practice-indoor-restart",
                ),
                QuizFeedback(
                    explanation=LocalizedText(
                        nl="Verwacht: ruimte / space.",
                        en="Expected: space / ruimte.",
                    ),
                    visualization_hint="practice-indoor-restart",
                ),
            ),
        ],
    ),
)

SCENARIO_INDOOR_SIDE_BOARD = PracticeScenario(
    id="practice-indoor-side-board",
    kind="indoor",
    title=LocalizedText(
        nl="Zaal: duel langs de zijband",
        en="Indoor: contest along the side board",
    ),
    situation=LocalizedText(
        nl=(
            "Twee spelers duelleren langs de zijband. De bal klem tussen sticks "
            "en band; lichaamshouding wordt smaller. Je moet onderscheiden tussen "
            "legitiem bandenspel en onveilig/oneerlijk contact."
        ),
        en=(
            "Two players contest along the side board. The ball is trapped "
            "between sticks and board; body shapes tighten. You must separate "
            "legitimate board play from unsafe/unfair contact."
        ),
    ),
    focus=LocalizedText(
        nl="Bandenspel vs. onveilig contact",
        en="Board play vs unsafe contact",
    ),
    order=6,
    visual_key="practice-side-board",
    quiz=Quiz(
        id="quiz-practice-indoor-side-board",
        title=LocalizedText(
            nl="Oefening: zijbandduel",
            en="Practice: side-board contest",
        ),
        questions=[
            _mc(
                "q1-board-contest",
                LocalizedText(
                    nl="Beste leidraad in dit duel?",
                    en="Best guide in this contest?",
                ),
                [
                    QuizOption(
                        id="a",
                        text=LocalizedText(
                            nl="Elk contact bij de band is een straf.",
                            en="Any contact at the board is a penalty.",
                        ),
                    ),
                    QuizOption(
                        id="b",
                        text=LocalizedText(
                            nl=(
                                "Laat legitiem bandenspel lopen; grijp in bij "
                                "onveilig of oneerlijk lichaam/stick-gebruik."
                            ),
                            en=(
                                "Allow legitimate board play; intervene on unsafe "
                                "or unfair body/stick use."
                            ),
                        ),
                    ),
                    QuizOption(
                        id="c",
                        text=LocalizedText(
                            nl="Wacht tot de bal stilvalt — dan pas fluiten.",
                            en="Wait until the ball stops — then whistle.",
                        ),
                    ),
                    QuizOption(
                        id="d",
                        text=LocalizedText(
                            nl="Altijd voordeel voor de aanvallende stick.",
                            en="Always advantage for the attacking stick.",
                        ),
                    ),
                ],
                "b",
                QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Juist. Bandenspel is deel van zaalhockey; veiligheid "
                            "en eerlijkheid blijven de filter. " + _FIH_NOTE_NL
                        ),
                        en=(
                            "Correct. Board play is part of indoor hockey; safety "
                            "and fairness stay the filter. " + _FIH_NOTE_EN
                        ),
                    ),
                    visualization_hint="practice-side-board",
                ),
                {
                    "a": QuizFeedback(
                        explanation=LocalizedText(
                            nl="Te breed — niet elk contact is fout.",
                            en="Too broad — not every contact is illegal.",
                        ),
                        visualization_hint="practice-side-board",
                    ),
                    "c": QuizFeedback(
                        explanation=LocalizedText(
                            nl="Onveiligheid vraagt soms sneller ingrijpen.",
                            en="Unsafe play sometimes needs a quicker intervention.",
                        ),
                        visualization_hint="practice-side-board",
                    ),
                    "d": QuizFeedback(
                        explanation=LocalizedText(
                            nl="Voordeel volgt context, geen automatische partijkeuze.",
                            en="Advantage follows context, not an automatic side.",
                        ),
                        visualization_hint="practice-side-board",
                    ),
                },
                QuizFeedback(
                    explanation=LocalizedText(
                        nl="Onjuist. Filter op veiligheid/eerlijkheid. " + _FIH_NOTE_NL,
                        en="Incorrect. Filter on safety/fairness. " + _FIH_NOTE_EN,
                    ),
                    visualization_hint="practice-side-board",
                ),
            ),
            _written(
                "q2-boards-keyword",
                LocalizedText(
                    nl=(
                        "Welk Engels sleutelwoord past bij spel langs de "
                        "zaalwanden? (één woord)"
                    ),
                    en=(
                        "Which English keyword fits play along the indoor "
                        "side walls? (one word)"
                    ),
                ),
                ["boards"],
                QuizFeedback(
                    explanation=LocalizedText(
                        nl="Juist. " + _FIH_NOTE_NL,
                        en="Correct. " + _FIH_NOTE_EN,
                    ),
                    visualization_hint="board-play",
                ),
                QuizFeedback(
                    explanation=LocalizedText(
                        nl="Verwacht: banden / boards.",
                        en="Expected: boards / banden.",
                    ),
                    visualization_hint="board-play",
                ),
            ),
        ],
    ),
)

PRACTICE_SCENARIOS: list[PracticeScenario] = [
    SCENARIO_FIELD_RAISED,
    SCENARIO_FIELD_RESTART,
    SCENARIO_FIELD_ADVANTAGE,
    SCENARIO_INDOOR_BOARD_LIFT,
    SCENARIO_INDOOR_RESTART,
    SCENARIO_INDOOR_SIDE_BOARD,
]


def get_practice_bank() -> PracticeBank:
    return PracticeBank(
        id="nl-hockey-practice-bank-v1",
        title=LocalizedText(
            nl="Oefenscenario's (beslissingen)",
            en="Practice scenarios (decisions)",
        ),
        description=LocalizedText(
            nl=(
                "Losstaande beslissingsscenario's voor veld en zaal — apart van "
                "de modulelessen. Meerkeuze + korte schriftelijke antwoorden met "
                "uitleg. " + _FIH_NOTE_NL
            ),
            en=(
                "Standalone decision scenarios for field and indoor — separate "
                "from module lessons. Multiple choice + short written answers "
                "with explanations. " + _FIH_NOTE_EN
            ),
        ),
        scenarios=PRACTICE_SCENARIOS,
    )


def practice_quizzes() -> dict[str, Quiz]:
    return {s.quiz.id: s.quiz for s in PRACTICE_SCENARIOS}


def practice_scenario_ids() -> set[str]:
    return {s.id for s in PRACTICE_SCENARIOS}


def scenario_id_for_quiz(quiz_id: str) -> str | None:
    for scenario in PRACTICE_SCENARIOS:
        if scenario.quiz.id == quiz_id:
            return scenario.id
    return None
