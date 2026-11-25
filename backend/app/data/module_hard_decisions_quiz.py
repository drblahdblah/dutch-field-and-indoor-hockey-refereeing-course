"""Quiz for hard umpiring decision scenarios (NL + EN).

Pedagogical framing only — no reproduced FIH/KNHB copyrighted rule text or art.
"""

from app.schemas import (
    LocalizedText,
    Quiz,
    QuizFeedback,
    QuizOption,
    QuizQuestion,
)

_FIH_NOTE_NL = (
    "Raadpleeg altijd de officiële FIH-regels en KNHB-interpretaties — dit is "
    "een besliskader, geen regelcitaat."
)
_FIH_NOTE_EN = (
    "Always consult official FIH rules and KNHB interpretations — this is a "
    "decision frame, not a rules quotation."
)

HARD_QUIZ = Quiz(
    id="quiz-hard-decisions",
    title=LocalizedText(
        nl="Quiz: harde scheidsrechterlijke beslissingen",
        en="Quiz: hard umpiring decisions",
    ),
    questions=[
        QuizQuestion(
            id="q1-raised-first",
            type="multiple_choice",
            prompt=LocalizedText(
                nl=(
                    "Een bal gaat hard omhoog richting een dichtbij staande "
                    "speler. Wat is je beste eerste lezing? (pedagogisch kader)"
                ),
                en=(
                    "A ball rises hard toward a nearby player. What is your "
                    "best first read? (pedagogical frame)"
                ),
            ),
            options=[
                QuizOption(
                    id="a",
                    text=LocalizedText(
                        nl="Direct groene kaart — omhoog is altijd illegaal.",
                        en="Green card immediately — raised is always illegal.",
                    ),
                ),
                QuizOption(
                    id="b",
                    text=LocalizedText(
                        nl="Alleen fluiten als iemand geraakt wordt.",
                        en="Only whistle if someone is hit.",
                    ),
                ),
                QuizOption(
                    id="c",
                    text=LocalizedText(
                        nl=(
                            "Weeg gevaar: richting × afstand × snelheid "
                            "(veld); check liftgrenzen en nabijheid (zaal)."
                        ),
                        en=(
                            "Weigh danger: direction × distance × speed "
                            "(field); check lift limits and proximity (indoor)."
                        ),
                    ),
                ),
                QuizOption(
                    id="d",
                    text=LocalizedText(
                        nl="Altijd doorspelen voor flow bij een aanval.",
                        en="Always play on for flow during an attack.",
                    ),
                ),
            ],
            correct_option_id="c",
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Juist. Hard decisions starten met gevaar wegen — "
                        "niet met een automatische kaart. Veld en zaal delen "
                        "het leesmodel, maar zaal heeft strengere liftgrenzen. "
                        + _FIH_NOTE_NL
                    ),
                    en=(
                        "Correct. Hard decisions start by weighing danger — "
                        "not an automatic card. Field and indoor share the "
                        "read model, but indoor has stricter lift limits. "
                        + _FIH_NOTE_EN
                    ),
                ),
                visualization_hint="hard-raised-danger",
            ),
            feedback_incorrect={
                "a": QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Onjuist. Omhoog is niet automatisch een kaart; "
                            "gevaar en context bepalen sanctie."
                        ),
                        en=(
                            "Incorrect. Raised is not automatically a card; "
                            "danger and context set the sanction."
                        ),
                    ),
                    visualization_hint="hard-raised-danger",
                ),
                "b": QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Te laat. Gevaarlijke trajecten kun je al "
                            "sanctioneren vóór contact."
                        ),
                        en=(
                            "Too late. Dangerous trajectories can be "
                            "sanctioned before contact."
                        ),
                    ),
                    visualization_hint="hard-raised-danger",
                ),
                "d": QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Flow mag niet boven veiligheid gaan — weeg "
                            "gevaar eerst."
                        ),
                        en=(
                            "Flow must not override safety — weigh danger "
                            "first."
                        ),
                    ),
                    visualization_hint="hard-raised-danger",
                ),
            },
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Herlees: richting × afstand × snelheid (en zaallift).",
                    en="Revisit: direction × distance × speed (and indoor lift).",
                ),
                visualization_hint="hard-raised-danger",
            ),
        ),
        QuizQuestion(
            id="q2-clear-pressure",
            type="multiple_choice",
            prompt=LocalizedText(
                nl=(
                    "Twee verdedigers drukken een aanvaller die duidelijk de "
                    "bal heeft. Wat weeg je eerst?"
                ),
                en=(
                    "Two defenders press an attacker who clearly has the "
                    "ball. What do you weigh first?"
                ),
            ),
            options=[
                QuizOption(
                    id="a",
                    text=LocalizedText(
                        nl="Altijd free hit voor de verdediging — 2-tegen-1.",
                        en="Always free hit for defence — 2-vs-1.",
                    ),
                ),
                QuizOption(
                    id="b",
                    text=LocalizedText(
                        nl="Wachten tot de bal stil ligt vóór je fluit.",
                        en="Wait until the ball is still before you whistle.",
                    ),
                ),
                QuizOption(
                    id="c",
                    text=LocalizedText(
                        nl="Zaal: altijd band-out; veld: altijd penalty corner.",
                        en="Indoor: always board-out; field: always penalty corner.",
                    ),
                ),
                QuizOption(
                    id="d",
                    text=LocalizedText(
                        nl=(
                            "Bezit is duidelijk bij de aanvaller: lees of "
                            "contact legaal is of de bal illegaal wordt "
                            "weggenomen."
                        ),
                        en=(
                            "Possession is clearly with the attacker: read "
                            "whether contact is legal or the ball is taken "
                            "illegally."
                        ),
                    ),
                ),
            ],
            correct_option_id="d",
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Juist. Bij duidelijk bezit lees je de tackle/contact "
                        "op de balbezitter — niet het aantal verdedigers. "
                        "Veld en zaal delen dit; zaal is sneller en dichter. "
                        + _FIH_NOTE_NL
                    ),
                    en=(
                        "Correct. With clear possession you read the "
                        "tackle/contact on the ball carrier — not the "
                        "defender count. Field and indoor share this; indoor "
                        "is faster and tighter. " + _FIH_NOTE_EN
                    ),
                ),
                visualization_hint="hard-pressure-clear",
            ),
            feedback_incorrect={
                "a": QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Aantal verdedigers is geen automatische fout. "
                            "Lees bezit en contact."
                        ),
                        en=(
                            "Defender count is not an automatic foul. Read "
                            "possession and contact."
                        ),
                    ),
                    visualization_hint="hard-pressure-clear",
                ),
                "b": QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Je moet in beweging lezen — stilstand is geen "
                            "voorwaarde om te fluiten."
                        ),
                        en=(
                            "You must read in motion — stillness is not a "
                            "precondition to whistle."
                        ),
                    ),
                    visualization_hint="hard-pressure-clear",
                ),
                "c": QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Geen vaste uitkomst per discipline — weeg "
                            "contact en bezit in context."
                        ),
                        en=(
                            "No fixed outcome per discipline — weigh contact "
                            "and possession in context."
                        ),
                    ),
                    visualization_hint="hard-pressure-clear",
                ),
            },
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Herlees: duidelijk bezit → lees de contactkwaliteit.",
                    en="Revisit: clear possession → read contact quality.",
                ),
                visualization_hint="hard-pressure-clear",
            ),
        ),
        QuizQuestion(
            id="q3-contested",
            type="multiple_choice",
            prompt=LocalizedText(
                nl=(
                    "De bal is betwist: twee sticks en geen duidelijke "
                    "controle. Welke optie is de slechtste reflex?"
                ),
                en=(
                    "The ball is contested: two sticks and no clear control. "
                    "Which option is the worst reflex?"
                ),
            ),
            options=[
                QuizOption(
                    id="a",
                    text=LocalizedText(
                        nl=(
                            "Automatisch ‘aanval’ fluiten omdat de aanvallende "
                            "helft dichterbij was."
                        ),
                        en=(
                            "Automatically whistle ‘attack’ because the "
                            "attacking half was closer."
                        ),
                    ),
                ),
                QuizOption(
                    id="b",
                    text=LocalizedText(
                        nl=(
                            "Wachten tot controle zichtbaar is, dan fluiten "
                            "of doorspelen op basis van wat je zag."
                        ),
                        en=(
                            "Wait until control is visible, then whistle or "
                            "play on based on what you saw."
                        ),
                    ),
                ),
                QuizOption(
                    id="c",
                    text=LocalizedText(
                        nl=(
                            "Korte eye contact met je partner als het op de "
                            "scheidingslijn speelt."
                        ),
                        en=(
                            "Brief eye contact with your partner if play is "
                            "on the split line."
                        ),
                    ),
                ),
                QuizOption(
                    id="d",
                    text=LocalizedText(
                        nl=(
                            "Advantage alleen geven als één kant duidelijk "
                            "ruimte krijgt."
                        ),
                        en=(
                            "Only play advantage when one side clearly gains "
                            "space."
                        ),
                    ),
                ),
            ],
            correct_option_id="a",
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Juist — dat is de slechtste reflex. Bij onduidelijk "
                        "bezit mag ‘aanval’-bias niet de lezing vervangen. "
                        "Wacht op controle of een duidelijke overtreding. "
                        + _FIH_NOTE_NL
                    ),
                    en=(
                        "Correct — that is the worst reflex. With unclear "
                        "possession, attack-bias must not replace the read. "
                        "Wait for control or a clear offence. " + _FIH_NOTE_EN
                    ),
                ),
                visualization_hint="hard-contested",
            ),
            feedback_incorrect={
                "b": QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Dat is juist goed gedrag — de vraag zocht de "
                            "slechtste reflex (automatisch ‘aanval’)."
                        ),
                        en=(
                            "That is good practice — the question sought the "
                            "worst reflex (automatic ‘attack’)."
                        ),
                    ),
                    visualization_hint="hard-contested",
                ),
                "c": QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Partnercontact is goed — niet de slechtste "
                            "reflex. Zoek de automatische ‘aanval’-fluit."
                        ),
                        en=(
                            "Partner contact is good — not the worst reflex. "
                            "Look for the automatic ‘attack’ whistle."
                        ),
                    ),
                    visualization_hint="hard-contested",
                ),
                "d": QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Voordeel met duidelijke ruimte is gezond — niet "
                            "de slechtste reflex."
                        ),
                        en=(
                            "Advantage with clear space is sound — not the "
                            "worst reflex."
                        ),
                    ),
                    visualization_hint="hard-contested",
                ),
            },
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="De slechtste reflex is automatische ‘aanval’-bias.",
                    en="The worst reflex is automatic attack-bias.",
                ),
                visualization_hint="hard-contested",
            ),
        ),
        QuizQuestion(
            id="q4-gk-dive",
            type="multiple_choice",
            prompt=LocalizedText(
                nl=(
                    "De keeper glijdt/duikt naar de bal terwijl een aanvaller "
                    "inloopt. Wat lees je eerst?"
                ),
                en=(
                    "The keeper slides/dives for the ball as an attacker "
                    "runs in. What do you read first?"
                ),
            ),
            options=[
                QuizOption(
                    id="a",
                    text=LocalizedText(
                        nl="Altijd penalty stroke — keeperslide is gevaarlijk.",
                        en="Always penalty stroke — keeper slide is dangerous.",
                    ),
                ),
                QuizOption(
                    id="b",
                    text=LocalizedText(
                        nl="Nooit fluiten in de cirkel tijdens een duik.",
                        en="Never whistle in the circle during a dive.",
                    ),
                ),
                QuizOption(
                    id="c",
                    text=LocalizedText(
                        nl=(
                            "Pad, timing en contact: speelt de keeper de bal, "
                            "of raakt de aanvaller illegaal? Zaal: banden "
                            "beperken uitwijkruimte."
                        ),
                        en=(
                            "Path, timing and contact: is the keeper playing "
                            "the ball, or illegally hitting the attacker? "
                            "Indoor: boards limit escape space."
                        ),
                    ),
                ),
                QuizOption(
                    id="d",
                    text=LocalizedText(
                        nl="Alleen kijken of de keeper de stick nog vasthoudt.",
                        en="Only check whether the keeper still holds the stick.",
                    ),
                ),
            ],
            correct_option_id="c",
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Juist. Keeperacties zijn hard decisions: lees pad → "
                        "timing → contact. Veld heeft meer ruimte; zaal is "
                        "dichter bij de banden. " + _FIH_NOTE_NL
                    ),
                    en=(
                        "Correct. Keeper actions are hard decisions: read "
                        "path → timing → contact. Field has more space; "
                        "indoor is tighter near the boards. " + _FIH_NOTE_EN
                    ),
                ),
                visualization_hint="hard-gk-dive",
            ),
            feedback_incorrect={
                "a": QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Geen automatische stroke — eerst pad, timing en "
                            "contact wegen."
                        ),
                        en=(
                            "No automatic stroke — first weigh path, timing "
                            "and contact."
                        ),
                    ),
                    visualization_hint="hard-gk-dive",
                ),
                "b": QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Je mag (en moet) fluiten bij illegale contact of "
                            "gevaar — ook tijdens een duik."
                        ),
                        en=(
                            "You may (and must) whistle illegal contact or "
                            "danger — also during a dive."
                        ),
                    ),
                    visualization_hint="hard-gk-dive",
                ),
                "d": QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Stickgrip is niet de hele lezing — pad en "
                            "contact tellen zwaarder."
                        ),
                        en=(
                            "Stick grip is not the whole read — path and "
                            "contact weigh more."
                        ),
                    ),
                    visualization_hint="hard-gk-dive",
                ),
            },
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Herlees: pad → timing → contact (veld vs zaal).",
                    en="Revisit: path → timing → contact (field vs indoor).",
                ),
                visualization_hint="hard-gk-dive",
            ),
        ),
        QuizQuestion(
            id="q5-pathway-refine",
            type="written",
            prompt=LocalizedText(
                nl=(
                    "Na deze module oefen je ritme, samenwerking en "
                    "consistentie in een latere cursusmodule die naar "
                    "topniveau leidt. Noem die module (korte frase / "
                    "trefwoord) — zie de lesstof."
                ),
                en=(
                    "After this module you practise cadence, collaboration "
                    "and consistency in a later course module that leads "
                    "toward top standard. Name that module (short phrase / "
                    "keyword) — see the lesson."
                ),
            ),
            accepted_answers=[
                "pathway",
                "professional pathway",
                "hoofdklasse",
                "hoofdklasse pathway",
                "pad",
                "professioneel pad",
                "pad naar professioneel",
                "pad naar professioneel niveau",
                "pad naar professioneel niveau (o.a. hoofdklasse)",
                "pathway toward professional",
                "pathway toward professional standard",
                "pathway toward professional standard (e.g. hoofdklasse)",
                "mod-pathway-hoofdklasse",
                "professional",
                "professioneel",
            ],
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Juist. Deze module leert de harde lezingen; het "
                        "pad naar professioneel niveau (o.a. Hoofdklasse) "
                        "verfijnt ritme, samenwerking en consistentie later. "
                        + _FIH_NOTE_NL
                    ),
                    en=(
                        "Correct. This module teaches the hard reads; the "
                        "pathway toward professional standard "
                        "(e.g. Hoofdklasse) later refines cadence, "
                        "collaboration and consistency. " + _FIH_NOTE_EN
                    ),
                ),
                visualization_hint="hard-decision-frame",
            ),
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Denk aan het professionele pad / Hoofdklasse-"
                        "pathway-module — daar worden deze oordelen later "
                        "verfijnd."
                    ),
                    en=(
                        "Think of the professional / Hoofdklasse pathway "
                        "module — that is where these judgments are refined "
                        "later."
                    ),
                ),
                visualization_hint="hard-decision-frame",
            ),
        ),
    ],
)
