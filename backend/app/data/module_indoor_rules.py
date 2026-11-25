"""Full learning module: indoor hockey rules core (NL + EN).

Pedagogical framing only — no reproduced FIH/KNHB copyrighted rule text or art.
"""

from app.schemas import (
    Attribution,
    FurtherReading,
    LearningSection,
    LocalizedText,
    ModuleStub,
    Quiz,
    QuizFeedback,
    QuizOption,
    QuizQuestion,
    VisualPlaceholder,
)

FIH_INDOOR_URL = (
    "https://www.fih.hockey/inside-fih/our-official-documents/rules-of-hockey"
)
KNHB_HOME_URL = "https://www.knhb.nl/"

INDOOR_VISUALS: list[VisualPlaceholder] = [
    VisualPlaceholder(
        id="viz-in-match-start",
        kind="svg_animation",
        title=LocalizedText(nl="Zaalwedstrijdstart", en="Indoor match start"),
        caption=LocalizedText(
            nl="Spelers tellen, doelen en banden checken, toss, kant en aftrap kiezen — kleinere ruimte, zelfde ritueel.",
            en="Count players, check goals and boards, toss, choose side and start — smaller space, same ritual.",
        ),
        animation_key="match-start",
    ),
    VisualPlaceholder(
        id="viz-in-position",
        kind="svg_animation",
        title=LocalizedText(nl="Positie in de zaal", en="Indoor positioning"),
        caption=LocalizedText(
            nl="Dichter op de bal dan op het veld; lead en support wisselen sneller bij bandenspel.",
            en="Closer to the ball than outdoors; lead and support switch faster on board play.",
        ),
        animation_key="umpire-position",
    ),
    VisualPlaceholder(
        id="viz-in-hit-types",
        kind="svg_animation",
        title=LocalizedText(nl="Slagtypes (zaal)", en="Stroke types (indoor)"),
        caption=LocalizedText(
            nl="Push en slap domineren; volle hit is zeldzamer — kracht × nabijheid weegt zwaar in krappe ruimte.",
            en="Push and slap dominate; full hits are rarer — power × proximity weighs heavily in tight space.",
        ),
        animation_key="hit-types",
    ),
    VisualPlaceholder(
        id="viz-in-obstruction",
        kind="svg_animation",
        title=LocalizedText(nl="Obstructie bij de banden", en="Obstruction at the boards"),
        caption=LocalizedText(
            nl="Stick-, lichaams- en schaduwobstructie — bij de banden is uitwijkruimte kleiner.",
            en="Stick, body and shadow obstruction — at the boards escape space is smaller.",
        ),
        animation_key="obstruction-types",
    ),
    VisualPlaceholder(
        id="viz-lift-limit",
        kind="svg_animation",
        title=LocalizedText(nl="Lift / omhoog (zaalbasis)", en="Lift / raised (indoor basics)"),
        caption=LocalizedText(
            nl="Plat is default; lift is strenger begrensd dan op het veld — check officiële uitzonderingen (o.a. schoten).",
            en="Flat is default; lift is bounded more tightly than outdoors — check official exceptions (e.g. shots).",
        ),
        animation_key="lift-limit",
    ),
    VisualPlaceholder(
        id="viz-in-cards",
        kind="svg_animation",
        title=LocalizedText(nl="Kaarten (zaal)", en="Cards (indoor)"),
        caption=LocalizedText(
            nl="Zelfde ladder groen → geel → rood; in de zaal escaleert herhaling sneller door tempo en nabijheid.",
            en="Same ladder green → yellow → red; indoors repetition escalates faster via tempo and proximity.",
        ),
        animation_key="card-ladder",
    ),
    VisualPlaceholder(
        id="viz-in-pc",
        kind="svg_animation",
        title=LocalizedText(nl="Strafcorner (zaal)", en="Penalty corner (indoor)"),
        caption=LocalizedText(
            nl="Set piece in kleinere ruimte — check aantallen, banden en klaar-signaal vóór de injectie.",
            en="Set piece in smaller space — check numbers, boards and ready signal before injection.",
        ),
        animation_key="penalty-corner",
    ),
    VisualPlaceholder(
        id="viz-in-ps",
        kind="svg_animation",
        title=LocalizedText(nl="Strafbal (zaal)", en="Penalty stroke (indoor)"),
        caption=LocalizedText(
            nl="Eén aanvaller vs keeper — stilstand en duidelijk signaal; banden veranderen de uitwijkhoek niet voor de procedure.",
            en="One attacker vs keeper — stillness and a clear signal; boards do not change the stroke procedure.",
        ),
        animation_key="penalty-stroke",
    ),
    VisualPlaceholder(
        id="viz-in-gk",
        kind="svg_animation",
        title=LocalizedText(nl="Zaalkeeper", en="Indoor keeper"),
        caption=LocalizedText(
            nl="Keeperrechten in de eigen zone; buiten die zone als veldspeler — banden beperken slides.",
            en="Keeper rights in their own zone; outside that zone as an outfielder — boards constrain slides.",
        ),
        animation_key="gk-limits",
    ),
    VisualPlaceholder(
        id="viz-court-boards",
        kind="svg_animation",
        title=LocalizedText(nl="Banden & speelvlak", en="Boards & playing area"),
        caption=LocalizedText(
            nl="Bal speelt van de band terug — lees of het veilig is of dat iemand klem zit tegen de band.",
            en="Ball comes back off the board — read whether it is safe or someone is pinned against the board.",
        ),
        animation_key="court-boards",
    ),
    VisualPlaceholder(
        id="viz-board-play",
        kind="svg_animation",
        title=LocalizedText(nl="Bandenspel", en="Board play"),
        caption=LocalizedText(
            nl="Duel langs de zijband: contact vs bal, en of de band het duel oneerlijk maakt.",
            en="Contest along the side board: contact vs ball, and whether the board makes the contest unfair.",
        ),
        animation_key="board-play",
    ),
    VisualPlaceholder(
        id="viz-tempo-proximity",
        kind="svg_animation",
        title=LocalizedText(nl="Tempo & nabijheid", en="Tempo & proximity"),
        caption=LocalizedText(
            nl="Zaal is sneller en dichter — kortere reactietijd, vaker dichter bij de actie staan.",
            en="Indoor is faster and tighter — shorter reaction time, stand closer to the action more often.",
        ),
        animation_key="tempo-proximity",
    ),
]

INDOOR_QUIZ = Quiz(
    id="quiz-indoor-rules-core",
    title=LocalizedText(
        nl="Quiz: zaalregels (kern)",
        en="Quiz: indoor rules (core)",
    ),
    questions=[
        QuizQuestion(
            id="q1-board-anticipation",
            type="multiple_choice",
            prompt=LocalizedText(
                nl=(
                    "In zaalhockey is de speelruimte kleiner en sneller dan op "
                    "het veld. Wat is de beste eerste aanpassing voor de "
                    "scheidsrechter (pedagogisch kader — geen regelcitaat)?"
                ),
                en=(
                    "Indoor hockey has less space and a faster tempo than "
                    "outdoor. What is the umpire’s best first adjustment "
                    "(pedagogical frame — not a rules quotation)?"
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
                        nl="Alleen bij de goal blijven; middenveld negeren.",
                        en="Stay only at the goal; ignore midfield.",
                    ),
                ),
                QuizOption(
                    id="c",
                    text=LocalizedText(
                        nl="Dichter bij blijven, banden eerder scannen, sneller communiceren.",
                        en="Stay closer, scan boards earlier, communicate sooner.",
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
            correct_option_id="c",
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Juist. Zaal vraagt snellere positionering en "
                        "bandenscan. Raadpleeg officiële FIH Indoor Rules / "
                        "KNHB-materiaal voor actuele voorschriften — hier "
                        "alleen een besliskader."
                    ),
                    en=(
                        "Correct. Indoor requires faster positioning and board "
                        "scanning. Consult official FIH Indoor Rules / KNHB "
                        "materials for current prescriptions — this is a "
                        "decision frame only."
                    ),
                ),
                visualization_hint="indoor-rebound",
            ),
            feedback_incorrect={
                "a": QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Onjuist. Tempo en ruimte veranderen hoe je kijkt "
                            "en wanneer je communiceert — niet per se de "
                            "ethiek, wel de uitvoering."
                        ),
                        en=(
                            "Incorrect. Tempo and space change how you look "
                            "and when you communicate — not necessarily "
                            "ethics, but execution."
                        ),
                    ),
                    visualization_hint="court-boards",
                ),
                "b": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Onjuist. Het hele veld (zaal) blijft relevant.",
                        en="Incorrect. The whole court remains relevant.",
                    ),
                    visualization_hint="court-boards",
                ),
                "d": QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Onjuist. Bandenspel kan veilig of problematisch "
                            "zijn; context beoordelen. Zie officiële bronnen."
                        ),
                        en=(
                            "Incorrect. Play off the boards can be safe or "
                            "not; assess context. See official sources."
                        ),
                    ),
                    visualization_hint="indoor-rebound",
                ),
            },
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Herlees het bandenscan-kader en link naar FIH Indoor Rules.",
                    en="Revisit the board-scan frame and link to FIH Indoor Rules.",
                ),
                visualization_hint="indoor-rebound",
            ),
        ),
        QuizQuestion(
            id="q2-lift-emphasis",
            type="multiple_choice",
            prompt=LocalizedText(
                nl=(
                    "Ten opzichte van veldhockey is omhoog spelen in de zaal "
                    "in dit cursusmodel vooral: (pedagogisch — geen citaat)"
                ),
                en=(
                    "Compared with outdoor hockey, raising the ball indoors "
                    "in this course model is mainly: (pedagogical — not a quote)"
                ),
            ),
            options=[
                QuizOption(
                    id="a",
                    text=LocalizedText(
                        nl="Altijd verboden, ongeacht hoogte of context.",
                        en="Always forbidden, regardless of height or context.",
                    ),
                ),
                QuizOption(
                    id="b",
                    text=LocalizedText(
                        nl="Vrijer dan op het veld omdat de banden beschermen.",
                        en="Freer than outdoors because the boards protect everyone.",
                    ),
                ),
                QuizOption(
                    id="c",
                    text=LocalizedText(
                        nl="Alleen relevant voor keepers; veldspelers negeren.",
                        en="Only relevant for keepers; ignore for outfield players.",
                    ),
                ),
                QuizOption(
                    id="d",
                    text=LocalizedText(
                        nl="Strakker wegen: veilige, leesbare lift in kleine ruimte.",
                        en="Judge tighter: safe, readable lift in tight space.",
                    ),
                ),
            ],
            correct_option_id="d",
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Juist. Zaalaccentueert liftbeoordeling door ruimte en "
                        "tempo. Exacte grenzen: FIH Indoor / KNHB."
                    ),
                    en=(
                        "Correct. Indoor tightens lift judgement via space and "
                        "tempo. Exact limits: FIH Indoor / KNHB."
                    ),
                ),
                visualization_hint="lift-limit",
            ),
            feedback_incorrect={
                "a": QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Te absoluut. Context telt; dit cursusmodel zegt "
                            "‘strakker wegen’, niet ‘altijd verboden’."
                        ),
                        en=(
                            "Too absolute. Context matters; this course model "
                            "says ‘judge more tightly’, not ‘always forbidden’."
                        ),
                    ),
                    visualization_hint="lift-limit",
                ),
                "b": QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Onjuist. Banden verkleinen de ruimte; ze maken "
                            "omhoog spelen niet vrijer."
                        ),
                        en=(
                            "Incorrect. Boards shrink the space; they do not "
                            "make raising freer."
                        ),
                    ),
                    visualization_hint="lift-limit",
                ),
                "c": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Liftbeoordeling geldt voor alle spelers in de zaal.",
                        en="Lift judgement applies to all players indoors.",
                    ),
                    visualization_hint="lift-limit",
                ),
            },
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Bekijk het liftkader: plat vs. omhoog in zaalcontext.",
                    en="Review the lift frame: flat vs raised in indoor context.",
                ),
                visualization_hint="lift-limit",
            ),
        ),
        QuizQuestion(
            id="q3-boards-keyword",
            type="written",
            prompt=LocalizedText(
                nl=(
                    "Welk Engels sleutelwoord gebruikt deze cursus voor de "
                    "zijwanden van de zaalbaan? (één woord)"
                ),
                en=(
                    "Which English keyword does this course use for the side "
                    "walls of the indoor court? (one word)"
                ),
            ),
            accepted_answers=["boards"],
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl="Juist — boards (banden).",
                    en="Correct — boards.",
                ),
                visualization_hint="court-boards",
            ),
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Verwacht antwoord: boards. Zie ook de zaalbaan-visual.",
                    en="Expected answer: boards. See also the court-boards visual.",
                ),
                visualization_hint="court-boards",
            ),
        ),
        QuizQuestion(
            id="q4-indoor-keyword",
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
                visualization_hint="court-boards",
            ),
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Verwacht antwoord: indoor.",
                    en="Expected answer: indoor.",
                ),
                visualization_hint="court-boards",
            ),
        ),
        QuizQuestion(
            id="q5-tempo-when",
            type="multiple_choice",
            prompt=LocalizedText(
                nl=(
                    "De zaal speelt snel en dichtbij. Wat past het best bij de "
                    "tempo- & nabijheidslens in dit cursusmodel (pedagogisch)?"
                ),
                en=(
                    "Indoor play is fast and close. What best matches the "
                    "tempo & proximity lens in this course model "
                    "(pedagogical)?"
                ),
            ),
            options=[
                QuizOption(
                    id="a",
                    text=LocalizedText(
                        nl="Blijf ver weg zodat je het hele veld overziet zonder te bewegen.",
                        en="Stay far away so you can see the whole court without moving.",
                    ),
                ),
                QuizOption(
                    id="b",
                    text=LocalizedText(
                        nl=(
                            "Dichter bij blijven, sneller scannen, en eerder "
                            "met je partner communiceren wanneer tempo oploopt."
                        ),
                        en=(
                            "Stay closer, scan sooner, and communicate earlier "
                            "with your partner when tempo rises."
                        ),
                    ),
                ),
                QuizOption(
                    id="c",
                    text=LocalizedText(
                        nl="Negeer je partner; zaal is altijd solo-werk.",
                        en="Ignore your partner; indoor is always solo work.",
                    ),
                ),
                QuizOption(
                    id="d",
                    text=LocalizedText(
                        nl="Wacht tot coaches aangeven wanneer je dichterbij mag.",
                        en="Wait for coaches to say when you may move closer.",
                    ),
                ),
            ],
            correct_option_id="b",
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Juist. De tempo-lens weegt nabijheid en snellere "
                        "partnercommunicatie — ná veiligheid, niet in plaats "
                        "ervan."
                    ),
                    en=(
                        "Correct. The tempo lens weighs proximity and faster "
                        "partner communication — after safety, not instead of "
                        "it."
                    ),
                ),
                visualization_hint="tempo-proximity",
            ),
            feedback_incorrect={
                "a": QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Te ver weg maakt bandenrebound en lift moeilijker "
                            "leesbaar in kleine ruimte."
                        ),
                        en=(
                            "Too far away makes board rebounds and lifts harder "
                            "to read in tight space."
                        ),
                    ),
                    visualization_hint="tempo-proximity",
                ),
                "c": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Partnercommunicatie blijft kern — ook in de zaal.",
                        en="Partner communication stays core — indoors too.",
                    ),
                    visualization_hint="tempo-proximity",
                ),
                "d": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Jij stuurt je positionering; coaches sturen niet jouw tempo-lens.",
                        en="You drive positioning; coaches do not own your tempo lens.",
                    ),
                    visualization_hint="tempo-proximity",
                ),
            },
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Herlees tempo & nabijheid: dichterbij → tempo → partner.",
                    en="Revisit tempo & proximity: closer → tempo → partner.",
                ),
                visualization_hint="tempo-proximity",
            ),
        ),
    ],
)

INDOOR_MODULE = ModuleStub(
    id="mod-indoor-rules-core",
    kind="indoor",
    title=LocalizedText(
        nl="Zaal: kernregels & besliskaders",
        en="Indoor: core rules & decision frames",
    ),
    summary=LocalizedText(
        nl=(
            "Showcase-module: rijke NL/EN-lesstof in klikstappen, originele "
            "zaalanimaties en een aparte nagekeken quiz — banden, lift, "
            "rebound en tempo."
        ),
        en=(
            "Showcase module: rich NL/EN reading in click-steps, original "
            "indoor animations and a separate graded quiz — boards, lift, "
            "rebound and tempo."
        ),
    ),
    learning_objectives=[
        LocalizedText(
            nl="Zaalbaan (banden, helften, cirkels) in eigen woorden lokaliseren.",
            en="Locate the indoor court (boards, halves, circles) in your own words.",
        ),
        LocalizedText(
            nl="Uitleggen waarom omhoog spelen in zaal strakker wordt gewogen.",
            en="Explain why raising the ball is judged more tightly indoors.",
        ),
        LocalizedText(
            nl="Een bandenscan toepassen: bal → band → herstel/contact.",
            en="Apply a board scan: ball → board → recovery/contact.",
        ),
        LocalizedText(
            nl="Tempo en nabijheid vertalen naar snellere positionering en communicatie.",
            en="Translate tempo and proximity into faster positioning and communication.",
        ),
    ],
    instruction_outline=[
        LocalizedText(
            nl="Zaalkaart: banden → helften → cirkels.",
            en="Court map: boards → halves → circles.",
        ),
        LocalizedText(
            nl="Lift: strakker wegen dan op het veld.",
            en="Lift: judge more tightly than outdoors.",
        ),
        LocalizedText(
            nl="Banden: scan bal → band → herstel.",
            en="Boards: scan ball → board → recovery.",
        ),
        LocalizedText(
            nl="Tempo: dichter bij, eerder communiceren.",
            en="Tempo: stay closer, communicate sooner.",
        ),
    ],
    content_status="full",
    sections=[
        LearningSection(
            id="sec-indoor-why",
            title=LocalizedText(nl="Wat je in deze module leert", en="What this module teaches"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Zaalkern: start, positie, slagtypes, obstructie, "
                        "lift, kaarten, PC/PS, keeper, banden en tempo. "
                        "Diagram = situatie; officiële tekst onder Verder "
                        "lezen. Harde scenario’s: Zaal: harde beslissingen."
                    ),
                    en=(
                        "Indoor core: start, positioning, stroke types, "
                        "obstruction, lift, cards, PC/PS, keeper, boards "
                        "and tempo. Diagram = situation; official text "
                        "under Further reading. Hard scenarios: Indoor: "
                        "hard decisions."
                    ),
                ),
            ],
            visual_id="viz-in-match-start",
        ),
        LearningSection(
            id="sec-in-match-start",
            title=LocalizedText(nl="Wedstrijdstart (zaal)", en="Match start (indoor)"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Tel spelers (zaalteams zijn kleiner dan veld — "
                        "check actuele KNHB/competitieaantallen), check "
                        "doelen, netten en banden op veiligheid, doe de "
                        "toss: winnaar kiest kant of aftrap."
                    ),
                    en=(
                        "Count players (indoor teams are smaller than "
                        "field — check current KNHB/competition numbers), "
                        "check goals, nets and boards for safety, do the "
                        "toss: winner chooses side or start."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Spreek lead/support af; in de zaal wissel je "
                        "vaker omdat de bal sneller de helft kruist."
                    ),
                    en=(
                        "Agree lead/support; indoors you switch more often "
                        "because the ball crosses the half faster."
                    ),
                ),
            ],
            visual_id="viz-in-match-start",
        ),
        LearningSection(
            id="sec-in-positioning",
            title=LocalizedText(nl="Waar staan (zaal)", en="Where to stand (indoor)"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Sta dichter bij de actie dan op het veld. Lead "
                        "dicht bij bal/bandenhoek; support dekt diepte en "
                        "tweede duel. Bij PC/stroke: hoek met zicht op "
                        "injectie en keeper."
                    ),
                    en=(
                        "Stand closer to the action than outdoors. Lead "
                        "near ball/board corner; support covers depth and "
                        "second contest. On PC/stroke: angle with sight of "
                        "injection and keeper."
                    ),
                ),
            ],
            visual_id="viz-in-position",
        ),
        LearningSection(
            id="sec-in-hit-types",
            title=LocalizedText(nl="Slagtypes (zaal)", en="Stroke types (indoor)"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Push en slap zijn dominant; volle hit is zeldzaam "
                        "en weegt zwaar op gevaar in krappe ruimte. Lees "
                        "type × kracht × nabijheid tot spelers en banden."
                    ),
                    en=(
                        "Push and slap dominate; a full hit is rare and "
                        "weighs heavily on danger in tight space. Read "
                        "type × power × proximity to players and boards."
                    ),
                ),
            ],
            visual_id="viz-in-hit-types",
        ),
        LearningSection(
            id="sec-in-obstruction",
            title=LocalizedText(nl="Obstructie (zaal)", en="Obstruction (indoor)"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Zelfde drie types (stick, lichaam, schaduw/derde-"
                        "man), maar bij de banden is uitwijkruimte kleiner "
                        "— afschermen is sneller oneerlijk. Lees of de "
                        "opponent een reële route naar de bal had."
                    ),
                    en=(
                        "Same three types (stick, body, shadow/third-man), "
                        "but at the boards escape space is smaller — "
                        "screening becomes unfair sooner. Read whether the "
                        "opponent had a real route to the ball."
                    ),
                ),
            ],
            visual_id="viz-in-obstruction",
        ),
        LearningSection(
            id="sec-lift-emphasis",
            title=LocalizedText(nl="Lift / omhoog (basis)", en="Lift / raised (basics)"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Zaal: plat is default; liftgrenzen zijn strenger "
                        "dan op het veld. Officiële uitzonderingen "
                        "(bijvoorbeeld bepaalde schoten) staan in FIH "
                        "Indoor / KNHB. Basis: te hoog of te dicht bij "
                        "een tegenstander → fluit."
                    ),
                    en=(
                        "Indoor: flat is default; lift limits are tighter "
                        "than outdoors. Official exceptions (e.g. certain "
                        "shots) live in FIH Indoor / KNHB. Basics: too "
                        "high or too close to an opponent → whistle."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Verdieping (lift in drukke hoeken, kaarten) volgt "
                        "in Zaal: harde beslissingen."
                    ),
                    en=(
                        "Deepening (lift in crowded corners, cards) follows "
                        "in Indoor: hard decisions."
                    ),
                ),
            ],
            visual_id="viz-lift-limit",
        ),
        LearningSection(
            id="sec-in-cards",
            title=LocalizedText(nl="Kaarten (zaal)", en="Cards (indoor)"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Groen → geel → rood zoals op het veld. Tempo en "
                        "nabijheid maken herhaling sneller zichtbaar — "
                        "communiceer vroeg. Procedures: KNHB/competitie."
                    ),
                    en=(
                        "Green → yellow → red as outdoors. Tempo and "
                        "proximity make repetition visible sooner — "
                        "communicate early. Procedures: KNHB/competition."
                    ),
                ),
            ],
            visual_id="viz-in-cards",
        ),
        LearningSection(
            id="sec-in-pc",
            title=LocalizedText(nl="Strafcorner (zaal)", en="Penalty corner (indoor)"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Zelfde idee als veld: fouten van de verdediging "
                        "in de eigen zone kunnen PC geven (lijst: FIH "
                        "Indoor). Check aantallen, bandenruimte en "
                        "klaar-signaal; tijdens: gevaar/lift en feet."
                    ),
                    en=(
                        "Same idea as field: defensive fouls in their own "
                        "zone can award a PC (list: FIH Indoor). Check "
                        "numbers, board space and ready signal; during: "
                        "danger/lift and feet."
                    ),
                ),
            ],
            visual_id="viz-in-pc",
        ),
        LearningSection(
            id="sec-in-ps",
            title=LocalizedText(nl="Strafbal (zaal)", en="Penalty stroke (indoor)"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Ernstige fouten die een scoringskans ontnemen: "
                        "strafbal (gronden: FIH Indoor). Stilstand, juiste "
                        "plek, duidelijk signaal — zelfde procedurekern "
                        "als veld."
                    ),
                    en=(
                        "Serious fouls that deny a scoring chance: penalty "
                        "stroke (grounds: FIH Indoor). Stillness, correct "
                        "spot, clear signal — same procedural core as field."
                    ),
                ),
            ],
            visual_id="viz-in-ps",
        ),
        LearningSection(
            id="sec-in-gk",
            title=LocalizedText(nl="Keeper (zaal)", en="Keeper (indoor)"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "In de eigen zone: keeperrechten. Buiten: "
                        "veldspeler. Banden beperken slides — raak de "
                        "aanvaller niet zonder bal. Verdieping in Zaal: "
                        "harde beslissingen."
                    ),
                    en=(
                        "In their own zone: keeper rights. Outside: "
                        "outfielder. Boards constrain slides — do not hit "
                        "the attacker without the ball. Deepening in "
                        "Indoor: hard decisions."
                    ),
                ),
            ],
            visual_id="viz-in-gk",
        ),
        LearningSection(
            id="sec-court-boards",
            title=LocalizedText(nl="Banden & speelvlak", en="Boards & playing area"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "De band is speelbaar: bal terug van de band is "
                        "normaal. Lees gevaar als iemand klem zit of hard "
                        "in de band wordt geduwd."
                    ),
                    en=(
                        "The board is in play: ball back off the board is "
                        "normal. Read danger if someone is pinned or shoved "
                        "hard into the board."
                    ),
                ),
            ],
            visual_id="viz-court-boards",
        ),
        LearningSection(
            id="sec-board-play",
            title=LocalizedText(nl="Bandenspel", en="Board play"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Duel langs de band: speelt de verdediger de bal "
                        "of de speler? Band mag het duel niet oneerlijk "
                        "maken door vastzetten zonder bal."
                    ),
                    en=(
                        "Contest along the board: is the defender playing "
                        "the ball or the player? The board must not make "
                        "the contest unfair by pinning without the ball."
                    ),
                ),
            ],
            visual_id="viz-board-play",
        ),
        LearningSection(
            id="sec-tempo-proximity",
            title=LocalizedText(nl="Tempo & nabijheid", en="Tempo & proximity"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Zaal vraagt kortere cycli: dichter staan, sneller "
                        "fluiten bij gevaar, vaker partner-cue."
                    ),
                    en=(
                        "Indoor needs shorter cycles: stand closer, whistle "
                        "danger sooner, use partner cues more often."
                    ),
                ),
            ],
            visual_id="viz-tempo-proximity",
        ),
        LearningSection(
            id="sec-indoor-practice-next",
            title=LocalizedText(nl="Quiz en volgende module", en="Quiz and next module"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Open de zaalquiz. Daarna: Zaal: harde beslissingen "
                        "voor lift in krappe hoeken, druk bij banden en "
                        "keeperslide — of het professionele pad."
                    ),
                    en=(
                        "Open the indoor quiz. Next: Indoor: hard decisions "
                        "for lift in tight corners, board pressure and "
                        "keeper slide — or the professional pathway."
                    ),
                ),
            ],
        ),
    ],
    visuals=INDOOR_VISUALS,
    quiz_id=INDOOR_QUIZ.id,
    further_reading=[
        FurtherReading(
            title=LocalizedText(
                nl="FIH Indoor Hockey Rules (officieel)",
                en="FIH Indoor Hockey Rules (official)",
            ),
            url=FIH_INDOOR_URL,
            attribution=Attribution(
                source_name="FIH Indoor Hockey Rules",
                source_url=FIH_INDOOR_URL,
                note=LocalizedText(
                    nl="Officiële FIH Indoor Hockey Rules — bron voor zaalhockeyregels.",
                    en="Official FIH Indoor Hockey Rules — source for indoor hockey rules.",
                ),
            ),
        ),
        FurtherReading(
            title=LocalizedText(
                nl="KNHB — regels & interpretaties (link/plaatshouder)",
                en="KNHB — rules & interpretations (link/placeholder)",
            ),
            url=KNHB_HOME_URL,
            attribution=Attribution(
                source_name="KNHB — regels & interpretaties",
                source_url=KNHB_HOME_URL,
                note=LocalizedText(
                    nl=(
                        "Geen KNHB-illustraties inbegrepen. Link naar officiële "
                        "KNHB-scheidsrechtersbronnen; EN-vertaling van "
                        "interpretaties: TODO."
                    ),
                    en=(
                        "No KNHB illustrations included. Link to official KNHB "
                        "umpire sources; EN translation of interpretations: TODO."
                    ),
                ),
                knhb_illustration_placeholder=True,
                translation_needed=True,
            ),
        ),
    ],
    order=3,
)
