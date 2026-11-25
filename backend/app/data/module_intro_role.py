"""First full learning module: umpire role foundations (NL + EN).

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

INTRO_VISUALS: list[VisualPlaceholder] = [
    VisualPlaceholder(
        id="viz-safety-triangle",
        kind="svg_animation",
        title=LocalizedText(
            nl="Driehoek van scheidsrechterlijke focus",
            en="Umpire focus triangle",
        ),
        caption=LocalizedText(
            nl=(
                "Originele cursusanimatie: veiligheid → eerlijkheid → flow. "
                "Geen officiële FIH/KNHB-illustratie."
            ),
            en=(
                "Original course animation: safety → fairness → flow. "
                "Not an official FIH/KNHB illustration."
            ),
        ),
        animation_key="safety-triangle",
    ),
    VisualPlaceholder(
        id="viz-scan-cycle",
        kind="svg_animation",
        title=LocalizedText(
            nl="Scan-cyclus (blikrichting)",
            en="Scan cycle (where to look)",
        ),
        caption=LocalizedText(
            nl=(
                "Originele SVG: bal → conflictzone → periferie → partner. "
                "Gebruik dit als geheugensteun, niet als officiële signalenkaart."
            ),
            en=(
                "Original SVG: ball → contest zone → periphery → partner. "
                "Memory aid only — not an official signals chart."
            ),
        ),
        animation_key="scan-cycle",
    ),
    VisualPlaceholder(
        id="viz-calm-signal",
        kind="svg_animation",
        title=LocalizedText(
            nl="Calm-signaal na een beslissing",
            en="Calm signal after a decision",
        ),
        caption=LocalizedText(
            nl=(
                "Originele cursusillustratie: calm → kort → zichtbaar. "
                "Geen KNHB-gebarenplaat."
            ),
            en=(
                "Original course illustration: calm → brief → visible. "
                "Not a KNHB signals chart."
            ),
        ),
        animation_key="calm-signal",
    ),
    VisualPlaceholder(
        id="viz-context-split",
        kind="svg_animation",
        title=LocalizedText(
            nl="Veld versus zaal — zelfde kader, ander tempo",
            en="Field versus indoor — same frame, different tempo",
        ),
        caption=LocalizedText(
            nl=(
                "Originele split-view: meer ruimte buiten, snellere cadans "
                "binnen. Pedagogisch — geen officiële veldtekening."
            ),
            en=(
                "Original split view: more space outdoors, faster cadence "
                "indoors. Pedagogical — not an official pitch diagram."
            ),
        ),
        animation_key="context-split",
    ),
    VisualPlaceholder(
        id="viz-presence-arc",
        kind="svg_animation",
        title=LocalizedText(
            nl="Professionele aanwezigheid",
            en="Professional presence",
        ),
        caption=LocalizedText(
            nl=(
                "Originele animatie: houding → scan → stem. Helpt je zichtbaar "
                "en leesbaar te blijven zonder ‘theater’."
            ),
            en=(
                "Original animation: posture → scan → voice. Helps you stay "
                "visible and readable without theatrics."
            ),
        ),
        animation_key="presence-arc",
    ),
    VisualPlaceholder(
        id="viz-knhb-signals-slot",
        kind="official_link_slot",
        title=LocalizedText(
            nl="Officiële gebaren / interpretaties (plaatshouder)",
            en="Official signals / interpretations (placeholder)",
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

INTRO_QUIZ = Quiz(
    id="quiz-intro-umpire-role",
    title=LocalizedText(
        nl="Quiz: rol van de scheidsrechter",
        en="Quiz: the umpire’s role",
    ),
    questions=[
        QuizQuestion(
            id="q1-priority-order",
            type="multiple_choice",
            prompt=LocalizedText(
                nl=(
                    "Bij een snelle aanval botsen twee spelers licht, terwijl de "
                    "bal doorloopt naar een vrije speler. Wat is de beste "
                    "eerste prioriteit in je besliskader (pedagogisch, geen "
                    "regelcitaat)?"
                ),
                en=(
                    "On a fast break two players brush lightly while the ball "
                    "runs on to a free attacker. What is the best first priority "
                    "in your decision frame (pedagogical — not a rules quote)?"
                ),
            ),
            options=[
                QuizOption(
                    id="a",
                    text=LocalizedText(
                        nl="Direct een kaart geven om ‘discipline te tonen’.",
                        en="Award a card immediately to ‘show discipline’.",
                    ),
                ),
                QuizOption(
                    id="b",
                    text=LocalizedText(
                        nl=(
                            "Eerst veiligheid en of er nog voordeel voor de "
                            "aanval is; daarna eerlijkheid/sanctioneren als "
                            "nodig."
                        ),
                        en=(
                            "First safety and whether advantage still exists "
                            "for the attack; then fairness/sanctioning if needed."
                        ),
                    ),
                ),
                QuizOption(
                    id="c",
                    text=LocalizedText(
                        nl="Altijd meteen fluiten bij elk contact.",
                        en="Always whistle immediately on any contact.",
                    ),
                ),
                QuizOption(
                    id="d",
                    text=LocalizedText(
                        nl="Alleen naar de coach kijken voor instructie.",
                        en="Only look to the coach for instruction.",
                    ),
                ),
            ],
            correct_option_id="b",
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Juist. Professioneel denken begint bij veiligheid en "
                        "spelvoordeel, daarna consistent sanctioneren. "
                        "Raadpleeg FIH/KNHB voor actuele voorschriften."
                    ),
                    en=(
                        "Correct. Professional thinking starts with safety and "
                        "advantage, then consistent sanctioning. Consult "
                        "FIH/KNHB for current prescriptions."
                    ),
                ),
                visualization_hint="safety-triangle",
            ),
            feedback_incorrect={
                "a": QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Kaarten zijn middelen, geen doel. Eerst context: "
                            "gevaar, voordeel, ernst — dan het juiste niveau."
                        ),
                        en=(
                            "Cards are tools, not goals. First context: danger, "
                            "advantage, severity — then the right level."
                        ),
                    ),
                    visualization_hint="safety-triangle",
                ),
                "c": QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Niet elk contact is een overtreding of vraagt een "
                            "fluit. Leer eerst kijken, dan kiezen."
                        ),
                        en=(
                            "Not every contact is an offence or needs a whistle. "
                            "Learn to see first, then choose."
                        ),
                    ),
                    visualization_hint="scan-cycle",
                ),
                "d": QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Coaches sturen hun team; jij blijft verantwoordelijk "
                            "voor veiligheid en eerlijkheid op het veld."
                        ),
                        en=(
                            "Coaches manage their team; you remain responsible "
                            "for safety and fairness on the pitch."
                        ),
                    ),
                ),
            },
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Herlees de sectie over prioriteiten: veiligheid → eerlijkheid → flow.",
                    en="Revisit the priorities section: safety → fairness → flow.",
                ),
                visualization_hint="safety-triangle",
            ),
        ),
        QuizQuestion(
            id="q2-scan-partner",
            type="multiple_choice",
            prompt=LocalizedText(
                nl=(
                    "Je scan-cyclus omvat bal, contestzone en periferie. Wat is "
                    "het vierde element in het cursusmodel?"
                ),
                en=(
                    "Your scan cycle covers ball, contest zone and periphery. "
                    "What is the fourth element in this course model?"
                ),
            ),
            options=[
                QuizOption(
                    id="a",
                    text=LocalizedText(
                        nl="Alleen de scorebordtijd.",
                        en="Only the scoreboard clock.",
                    ),
                ),
                QuizOption(
                    id="b",
                    text=LocalizedText(
                        nl="Je partner-scheidsrechter (of teammanagement-lijn).",
                        en="Your partner umpire (or team-management line).",
                    ),
                ),
                QuizOption(
                    id="c",
                    text=LocalizedText(
                        nl="De kleur van de ballen.",
                        en="The colour of the balls.",
                    ),
                ),
                QuizOption(
                    id="d",
                    text=LocalizedText(
                        nl="Alleen de dug-out van de thuisclub.",
                        en="Only the home dug-out.",
                    ),
                ),
            ],
            correct_option_id="b",
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Juist. Partnership voorkomt blinde vlekken: korte "
                        "oogcontacten en duidelijke verantwoordelijkheidszones."
                    ),
                    en=(
                        "Correct. Partnership prevents blind spots: brief eye "
                        "contact and clear areas of responsibility."
                    ),
                ),
                visualization_hint="scan-cycle",
            ),
            feedback_incorrect={
                "a": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Tijd telt, maar hoort niet in de primaire scan-cyclus van dit model.",
                        en="Time matters, but is not in this model’s primary scan cycle.",
                    ),
                    visualization_hint="scan-cycle",
                ),
                "c": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Irrelevant voor het scanmodel.",
                        en="Irrelevant to the scan model.",
                    ),
                ),
                "d": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Teammanagement kan relevant zijn, maar het model noemt je partner eerst.",
                        en="Team management can matter, but the model names your partner first.",
                    ),
                    visualization_hint="scan-cycle",
                ),
            },
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Vierde element: partner (teamwork).",
                    en="Fourth element: partner (teamwork).",
                ),
                visualization_hint="scan-cycle",
            ),
        ),
        QuizQuestion(
            id="q3-safety-keyword",
            type="written",
            prompt=LocalizedText(
                nl=(
                    "Welk Engels sleutelwoord vat de eerste hoek van de focus-"
                    "driehoek samen? (één woord)"
                ),
                en=(
                    "Which English keyword summarises the first corner of the "
                    "focus triangle? (one word)"
                ),
            ),
            accepted_answers=["safety"],
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl="Juist — safety (veiligheid) eerst.",
                    en="Correct — safety first.",
                ),
                visualization_hint="safety-triangle",
            ),
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Verwacht antwoord: safety. Daarna fairness en flow.",
                    en="Expected answer: safety. Then fairness and flow.",
                ),
                visualization_hint="safety-triangle",
            ),
        ),
        QuizQuestion(
            id="q4-calm-communication",
            type="written",
            prompt=LocalizedText(
                nl=(
                    "Welk Engels woord gebruikt deze cursus voor korte, rustige "
                    "spelercommunicatie na een beslissing? (één woord)"
                ),
                en=(
                    "Which English word does this course use for brief, steady "
                    "player talk after a decision? (one word)"
                ),
            ),
            accepted_answers=["calm"],
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl="Juist — calm: kort, duidelijk, zonder discussie te voeden.",
                    en="Correct — calm: brief, clear, without feeding an argument.",
                ),
                visualization_hint="calm-signal",
            ),
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Verwacht antwoord: calm.",
                    en="Expected answer: calm.",
                ),
                visualization_hint="calm-signal",
            ),
        ),
        QuizQuestion(
            id="q5-context-cadence",
            type="multiple_choice",
            prompt=LocalizedText(
                nl=(
                    "Wat blijft gelijk tussen veld en zaal in dit cursusmodel, "
                    "terwijl de cadans verandert?"
                ),
                en=(
                    "What stays the same between field and indoor in this course "
                    "model, while the cadence changes?"
                ),
            ),
            options=[
                QuizOption(
                    id="a",
                    text=LocalizedText(
                        nl="Alleen de kleur van de ballen.",
                        en="Only the colour of the balls.",
                    ),
                ),
                QuizOption(
                    id="b",
                    text=LocalizedText(
                        nl=(
                            "Het gedeelde besliskader (veiligheid → eerlijkheid "
                            "→ flow) en de scan-logica."
                        ),
                        en=(
                            "The shared decision frame (safety → fairness → flow) "
                            "and the scan logic."
                        ),
                    ),
                ),
                QuizOption(
                    id="c",
                    text=LocalizedText(
                        nl="De exacte afstanden op het veld.",
                        en="The exact distances on the pitch.",
                    ),
                ),
                QuizOption(
                    id="d",
                    text=LocalizedText(
                        nl="Alleen de menigte op de tribune.",
                        en="Only the crowd in the stands.",
                    ),
                ),
            ],
            correct_option_id="b",
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Juist. Context verandert tempo en dichtheid; het "
                        "denkkader blijft herbruikbaar."
                    ),
                    en=(
                        "Correct. Context changes tempo and density; the "
                        "thinking frame stays reusable."
                    ),
                ),
                visualization_hint="context-split",
            ),
            feedback_incorrect={
                "a": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Irrelevant voor het cursusmodel.",
                        en="Irrelevant to the course model.",
                    ),
                ),
                "c": QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Afstanden verschillen juist — daarom verandert de "
                            "cadans, niet het kader."
                        ),
                        en=(
                            "Distances differ — that is why cadence changes, "
                            "not the frame."
                        ),
                    ),
                    visualization_hint="context-split",
                ),
                "d": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Publiek kan druk geven, maar is niet het gedeelde model.",
                        en="Crowds can add pressure, but are not the shared model.",
                    ),
                    visualization_hint="presence-arc",
                ),
            },
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Herlees veld versus zaal: zelfde kader, ander tempo.",
                    en="Revisit field versus indoor: same frame, different tempo.",
                ),
                visualization_hint="context-split",
            ),
        ),
    ],
)

INTRO_MODULE = ModuleStub(
    id="mod-intro-role",
    kind="shared",
    title=LocalizedText(
        nl="Introductie: rol van de scheidsrechter",
        en="Introduction: the umpire’s role",
    ),
    summary=LocalizedText(
        nl=(
            "Showcase-module: rijke NL/EN-lesstof, originele animaties en een "
            "aparte nagekeken quiz — veiligheid, eerlijkheid en flow als "
            "professioneel besliskader."
        ),
        en=(
            "Showcase module: rich NL/EN reading, original animations and a "
            "separate graded quiz — safety, fairness and flow as a professional "
            "decision frame."
        ),
    ),
    learning_objectives=[
        LocalizedText(
            nl="De drie prioriteiten (veiligheid, eerlijkheid, flow) in eigen woorden uitleggen.",
            en="Explain the three priorities (safety, fairness, flow) in your own words.",
        ),
        LocalizedText(
            nl="Een eenvoudige scan-cyclus toepassen inclusief partner-check.",
            en="Apply a simple scan cycle including a partner check.",
        ),
        LocalizedText(
            nl="Rustige, korte, zichtbare communicatie beschrijven na een beslissing.",
            en="Describe calm, brief, visible communication after a decision.",
        ),
        LocalizedText(
            nl="Veld- versus zaalcontext op hoog niveau onderscheiden zonder regeltekst te citeren.",
            en="Distinguish field vs indoor context at a high level without quoting rule text.",
        ),
        LocalizedText(
            nl="Professionele aanwezigheid (houding, scan, stem) in één zin samenvatten.",
            en="Summarise professional presence (posture, scan, voice) in one sentence.",
        ),
    ],
    instruction_outline=[
        LocalizedText(
            nl="Prioriteiten: veiligheid → eerlijkheid → flow.",
            en="Priorities: safety → fairness → flow.",
        ),
        LocalizedText(
            nl="Scan-cyclus: bal → contest → periferie → partner.",
            en="Scan cycle: ball → contest → periphery → partner.",
        ),
        LocalizedText(
            nl="Communicatie: calm, kort, zichtbaar.",
            en="Communication: calm, brief, visible.",
        ),
        LocalizedText(
            nl="Context: veldtempo vs zaalsnelheid (hoog niveau).",
            en="Context: outdoor tempo vs indoor pace (high level).",
        ),
    ],
    content_status="full",
    sections=[
        LearningSection(
            id="sec-why-this-matters",
            title=LocalizedText(
                nl="Waarom deze module eerst",
                en="Why this module comes first",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Nederlandse scheidsrechters werken in een continuum: "
                        "van clubjeugd tot topcompetities zoals de Hoofdklasse. "
                        "Techniek en fitheid tellen, maar professioneel niveau "
                        "begint bij een stabiel besliskader: wat bescherm je "
                        "eerst, hoe blijf je consistent, en hoe houd je het "
                        "spel leesbaar voor iedereen."
                    ),
                    en=(
                        "Dutch umpires work across a continuum: from club youth "
                        "to top competitions such as the Hoofdklasse. Technique "
                        "and fitness matter, but professional standard starts "
                        "with a stable decision frame: what you protect first, "
                        "how you stay consistent, and how you keep the game "
                        "readable for everyone."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Deze cursus citeert geen auteursrechtelijk beschermde "
                        "FIH- of KNHB-regeltekst. We bouwen pedagogische "
                        "kaders en verwijzen naar officiële documenten voor de "
                        "actuele standaard."
                    ),
                    en=(
                        "This course does not reproduce copyrighted FIH or KNHB "
                        "rule text. We build pedagogical frames and point to "
                        "official documents for the current standard."
                    ),
                ),
            ],
        ),
        LearningSection(
            id="sec-priority-triangle",
            title=LocalizedText(
                nl="Besliskader: veiligheid → eerlijkheid → flow",
                en="Decision frame: safety → fairness → flow",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Veiligheid: bescherm spelers tegen gevaarlijke situaties "
                        "en escalatie. Als iets er onveilig uitziet, vertraag je "
                        "intern je oordeel niet — je toetst eerst of iemand "
                        "risico loopt."
                    ),
                    en=(
                        "Safety: protect players from dangerous situations and "
                        "escalation. If something looks unsafe, do not delay "
                        "your internal check — first ask whether someone is at "
                        "risk."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Eerlijkheid: gelijke behandeling van beide teams, "
                        "duidelijke standaard over de wedstrijd heen, en "
                        "sanctioneren dat past bij ernst — niet bij wie het "
                        "hardst klaagt."
                    ),
                    en=(
                        "Fairness: equal treatment of both teams, a clear "
                        "standard across the match, and sanctions that match "
                        "severity — not whoever complains loudest."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Flow: waar veiligheid en eerlijkheid het toelaten, "
                        "houd je het spel levend. Onnodig fluiten of lange "
                        "discussies ondermijnen leesbaarheid — vooral op weg "
                        "naar hoger niveau."
                    ),
                    en=(
                        "Flow: where safety and fairness allow, keep the game "
                        "alive. Unnecessary whistles or long debates undermine "
                        "readability — especially on the path to higher levels."
                    ),
                ),
            ],
            visual_id="viz-safety-triangle",
        ),
        LearningSection(
            id="sec-scan-cycle",
            title=LocalizedText(
                nl="Kijken voordat je fluit: de scan-cyclus",
                en="See before you whistle: the scan cycle",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Een bruikbare gewoonte: bal → contestzone (waar "
                        "lichamen en sticks samenkomen) → periferie (nabije "
                        "spelers, vrije ruimte, teammanagement) → partner. "
                        "Herhaal dit in korte cycli, niet als starre checklist "
                        "tijdens elke seconde."
                    ),
                    en=(
                        "A useful habit: ball → contest zone (where bodies and "
                        "sticks meet) → periphery (nearby players, free space, "
                        "team management) → partner. Repeat in short cycles — "
                        "not as a rigid checklist every second."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Op het veld heb je meer ruimte en vaak iets meer tijd; "
                        "in de zaal is alles dichter en sneller. Het model blijft "
                        "hetzelfde — de cadans verandert."
                    ),
                    en=(
                        "Outdoors you usually have more space and a touch more "
                        "time; indoors everything is tighter and faster. The "
                        "model stays the same — the cadence changes."
                    ),
                ),
            ],
            visual_id="viz-scan-cycle",
        ),
        LearningSection(
            id="sec-communication",
            title=LocalizedText(
                nl="Communicatie: calm, kort, zichtbaar",
                en="Communication: calm, brief, visible",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Na een beslissing: één korte zin of duidelijk gebaar, "
                        "oogcontact indien veilig, en door. Lange onderhandelingen "
                        "op het veld trainen spelers om te debatteren in plaats "
                        "van te spelen."
                    ),
                    en=(
                        "After a decision: one short sentence or a clear signal, "
                        "eye contact if safe, and move on. Long on-field "
                        "negotiations train players to debate instead of play."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Met je partner: vooraf zones en ‘help mij’-signalen "
                        "afspreken. Professioneel teamwork is zichtbaar zonder "
                        "dat toeschouwers een overlegvergadering zien."
                    ),
                    en=(
                        "With your partner: agree zones and ‘help me’ cues "
                        "beforehand. Professional teamwork is visible without "
                        "looking like a committee meeting."
                    ),
                ),
            ],
            visual_id="viz-calm-signal",
        ),
        LearningSection(
            id="sec-presence",
            title=LocalizedText(
                nl="Aanwezigheid: houding, scan, stem",
                en="Presence: posture, scan, voice",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Professioneel niveau is niet alleen ‘juiste fluiten’. "
                        "Spelers lezen je lichaam: open houding, stabiele "
                        "positie, en een stem die kort blijft. Zo blijf je "
                        "zichtbaar zonder het middelpunt van de discussie te "
                        "worden."
                    ),
                    en=(
                        "Professional standard is not only ‘correct whistles’. "
                        "Players read your body: open posture, stable position, "
                        "and a voice that stays brief. That keeps you visible "
                        "without becoming the centre of every debate."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Koppel aanwezigheid aan je scan: als je al weet waar "
                        "je partner staat, kun je sneller beslissen en rustiger "
                        "uitleggen. Aanwezigheid is dus geen show — het is "
                        "leesbaarheid."
                    ),
                    en=(
                        "Tie presence to your scan: when you already know where "
                        "your partner is, you decide faster and explain more "
                        "calmly. Presence is not a show — it is readability."
                    ),
                ),
            ],
            visual_id="viz-presence-arc",
        ),
        LearningSection(
            id="sec-field-vs-indoor",
            title=LocalizedText(
                nl="Veld versus zaal (hoog niveau)",
                en="Field versus indoor (high level)",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Veld: grotere afstanden, andere lift-/gevaarspatronen, "
                        "meer ruimte om voordeel te lezen. Zaal: banden, "
                        "kortere reactietijden, snellere herstart van scannen. "
                        "Latere modules verdiepen beide contexten — hier leer "
                        "je eerst het gedeelde denkkader."
                    ),
                    en=(
                        "Field: longer distances, different lift/danger "
                        "patterns, more space to read advantage. Indoor: "
                        "boards, shorter reaction times, faster restarts of "
                        "your scan. Later modules deepen both contexts — here "
                        "you first lock the shared thinking frame."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Onthoud: het model blijft veiligheid → eerlijkheid → "
                        "flow. Alleen de cadans van kijken en beslissen "
                        "versnelt of vertraagt met de context."
                    ),
                    en=(
                        "Remember: the model stays safety → fairness → flow. "
                        "Only the cadence of seeing and deciding speeds up or "
                        "slows down with the context."
                    ),
                ),
            ],
            visual_id="viz-context-split",
        ),
        LearningSection(
            id="sec-official-signals",
            title=LocalizedText(
                nl="Officiële bronnen (geen gekopieerde kunst)",
                en="Official sources (no copied artwork)",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Gebaren, interpretaties en wedstrijdvoorschriften horen "
                        "bij FIH/KNHB. Deze cursus toont alleen originele "
                        "pedagogische visuals en linkt naar officiële pagina’s "
                        "— nooit KNHB-illustraties in de repo."
                    ),
                    en=(
                        "Signals, interpretations and match prescriptions belong "
                        "with FIH/KNHB. This course only shows original "
                        "pedagogical visuals and links to official pages — "
                        "never KNHB illustrations in the repo."
                    ),
                ),
            ],
            visual_id="viz-knhb-signals-slot",
        ),
        LearningSection(
            id="sec-practice-next",
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
                        "hervatten. Ga daarna door naar veld- en zaalmodules; "
                        "houd officiële FIH/KNHB-bronnen bij de hand voor "
                        "concrete regelvragen."
                    ),
                    en=(
                        "When you have finished the reading, open the module "
                        "quiz via the button below — on a separate page, with "
                        "multiple-choice and written items, explanations and "
                        "visuals. Save progress via your course session so you "
                        "can resume later. Then continue into field and indoor "
                        "modules; keep official FIH/KNHB sources handy for "
                        "concrete rules questions."
                    ),
                ),
            ],
        ),
    ],
    visuals=INTRO_VISUALS,
    quiz_id=INTRO_QUIZ.id,
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
    order=1,
)
