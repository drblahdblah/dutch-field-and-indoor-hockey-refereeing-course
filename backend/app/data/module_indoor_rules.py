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
        id="viz-court-boards",
        kind="svg_animation",
        title=LocalizedText(
            nl="Zaalbaan met banden (scheidsrechterlijk overzicht)",
            en="Indoor court with boards (umpire overview)",
        ),
        caption=LocalizedText(
            nl=(
                "Originele SVG: rechthoekige baan, zijbanden, helften, cirkels. "
                "Geen officiële FIH/KNHB-zaaltekening — exacte afmetingen in "
                "officiële bronnen."
            ),
            en=(
                "Original SVG: rectangular court, side boards, halves, circles. "
                "Not an official FIH/KNHB court diagram — exact dimensions in "
                "official sources."
            ),
        ),
        animation_key="court-boards",
    ),
    VisualPlaceholder(
        id="viz-lift-limit",
        kind="svg_animation",
        title=LocalizedText(
            nl="Liftkader: plat vs. omhoog (zaalaccent)",
            en="Lift frame: flat vs raised (indoor emphasis)",
        ),
        caption=LocalizedText(
            nl=(
                "Originele cursusanimatie: in zaal is omhoog spelen strakker "
                "beoordeeld dan op het veld. Geen overgenomen regeltekst."
            ),
            en=(
                "Original course animation: indoors, raising the ball is judged "
                "more tightly than outdoors. No reproduced rule text."
            ),
        ),
        animation_key="lift-limit",
    ),
    VisualPlaceholder(
        id="viz-board-play",
        kind="svg_animation",
        title=LocalizedText(
            nl="Bandenscan: bal → band → herstel",
            en="Board scan: ball → board → recovery",
        ),
        caption=LocalizedText(
            nl=(
                "Originele SVG: scanpatroon wanneer de bal de band raakt. "
                "Procedures en uitzonderingen: FIH Indoor / KNHB."
            ),
            en=(
                "Original SVG: scan pattern when the ball meets the boards. "
                "Procedures and exceptions: FIH Indoor / KNHB."
            ),
        ),
        animation_key="board-play",
    ),
    VisualPlaceholder(
        id="viz-knhb-indoor-interpretations-slot",
        kind="official_link_slot",
        title=LocalizedText(
            nl="Officiële zaalinterpretaties (plaatshouder)",
            en="Official indoor interpretations (placeholder)",
        ),
        caption=LocalizedText(
            nl=(
                "Link naar KNHB/FIH-materiaal. Geen KNHB-illustratie in deze "
                "repo. EN-vertaling van NL-interpretaties: volgt later."
            ),
            en=(
                "Link to KNHB/FIH materials. No KNHB illustration ships in this "
                "repo. EN translation of NL interpretations: TBD."
            ),
        ),
        official_source_url=KNHB_HOME_URL,
        official_source_name="KNHB",
        knhb_illustration_placeholder=True,
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
                visualization_hint="board-play",
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
                    visualization_hint="board-play",
                ),
            },
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Herlees het bandenscan-kader en link naar FIH Indoor Rules.",
                    en="Revisit the board-scan frame and link to FIH Indoor Rules.",
                ),
                visualization_hint="board-play",
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
            "Volledige module: zaalbaan met banden, liftaccent, bandenscan en "
            "tempo — met visuals, oefenquiz en officiële bronlinks."
        ),
        en=(
            "Full module: court with boards, lift emphasis, board scan and "
            "tempo — with visuals, practice quiz and official source links."
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
            title=LocalizedText(
                nl="Waarom zaalregels als kernmodule",
                en="Why indoor rules as a core module",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Na veldregels vertaal je hetzelfde besliskader "
                        "(veiligheid → eerlijkheid → flow) naar de zaal: "
                        "minder ruimte, sneller tempo, en banden die het "
                        "speelbeeld veranderen."
                    ),
                    en=(
                        "After field rules you translate the same decision "
                        "frame (safety → fairness → flow) indoors: less space, "
                        "faster tempo, and boards that reshape the picture."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Deze module citeert geen auteursrechtelijk beschermde "
                        "FIH- of KNHB-regeltekst. We bouwen pedagogische "
                        "kaarten en verwijzen naar officiële Indoor Rules voor "
                        "de actuele standaard."
                    ),
                    en=(
                        "This module does not reproduce copyrighted FIH or "
                        "KNHB rule text. We build pedagogical maps and point "
                        "to official Indoor Rules for the current standard."
                    ),
                ),
            ],
        ),
        LearningSection(
            id="sec-court-boards",
            title=LocalizedText(
                nl="Zaalbaan & banden: waar je aandacht verandert",
                en="Court & boards: where your attention shifts",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Denk in lagen: zijbanden als harde grenzen, helften "
                        "voor cadans, en cirkels als zones met hogere "
                        "scoringsdichtheid. Exacte lijnen en afmetingen staan "
                        "in de officiële FIH Indoor Rules — hier alleen het "
                        "aandachtsmodel."
                    ),
                    en=(
                        "Think in layers: side boards as hard boundaries, "
                        "halves for cadence, and circles as zones with higher "
                        "scoring density. Exact lines and dimensions live in "
                        "the official FIH Indoor Rules — here only the "
                        "attention model."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Banden verkorten afstanden: een pass of rebound kan "
                        "snel van flank naar midden springen. Houd de "
                        "bandrand in je perifere scan."
                    ),
                    en=(
                        "Boards shorten distances: a pass or rebound can jump "
                        "from flank to middle quickly. Keep the board edge in "
                        "your peripheral scan."
                    ),
                ),
            ],
            visual_id="viz-court-boards",
        ),
        LearningSection(
            id="sec-lift-emphasis",
            title=LocalizedText(
                nl="Lift & omhoog spelen (zaalaccent)",
                en="Lift & raised ball (indoor emphasis)",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "In de zaal is omhoog spelen vaak strakker beoordeeld "
                        "dan op het veld: kleinere ruimte, snellere reacties, "
                        "meer lichamen dichtbij. Dit cursusmodel vraagt: is "
                        "de lift veilig en leesbaar — niet of ‘alles omhoog’ "
                        "mag."
                    ),
                    en=(
                        "Indoors, raising the ball is often judged more "
                        "tightly than outdoors: less space, faster reactions, "
                        "more bodies nearby. This course model asks: is the "
                        "lift safe and readable — not whether ‘anything raised’ "
                        "is fine."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Exacte hoogtegrenzen, uitzonderingen en "
                        "strafprocedures horen in FIH Indoor / KNHB. Hier "
                        "train je de reflex: plat als default, lift alleen "
                        "met context."
                    ),
                    en=(
                        "Exact height limits, exceptions and sanction "
                        "procedures belong in FIH Indoor / KNHB. Here you "
                        "train the reflex: flat as default, lift only with "
                        "context."
                    ),
                ),
            ],
            visual_id="viz-lift-limit",
        ),
        LearningSection(
            id="sec-board-play",
            title=LocalizedText(
                nl="Bandenspel: scan bal → band → herstel",
                en="Board play: scan ball → board → recovery",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Wanneer de bal de band nadert of raakt, verscherp je "
                        "scan: waar gaat de rebound, wie is dichtbij, is er "
                        "contact of gevaar? Bandenspel kan veilig én "
                        "problematisch zijn — context eerst."
                    ),
                    en=(
                        "When the ball approaches or meets the boards, "
                        "tighten your scan: where does the rebound go, who is "
                        "nearby, is there contact or danger? Board play can be "
                        "safe and problematic — context first."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Koppel terug aan de prioriteitsdriehoek: veiligheid "
                        "bij de band, dan eerlijk sanctioneren, dan flow als "
                        "het speelbeeld het toelaat."
                    ),
                    en=(
                        "Tie back to the priority triangle: safety at the "
                        "boards, then fair sanctioning, then flow if the "
                        "picture allows."
                    ),
                ),
            ],
            visual_id="viz-board-play",
        ),
        LearningSection(
            id="sec-indoor-tempo",
            title=LocalizedText(
                nl="Tempo & nabijheid",
                en="Tempo & proximity",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Kleinere ruimte betekent kortere besliscycli: dichter "
                        "bij het spel blijven, eerder oogcontact met je "
                        "partner, en sneller communiceren bij herstarten of "
                        "escalatie."
                    ),
                    en=(
                        "Less space means shorter decision cycles: stay closer "
                        "to play, seek partner eye contact earlier, and "
                        "communicate sooner on restarts or escalation."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Gebruik de KNHB/FIH-plaatshouder hieronder voor "
                        "officiële interpretaties; deze cursus bundelt geen "
                        "KNHB-kunst."
                    ),
                    en=(
                        "Use the KNHB/FIH placeholder below for official "
                        "interpretations; this course ships no KNHB art."
                    ),
                ),
            ],
            visual_id="viz-knhb-indoor-interpretations-slot",
        ),
        LearningSection(
            id="sec-indoor-practice-next",
            title=LocalizedText(
                nl="Oefenen en verder",
                en="Practice and next steps",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Maak de quiz hieronder. Sla voortgang op via je "
                        "cursussessie. Daarna: het pad naar professioneel "
                        "niveau (stub). Houd officiële FIH Indoor / "
                        "KNHB-bronnen bij de hand voor concrete regelvragen."
                    ),
                    en=(
                        "Take the quiz below. Save progress via your course "
                        "session. Next: the pathway toward professional "
                        "standard (stub). Keep official FIH Indoor / KNHB "
                        "sources handy for concrete rules questions."
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
