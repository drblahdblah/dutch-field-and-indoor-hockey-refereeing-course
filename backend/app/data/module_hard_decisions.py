"""Full learning module: hard umpiring decision scenarios (NL + EN).

Pedagogical framing only — no reproduced FIH/KNHB copyrighted rule text or art.
Hoofdklasse / professional pathway refines these judgment skills later.
"""

from app.data.module_hard_decisions_quiz import HARD_QUIZ
from app.schemas import (
    Attribution,
    FurtherReading,
    LearningSection,
    LocalizedText,
    ModuleStub,
    VisualPlaceholder,
)

FIH_RULES_URL = (
    "https://www.fih.hockey/inside-fih/our-official-documents/rules-of-hockey"
)
KNHB_HOME_URL = "https://www.knhb.nl/"

HARD_VISUALS: list[VisualPlaceholder] = [
    VisualPlaceholder(
        id="viz-hard-frame",
        kind="svg_animation",
        title=LocalizedText(
            nl="Besliskader: lees → weeg → fluit",
            en="Decision frame: read → weigh → whistle",
        ),
        caption=LocalizedText(
            nl=(
                "Originele cursus-SVG: hard decisions beginnen met lezen, "
                "niet met reflexfluiten. Geen KNHB-kunst."
            ),
            en=(
                "Original course SVG: hard decisions start with reading, not "
                "reflex whistling. No KNHB art."
            ),
        ),
        animation_key="hard-decision-frame",
    ),
    VisualPlaceholder(
        id="viz-hard-raised",
        kind="svg_animation",
        title=LocalizedText(
            nl="Scenario: omhoog / gevaarlijke bal",
            en="Scenario: raised / dangerous ball",
        ),
        caption=LocalizedText(
            nl=(
                "Originele SVG: richting × afstand × snelheid (veld) vs "
                "strengere liftgrenzen (zaal). Pedagogisch model."
            ),
            en=(
                "Original SVG: direction × distance × speed (field) vs "
                "stricter lift limits (indoor). Pedagogical model."
            ),
        ),
        animation_key="hard-raised-danger",
    ),
    VisualPlaceholder(
        id="viz-hard-pressure",
        kind="svg_animation",
        title=LocalizedText(
            nl="Scenario: druk bij duidelijke balbezit",
            en="Scenario: pressure with clear possession",
        ),
        caption=LocalizedText(
            nl=(
                "Originele SVG: twee verdedigers drukken een aanvaller met "
                "duidelijke bal — lees bezit vóór contact."
            ),
            en=(
                "Original SVG: two defenders press an attacker with clear "
                "ball — read possession before contact."
            ),
        ),
        animation_key="hard-pressure-clear",
    ),
    VisualPlaceholder(
        id="viz-hard-contested",
        kind="svg_animation",
        title=LocalizedText(
            nl="Scenario: betwist / onduidelijk bezit",
            en="Scenario: contested / unclear possession",
        ),
        caption=LocalizedText(
            nl=(
                "Originele SVG: bal tussen spelers — geen automatische "
                "‘aanval’-fluit; weeg wie controle had."
            ),
            en=(
                "Original SVG: ball between players — no automatic ‘attack’ "
                "whistle; weigh who had control."
            ),
        ),
        animation_key="hard-contested",
    ),
    VisualPlaceholder(
        id="viz-hard-gk",
        kind="svg_animation",
        title=LocalizedText(
            nl="Scenario: keeperslide / duik",
            en="Scenario: goalkeeper slide / dive",
        ),
        caption=LocalizedText(
            nl=(
                "Originele SVG: keeper glijdt of duikt — lees pad, timing en "
                "contact; zaal: banden beperken ruimte."
            ),
            en=(
                "Original SVG: keeper slides or dives — read path, timing and "
                "contact; indoor: boards constrain space."
            ),
        ),
        animation_key="hard-gk-dive",
    ),
]

HARD_MODULE = ModuleStub(
    id="mod-hard-decisions",
    kind="shared",
    title=LocalizedText(
        nl="Harde beslissingen: gevaar, bezit & keeper",
        en="Hard decisions: danger, possession & keeper",
    ),
    summary=LocalizedText(
        nl=(
            "Showcase-module: klikstappen over omhoog/gevaar, druk bij "
            "duidelijk bezit, betwist bezit en keeperslide — veld én zaal "
            "waar ze verschillen. Originele SVG-animaties en aparte quiz. "
            "Het pad naar Hoofdklasse verfijnt deze oordelen later."
        ),
        en=(
            "Showcase module: click-steps on raised/danger, pressure with "
            "clear possession, contested possession and keeper slide — "
            "field and indoor where they differ. Original SVG animations "
            "and a separate quiz. The Hoofdklasse pathway refines these "
            "judgments later."
        ),
    ),
    learning_objectives=[
        LocalizedText(
            nl="Gevaar bij omhoog spelen wegen (veld vs zaallift).",
            en="Weigh danger on raised play (field vs indoor lift).",
        ),
        LocalizedText(
            nl="Bij duidelijk bezit contact/tackle lezen i.p.v. aantallen.",
            en="With clear possession, read contact/tackle — not headcount.",
        ),
        LocalizedText(
            nl="Bij betwist bezit ‘aanval’-bias vermijden.",
            en="Avoid attack-bias when possession is contested.",
        ),
        LocalizedText(
            nl="Keeperslide/duik lezen via pad → timing → contact.",
            en="Read keeper slide/dive via path → timing → contact.",
        ),
        LocalizedText(
            nl="Weten dat het Hoofdklasse-pad deze oordelen later verfijnt.",
            en="Know the Hoofdklasse pathway later refines these judgments.",
        ),
    ],
    instruction_outline=[
        LocalizedText(
            nl="Besliskader: lees → weeg → fluit.",
            en="Decision frame: read → weigh → whistle.",
        ),
        LocalizedText(
            nl="Omhoog / gevaarlijke bal (veld + zaal).",
            en="Raised / dangerous ball (field + indoor).",
        ),
        LocalizedText(
            nl="Twee verdedigers bij duidelijk bezit.",
            en="Two defenders with clear possession.",
        ),
        LocalizedText(
            nl="Betwist / onduidelijk bezit.",
            en="Contested / unclear possession.",
        ),
        LocalizedText(
            nl="Keeperslide / duik.",
            en="Goalkeeper slide / dive.",
        ),
    ],
    content_status="full",
    sections=[
        LearningSection(
            id="sec-hard-why",
            title=LocalizedText(
                nl="Waarom harde beslissingen",
                en="Why hard decisions",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Basisregels zeggen wát mag; harde wedstrijden vragen "
                        "hóe je in een fractie leest: gevaar, bezit en "
                        "keepercontact. Deze module oefent die oordelen met "
                        "klikstappen en visuals — geen overgenomen "
                        "FIH-/KNHB-tekst of KNHB-kunst."
                    ),
                    en=(
                        "Basic rules say what is allowed; hard matches ask "
                        "how you read in a split second: danger, possession "
                        "and keeper contact. This module drills those "
                        "judgments with click-steps and visuals — no "
                        "reproduced FIH/KNHB text or KNHB art."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Het pad naar professioneel niveau (o.a. Hoofdklasse) "
                        "komt daarna: ritme, samenwerking en consistentie "
                        "verfijnen dezezelfde oordelen. Hier bouw je eerst "
                        "het besliskader."
                    ),
                    en=(
                        "The pathway toward professional standard "
                        "(e.g. Hoofdklasse) comes after: cadence, "
                        "collaboration and consistency refine these same "
                        "judgments. Here you build the decision frame first."
                    ),
                ),
            ],
            visual_id="viz-hard-frame",
        ),
        LearningSection(
            id="sec-raised-dangerous",
            title=LocalizedText(
                nl="Omhoog / gevaarlijke bal",
                en="Raised / dangerous ball",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Veld: weeg richting × afstand × snelheid vóór je "
                        "automatisch fluit of kaarten trekt. Een omhooggaande "
                        "bal is niet per definitie illegaal — gevaar en "
                        "context bepalen."
                    ),
                    en=(
                        "Field: weigh direction × distance × speed before "
                        "you automatically whistle or card. A raised ball is "
                        "not illegal by definition — danger and context "
                        "decide."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Zaal: liftgrenzen zijn strenger en de ruimte "
                        "kleiner. Dezelfde leeslus (richting, nabijheid, "
                        "tempo) — maar de drempel voor ‘te hoog / te dicht’ "
                        "ligt lager. Officiële limieten: FIH Indoor / KNHB."
                    ),
                    en=(
                        "Indoor: lift limits are stricter and space is "
                        "tighter. Same read loop (direction, proximity, "
                        "tempo) — but the threshold for ‘too high / too "
                        "close’ is lower. Official limits: FIH Indoor / KNHB."
                    ),
                ),
            ],
            visual_id="viz-hard-raised",
        ),
        LearningSection(
            id="sec-clear-possession-pressure",
            title=LocalizedText(
                nl="Druk bij duidelijke balbezit",
                en="Pressure with clear possession",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Twee verdedigers op één aanvaller met duidelijke "
                        "bal: lees of de tackle/contact legaal de bal speelt "
                        "of de bezitter illegaal raakt. Het aantal "
                        "verdedigers is geen automatische fout."
                    ),
                    en=(
                        "Two defenders on one attacker with a clear ball: "
                        "read whether the tackle/contact legally plays the "
                        "ball or illegally hits the carrier. Defender count "
                        "is not an automatic foul."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Zaal is sneller en dichter bij de banden — dezelfde "
                        "bezitslezing, kortere reactietijd. Communiceer "
                        "vroeg met je partner als het spel de helft kruist."
                    ),
                    en=(
                        "Indoor is faster and closer to the boards — same "
                        "possession read, shorter reaction time. Communicate "
                        "early with your partner when play crosses the half."
                    ),
                ),
            ],
            visual_id="viz-hard-pressure",
        ),
        LearningSection(
            id="sec-contested-possession",
            title=LocalizedText(
                nl="Betwist / onduidelijk bezit",
                en="Contested / unclear possession",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Als twee sticks de bal delen en niemand controle "
                        "heeft, vermijd ‘aanval’-bias: niet automatisch "
                        "fluiten voor de aanvallende kant omdat die dichter "
                        "bij het doel staat."
                    ),
                    en=(
                        "When two sticks share the ball and nobody has "
                        "control, avoid attack-bias: do not automatically "
                        "whistle for the attacking side because they are "
                        "closer to goal."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Wacht tot controle zichtbaar is of tot een "
                        "duidelijke overtreding. Advantage alleen als één "
                        "kant écht ruimte krijgt. Op topniveau (later in "
                        "het pad) wordt deze consistentie nóg strenger "
                        "getoetst."
                    ),
                    en=(
                        "Wait until control is visible or until a clear "
                        "offence. Advantage only when one side truly gains "
                        "space. At top standard (later in the pathway) this "
                        "consistency is tested even harder."
                    ),
                ),
            ],
            visual_id="viz-hard-contested",
        ),
        LearningSection(
            id="sec-gk-sliding",
            title=LocalizedText(
                nl="Keeperslide / duik",
                en="Goalkeeper slide / dive",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Lees in volgorde: pad van de keeper → timing t.o.v. "
                        "de aanvaller → contactkwaliteit (bal of lichaam). "
                        "Geen automatische stroke omdat er een duik is."
                    ),
                    en=(
                        "Read in order: keeper’s path → timing vs the "
                        "attacker → contact quality (ball or body). No "
                        "automatic stroke just because there is a dive."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Veld: meer uitwijkruimte. Zaal: banden en kleinere "
                        "cirkel/zone beperken ontsnapping — weeg nabijheid "
                        "zwaarder. Officiële keeperregels blijven bij FIH/"
                        "KNHB (Verder lezen)."
                    ),
                    en=(
                        "Field: more escape space. Indoor: boards and a "
                        "smaller circle/zone limit escape — weigh proximity "
                        "more heavily. Official keeper rules stay with "
                        "FIH/KNHB (Further reading)."
                    ),
                ),
            ],
            visual_id="viz-hard-gk",
        ),
        LearningSection(
            id="sec-hard-practice-next",
            title=LocalizedText(
                nl="Quiz en verder naar het pad",
                en="Quiz and on to the pathway",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Open hieronder de modulequiz op een aparte pagina: "
                        "meerkeuze plus een korte schrijfvraag, met uitleg "
                        "en visuals bij foute antwoorden. Sla voortgang op "
                        "via je cursussessie. Daarna: het pad naar "
                        "professioneel niveau (o.a. Hoofdklasse) — daar "
                        "worden ritme, samenwerking en consistentie "
                        "toegevoegd om deze oordelen te verfijnen. Losse "
                        "oefenscenario’s blijven beschikbaar onder "
                        "Oefenscenario’s."
                    ),
                    en=(
                        "Open the module quiz below on a separate page: "
                        "multiple-choice plus a short written item, with "
                        "explanations and visuals on wrong answers. Save "
                        "progress via your course session. Next: the "
                        "pathway toward professional standard "
                        "(e.g. Hoofdklasse) — there cadence, collaboration "
                        "and consistency are added to refine these "
                        "judgments. Standalone drills remain under Practice "
                        "scenarios."
                    ),
                ),
            ],
        ),
    ],
    visuals=HARD_VISUALS,
    quiz_id=HARD_QUIZ.id,
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
                    nl="Officiële FIH Rules of Hockey — internationale regelbasis.",
                    en="Official FIH Rules of Hockey — international rules base.",
                ),
            ),
        ),
        FurtherReading(
            title=LocalizedText(
                nl="KNHB — regels & scheidsrechters (link/plaatshouder)",
                en="KNHB — rules & umpires (link/placeholder)",
            ),
            url=KNHB_HOME_URL,
            attribution=Attribution(
                source_name="KNHB — regels & scheidsrechters",
                source_url=KNHB_HOME_URL,
                note=LocalizedText(
                    nl=(
                        "Geen KNHB-illustraties inbegrepen. Link naar "
                        "officiële KNHB-bronnen; EN-vertaling: TODO."
                    ),
                    en=(
                        "No KNHB illustrations included. Link to official "
                        "KNHB sources; EN translation: TODO."
                    ),
                ),
                knhb_illustration_placeholder=True,
                translation_needed=True,
            ),
        ),
    ],
    order=4,
)
