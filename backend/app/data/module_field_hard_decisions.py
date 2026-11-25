"""Field hockey advanced / hard-decision module (NL + EN).

Pedagogical framing only — no reproduced FIH/KNHB copyrighted rule text or art.
Builds on mod-field-rules-core basics.
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
_NOTE_NL = (
    "Exacte formulering en sanctietreden: officiële FIH Rules / KNHB — "
    "dit is een besliskader, geen regelcitaat."
)
_NOTE_EN = (
    "Exact wording and sanction steps: official FIH Rules / KNHB — "
    "this is a decision frame, not a rules quotation."
)

FIELD_HARD_VISUALS: list[VisualPlaceholder] = [
    VisualPlaceholder(
        id="viz-fh-frame",
        kind="svg_animation",
        title=LocalizedText(nl="Veld: harde lezing", en="Field: hard read"),
        caption=LocalizedText(
            nl="Je scant richting, afstand en contact vóór je fluit — niet op reflex.",
            en="You scan direction, distance and contact before you whistle — not on reflex.",
        ),
        animation_key="hard-decision-frame",
    ),
    VisualPlaceholder(
        id="viz-fh-raised",
        kind="svg_animation",
        title=LocalizedText(nl="Omhoog in een drukke 23m", en="Raised into a crowded 23m"),
        caption=LocalizedText(
            nl="Aanval vanuit de 23m: bal hard omhoog naar een verdediger op korte afstand in een volle zone.",
            en="Attack from the 23m: ball raised hard toward a defender at short range in a crowded zone.",
        ),
        animation_key="hard-raised-danger",
    ),
    VisualPlaceholder(
        id="viz-fh-pressure",
        kind="svg_animation",
        title=LocalizedText(nl="Twee verdedigers, duidelijke bal", en="Two defenders, clear ball"),
        caption=LocalizedText(
            nl="Aanvaller dribbelt duidelijk; twee verdedigers drukken — lees of de tackle de bal of de speler raakt.",
            en="Attacker dribbles clearly; two defenders press — read whether the tackle hits the ball or the player.",
        ),
        animation_key="hard-pressure-clear",
    ),
    VisualPlaceholder(
        id="viz-fh-contested",
        kind="svg_animation",
        title=LocalizedText(nl="Betwist bezit middenveld", en="Contested midfield possession"),
        caption=LocalizedText(
            nl="Twee sticks bij de bal, niemand dribbelt weg — nabijheid van het doel is geen fout.",
            en="Two sticks at the ball, nobody dribbles away — proximity to goal is not a foul.",
        ),
        animation_key="hard-contested",
    ),
    VisualPlaceholder(
        id="viz-fh-gk",
        kind="svg_animation",
        title=LocalizedText(nl="Keeperslide in de cirkel", en="Keeper slide in the circle"),
        caption=LocalizedText(
            nl="Keeper glijdt schuin naar voren: speelt die eerst de bal, of raakt die eerst de aanvaller?",
            en="Keeper slides diagonally forward: do they play the ball first, or hit the attacker first?",
        ),
        animation_key="hard-gk-dive",
    ),
    VisualPlaceholder(
        id="viz-fh-cards-raised",
        kind="svg_animation",
        title=LocalizedText(nl="Kaart na omhoog / push", en="Card after raised / push"),
        caption=LocalizedText(
            nl="Harde push of omhoog in een verdediger, soms met pirouette — weeg gevaar én intensiteit voor de kaart.",
            en="Hard push or raised into a defender, sometimes with a pirouette — weigh danger and intensity for the card.",
        ),
        animation_key="card-ladder",
    ),
]

FIELD_HARD_QUIZ = Quiz(
    id="quiz-field-hard-decisions",
    title=LocalizedText(
        nl="Quiz: veld — harde beslissingen",
        en="Quiz: field — hard decisions",
    ),
    questions=[
        QuizQuestion(
            id="q1-crowded-raised",
            type="multiple_choice",
            prompt=LocalizedText(
                nl="Bal hard omhoog in een volle 23m op een dichtbij staande verdediger. Beste eerste lezing?",
                en="Ball raised hard in a crowded 23m at a nearby defender. Best first read?",
            ),
            options=[
                QuizOption(id="a", text=LocalizedText(nl="Altijd groene kaart.", en="Always a green card.")),
                QuizOption(id="b", text=LocalizedText(nl="Alleen fluiten bij contact.", en="Only whistle on contact.")),
                QuizOption(
                    id="c",
                    text=LocalizedText(
                        nl="Weeg richting × afstand × snelheid; gevaar kan zonder contact — fluit/sanctioneer passend.",
                        en="Weigh direction × distance × speed; danger can exist without contact — whistle/sanction accordingly.",
                    ),
                ),
                QuizOption(id="d", text=LocalizedText(nl="Altijd doorspelen voor flow.", en="Always play on for flow.")),
            ],
            correct_option_id="c",
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl="Juist. Drukke zones maken dezelfde omhooggaande bal sneller gevaarlijk. " + _NOTE_NL,
                    en="Correct. Crowded zones make the same raised ball dangerous sooner. " + _NOTE_EN,
                ),
                visualization_hint="hard-raised-danger",
            ),
            feedback_incorrect={
                "a": QuizFeedback(
                    explanation=LocalizedText(nl="Kaart volgt na de gevaarlezing — niet als reflex.", en="A card follows the danger read — not as a reflex."),
                    visualization_hint="card-ladder",
                ),
                "b": QuizFeedback(
                    explanation=LocalizedText(nl="Gevaar kan zonder contact — te laat wachten op een treffer.", en="Danger can exist without contact — waiting for a hit is too late."),
                    visualization_hint="hard-raised-danger",
                ),
                "d": QuizFeedback(
                    explanation=LocalizedText(nl="Flow komt na veiligheid.", en="Flow comes after safety."),
                    visualization_hint="hard-raised-danger",
                ),
            },
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(nl="Herlees: richting × afstand × snelheid in drukke zones.", en="Revisit: direction × distance × speed in crowded zones."),
                visualization_hint="hard-raised-danger",
            ),
        ),
        QuizQuestion(
            id="q2-pressure",
            type="multiple_choice",
            prompt=LocalizedText(
                nl="Twee verdedigers drukken een aanvaller met duidelijke bal. Wat weegt?",
                en="Two defenders press an attacker with a clear ball. What counts?",
            ),
            options=[
                QuizOption(id="a", text=LocalizedText(nl="Automatisch fout door 2-tegen-1.", en="Automatic foul because of 2-vs-1.")),
                QuizOption(id="b", text=LocalizedText(nl="Of de tackle de bal speelt of de speler raakt.", en="Whether the tackle plays the ball or hits the player.")),
                QuizOption(id="c", text=LocalizedText(nl="Alleen of de bal stil ligt.", en="Only whether the ball is still.")),
                QuizOption(id="d", text=LocalizedText(nl="Altijd penalty corner.", en="Always a penalty corner.")),
            ],
            correct_option_id="b",
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl="Juist. Aantal verdedigers is geen aparte regelgrond — contactkwaliteit wel. " + _NOTE_NL,
                    en="Correct. Defender count is not a separate rule ground — contact quality is. " + _NOTE_EN,
                ),
                visualization_hint="hard-pressure-clear",
            ),
            feedback_incorrect={
                "a": QuizFeedback(explanation=LocalizedText(nl="2-tegen-1 is geen automatische fout.", en="2-vs-1 is not an automatic foul."), visualization_hint="hard-pressure-clear"),
                "c": QuizFeedback(explanation=LocalizedText(nl="Je leest in beweging.", en="You read in motion."), visualization_hint="hard-pressure-clear"),
                "d": QuizFeedback(explanation=LocalizedText(nl="Geen vaste uitkomst — lees contact.", en="No fixed outcome — read contact."), visualization_hint="hard-pressure-clear"),
            },
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(nl="Herlees: bal vs speler bij duidelijk bezit.", en="Revisit: ball vs player with clear possession."),
                visualization_hint="hard-pressure-clear",
            ),
        ),
        QuizQuestion(
            id="q3-contested",
            type="multiple_choice",
            prompt=LocalizedText(
                nl="Betwist bezit, geen duidelijke fout. Slechtste reflex?",
                en="Contested possession, no clear foul. Worst reflex?",
            ),
            options=[
                QuizOption(id="a", text=LocalizedText(nl="Automatisch ‘aanval’ fluiten omdat die kant dichter bij het doel staat.", en="Automatically whistle ‘attack’ because that side is closer to goal.")),
                QuizOption(id="b", text=LocalizedText(nl="Wachten tot controle zichtbaar is.", en="Wait until control is visible.")),
                QuizOption(id="c", text=LocalizedText(nl="Eye contact met je partner.", en="Eye contact with your partner.")),
                QuizOption(id="d", text=LocalizedText(nl="Advantage bij echte ruimte.", en="Advantage when there is real space.")),
            ],
            correct_option_id="a",
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl="Juist — dat is de slechtste reflex. Doel-nabijheid ≠ fout. " + _NOTE_NL,
                    en="Correct — that is the worst reflex. Goal proximity ≠ foul. " + _NOTE_EN,
                ),
                visualization_hint="hard-contested",
            ),
            feedback_incorrect={
                "b": QuizFeedback(explanation=LocalizedText(nl="Dat is goed gedrag — de vraag zocht de slechtste reflex.", en="That is good practice — the question sought the worst reflex."), visualization_hint="hard-contested"),
                "c": QuizFeedback(explanation=LocalizedText(nl="Partnercontact is goed.", en="Partner contact is good."), visualization_hint="hard-contested"),
                "d": QuizFeedback(explanation=LocalizedText(nl="Voordeel met ruimte is gezond.", en="Advantage with space is sound."), visualization_hint="hard-contested"),
            },
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(nl="Slechtste reflex: automatische aanval-bias.", en="Worst reflex: automatic attack-bias."),
                visualization_hint="hard-contested",
            ),
        ),
        QuizQuestion(
            id="q4-gk",
            type="multiple_choice",
            prompt=LocalizedText(
                nl="Keeperslide: wat lees je eerst?",
                en="Keeper slide: what do you read first?",
            ),
            options=[
                QuizOption(id="a", text=LocalizedText(nl="Altijd stroke — slide is gevaarlijk.", en="Always a stroke — a slide is dangerous.")),
                QuizOption(id="b", text=LocalizedText(nl="Pad → timing → contact (bal of lichaam).", en="Path → timing → contact (ball or body).")),
                QuizOption(id="c", text=LocalizedText(nl="Nooit fluiten in de cirkel.", en="Never whistle in the circle.")),
                QuizOption(id="d", text=LocalizedText(nl="Alleen of de keeper de stick vasthoudt.", en="Only whether the keeper holds the stick.")),
            ],
            correct_option_id="b",
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl="Juist. Geen automatische stroke omdat er een duik is. " + _NOTE_NL,
                    en="Correct. No automatic stroke just because there is a dive. " + _NOTE_EN,
                ),
                visualization_hint="hard-gk-dive",
            ),
            feedback_incorrect={
                "a": QuizFeedback(explanation=LocalizedText(nl="Eerst pad/timing/contact wegen.", en="First weigh path/timing/contact."), visualization_hint="hard-gk-dive"),
                "c": QuizFeedback(explanation=LocalizedText(nl="Je mag fluiten bij illegale contact.", en="You may whistle illegal contact."), visualization_hint="hard-gk-dive"),
                "d": QuizFeedback(explanation=LocalizedText(nl="Stickgrip is niet de hele lezing.", en="Stick grip is not the whole read."), visualization_hint="hard-gk-dive"),
            },
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(nl="Herlees: pad → timing → contact.", en="Revisit: path → timing → contact."),
                visualization_hint="hard-gk-dive",
            ),
        ),
        QuizQuestion(
            id="q5-card-pirouette",
            type="written",
            prompt=LocalizedText(
                nl="Na een harde push/omhoog in een verdediger (soms met pirouette) weeg je gevaar én … (één woord) vóór je een kaart trekt.",
                en="After a hard push/raised into a defender (sometimes with a pirouette) you weigh danger and … (one word) before you show a card.",
            ),
            accepted_answers=[
                "intensity", "intensiteit", "severity", "ernst", "intent", "intentie",
                "force", "kracht", "recklessness", "roekeloosheid",
            ],
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl="Juist. Kaarten volgen gevaar + intensiteit/ernst — geen automatisme. " + _NOTE_NL,
                    en="Correct. Cards follow danger + intensity/severity — not automatic. " + _NOTE_EN,
                ),
                visualization_hint="card-ladder",
            ),
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Denk aan intensiteit / ernst / intentie naast gevaar.",
                    en="Think intensity / severity / intent alongside danger.",
                ),
                visualization_hint="card-ladder",
            ),
        ),
    ],
)

FIELD_HARD_MODULE = ModuleStub(
    id="mod-field-hard-decisions",
    kind="field",
    title=LocalizedText(
        nl="Veld: harde beslissingen",
        en="Field: hard decisions",
    ),
    summary=LocalizedText(
        nl=(
            "Verdieping ná de veldkern: omhoog in drukke zones, druk bij "
            "duidelijk bezit, betwist bezit, keeperslide, en kaarten bij "
            "omhoog/push (incl. pirouette). Regelprincipe + uitgewerkt "
            "voorbeeld per stap."
        ),
        en=(
            "Deepening after field core: raised into crowded zones, pressure "
            "with clear possession, contested possession, keeper slide, and "
            "cards on raised/push (incl. pirouette). Rule principle + worked "
            "example per step."
        ),
    ),
    learning_objectives=[
        LocalizedText(nl="Omhoog in drukke veldzones wegen en sanctioneren.", en="Weigh and sanction raised balls in crowded field zones."),
        LocalizedText(nl="Druk bij duidelijk bezit lezen op bal vs speler.", en="Read pressure with clear possession as ball vs player."),
        LocalizedText(nl="Betwist bezit zonder aanval-bias afhandelen.", en="Handle contested possession without attack-bias."),
        LocalizedText(nl="Keeperslide via pad → timing → contact lezen.", en="Read keeper slide via path → timing → contact."),
        LocalizedText(nl="Kaarten voor omhoog/push/pirouette koppelen aan gevaar + intensiteit.", en="Tie cards for raised/push/pirouette to danger + intensity."),
    ],
    instruction_outline=[
        LocalizedText(nl="Omhoog in drukke 23m/cirkel.", en="Raised in crowded 23m/circle."),
        LocalizedText(nl="Twee verdedigers, duidelijke bal.", en="Two defenders, clear ball."),
        LocalizedText(nl="Betwist bezit.", en="Contested possession."),
        LocalizedText(nl="Keeperslide.", en="Keeper slide."),
        LocalizedText(nl="Kaarten na omhoog/push/pirouette.", en="Cards after raised/push/pirouette."),
    ],
    content_status="full",
    sections=[
        LearningSection(
            id="sec-fh-why",
            title=LocalizedText(nl="Na de veldkern", en="After field core"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Je kent slagtypes, obstructie, PC/PS, kaarten en "
                        "basis omhoog. Hier train je de lastige frames: drukke "
                        "zones, dubbele druk, keeperduiken en wanneer een "
                        "kaart wél volgt. Lespatroon: regelprincipe → "
                        "uitgewerkt voorbeeld → besluit/waarom."
                    ),
                    en=(
                        "You know stroke types, obstruction, PC/PS, cards and "
                        "basic raised play. Here you train the hard frames: "
                        "crowded zones, double pressure, keeper dives and when "
                        "a card does follow. Pattern: rule principle → worked "
                        "example → decision/why."
                    ),
                ),
            ],
            visual_id="viz-fh-frame",
        ),
        LearningSection(
            id="sec-fh-crowded-raised",
            title=LocalizedText(nl="Omhoog in een drukke zone", en="Raised into a crowded zone"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Regelprincipe: gevaarlijk spel (of spel dat tot "
                        "gevaar leidt) moet gestopt worden. Omhoog is niet "
                        "automatisch fout — richting × afstand × snelheid "
                        "bepalen. In een volle 23m/cirkel is dezelfde bal "
                        "sneller gevaarlijk omdat uitwijkruimte ontbreekt. "
                        + _NOTE_NL
                    ),
                    en=(
                        "Rule principle: dangerous play (or play that leads "
                        "to danger) must be stopped. Raised is not "
                        "automatically illegal — direction × distance × "
                        "speed decide. In a crowded 23m/circle the same ball "
                        "is dangerous sooner because escape space is gone. "
                        + _NOTE_EN
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Uitgewerkt voorbeeld: A speelt hard omhoog "
                        "(~kniehoogte) vanuit de 23m recht op D op ~3 m, "
                        "met twee andere spelers dichtbij. D duikt weg "
                        "zonder geraakt te worden."
                    ),
                    en=(
                        "Worked example: A plays hard raised (~knee height) "
                        "from the 23m straight at D at ~3 m, with two other "
                        "players nearby. D ducks away without being hit."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Besluit en waarom: fluit — gevaarlijke bal. "
                        "Richting op D, korte afstand, hoge snelheid, weinig "
                        "ruimte. Kaart alleen als intensiteit/ernst dat vraagt "
                        "(zie kaartenstap)."
                    ),
                    en=(
                        "Decision and why: whistle — dangerous ball. "
                        "Direction at D, short distance, high speed, little "
                        "space. Card only if intensity/severity asks for it "
                        "(see cards step)."
                    ),
                ),
            ],
            visual_id="viz-fh-raised",
        ),
        LearningSection(
            id="sec-fh-pressure",
            title=LocalizedText(nl="Druk bij duidelijke balbezit", en="Pressure with clear possession"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Regelprincipe: legale tackle speelt de bal; contact "
                        "op de bezitter zonder bal is een fout. Aantal "
                        "verdedigers is geen aparte regelgrond. " + _NOTE_NL
                    ),
                    en=(
                        "Rule principle: a legal tackle plays the ball; "
                        "contact on the carrier without the ball is a foul. "
                        "Defender count is not a separate rule ground. "
                        + _NOTE_EN
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Uitgewerkt voorbeeld: A dribbelt duidelijk; D1 speelt "
                        "de bal schoon van de stick; D2 raakt A’s lichaam "
                        "daarna zonder bal."
                    ),
                    en=(
                        "Worked example: A dribbles clearly; D1 plays the "
                        "ball cleanly off the stick; D2 then hits A’s body "
                        "without the ball."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Besluit en waarom: speel door op D1’s tackle; fluit "
                        "de latere body-fout van D2. Twee verdedigers maken "
                        "D1 niet automatisch fout."
                    ),
                    en=(
                        "Decision and why: play on D1’s tackle; whistle D2’s "
                        "later body foul. Two defenders do not make D1 "
                        "automatically illegal."
                    ),
                ),
            ],
            visual_id="viz-fh-pressure",
        ),
        LearningSection(
            id="sec-fh-contested",
            title=LocalizedText(nl="Betwist bezit", en="Contested possession"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Regelprincipe: zonder leesbare fout en zonder "
                        "controle is ‘aanval’ fluiten omdat die kant dichter "
                        "bij het doel staat bias — geen regelgrond. "
                        + _NOTE_NL
                    ),
                    en=(
                        "Rule principle: without a readable foul and without "
                        "control, whistling ‘attack’ because that side is "
                        "closer to goal is bias — not a rule ground. "
                        + _NOTE_EN
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Uitgewerkt voorbeeld: A en D sticks bij de bal "
                        "middenveld; niemand dribbelt weg; A dichter bij het "
                        "aanvallende doel; geen body-check of gevaarlijke lift."
                    ),
                    en=(
                        "Worked example: A and D sticks at the midfield ball; "
                        "nobody dribbles away; A closer to the attacking "
                        "goal; no body check or dangerous lift."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Besluit en waarom: speel door / houd de fluit tot "
                        "controle of een duidelijke fout. Slechtste reflex: "
                        "automatische aanval-fluit."
                    ),
                    en=(
                        "Decision and why: play on / hold the whistle until "
                        "control or a clear foul. Worst reflex: automatic "
                        "attack whistle."
                    ),
                ),
            ],
            visual_id="viz-fh-contested",
        ),
        LearningSection(
            id="sec-fh-gk",
            title=LocalizedText(nl="Keeperslide / duik", en="Keeper slide / dive"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Regelprincipe: keeper mag verdedigen in de cirkel "
                        "binnen keeperrechten; slide ≠ automatische stroke. "
                        "Lees pad → timing → contact. " + _NOTE_NL
                    ),
                    en=(
                        "Rule principle: keeper may defend in the circle "
                        "within keeper rights; slide ≠ automatic stroke. "
                        "Read path → timing → contact. " + _NOTE_EN
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Uitgewerkt voorbeeld: K speelt eerst de bal weg, "
                        "raakt A’s been pas daarna; A valt."
                    ),
                    en=(
                        "Worked example: K first plays the ball away, then "
                        "contacts A’s leg; A falls."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Besluit en waarom: speel door (tenzij ná-contact "
                        "apart fout is). Tegenvoorbeeld: lichaam vóór de bal "
                        "→ fluit (vaak stroke per officiële tabel)."
                    ),
                    en=(
                        "Decision and why: play on (unless after-contact is "
                        "a separate foul). Counter-example: body before the "
                        "ball → whistle (often stroke per official table)."
                    ),
                ),
            ],
            visual_id="viz-fh-gk",
        ),
        LearningSection(
            id="sec-fh-cards",
            title=LocalizedText(
                nl="Kaarten: omhoog, push, pirouette",
                en="Cards: raised, push, pirouette",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Regelprincipe: kaarten escaleren (groen → geel → "
                        "rood) op basis van gevaar, intensiteit en herhaling "
                        "— niet elke omhooggaande bal is een kaart, en niet "
                        "elke push in een verdediger is rood. Een pirouette "
                        "(draai) die de verdediger hard raakt weegt zwaar op "
                        "intensiteit. " + _NOTE_NL
                    ),
                    en=(
                        "Rule principle: cards escalate (green → yellow → "
                        "red) on danger, intensity and repetition — not every "
                        "raised ball is a card, and not every push into a "
                        "defender is red. A pirouette (turn) that hits the "
                        "defender hard weighs heavily on intensity. "
                        + _NOTE_EN
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Uitgewerkt voorbeeld: A pusht hard omhoog in D’s "
                        "lichaam op korte afstand en draait (pirouette) door "
                        "het contact heen; D valt. Geen eerdere waarschuwing."
                    ),
                    en=(
                        "Worked example: A pushes hard raised into D’s body "
                        "at short range and turns (pirouette) through the "
                        "contact; D falls. No prior warning."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Besluit en waarom: fluit de gevaarlijke/illegale "
                        "actie; toon minimaal geel bij hoge intensiteit "
                        "(vaak), groen alleen bij lichtere waarschuwing, "
                        "rood bij ernst/geweld per officiële ladder. "
                        "Communiceer kort en leesbaar."
                    ),
                    en=(
                        "Decision and why: whistle the dangerous/illegal "
                        "action; show at least yellow at high intensity "
                        "(often), green only for a lighter warning, red for "
                        "severity/violence per the official ladder. "
                        "Communicate briefly and readably."
                    ),
                ),
            ],
            visual_id="viz-fh-cards-raised",
        ),
        LearningSection(
            id="sec-fh-next",
            title=LocalizedText(nl="Quiz en verder", en="Quiz and next"),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Open de modulequiz hieronder. Daarna: zaal harde "
                        "beslissingen of het pad naar professioneel niveau. "
                        "Houd FIH/KNHB bij de hand voor exacte tekst."
                    ),
                    en=(
                        "Open the module quiz below. Next: indoor hard "
                        "decisions or the pathway toward professional "
                        "standard. Keep FIH/KNHB handy for exact wording."
                    ),
                ),
            ],
        ),
    ],
    visuals=FIELD_HARD_VISUALS,
    quiz_id=FIELD_HARD_QUIZ.id,
    further_reading=[
        FurtherReading(
            title=LocalizedText(nl="FIH Rules of Hockey (officieel)", en="FIH Rules of Hockey (official)"),
            url=FIH_RULES_URL,
            attribution=Attribution(
                source_name="FIH Rules of Hockey",
                source_url=FIH_RULES_URL,
                note=LocalizedText(
                    nl="Officiële FIH Rules of Hockey.",
                    en="Official FIH Rules of Hockey.",
                ),
            ),
        ),
        FurtherReading(
            title=LocalizedText(nl="KNHB — regels & scheidsrechters", en="KNHB — rules & umpires"),
            url=KNHB_HOME_URL,
            attribution=Attribution(
                source_name="KNHB",
                source_url=KNHB_HOME_URL,
                note=LocalizedText(
                    nl="Geen KNHB-illustraties; link naar officiële bronnen.",
                    en="No KNHB illustrations; link to official sources.",
                ),
                knhb_illustration_placeholder=True,
                translation_needed=True,
            ),
        ),
    ],
    order=4,
)
