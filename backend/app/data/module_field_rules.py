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
        id="viz-pitch-zones",
        kind="svg_animation",
        title=LocalizedText(
            nl="Veldzones (scheidsrechterlijk overzicht)",
            en="Pitch zones (umpire overview)",
        ),
        caption=LocalizedText(
            nl=(
                "Originele SVG: helften, 23m-band, cirkels. Geen officiële "
                "FIH/KNHB-veldmaat illustratie — raadpleeg officiële bronnen "
                "voor exacte afmetingen."
            ),
            en=(
                "Original SVG: halves, 23m band, circles. Not an official "
                "FIH/KNHB pitch diagram — consult official sources for exact "
                "dimensions."
            ),
        ),
        animation_key="pitch-zones",
    ),
    VisualPlaceholder(
        id="viz-danger-cone",
        kind="svg_animation",
        title=LocalizedText(
            nl="Gevaarskegel: richting × afstand × snelheid",
            en="Danger cone: direction × distance × speed",
        ),
        caption=LocalizedText(
            nl=(
                "Originele cursusanimatie voor omhoog/hard gespeelde ballen. "
                "Geen overgenomen regeltekst of KNHB-kunst."
            ),
            en=(
                "Original course animation for raised/hard balls. No reproduced "
                "rule text or KNHB art."
            ),
        ),
        animation_key="danger-cone",
    ),
    VisualPlaceholder(
        id="viz-restart-bubble",
        kind="svg_animation",
        title=LocalizedText(
            nl="Herstartbubbel (afstand tot tegenstanders)",
            en="Restart bubble (space from opponents)",
        ),
        caption=LocalizedText(
            nl=(
                "Originele SVG: denk in een ‘bubbel’ rond de herstartplek. "
                "Exacte meters en procedures: FIH/KNHB."
            ),
            en=(
                "Original SVG: think in a ‘bubble’ around the restart spot. "
                "Exact metres and procedures: FIH/KNHB."
            ),
        ),
        animation_key="restart-bubble",
    ),
    VisualPlaceholder(
        id="viz-field-attack",
        kind="svg_animation",
        title=LocalizedText(
            nl="Scenario: aanval richting cirkel",
            en="Scenario: attack toward the circle",
        ),
        caption=LocalizedText(
            nl=(
                "Originele scenario-SVG: aanvalspad + gevaarskegel in de "
                "23m/cirkel. Geen KNHB-kunst of officiële veldmaat."
            ),
            en=(
                "Original scenario SVG: attack path + danger cone in the "
                "23m/circle. No KNHB art or official pitch diagram."
            ),
        ),
        animation_key="field-attack",
    ),
    VisualPlaceholder(
        id="viz-advantage-lens",
        kind="svg_animation",
        title=LocalizedText(
            nl="Voordeellens (leesbaar doorlaten)",
            en="Advantage lens (readable play-on)",
        ),
        caption=LocalizedText(
            nl=(
                "Originele cursusillustratie: contest → voordeel lezen → "
                "ruimte houden. Geen KNHB-/FIH-gebarenplaat — officiële "
                "bronnen staan onder Verder lezen."
            ),
            en=(
                "Original course illustration: contest → read advantage → "
                "keep space. Not a KNHB/FIH signals chart — official sources "
                "are under Further reading."
            ),
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
            "Showcase-module: rijke NL/EN-lesstof in klikstappen, originele "
            "veldanimaties en een aparte nagekeken quiz — zones, herstarten, "
            "gevaar en voordeel."
        ),
        en=(
            "Showcase module: rich NL/EN reading in click-steps, original "
            "field animations and a separate graded quiz — zones, restarts, "
            "danger and advantage."
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
            title=LocalizedText(
                nl="Waarom veldregels als kernmodule",
                en="Why field rules as a core module",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Na het gedeelde besliskader (veiligheid → eerlijkheid → "
                        "flow) vertaal je dat naar het veld: waar gebeurt wat, "
                        "wanneer verscherp je je scan, en hoe blijf je "
                        "leesbaar bij herstarten en gevaar."
                    ),
                    en=(
                        "After the shared decision frame (safety → fairness → "
                        "flow) you translate it outdoors: where things happen, "
                        "when you tighten your scan, and how you stay readable "
                        "on restarts and danger."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Deze module citeert geen auteursrechtelijk beschermde "
                        "FIH- of KNHB-regeltekst. We bouwen pedagogische "
                        "kaarten en verwijzen naar officiële documenten voor "
                        "de actuele standaard."
                    ),
                    en=(
                        "This module does not reproduce copyrighted FIH or KNHB "
                        "rule text. We build pedagogical maps and point to "
                        "official documents for the current standard."
                    ),
                ),
            ],
        ),
        LearningSection(
            id="sec-pitch-zones",
            title=LocalizedText(
                nl="Veldzones: waar je aandacht verandert",
                en="Pitch zones: where your attention shifts",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Denk in lagen: eigen helft / andere helft, de 23m-band "
                        "als overgang naar aanvalsdruk, en de cirkels als "
                        "zones waar scoringskansen en contactrisico’s dichter "
                        "op elkaar zitten. Exacte lijnen en afmetingen staan "
                        "in de officiële FIH Rules — hier alleen het "
                        "aandachtsmodel."
                    ),
                    en=(
                        "Think in layers: own half / other half, the 23m band "
                        "as the shift into attacking pressure, and the circles "
                        "as zones where scoring chances and contact risks sit "
                        "closer together. Exact lines and dimensions live in "
                        "the official FIH Rules — here only the attention model."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Gebruik de zones om je cadans te sturen: meer ruimte "
                        "middenveld → bredere scan; dichter bij de cirkel → "
                        "kortere cycli en vaker partner-check."
                    ),
                    en=(
                        "Use the zones to drive your cadence: more midfield "
                        "space → wider scan; closer to the circle → shorter "
                        "cycles and more frequent partner checks."
                    ),
                ),
            ],
            visual_id="viz-pitch-zones",
        ),
        LearningSection(
            id="sec-restarts",
            title=LocalizedText(
                nl="Herstarten: eerst ruimte, dan speelbeeld",
                en="Restarts: space first, then the play",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Vrije slagen en andere herstarten vragen om een "
                        "leesbaar startbeeld. In dit cursusmodel check je "
                        "eerst of er een ‘bubbel’ van ruimte rond de "
                        "herstartplek is — genoeg afstand tot tegenstanders "
                        "om veilig en eerlijk te starten — en pas daarna "
                        "lees je het aanvallende/verdedigende speelbeeld."
                    ),
                    en=(
                        "Free hits and other restarts need a readable starting "
                        "picture. In this course model you first check for a "
                        "‘bubble’ of space around the restart spot — enough "
                        "distance from opponents to start safely and fairly — "
                        "and only then read the attacking/defending picture."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Meters, zelfpass-opties en speciale situaties "
                        "(bijvoorbeeld dicht bij de cirkel) horen in de "
                        "officiële bronnen. Hier train je de volgorde: "
                        "ruimte → veiligheid → flow."
                    ),
                    en=(
                        "Metres, self-pass options and special situations "
                        "(for example near the circle) belong in the official "
                        "sources. Here you train the order: space → safety → "
                        "flow."
                    ),
                ),
            ],
            visual_id="viz-restart-bubble",
        ),
        LearningSection(
            id="sec-danger-raised",
            title=LocalizedText(
                nl="Gevaarlijk spel & omhoog spelen",
                en="Dangerous play & raised ball",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Een harde of omhoog gespeelde bal is niet automatisch "
                        "fout — en niet automatisch oké. Weeg richting "
                        "(naar wie?), afstand (hoe dichtbij?) en snelheid "
                        "(hoe hard?). Gevaar kan bestaan zonder contact."
                    ),
                    en=(
                        "A hard or raised ball is not automatically illegal — "
                        "and not automatically fine. Weigh direction (toward "
                        "whom?), distance (how close?) and speed (how hard?). "
                        "Danger can exist without contact."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Koppel dit terug aan de prioriteitsdriehoek: "
                        "veiligheid eerst, dan eerlijk sanctioneren, dan flow "
                        "als het speelbeeld het toelaat. Kaarten zijn middelen, "
                        "geen automatische reflex."
                    ),
                    en=(
                        "Tie this back to the priority triangle: safety first, "
                        "then fair sanctioning, then flow if the picture "
                        "allows. Cards are tools, not an automatic reflex."
                    ),
                ),
            ],
            visual_id="viz-danger-cone",
        ),
        LearningSection(
            id="sec-circle-context",
            title=LocalizedText(
                nl="Cirkelcontext (hoog niveau)",
                en="Circle context (high level)",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "In en rond de cirkel stijgt de dichtheid: schoten, "
                        "blokken, sticks dicht bij voeten, en snellere "
                        "escalatie. Verhoog je scan-frequentie, zoek eerder "
                        "oogcontact met je partner, en wees scherp op "
                        "herstarten die de bubbel raken."
                    ),
                    en=(
                        "In and around the circle density rises: shots, "
                        "blocks, sticks near feet, and faster escalation. "
                        "Raise your scan frequency, seek partner eye contact "
                        "earlier, and stay sharp on restarts that touch the "
                        "bubble."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Strafcorners en andere set pieces krijgen later "
                        "eigen verdieping. Voor nu: herken de zone, "
                        "bescherm veiligheid, houd beslissingen leesbaar."
                    ),
                    en=(
                        "Penalty corners and other set pieces get deeper "
                        "treatment later. For now: recognise the zone, "
                        "protect safety, keep decisions readable."
                    ),
                ),
            ],
            visual_id="viz-field-attack",
        ),
        LearningSection(
            id="sec-advantage-lens",
            title=LocalizedText(
                nl="Voordeel lezen zonder de standaard te verliezen",
                en="Read advantage without losing the standard",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Niet elke overtreding vraagt om een fluit. Als de "
                        "aanval na een lichte fout nog duidelijk ruimte en "
                        "tempo heeft — en veiligheid niet in het geding is — "
                        "houd je het speelbeeld leesbaar door voordeel te "
                        "geven. Dat is flow ná veiligheid en eerlijkheid, "
                        "geen vrijbrief."
                    ),
                    en=(
                        "Not every offence needs a whistle. If after a light "
                        "fault the attack still has clear space and tempo — "
                        "and safety is not at risk — you keep the picture "
                        "readable by playing advantage. That is flow after "
                        "safety and fairness, not a free pass."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Officiële FIH-/KNHB-voorschriften en interpretaties "
                        "blijven bij hun bronnen (zie Verder lezen). Hier "
                        "oefen je alleen de voordeellens als cursusmodel."
                    ),
                    en=(
                        "Official FIH/KNHB prescriptions and interpretations "
                        "stay with their sources (see Further reading). Here "
                        "you practise only the advantage lens as a course "
                        "model."
                    ),
                ),
            ],
            visual_id="viz-advantage-lens",
        ),
        LearningSection(
            id="sec-field-practice-next",
            title=LocalizedText(
                nl="Oefenen en verder",
                en="Practice and next steps",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Als je de lesstof hebt gelezen, open je de modulequiz "
                        "via de knop onderaan — op een aparte pagina, met "
                        "meerkeuze én open vragen, uitleg en visuals. Sla "
                        "voortgang op via je cursussessie zodat je later kunt "
                        "hervatten. Ga daarna door naar de zaalmodule; houd "
                        "officiële FIH/KNHB-bronnen bij de hand voor concrete "
                        "regelvragen."
                    ),
                    en=(
                        "When you have finished the reading, open the module "
                        "quiz via the button below — on a separate page, with "
                        "multiple-choice and written items, explanations and "
                        "visuals. Save progress via your course session so you "
                        "can resume later. Then continue into the indoor "
                        "module; keep official FIH/KNHB sources handy for "
                        "concrete rules questions."
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
