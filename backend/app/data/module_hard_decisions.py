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
            "Showcase-module: per hard scenario het regelprincipe "
            "(pedagogisch) plus een uitgewerkt voorbeeld — omhoog/gevaar, "
            "druk bij duidelijk bezit, betwist bezit en keeperslide "
            "(veld vs zaal). Originele SVG’s en aparte quiz. Het pad naar "
            "Hoofdklasse verfijnt deze oordelen later."
        ),
        en=(
            "Showcase module: for each hard scenario the rule principle "
            "(pedagogical) plus a worked example — raised/danger, pressure "
            "with clear possession, contested possession and keeper slide "
            "(field vs indoor). Original SVGs and a separate quiz. The "
            "Hoofdklasse pathway refines these judgments later."
        ),
    ),
    learning_objectives=[
        LocalizedText(
            nl=(
                "Het regelprincipe voor gevaarlijke/omhoog gespeelde ballen "
                "noemen en in een uitgewerkt voorbeeld toepassen."
            ),
            en=(
                "State the rule principle for dangerous/raised balls and "
                "apply it in a worked example."
            ),
        ),
        LocalizedText(
            nl=(
                "Bij duidelijk bezit uitleggen waarom contact/tackle telt "
                "— niet het aantal verdedigers — met een voorbeeld."
            ),
            en=(
                "With clear possession, explain why contact/tackle counts "
                "— not defender count — with a worked example."
            ),
        ),
        LocalizedText(
            nl=(
                "Bij betwist bezit ‘aanval’-bias herkennen en een "
                "uitgewerkt voorbeeld correct afhandelen."
            ),
            en=(
                "Recognise attack-bias on contested possession and resolve "
                "a worked example correctly."
            ),
        ),
        LocalizedText(
            nl=(
                "Keeperslide/duik uitleggen via pad → timing → contact, "
                "met veld/zaalverschil in een voorbeeld."
            ),
            en=(
                "Explain keeper slide/dive via path → timing → contact, "
                "with field/indoor contrast in a worked example."
            ),
        ),
        LocalizedText(
            nl="Weten dat het Hoofdklasse-pad deze oordelen later verfijnt.",
            en="Know the Hoofdklasse pathway later refines these judgments.",
        ),
    ],
    instruction_outline=[
        LocalizedText(
            nl="Lespatroon: regelprincipe → uitgewerkt voorbeeld → besluit.",
            en="Lesson pattern: rule principle → worked example → decision.",
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
                nl="Hoe deze module leert",
                en="How this module teaches",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Elke harde situatie volgt hetzelfde lespatroon: "
                        "(1) wat het regelkader vastlegt — pedagogische "
                        "samenvatting, geen overgenomen FIH-/KNHB-citaat; "
                        "(2) een uitgewerkt voorbeeld met concrete feiten; "
                        "(3) het besluit en waarom. Exacte formuleringen en "
                        "limieten staan in de officiële bronnen (Verder lezen)."
                    ),
                    en=(
                        "Each hard situation follows the same teaching "
                        "pattern: (1) what the rules framework establishes — "
                        "pedagogical summary, not a reproduced FIH/KNHB "
                        "quotation; (2) a worked example with concrete "
                        "facts; (3) the decision and why. Exact wording and "
                        "limits live in the official sources (Further reading)."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Gebruik altijd de lus lees → weeg → fluit. Kaarten "
                        "en herstarten zijn middelen ná die lezing — geen "
                        "reflex. Het pad naar professioneel niveau "
                        "(o.a. Hoofdklasse) komt later: daar verfijn je "
                        "ritme, samenwerking en consistentie op dezezelfde "
                        "oordelen."
                    ),
                    en=(
                        "Always use the loop read → weigh → whistle. Cards "
                        "and restarts are tools after that read — not a "
                        "reflex. The pathway toward professional standard "
                        "(e.g. Hoofdklasse) comes later: there you refine "
                        "cadence, collaboration and consistency on these "
                        "same judgments."
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
                        "Wat het regelkader vastlegt (veld): een hard of "
                        "omhoog gespeelde bal is niet automatisch fout én "
                        "niet automatisch toegestaan. Spel dat gevaarlijk "
                        "is — of dat tot gevaarlijk spel leidt — hoort "
                        "gestopt/gesanctioneerd te worden. Jouw lezing "
                        "weegt richting (naar wie?), afstand (hoe dicht?) "
                        "en snelheid (hoe hard?). Gevaar kan bestaan zonder "
                        "contact. Exacte sanctietreden: FIH Rules / KNHB."
                    ),
                    en=(
                        "What the rules framework establishes (field): a "
                        "hard or raised ball is not automatically illegal "
                        "and not automatically allowed. Play that is "
                        "dangerous — or that leads to dangerous play — "
                        "should be stopped/sanctioned. Your read weighs "
                        "direction (toward whom?), distance (how close?) "
                        "and speed (how hard?). Danger can exist without "
                        "contact. Exact sanction steps: FIH Rules / KNHB."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Wat het regelkader vastlegt (zaal): lift wordt "
                        "strenger begrensd dan op het veld; plat spel is "
                        "de default. In de kleine ruimte is ‘te hoog / te "
                        "dicht bij een tegenstander’ sneller gevaarlijk. "
                        "Officiële liftgrenzen en uitzonderingen "
                        "(bijv. schoten) staan in FIH Indoor / KNHB — hier "
                        "train je de lezing, geen citaten."
                    ),
                    en=(
                        "What the rules framework establishes (indoor): "
                        "lift is bounded more tightly than outdoors; flat "
                        "play is the default. In tight space, ‘too high / "
                        "too close to an opponent’ becomes dangerous "
                        "sooner. Official lift limits and exceptions "
                        "(e.g. shots) live in FIH Indoor / KNHB — here you "
                        "train the read, not quotations."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Uitgewerkt voorbeeld (veld): aanval vanuit de 23m. "
                        "Aanvaller A speelt de bal hard en omhoog (~kniehoogte "
                        "op aankomst) recht op verdediger D die ~4 m verder "
                        "staat en de bal niet veilig kan ontwijken. D wordt "
                        "niet geraakt — maar moet wegduiken."
                    ),
                    en=(
                        "Worked example (field): attack from the 23m. "
                        "Attacker A plays the ball hard and raised "
                        "(~knee height on arrival) straight at defender D "
                        "standing ~4 m away who cannot safely evade. D is "
                        "not hit — but must duck away."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Besluit en waarom: fluit — gevaarlijke bal. "
                        "Richting = op D, afstand = kort, snelheid = hoog → "
                        "gevaar ook zonder contact. Herstart volgens "
                        "officiële plaats/richting (bronnen). Niet "
                        "automatisch een kaart: weeg intentie/ernst; "
                        "kaart alleen als de situatie dat vraagt. "
                        "Zaalvariant: dezelfde trajecten zijn sneller fout "
                        "door strengere liftgrenzen — fluit eerder."
                    ),
                    en=(
                        "Decision and why: whistle — dangerous ball. "
                        "Direction = at D, distance = short, speed = high → "
                        "danger even without contact. Restart per official "
                        "spot/direction (sources). Not an automatic card: "
                        "weigh intent/severity; card only if the picture "
                        "asks for it. Indoor variant: the same trajectories "
                        "are illegal sooner under tighter lift limits — "
                        "whistle earlier."
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
                        "Wat het regelkader vastlegt: wie de bal speelt, "
                        "mag dat met een legale stick/tackle. Contact dat "
                        "de balbezitter raakt (lichaam, stick-op-stick dat "
                        "de bal wegneemt zonder legale tackle) of dat de "
                        "balbezitter omver speelt, is een overtreding. Het "
                        "aantal verdedigers (1 of 2) is géén aparte "
                        "regelgrond — bezit en contactkwaliteit wel. "
                        "Exacte formulering: FIH / KNHB."
                    ),
                    en=(
                        "What the rules framework establishes: whoever "
                        "plays the ball may do so with a legal stick/"
                        "tackle. Contact that hits the ball carrier (body, "
                        "stick-on-stick that strips the ball without a "
                        "legal tackle) or that plays the carrier over is "
                        "an offence. Defender count (1 or 2) is not a "
                        "separate rule ground — possession and contact "
                        "quality are. Exact wording: FIH / KNHB."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Uitgewerkt voorbeeld (veld): aanvaller A dribbelt "
                        "duidelijk met de bal aan de stick richting de "
                        "cirkel. Verdedigers D1 en D2 drukken samen. D1 "
                        "speelt eerst de bal schoon van A’s stick; A blijft "
                        "overeind en speelt door. Geen body-check, geen "
                        "stick over de handen."
                    ),
                    en=(
                        "Worked example (field): attacker A dribbles clearly "
                        "with the ball on the stick toward the circle. "
                        "Defenders D1 and D2 press together. D1 first plays "
                        "the ball cleanly off A’s stick; A stays upright "
                        "and plays on. No body check, no stick over the "
                        "hands."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Besluit en waarom: speel door (of geef advantage "
                        "als A duidelijk ruimte houdt). Duidelijk bezit lag "
                        "bij A; D1 speelde de bal, niet de speler. Twee "
                        "verdedigers maken het niet automatisch een fout. "
                        "Als D2 daarna A’s lichaam raakt zonder bal → fluit "
                        "dan wél voor die contactfout."
                    ),
                    en=(
                        "Decision and why: play on (or advantage if A "
                        "clearly keeps space). Clear possession was with A; "
                        "D1 played the ball, not the player. Two defenders "
                        "do not make it automatically a foul. If D2 then "
                        "hits A’s body without the ball → whistle that "
                        "contact foul."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Zaalvariant: dezelfde lezing, kortere tijd. Bij "
                        "de banden is ‘schone tackle’ nog steeds de "
                        "standaard — maar D die A in de band duwt zonder "
                        "bal is sneller zichtbaar illegaal. Communiceer "
                        "vroeg met je partner als het spel de helft kruist."
                    ),
                    en=(
                        "Indoor variant: same read, less time. Near the "
                        "boards a ‘clean tackle’ is still the standard — "
                        "but D shoving A into the boards without the ball "
                        "is illegal sooner to the eye. Communicate early "
                        "with your partner when play crosses the half."
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
                        "Wat het regelkader vastlegt: een overtreding "
                        "vereist een leesbare fout (illegaal contact, "
                        "gevaar, obstructie, …) — niet ‘de aanvallende "
                        "kant stond dichter bij het doel’. Zolang niemand "
                        "controle heeft en er geen duidelijke fout is, "
                        "is doorspelen of wachten op controle correcter "
                        "dan een automatische ‘aanval’-fluit. Advantage "
                        "alleen als één kant écht ruimte/tempo wint. "
                        "Bronnen: FIH / KNHB."
                    ),
                    en=(
                        "What the rules framework establishes: an offence "
                        "needs a readable foul (illegal contact, danger, "
                        "obstruction, …) — not ‘the attacking side was "
                        "closer to goal’. While nobody has control and "
                        "there is no clear foul, playing on or waiting "
                        "for control is better than an automatic ‘attack’ "
                        "whistle. Advantage only when one side truly gains "
                        "space/tempo. Sources: FIH / KNHB."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Uitgewerkt voorbeeld: middenveld. A en D hebben "
                        "beide de stick bij de bal; de bal ligt tussen de "
                        "sticks, niemand dribbelt weg. A staat dichter bij "
                        "het aanvallende doel. Geen stick-over-stick die "
                        "iemand omver speelt, geen gevaarlijke lift, geen "
                        "body-check."
                    ),
                    en=(
                        "Worked example: midfield. A and D both have the "
                        "stick at the ball; the ball sits between the "
                        "sticks, nobody dribbles away. A is closer to the "
                        "attacking goal. No stick-over-stick that plays "
                        "someone over, no dangerous lift, no body check."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Besluit en waarom: speel door / houd de fluit. "
                        "Bezit is onduidelijk; nabijheid van het doel is "
                        "geen fout. Fluit pas als A of D een leesbare "
                        "overtreding maakt (bijv. D haakt A’s stick en "
                        "trekt A om) of als één kant duidelijk controle "
                        "neemt. Slechtste reflex: ‘aanval’ fluiten alleen "
                        "omdat A dichter bij het doel stond."
                    ),
                    en=(
                        "Decision and why: play on / hold the whistle. "
                        "Possession is unclear; proximity to goal is not "
                        "a foul. Whistle only when A or D commits a "
                        "readable offence (e.g. D hooks A’s stick and "
                        "pulls A over) or when one side clearly takes "
                        "control. Worst reflex: whistling ‘attack’ only "
                        "because A stood closer to goal."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Veld vs zaal: het principe is gelijk. Zaal is "
                        "sneller en dichter — je hebt minder frames om te "
                        "wachten, dus train vroege eye contact met je "
                        "partner op de scheidingslijn. Op topniveau "
                        "(later in het pad) wordt deze consistentie "
                        "strenger getoetst."
                    ),
                    en=(
                        "Field vs indoor: the principle is the same. "
                        "Indoor is faster and tighter — you have fewer "
                        "frames to wait, so train early eye contact with "
                        "your partner on the split line. At top standard "
                        "(later in the pathway) this consistency is "
                        "tested harder."
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
                        "Wat het regelkader vastlegt: de keeper mag de "
                        "bal verdedigen binnen de eigen cirkel/zone met "
                        "lichaam en uitrusting volgens de keeperregels. "
                        "Een slide of duik is niet automatisch een "
                        "penalty stroke — en niet automatisch legaal. "
                        "Illegaal is o.a. de aanvaller raken zonder de "
                        "bal te spelen, of gevaarlijk contact. Lees "
                        "altijd: pad → timing → contact (bal of lichaam). "
                        "Exacte keeperrechten: FIH / KNHB."
                    ),
                    en=(
                        "What the rules framework establishes: the keeper "
                        "may defend the ball inside their own circle/zone "
                        "with body and equipment per the keeper rules. A "
                        "slide or dive is not automatically a penalty "
                        "stroke — and not automatically legal. Illegal "
                        "includes hitting the attacker without playing "
                        "the ball, or dangerous contact. Always read: "
                        "path → timing → contact (ball or body). Exact "
                        "keeper rights: FIH / KNHB."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Uitgewerkt voorbeeld (veld): A dribbelt de cirkel "
                        "in met de bal aan de stick. Keeper K glijdt "
                        "schuin naar voren, speelt eerst de bal weg met "
                        "de stick/pad, en raakt A’s been pas nádat de "
                        "bal al weg is — A valt. Timing: K was bij de "
                        "bal vóór het contact met A."
                    ),
                    en=(
                        "Worked example (field): A dribbles into the "
                        "circle with the ball on the stick. Keeper K "
                        "slides diagonally forward, first plays the ball "
                        "away with stick/pad, and only then contacts A’s "
                        "leg after the ball is already gone — A falls. "
                        "Timing: K was at the ball before contact with A."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Besluit en waarom: speel door (of fluit alleen "
                        "als het ná-contact nog een aparte fout is). K "
                        "speelde eerst de bal; pad en timing kloppen. "
                        "Geen automatische stroke omdat A viel. "
                        "Tegenvoorbeeld: als K’s pad A’s lichaam raakt "
                        "vóór of zonder de bal → fluit (vaak stroke/"
                        "sanction per officiële tabel) — waarom: contact "
                        "op de speler, niet op de bal."
                    ),
                    en=(
                        "Decision and why: play on (or whistle only if "
                        "the after-contact is still a separate foul). K "
                        "played the ball first; path and timing fit. No "
                        "automatic stroke because A fell. Counter-"
                        "example: if K’s path hits A’s body before or "
                        "without the ball → whistle (often stroke/"
                        "sanction per the official table) — why: contact "
                        "on the player, not the ball."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Zaalvariant: banden en kleinere ruimte beperken "
                        "A’s uitwijkpad. Dezelfde lus (pad → timing → "
                        "contact), maar nabijheid weegt zwaarder — een "
                        "slide die A in de band duwt zonder bal is sneller "
                        "illegaal. Check officiële indoor-keeperregels "
                        "voor limieten."
                    ),
                    en=(
                        "Indoor variant: boards and smaller space limit "
                        "A’s escape path. Same loop (path → timing → "
                        "contact), but proximity weighs more — a slide "
                        "that shoves A into the boards without the ball "
                        "is illegal sooner. Check official indoor keeper "
                        "rules for limits."
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
                        "Je hebt per scenario het regelprincipe en een "
                        "uitgewerkt voorbeeld gezien. Open hieronder de "
                        "modulequiz op een aparte pagina: meerkeuze plus "
                        "een korte schrijfvraag, met uitleg en visuals bij "
                        "foute antwoorden. Sla voortgang op via je "
                        "cursussessie."
                    ),
                    en=(
                        "You have seen the rule principle and a worked "
                        "example per scenario. Open the module quiz below "
                        "on a separate page: multiple-choice plus a short "
                        "written item, with explanations and visuals on "
                        "wrong answers. Save progress via your course "
                        "session."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Daarna: het pad naar professioneel niveau "
                        "(o.a. Hoofdklasse) — daar worden ritme, "
                        "samenwerking en consistentie toegevoegd om "
                        "deze oordelen te verfijnen. Losse "
                        "oefenscenario’s blijven beschikbaar onder "
                        "Oefenscenario’s. Houd FIH-/KNHB-bronnen bij de "
                        "hand voor exacte tekst."
                    ),
                    en=(
                        "Next: the pathway toward professional standard "
                        "(e.g. Hoofdklasse) — there cadence, collaboration "
                        "and consistency are added to refine these "
                        "judgments. Standalone drills remain under "
                        "Practice scenarios. Keep FIH/KNHB sources handy "
                        "for exact wording."
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
