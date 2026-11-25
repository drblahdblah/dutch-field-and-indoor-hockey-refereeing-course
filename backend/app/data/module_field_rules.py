"""Full learning module: field hockey rules core (NL + EN).

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

FIH_RULES_URL = (
    "https://www.fih.hockey/inside-fih/our-official-documents/rules-of-hockey"
)
KNHB_HOME_URL = "https://www.knhb.nl/"

FIELD_VISUALS: list[VisualPlaceholder] = [
    VisualPlaceholder(
        id="viz-match-start",
        kind="svg_animation",
        title=LocalizedText(nl="Wedstrijdstart", en="Match start"),
        caption=LocalizedText(
            nl="Voor de aftrap: spelers tellen, doelen checken, toss met de stick, kant en aftrap kiezen.",
            en="Before push-back: count players, check goals, toss with the stick, choose side and who starts.",
        ),
        animation_key="match-start",
    ),
    VisualPlaceholder(
        id="viz-umpire-position",
        kind="svg_animation",
        title=LocalizedText(nl="Waar je staat", en="Where you stand"),
        caption=LocalizedText(
            nl="Lead-scheidsrechter dicht bij de bal op de eigen helft; support dekt de andere helft en de diepte.",
            en="Lead umpire near the ball on their half; support covers the other half and depth.",
        ),
        animation_key="umpire-position",
    ),
    VisualPlaceholder(
        id="viz-hit-types",
        kind="svg_animation",
        title=LocalizedText(nl="Slagtypes", en="Stroke types"),
        caption=LocalizedText(
            nl="Drie basisbewegingen: push (duwen), slap (korte slag), hit (volle slag) — lees kracht en richting.",
            en="Three basic strokes: push, slap, hit — read power and direction.",
        ),
        animation_key="hit-types",
    ),
    VisualPlaceholder(
        id="viz-obstruction-types",
        kind="svg_animation",
        title=LocalizedText(nl="Obstructie", en="Obstruction"),
        caption=LocalizedText(
            nl="Stick-obstructie, lichaamsobstructie, en schaduw/derde-man die de opponent wegblokkeert van de bal.",
            en="Stick obstruction, body obstruction, and shadow/third-man blocking the opponent from the ball.",
        ),
        animation_key="obstruction-types",
    ),
    VisualPlaceholder(
        id="viz-danger-cone",
        kind="svg_animation",
        title=LocalizedText(nl="Omhoog / gevaar (basis)", en="Raised / danger (basics)"),
        caption=LocalizedText(
            nl="Bal speelt hard of omhoog richting een dichtbij staande speler — weeg richting, afstand en snelheid.",
            en="Ball played hard or raised toward a nearby player — weigh direction, distance and speed.",
        ),
        animation_key="danger-cone",
    ),
    VisualPlaceholder(
        id="viz-card-ladder",
        kind="svg_animation",
        title=LocalizedText(nl="Kaarten", en="Cards"),
        caption=LocalizedText(
            nl="Escalatie: groen (waarschuwing), geel (tijdstraf), rood (uitsluiting) — koppel aan ernst en herhaling.",
            en="Escalation: green (warning), yellow (time penalty), red (dismissal) — tie to severity and repetition.",
        ),
        animation_key="card-ladder",
    ),
    VisualPlaceholder(
        id="viz-penalty-corner",
        kind="svg_animation",
        title=LocalizedText(nl="Strafcorner", en="Penalty corner"),
        caption=LocalizedText(
            nl="Aanval zet klaar buiten de cirkel; verdediging en keeper op de lijn — jij checkt aantallen en ruimte vóór de injectie.",
            en="Attack set outside the circle; defence and keeper on the line — you check numbers and space before the injection.",
        ),
        animation_key="penalty-corner",
    ),
    VisualPlaceholder(
        id="viz-penalty-stroke",
        kind="svg_animation",
        title=LocalizedText(nl="Strafbal", en="Penalty stroke"),
        caption=LocalizedText(
            nl="Eén aanvaller tegen de keeper op de strafbalstip — jij controleert stilstand en signaleert duidelijk.",
            en="One attacker versus the keeper at the stroke spot — you check stillness and signal clearly.",
        ),
        animation_key="penalty-stroke",
    ),
    VisualPlaceholder(
        id="viz-gk-limits",
        kind="svg_animation",
        title=LocalizedText(nl="Keeper: wat mag", en="Keeper: what is allowed"),
        caption=LocalizedText(
            nl="In de eigen cirkel mag de keeper met lichaam/uitrusting verdedigen; buiten die zone gelden veldspelersregels.",
            en="Inside their own circle the keeper may defend with body/equipment; outside that zone outfield rules apply.",
        ),
        animation_key="gk-limits",
    ),
    VisualPlaceholder(
        id="viz-pitch-zones",
        kind="svg_animation",
        title=LocalizedText(nl="Veldzones", en="Pitch zones"),
        caption=LocalizedText(
            nl="Helft, 23m-band en cirkel — dichter bij het doel betekent kortere scan-cycli en vaker partner-check.",
            en="Half, 23m band and circle — closer to goal means shorter scan cycles and more partner checks.",
        ),
        animation_key="pitch-zones",
    ),
    VisualPlaceholder(
        id="viz-restart-bubble",
        kind="svg_animation",
        title=LocalizedText(nl="Herstart", en="Restart"),
        caption=LocalizedText(
            nl="Vrije slag: eerst een leesbare ruimtebubbel rond de bal, dan het speelbeeld.",
            en="Free hit: first a readable space bubble around the ball, then the play.",
        ),
        animation_key="restart-bubble",
    ),
    VisualPlaceholder(
        id="viz-advantage-lens",
        kind="svg_animation",
        title=LocalizedText(nl="Voordeel", en="Advantage"),
        caption=LocalizedText(
            nl="Lichte fout, maar de aanval houdt ruimte en tempo — speel voordeel ná veiligheid.",
            en="Light fault, but the attack keeps space and tempo — play advantage after safety.",
        ),
        animation_key="advantage-lens",
    ),
]

FIELD_QUIZ = Quiz(
    id="quiz-field-rules-core",
    title=LocalizedText(
        nl="Quiz: veldregels (kern)",
        en="Quiz: field rules (core)",
    ),
    questions=[
        QuizQuestion(
            id="q1-raised-ball",
            type="multiple_choice",
            prompt=LocalizedText(
                nl=(
                    "Een speler speelt de bal hard en omhoog in de richting van "
                    "een tegenstander op korte afstand. Wat is de beste eerste "
                    "overweging (pedagogisch kader — geen regelcitaat)?"
                ),
                en=(
                    "A player plays the ball hard and raised toward an opponent "
                    "at close range. What is the umpire’s best first "
                    "consideration (pedagogical frame — not a rules quote)?"
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
                        "Juist. Gevaar hangt af van context: richting, afstand "
                        "en snelheid. Consulteer FIH-regels/KNHB-interpretaties "
                        "voor de actuele standaard."
                    ),
                    en=(
                        "Correct. Danger depends on context: direction, distance "
                        "and speed. Consult FIH rules / KNHB interpretations for "
                        "the current standard."
                    ),
                ),
                visualization_hint="danger-cone",
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
                    visualization_hint="danger-cone",
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
                    visualization_hint="danger-cone",
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
                    visualization_hint="danger-cone",
                ),
            },
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Bekijk de gevaarskegel: richting, afstand, snelheid.",
                    en="Review the danger cone: direction, distance, speed.",
                ),
                visualization_hint="danger-cone",
            ),
        ),
        QuizQuestion(
            id="q2-restart-space",
            type="multiple_choice",
            prompt=LocalizedText(
                nl=(
                    "Bij een vrije slag / herstart dicht bij tegenstanders: wat "
                    "is de beste eerste scheidsrechterlijke focus in dit "
                    "cursusmodel?"
                ),
                en=(
                    "At a free hit / restart close to opponents: what is the "
                    "best first umpiring focus in this course model?"
                ),
            ),
            options=[
                QuizOption(
                    id="a",
                    text=LocalizedText(
                        nl="Alleen naar de dug-out kijken tot iemand klaagt.",
                        en="Only watch the dug-out until someone complains.",
                    ),
                ),
                QuizOption(
                    id="b",
                    text=LocalizedText(
                        nl="Altijd meteen een strafcorner toekennen.",
                        en="Always award a penalty corner immediately.",
                    ),
                ),
                QuizOption(
                    id="c",
                    text=LocalizedText(
                        nl=(
                            "Check of er genoeg ruimte (‘bubbel’) is en of de "
                            "herstart veilig en leesbaar kan starten — daarna "
                            "het speelbeeld."
                        ),
                        en=(
                            "Check that enough space (‘bubble’) exists and the "
                            "restart can begin safely and readably — then read "
                            "the play."
                        ),
                    ),
                ),
                QuizOption(
                    id="d",
                    text=LocalizedText(
                        nl="Negeer afstand; alleen de balbaan telt.",
                        en="Ignore distance; only the ball path matters.",
                    ),
                ),
            ],
            correct_option_id="c",
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Juist. Herstarten vragen eerst om ruimte en leesbaarheid. "
                        "Exacte afstanden: officiële FIH/KNHB-bronnen."
                    ),
                    en=(
                        "Correct. Restarts first need space and readability. "
                        "Exact distances: official FIH/KNHB sources."
                    ),
                ),
                visualization_hint="restart-bubble",
            ),
            feedback_incorrect={
                "a": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Teammanagement kan later relevant zijn; eerst de herstartzone.",
                        en="Team management can matter later; first the restart zone.",
                    ),
                    visualization_hint="restart-bubble",
                ),
                "b": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Strafcorners zijn situatief — niet de standaardreactie op elke herstart.",
                        en="Penalty corners are situational — not the default for every restart.",
                    ),
                    visualization_hint="restart-bubble",
                ),
                "d": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Afstand tot tegenstanders hoort bij een veilige, eerlijke herstart.",
                        en="Distance from opponents is part of a safe, fair restart.",
                    ),
                    visualization_hint="restart-bubble",
                ),
            },
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Herlees de herstartbubbel: ruimte eerst, dan speelbeeld.",
                    en="Revisit the restart bubble: space first, then the play.",
                ),
                visualization_hint="restart-bubble",
            ),
        ),
        QuizQuestion(
            id="q3-scoring-area-keyword",
            type="written",
            prompt=LocalizedText(
                nl=(
                    "Welk Engels sleutelwoord gebruikt deze cursus voor het "
                    "halfronde scoringsgebied bij het doel? (één woord)"
                ),
                en=(
                    "Which English keyword does this course use for the "
                    "semi-circular scoring area by the goal? (one word)"
                ),
            ),
            accepted_answers=["circle"],
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl="Juist — circle (cirkel / strafschopgebied in spreektaal).",
                    en="Correct — circle.",
                ),
                visualization_hint="pitch-zones",
            ),
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Verwacht antwoord: circle. Zie ook de veldzones-visual.",
                    en="Expected answer: circle. See also the pitch-zones visual.",
                ),
                visualization_hint="pitch-zones",
            ),
        ),
        QuizQuestion(
            id="q4-advantage-keyword",
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
            accepted_answers=["advantage"],
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl="Juist — ‘advantage’ (voordeel) is het gangbare signaalwoord.",
                    en="Correct — ‘advantage’ is the common signal word.",
                ),
                visualization_hint="advantage-lens",
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
                visualization_hint="advantage-lens",
            ),
        ),
        QuizQuestion(
            id="q5-advantage-when",
            type="multiple_choice",
            prompt=LocalizedText(
                nl=(
                    "Er is een lichte overtreding, maar de aanval heeft nog "
                    "duidelijke ruimte en tempo. Wat past het best bij de "
                    "voordeellens in dit cursusmodel (pedagogisch)?"
                ),
                en=(
                    "There is a light offence, but the attack still has clear "
                    "space and tempo. What best matches the advantage lens in "
                    "this course model (pedagogical)?"
                ),
            ),
            options=[
                QuizOption(
                    id="a",
                    text=LocalizedText(
                        nl="Altijd meteen fluiten — elke overtreding stoppen.",
                        en="Always whistle immediately — stop every offence.",
                    ),
                ),
                QuizOption(
                    id="b",
                    text=LocalizedText(
                        nl=(
                            "Eerst checken of de aanval nog voordeel heeft "
                            "zonder veiligheidsrisico; zo ja, leesbaar "
                            "doorlaten en later herstellen indien nodig."
                        ),
                        en=(
                            "First check whether the attack still has advantage "
                            "without a safety risk; if so, play on readably and "
                            "reset later if needed."
                        ),
                    ),
                ),
                QuizOption(
                    id="c",
                    text=LocalizedText(
                        nl="Negeer veiligheid zolang de score open blijft.",
                        en="Ignore safety as long as the score stays open.",
                    ),
                ),
                QuizOption(
                    id="d",
                    text=LocalizedText(
                        nl="Vraag de coach welke optie hij prefereert.",
                        en="Ask the coach which option they prefer.",
                    ),
                ),
            ],
            correct_option_id="b",
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Juist. De voordeellens weegt ruimte en tempo ná "
                        "veiligheid — niet in plaats daarvan."
                    ),
                    en=(
                        "Correct. The advantage lens weighs space and tempo "
                        "after safety — not instead of it."
                    ),
                ),
                visualization_hint="advantage-lens",
            ),
            feedback_incorrect={
                "a": QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Niet altijd. Onnodig fluiten kan flow én "
                            "leesbaarheid schaden wanneer de aanval nog "
                            "duidelijk voordeel heeft."
                        ),
                        en=(
                            "Not always. Unnecessary whistles can harm flow "
                            "and readability when the attack still has clear "
                            "advantage."
                        ),
                    ),
                    visualization_hint="advantage-lens",
                ),
                "c": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Veiligheid blijft eerst — voordeel volgt daarna.",
                        en="Safety stays first — advantage comes after.",
                    ),
                    visualization_hint="danger-cone",
                ),
                "d": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Jij beslist; coaches sturen niet jouw voordeellens.",
                        en="You decide; coaches do not drive your advantage lens.",
                    ),
                    visualization_hint="advantage-lens",
                ),
            },
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Herlees de voordeellens: contest → voordeel → ruimte.",
                    en="Revisit the advantage lens: contest → advantage → space.",
                ),
                visualization_hint="advantage-lens",
            ),
        ),
    ],
)

FIELD_MODULE = ModuleStub(
    id="mod-field-rules-core",
    kind="field",
    title=LocalizedText(
        nl="Veld: kernregels & besliskaders",
        en="Field: core rules & decision frames",
    ),
    summary=LocalizedText(
        nl=(
            "Veldkern: wedstrijdstart, positie, slagtypes, obstructie, "
            "omhoog, kaarten, PC/PS, keeper, zones, herstarten en voordeel "
            "— met situatiediagrammen en een aparte quiz."
        ),
        en=(
            "Field core: match start, positioning, stroke types, "
            "obstruction, raised, cards, PC/PS, keeper, zones, restarts "
            "and advantage — with situation diagrams and a separate quiz."
        ),
    ),
    learning_objectives=[
        LocalizedText(
            nl="Veldzones (helften, 23m, cirkels) in eigen woorden lokaliseren.",
            en="Locate pitch zones (halves, 23m, circles) in your own words.",
        ),
        LocalizedText(
            nl="Een herstart beoordelen op ruimte/leesbaarheid vóór het speelbeeld.",
            en="Judge a restart for space/readability before reading the play.",
        ),
        LocalizedText(
            nl="Gevaar bij omhoog/hard gespeelde ballen via richting×afstand×snelheid wegen.",
            en="Weigh danger on raised/hard balls via direction×distance×speed.",
        ),
        LocalizedText(
            nl="Cirkelaanvallen herkennen als zone met hogere aandacht zonder regeltekst te citeren.",
            en="Recognise circle attacks as a higher-attention zone without quoting rule text.",
        ),
        LocalizedText(
            nl="Voordeel lezen wanneer de aanval nog ruimte en tempo heeft (na veiligheid).",
            en="Read advantage when the attack still has space and tempo (after safety).",
        ),
    ],
    instruction_outline=[
        LocalizedText(
            nl="Veldkaart: helften → 23m → cirkels.",
            en="Pitch map: halves → 23m → circles.",
        ),
        LocalizedText(
            nl="Herstarten: bubbel van ruimte, dan speelbeeld.",
            en="Restarts: space bubble, then the play.",
        ),
        LocalizedText(
            nl="Gevaar: richting × afstand × snelheid.",
            en="Danger: direction × distance × speed.",
        ),
        LocalizedText(
            nl="Cirkel: hogere scan-dichtheid, partner-check.",
            en="Circle: denser scan, partner check.",
        ),
        LocalizedText(
            nl="Voordeel: contest → lens → ruimte (na veiligheid).",
            en="Advantage: contest → lens → space (after safety).",
        ),
    ],
    content_status="full",
    sections=[
        LearningSection(
            id="sec-field-why",
            title=LocalizedText(nl="Wat je in deze module leert", en="What this module teaches"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Dit is de veldkern: wedstrijdstart, positie, slagtypes, "
                        "obstructie, omhoog (basis), kaarten, strafcorner, "
                        "strafbal, keeperrechten, zones, herstarten en voordeel. "
                        "Elke stap: diagram van de situatie, dan uitleg. Geen "
                        "overgenomen FIH-/KNHB-citaat — officiële tekst onder "
                        "Verder lezen. Harde scenario’s volgen in de module "
                        "Veld: harde beslissingen."
                    ),
                    en=(
                        "This is field core: match start, positioning, stroke "
                        "types, obstruction, raised (basics), cards, penalty "
                        "corner, penalty stroke, keeper rights, zones, "
                        "restarts and advantage. Each step: situation diagram, "
                        "then explanation. No reproduced FIH/KNHB quotation — "
                        "official text under Further reading. Hard scenarios "
                        "follow in Field: hard decisions."
                    ),
                ),
            ],
            visual_id="viz-match-start",
        ),
        LearningSection(
            id="sec-match-start",
            title=LocalizedText(nl="Wedstrijdstart", en="Match start"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Voor de aftrap: (1) tel de spelers per team — "
                        "officieel maximum veldspelers staat in FIH/KNHB "
                        "(meestal 11 inclusief keeper; check actuele "
                        "competitieregels); (2) check doelen, netten en "
                        "veldlijnen op veilige speelbaarheid; (3) doe de "
                        "toss met de stick (of munt): de winnaar kiest kant "
                        "óf aftrap (bal), de ander krijgt het restant."
                    ),
                    en=(
                        "Before push-back: (1) count players per team — the "
                        "official outfield maximum is in FIH/KNHB (usually 11 "
                        "including the keeper; check current competition "
                        "rules); (2) check goals, nets and pitch lines for "
                        "safe playability; (3) do the toss with the stick "
                        "(or coin): the winner chooses side or push-back "
                        "(ball), the other gets the remainder."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Noteer wie aftrapt en welke kant. Stem kort met je "
                        "partner over lead/support-helften. Exacte "
                        "wedstrijdformules (speeltijd, time-outs) horen in "
                        "bond-/competitieregels."
                    ),
                    en=(
                        "Note who pushes back and which side. Briefly agree "
                        "lead/support halves with your partner. Exact match "
                        "formats (playing time, time-outs) live in "
                        "federation/competition rules."
                    ),
                ),
            ],
            visual_id="viz-match-start",
        ),
        LearningSection(
            id="sec-positioning",
            title=LocalizedText(nl="Waar staan tijdens het spel", en="Where to stand during play"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Basis: jij hebt een helft als lead — blijf dichter "
                        "bij de bal wanneer die op jouw helft speelt, met "
                        "zicht op cirkel én sideline. Je partner support: "
                        "diepte, tweede duel, en overdracht wanneer de bal "
                        "de middellijn kruist."
                    ),
                    en=(
                        "Basics: you own a half as lead — stay closer to the "
                        "ball when it is on your half, with sight of circle "
                        "and sideline. Your partner supports: depth, second "
                        "contest, and handoff when the ball crosses halfway."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Bij set pieces (PC, stroke, herstart dicht bij de "
                        "cirkel) verplaats je vóór de uitvoering naar een "
                        "hoek met zicht op injectie/schot én keeper. Beweeg "
                        "actief; sta niet vast op de sideline."
                    ),
                    en=(
                        "On set pieces (PC, stroke, restart near the circle) "
                        "move before the play to an angle with sight of "
                        "injection/shot and keeper. Move actively; do not "
                        "freeze on the sideline."
                    ),
                ),
            ],
            visual_id="viz-umpire-position",
        ),
        LearningSection(
            id="sec-hit-types",
            title=LocalizedText(nl="Slagtypes: push, slap, hit", en="Stroke types: push, slap, hit"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Push: bal wordt geduwd zonder slagbeweging — vaak "
                        "controle, minder kracht. Slap: korte, gecontroleerde "
                        "slag met beperkte backswing. Hit: volle slag met "
                        "langere backswing en meer kracht/snelheid."
                    ),
                    en=(
                        "Push: ball is pushed without a striking swing — "
                        "often control, less power. Slap: short controlled "
                        "strike with limited backswing. Hit: full strike with "
                        "longer backswing and more power/speed."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Waarom dit telt: een hit of harde slap omhoog/in "
                        "iemand weegt zwaarder op gevaar dan een zachte push. "
                        "Lees type + richting + nabijheid samen. Exacte "
                        "techniekdefinities: FIH/KNHB."
                    ),
                    en=(
                        "Why it matters: a hit or hard slap raised/into "
                        "someone weighs heavier on danger than a soft push. "
                        "Read type + direction + proximity together. Exact "
                        "technique definitions: FIH/KNHB."
                    ),
                ),
            ],
            visual_id="viz-hit-types",
        ),
        LearningSection(
            id="sec-obstruction",
            title=LocalizedText(
                nl="Obstructie: stick, lichaam, schaduw",
                en="Obstruction: stick, body, shadow",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Stick-obstructie: de stick blokkeert de opponent "
                        "onrechtmatig van de bal. Lichaamsobstructie "
                        "(normaal): lichaam schermt de bal af zodat de "
                        "opponent er niet legaal bij kan. Schaduw/derde-man: "
                        "een derde speler blokkeert of ‘schaduwt’ de "
                        "opponent weg van de balbezitter."
                    ),
                    en=(
                        "Stick obstruction: the stick unlawfully blocks the "
                        "opponent from the ball. Body obstruction (normal): "
                        "the body screens the ball so the opponent cannot "
                        "legally reach it. Shadow/third-man: a third player "
                        "blocks or ‘shadows’ the opponent away from the "
                        "ball carrier."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Lees: had de opponent een reële kans op de bal? "
                        "Was er actieve afscherming? Fluit als de afscherming "
                        "de duel oneerlijk maakt; speel door als de opponent "
                        "geen echte route had. Exacte criteria: FIH/KNHB."
                    ),
                    en=(
                        "Read: did the opponent have a real chance at the "
                        "ball? Was there active screening? Whistle if the "
                        "screen makes the contest unfair; play on if the "
                        "opponent had no real route. Exact criteria: FIH/KNHB."
                    ),
                ),
            ],
            visual_id="viz-obstruction-types",
        ),
        LearningSection(
            id="sec-danger-raised",
            title=LocalizedText(nl="Omhoog spelen (basis)", en="Raised ball (basics)"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Een omhoog of hard gespeelde bal is niet "
                        "automatisch fout. Weeg richting (naar wie?), "
                        "afstand (hoe dicht?) en snelheid (hoe hard?). "
                        "Gevaar kan zonder contact. Prioriteit: veiligheid "
                        "→ eerlijk sanctioneren → flow."
                    ),
                    en=(
                        "A raised or hard ball is not automatically illegal. "
                        "Weigh direction (toward whom?), distance (how "
                        "close?) and speed (how hard?). Danger can exist "
                        "without contact. Priority: safety → fair sanction "
                        "→ flow."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Basisvoorbeeld: zachte push over een lege zone → "
                        "vaak speel door. Harde hit kniehoogte op iemand "
                        "dichtbij → fluit. Verdieping (drukke zones, "
                        "kaarten) volgt in Veld: harde beslissingen."
                    ),
                    en=(
                        "Basic example: soft push across empty space → "
                        "often play on. Hard hit at knee height into someone "
                        "nearby → whistle. Deepening (crowded zones, cards) "
                        "follows in Field: hard decisions."
                    ),
                ),
            ],
            visual_id="viz-danger-cone",
        ),
        LearningSection(
            id="sec-cards",
            title=LocalizedText(nl="Kaarten: wanneer en hoe", en="Cards: when and how"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Groen: waarschuwing / korte time-out van de speler "
                        "(exacte duur: bond). Geel: zwaardere tijdelijke "
                        "uitsluiting. Rood: permanente uitsluiting. Kaarten "
                        "escaleren bij herhaling of ernst; communiceer "
                        "zichtbaar (kaart omhoog, kort signaal)."
                    ),
                    en=(
                        "Green: warning / short player time-out (exact "
                        "duration: federation). Yellow: heavier temporary "
                        "suspension. Red: permanent dismissal. Cards "
                        "escalate with repetition or severity; communicate "
                        "visibly (card up, short signal)."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Wanneer: na een leesbare fout die waarschuwing of "
                        "straf verdient — niet als vervanging voor een "
                        "ontbrekende gevaarlezing. Hoe: stop het spel waar "
                        "nodig, toon de kaart aan speler en tafel, noteer. "
                        "Exacte procedures: KNHB/competitie."
                    ),
                    en=(
                        "When: after a readable foul that deserves warning "
                        "or penalty — not as a substitute for a missing "
                        "danger read. How: stop play where needed, show the "
                        "card to player and table, record it. Exact "
                        "procedures: KNHB/competition."
                    ),
                ),
            ],
            visual_id="viz-card-ladder",
        ),
        LearningSection(
            id="sec-penalty-corner",
            title=LocalizedText(nl="Strafcorner (basis)", en="Penalty corner (basics)"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Een strafcorner volgt op bepaalde fouten van de "
                        "verdediging in de eigen 23m/cirkel (exacte lijst: "
                        "FIH). Opstelling: aanvallers buiten de cirkel tot "
                        "de injectie; verdedigers/keeper achter de "
                        "achterlijn tot de bal gespeeld is — aantallen en "
                        "posities volgens officiële regels."
                    ),
                    en=(
                        "A penalty corner follows certain defensive fouls in "
                        "their own 23m/circle (exact list: FIH). Setup: "
                        "attackers outside the circle until injection; "
                        "defenders/keeper behind the backline until the ball "
                        "is played — numbers and positions per official rules."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Jouw job vóór de injectie: check aantallen, "
                        "afstanden, stilte/klaar-signaal; tijdens: gevaar "
                        "bij schot/omhoog, feet in de cirkel, vroege run. "
                        "Na een goal of herstart: herstel het beeld met je "
                        "partner."
                    ),
                    en=(
                        "Your job before injection: check numbers, "
                        "distances, ready signal; during: danger on "
                        "shot/raised, feet in the circle, early run. After "
                        "a goal or restart: reset the picture with your "
                        "partner."
                    ),
                ),
            ],
            visual_id="viz-penalty-corner",
        ),
        LearningSection(
            id="sec-penalty-stroke",
            title=LocalizedText(nl="Strafbal (basis)", en="Penalty stroke (basics)"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Strafbal volgt op ernstige fouten die een "
                        "duidelijke scoringskans ontnemen in de cirkel "
                        "(exacte gronden: FIH). Eén aanvaller neemt de bal "
                        "vanuit de strafbalstip; alleen de keeper verdedigt "
                        "op de lijn tot de bal gespeeld is."
                    ),
                    en=(
                        "A penalty stroke follows serious fouls that deny a "
                        "clear goal-scoring opportunity in the circle "
                        "(exact grounds: FIH). One attacker takes from the "
                        "stroke spot; only the keeper defends on the line "
                        "until the ball is played."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Check: stilstand van bal en keeper, juiste plek, "
                        "geen vroege beweging. Signaleer duidelijk. Na de "
                        "stroke: goal, herstart of herneming volgens "
                        "uitkomst — zie officiële tabel."
                    ),
                    en=(
                        "Check: stillness of ball and keeper, correct spot, "
                        "no early movement. Signal clearly. After the "
                        "stroke: goal, restart or retake per the outcome — "
                        "see the official table."
                    ),
                ),
            ],
            visual_id="viz-penalty-stroke",
        ),
        LearningSection(
            id="sec-gk-basics",
            title=LocalizedText(nl="Keeper: wat mag / niet mag", en="Keeper: what is / is not allowed"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "In de eigen cirkel mag de keeper de bal verdedigen "
                        "met stick, pads, body en (waar toegestaan) handen/"
                        "bescherming volgens keeperregels. Buiten de cirkel "
                        "gedraagt de keeper zich als veldspeler tenzij de "
                        "regels een uitzondering geven."
                    ),
                    en=(
                        "Inside their own circle the keeper may defend the "
                        "ball with stick, pads, body and (where allowed) "
                        "hands/protection per keeper rules. Outside the "
                        "circle the keeper acts as an outfield player unless "
                        "rules give an exception."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Niet: de aanvaller raken zonder de bal te spelen, "
                        "gevaarlijk contact, of rechten claimen buiten de "
                        "zone. Slide/duik komt dieper in Veld: harde "
                        "beslissingen. Exacte keeperrechten: FIH/KNHB."
                    ),
                    en=(
                        "Not allowed: hitting the attacker without playing "
                        "the ball, dangerous contact, or claiming rights "
                        "outside the zone. Slide/dive is deepened in Field: "
                        "hard decisions. Exact keeper rights: FIH/KNHB."
                    ),
                ),
            ],
            visual_id="viz-gk-limits",
        ),
        LearningSection(
            id="sec-pitch-zones",
            title=LocalizedText(nl="Veldzones & aandacht", en="Pitch zones & attention"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Helft → 23m → cirkel: dichter bij het doel betekent "
                        "meer contactrisico en scoringskans. Verhoog "
                        "scan-frequentie en partner-checks nabij de cirkel."
                    ),
                    en=(
                        "Half → 23m → circle: closer to goal means more "
                        "contact risk and scoring chance. Raise scan "
                        "frequency and partner checks near the circle."
                    ),
                ),
            ],
            visual_id="viz-pitch-zones",
        ),
        LearningSection(
            id="sec-restarts",
            title=LocalizedText(nl="Herstarten", en="Restarts"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Vrije slag: check eerst ruimte (bubbel) tot "
                        "tegenstanders, dan speelbeeld. Meters en "
                        "zelfpass-regels: FIH/KNHB."
                    ),
                    en=(
                        "Free hit: first check space (bubble) from "
                        "opponents, then the play. Metres and self-pass "
                        "rules: FIH/KNHB."
                    ),
                ),
            ],
            visual_id="viz-restart-bubble",
        ),
        LearningSection(
            id="sec-advantage-lens",
            title=LocalizedText(nl="Voordeel (basis)", en="Advantage (basics)"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Niet elke lichte fout vraagt om een fluit. Als "
                        "veiligheid oké is en de aanval ruimte/tempo houdt, "
                        "geef voordeel. Geen vrijbrief bij gevaar."
                    ),
                    en=(
                        "Not every light fault needs a whistle. If safety is "
                        "ok and the attack keeps space/tempo, play "
                        "advantage. Not a free pass on danger."
                    ),
                ),
            ],
            visual_id="viz-advantage-lens",
        ),
        LearningSection(
            id="sec-field-practice-next",
            title=LocalizedText(nl="Quiz en volgende module", en="Quiz and next module"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Open de veldquiz hieronder. Ga daarna naar "
                        "Zaalkernregels, of naar Veld: harde beslissingen "
                        "voor drukke omhoog-situaties, keeperslide en "
                        "kaarten bij push/pirouette."
                    ),
                    en=(
                        "Open the field quiz below. Then go to Indoor core "
                        "rules, or to Field: hard decisions for crowded "
                        "raised situations, keeper slide and cards on "
                        "push/pirouette."
                    ),
                ),
            ],
        ),
    ],
    visuals=FIELD_VISUALS,
    quiz_id=FIELD_QUIZ.id,
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
                    nl="Officiële FIH Rules of Hockey — bron voor veldhockeyregels.",
                    en="Official FIH Rules of Hockey — source for outdoor hockey rules.",
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
    order=2,
)
