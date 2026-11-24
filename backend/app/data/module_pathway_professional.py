"""Full learning module: pathway toward professional / Hoofdklasse standard (NL + EN).

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

PATHWAY_VISUALS: list[VisualPlaceholder] = [
    VisualPlaceholder(
        id="viz-match-cadence",
        kind="svg_animation",
        title=LocalizedText(
            nl="Wedstrijdritme: voor → tijdens → na",
            en="Match cadence: before → during → after",
        ),
        caption=LocalizedText(
            nl=(
                "Originele SVG: drie fasen van match management. Geen "
                "officieel KNHB-wedstrijdprotocol — procedures bij KNHB/club."
            ),
            en=(
                "Original SVG: three phases of match management. Not an "
                "official KNHB match protocol — procedures via KNHB/club."
            ),
        ),
        animation_key="match-cadence",
    ),
    VisualPlaceholder(
        id="viz-partner-handoff",
        kind="svg_animation",
        title=LocalizedText(
            nl="Samenwerking: overdracht tussen partners",
            en="Collaboration: handoff between partners",
        ),
        caption=LocalizedText(
            nl=(
                "Originele cursusanimatie: wie leidt, wie ondersteunt, wanneer "
                "je overdraagt. Geen overgenomen gebarenplaatjes."
            ),
            en=(
                "Original course animation: who leads, who supports, when you "
                "hand off. No reproduced signal charts."
            ),
        ),
        animation_key="partner-handoff",
    ),
    VisualPlaceholder(
        id="viz-consistency-loop",
        kind="svg_animation",
        title=LocalizedText(
            nl="Consistentie:zelfde criterium, herhaalbaar",
            en="Consistency: same criterion, repeatable",
        ),
        caption=LocalizedText(
            nl=(
                "Originele SVG: observeer → besluit → communiceer → review. "
                "Pedagogisch model, geen FIH-citaat."
            ),
            en=(
                "Original SVG: observe → decide → communicate → review. "
                "Pedagogical model, not an FIH quotation."
            ),
        ),
        animation_key="consistency-loop",
    ),
    VisualPlaceholder(
        id="viz-match-pressure",
        kind="svg_animation",
        title=LocalizedText(
            nl="Scenario: oplopende wedstrijddruk",
            en="Scenario: rising match pressure",
        ),
        caption=LocalizedText(
            nl=(
                "Originele scenario-SVG: vóór → tijdens → ná met oplopende "
                "druk. Pedagogisch model — geen KNHB-protocolplaatje."
            ),
            en=(
                "Original scenario SVG: before → during → after with rising "
                "pressure. Pedagogical model — not a KNHB protocol chart."
            ),
        ),
        animation_key="match-pressure",
    ),
    VisualPlaceholder(
        id="viz-knhb-pathway-slot",
        kind="official_link_slot",
        title=LocalizedText(
            nl="KNHB-ontwikkelpad (plaatshouder)",
            en="KNHB development pathway (placeholder)",
        ),
        caption=LocalizedText(
            nl=(
                "Link naar KNHB-scheidsrechters-/opleidingsmateriaal. Geen "
                "KNHB-illustratie in deze repo. EN-vertaling: volgt later."
            ),
            en=(
                "Link to KNHB umpire / education materials. No KNHB "
                "illustration ships in this repo. EN translation: TBD."
            ),
        ),
        official_source_url=KNHB_HOME_URL,
        official_source_name="KNHB",
        knhb_illustration_placeholder=True,
    ),
]

PATHWAY_QUIZ = Quiz(
    id="quiz-pathway-professional",
    title=LocalizedText(
        nl="Quiz: pad naar professioneel niveau",
        en="Quiz: pathway toward professional standard",
    ),
    questions=[
        QuizQuestion(
            id="q1-match-management",
            type="multiple_choice",
            prompt=LocalizedText(
                nl=(
                    "Op topniveau (pedagogisch kader — geen regelcitaat) is "
                    "goed match management vooral:"
                ),
                en=(
                    "At top level (pedagogical frame — not a rules quotation), "
                    "strong match management is mainly:"
                ),
            ),
            options=[
                QuizOption(
                    id="a",
                    text=LocalizedText(
                        nl="Alleen fluiten; voor- en nabespreking zijn optioneel.",
                        en="Whistle only; pre- and post-briefings are optional.",
                    ),
                ),
                QuizOption(
                    id="b",
                    text=LocalizedText(
                        nl="Alleen fitness; beslissingen volgen vanzelf.",
                        en="Fitness alone; decisions will follow by themselves.",
                    ),
                ),
                QuizOption(
                    id="c",
                    text=LocalizedText(
                        nl="Ritme vóór, tijdens en ná de wedstrijd bewust sturen.",
                        en="Deliberately steer cadence before, during and after.",
                    ),
                ),
                QuizOption(
                    id="d",
                    text=LocalizedText(
                        nl="Nooit met je partner over de wedstrijd praten.",
                        en="Never discuss the match with your partner.",
                    ),
                ),
            ],
            correct_option_id="c",
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Juist. Professioneel ritme omvat briefing, in-game "
                        "sturing en nabespreking. Club-/KNHB-protocollen voor "
                        "concrete stappen — hier alleen het kader."
                    ),
                    en=(
                        "Correct. Professional cadence includes briefing, "
                        "in-game steering and debrief. Club/KNHB protocols for "
                        "concrete steps — this is the frame only."
                    ),
                ),
                visualization_hint="match-pressure",
            ),
            feedback_incorrect={
                "a": QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Onjuist. Voor- en nabespreking horen bij "
                            "professioneel match management."
                        ),
                        en=(
                            "Incorrect. Pre- and post-briefings belong to "
                            "professional match management."
                        ),
                    ),
                    visualization_hint="match-pressure",
                ),
                "b": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Fitness helpt, maar vervangt geen besliskaders.",
                        en="Fitness helps, but does not replace decision frames.",
                    ),
                    visualization_hint="consistency-loop",
                ),
                "d": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Partneroverleg is juist een kern van samenwerking.",
                        en="Partner dialogue is a core of collaboration.",
                    ),
                    visualization_hint="partner-handoff",
                ),
            },
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Herlees het wedstrijdritme: vóór → tijdens → ná.",
                    en="Revisit match cadence: before → during → after.",
                ),
                visualization_hint="match-pressure",
            ),
        ),
        QuizQuestion(
            id="q2-collaboration",
            type="multiple_choice",
            prompt=LocalizedText(
                nl=(
                    "Bij samenwerking tussen twee scheidsrechters is de beste "
                    "eerste gewoonte (cursusmodel — geen citaat):"
                ),
                en=(
                    "When two umpires collaborate, the best first habit "
                    "(course model — not a quotation) is:"
                ),
            ),
            options=[
                QuizOption(
                    id="a",
                    text=LocalizedText(
                        nl="Altijd zelf fluiten, ook buiten je helft.",
                        en="Always whistle yourself, even outside your half.",
                    ),
                ),
                QuizOption(
                    id="b",
                    text=LocalizedText(
                        nl="Partner negeren tot er een protest is.",
                        en="Ignore your partner until there is a protest.",
                    ),
                ),
                QuizOption(
                    id="c",
                    text=LocalizedText(
                        nl="Alleen non-verbaal; nooit eye contact zoeken.",
                        en="Non-verbal only; never seek eye contact.",
                    ),
                ),
                QuizOption(
                    id="d",
                    text=LocalizedText(
                        nl="Lead/support en vroege overdracht afspreken.",
                        en="Agree clear lead/support and early handoff cues.",
                    ),
                ),
            ],
            correct_option_id="d",
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Juist. Lead/support en overdracht verminderen "
                        "dubbele fluiten en gaten. Exacte teamprotocollen: "
                        "club/KNHB."
                    ),
                    en=(
                        "Correct. Lead/support and handoff reduce double "
                        "whistles and gaps. Exact team protocols: club/KNHB."
                    ),
                ),
                visualization_hint="partner-handoff",
            ),
            feedback_incorrect={
                "a": QuizFeedback(
                    explanation=LocalizedText(
                        nl=(
                            "Onjuist. Buiten je verantwoordelijkheid fluiten "
                            "breekt het partnersysteem."
                        ),
                        en=(
                            "Incorrect. Whistling outside your remit breaks "
                            "the partner system."
                        ),
                    ),
                    visualization_hint="partner-handoff",
                ),
                "b": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Te laat: samenwerking begint vóór protesten.",
                        en="Too late: collaboration starts before protests.",
                    ),
                    visualization_hint="partner-handoff",
                ),
                "c": QuizFeedback(
                    explanation=LocalizedText(
                        nl="Eye contact en korte cues horen er juist bij.",
                        en="Eye contact and short cues belong in the model.",
                    ),
                    visualization_hint="partner-handoff",
                ),
            },
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Bekijk de partner-overdracht: lead → support → handoff.",
                    en="Review partner handoff: lead → support → handoff.",
                ),
                visualization_hint="partner-handoff",
            ),
        ),
        QuizQuestion(
            id="q3-consistency-keyword",
            type="written",
            prompt=LocalizedText(
                nl=(
                    "Welk Engels sleutelwoord gebruikt deze cursus voor "
                    "herhaalbare, gelijkwaardige beslissingen over de "
                    "wedstrijd? (één woord)"
                ),
                en=(
                    "Which English keyword does this course use for "
                    "repeatable, like-for-like decisions across the match? "
                    "(one word)"
                ),
            ),
            accepted_answers=["consistency"],
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl="Juist — consistency (beslissingsconsistentie).",
                    en="Correct — consistency.",
                ),
                visualization_hint="consistency-loop",
            ),
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl=(
                        "Verwacht antwoord: consistency. Zie de "
                        "consistentielus-visual."
                    ),
                    en=(
                        "Expected answer: consistency. See the "
                        "consistency-loop visual."
                    ),
                ),
                visualization_hint="consistency-loop",
            ),
        ),
        QuizQuestion(
            id="q4-pathway-keyword",
            type="written",
            prompt=LocalizedText(
                nl=(
                    "Welk Engels woord gebruikt deze cursus voor het "
                    "ontwikkeltraject van clubniveau naar topcompetitie "
                    "(bijv. Hoofdklasse)? (één woord)"
                ),
                en=(
                    "Which English word does this course use for the "
                    "development track from club level toward top competition "
                    "(e.g. Hoofdklasse)? (one word)"
                ),
            ),
            accepted_answers=["pathway"],
            feedback_correct=QuizFeedback(
                explanation=LocalizedText(
                    nl="Juist — pathway (ontwikkelpad).",
                    en="Correct — pathway.",
                ),
                visualization_hint=None,
            ),
            feedback_incorrect_default=QuizFeedback(
                explanation=LocalizedText(
                    nl="Verwacht antwoord: pathway.",
                    en="Expected answer: pathway.",
                ),
                visualization_hint=None,
            ),
        ),
    ],
)

PATHWAY_MODULE = ModuleStub(
    id="mod-pathway-hoofdklasse",
    kind="shared",
    title=LocalizedText(
        nl="Pad naar professioneel niveau (o.a. Hoofdklasse)",
        en="Pathway toward professional standard (e.g. Hoofdklasse)",
    ),
    summary=LocalizedText(
        nl=(
            "Volledige module: match management, samenwerking, "
            "beslissingsconsistentie en KNHB-padwijzers — met visuals, "
            "oefenquiz en officiële bronlinks."
        ),
        en=(
            "Full module: match management, collaboration, decision "
            "consistency and KNHB pathway pointers — with visuals, practice "
            "quiz and official source links."
        ),
    ),
    learning_objectives=[
        LocalizedText(
            nl="Wedstrijdritme (vóór / tijdens / ná) in eigen woorden beschrijven.",
            en="Describe match cadence (before / during / after) in your own words.",
        ),
        LocalizedText(
            nl="Lead/support en overdracht met je partner afspreken.",
            en="Agree lead/support and handoff with your partner.",
        ),
        LocalizedText(
            nl="Een consistentiecriterium toepassen over een hele wedstrijd.",
            en="Apply a consistency criterion across a whole match.",
        ),
        LocalizedText(
            nl="KNHB/FIH-bronnen aanwijzen voor officiële opleidingsstappen.",
            en="Point to KNHB/FIH sources for official education steps.",
        ),
    ],
    instruction_outline=[
        LocalizedText(
            nl="Match management: vóór → tijdens → ná.",
            en="Match management: before → during → after.",
        ),
        LocalizedText(
            nl="Samenwerking: lead, support, overdracht.",
            en="Collaboration: lead, support, handoff.",
        ),
        LocalizedText(
            nl="Consistentie:zelfde criterium, herhaalbaar.",
            en="Consistency: same criterion, repeatable.",
        ),
        LocalizedText(
            nl="Padwijzers: KNHB/FIH-links (geen auteursrechtelijke kunst).",
            en="Pathway pointers: KNHB/FIH links (no copyrighted art).",
        ),
    ],
    content_status="full",
    sections=[
        LearningSection(
            id="sec-pathway-why",
            title=LocalizedText(
                nl="Waarom een professioneel pad",
                en="Why a professional pathway",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Na intro-rol, veld- en zaalkernen verschuift de "
                        "focus van ‘wat fluit ik’ naar ‘hoe leid ik een "
                        "wedstrijd op topniveau’. In NL-context is "
                        "Hoofdklasse een bekende referentie — niet de enige "
                        "route, wel een bruikbaar anker voor standaard."
                    ),
                    en=(
                        "After intro role, field and indoor cores, focus "
                        "shifts from ‘what do I whistle’ to ‘how do I lead a "
                        "match at top standard’. In the NL context, "
                        "Hoofdklasse is a familiar reference — not the only "
                        "route, but a useful anchor for standard."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Deze module citeert geen auteursrechtelijk "
                        "beschermde FIH- of KNHB-tekst en levert geen "
                        "KNHB-kunst. We bouwen pedagogische kaders en linken "
                        "naar officiële bronnen voor actuele eisen."
                    ),
                    en=(
                        "This module does not reproduce copyrighted FIH or "
                        "KNHB text and ships no KNHB art. We build "
                        "pedagogical frames and link to official sources for "
                        "current requirements."
                    ),
                ),
            ],
        ),
        LearningSection(
            id="sec-match-management",
            title=LocalizedText(
                nl="Scenario: match management onder oplopende druk",
                en="Scenario: match management under rising pressure",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Denk in drie fasen: vóór (briefing, rollen, "
                        "escalatieafspraken), tijdens (tempo, advantage, "
                        "communicatie), ná (korte nabespreking met je "
                        "partner). Exacte club- of KNHB-checklists horen "
                        "elders — hier het ritmemodel."
                    ),
                    en=(
                        "Think in three phases: before (briefing, roles, "
                        "escalation agreements), during (tempo, advantage, "
                        "communication), after (short debrief with your "
                        "partner). Exact club or KNHB checklists live "
                        "elsewhere — here the cadence model."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Op topniveau merken spelers en coaches of jullie "
                        "het speelbeeld sturen of erachteraan hollen. "
                        "Ritme is zichtbaar leiderschap."
                    ),
                    en=(
                        "At top level, players and coaches notice whether you "
                        "steer the picture or chase it. Cadence is visible "
                        "leadership."
                    ),
                ),
            ],
            visual_id="viz-match-pressure",
        ),
        LearningSection(
            id="sec-collaboration",
            title=LocalizedText(
                nl="Samenwerking & overdracht",
                en="Collaboration & handoff",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Twee scheidsrechters werken als één systeem: "
                        "duidelijke lead/support, vroege eye contact, en "
                        "afgesproken overdracht wanneer het spel de "
                        "helftgrens of verantwoordelijkheid kruist."
                    ),
                    en=(
                        "Two umpires work as one system: clear lead/support, "
                        "early eye contact, and agreed handoff when play "
                        "crosses the half or responsibility line."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Oefen korte cues (hand, stem, blik) in training — "
                        "niet pas tijdens een contest. Officiële "
                        "teamgebieden/protocollen: KNHB of bond."
                    ),
                    en=(
                        "Practice short cues (hand, voice, glance) in "
                        "training — not only mid-contest. Official team "
                        "areas/protocols: KNHB or federation."
                    ),
                ),
            ],
            visual_id="viz-partner-handoff",
        ),
        LearningSection(
            id="sec-decision-consistency",
            title=LocalizedText(
                nl="Beslissingsconsistentie",
                en="Decision consistency",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Consistentie betekent: hetzelfde criterium "
                        "toepassen voor vergelijkbare situaties over de "
                        "hele wedstrijd — niet ‘strenger worden’ zonder "
                        "reden, en niet ‘losser’ onder druk."
                    ),
                    en=(
                        "Consistency means: apply the same criterion to "
                        "like situations across the whole match — not "
                        "‘getting stricter’ without cause, and not ‘looser’ "
                        "under pressure."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "Gebruik de lus: observeer → besluit → communiceer "
                        "→ korte review (met partner of coach). Video-review "
                        "en mentoring horen bij professionele ontwikkeling; "
                        "deze cursus levert geen copyrighted clips."
                    ),
                    en=(
                        "Use the loop: observe → decide → communicate → "
                        "brief review (with partner or coach). Video review "
                        "and mentoring belong to professional development; "
                        "this course ships no copyrighted clips."
                    ),
                ),
            ],
            visual_id="viz-consistency-loop",
        ),
        LearningSection(
            id="sec-knhb-pathway",
            title=LocalizedText(
                nl="KNHB-padwijzers (attributie)",
                en="KNHB pathway pointers (attribution)",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Concrete opleidingsstappen, licenties en "
                        "aanmeldroutes staan bij de KNHB — niet in deze "
                        "repo. Gebruik de plaatshouder-link hieronder; "
                        "controleer altijd de actuele KNHB-pagina."
                    ),
                    en=(
                        "Concrete education steps, licences and application "
                        "routes live with the KNHB — not in this repo. Use "
                        "the placeholder link below; always check the "
                        "current KNHB page."
                    ),
                ),
                LocalizedText(
                    nl=(
                        "FIH Rules blijven de internationale regelbasis; "
                        "KNHB-interpretaties en opleidingen vertalen die "
                        "naar NL-competities. Geen KNHB-illustraties hier."
                    ),
                    en=(
                        "FIH Rules remain the international rules base; "
                        "KNHB interpretations and education translate them "
                        "for NL competitions. No KNHB illustrations here."
                    ),
                ),
            ],
            visual_id="viz-knhb-pathway-slot",
        ),
        LearningSection(
            id="sec-pathway-practice-next",
            title=LocalizedText(
                nl="Oefenen en verder",
                en="Practice and next steps",
            ),
            paragraphs=[
                LocalizedText(
                    nl=(
                        "Maak de quiz hieronder. Sla voortgang op via je "
                        "cursussessie. Daarna: de KNHB-interpretatielaag "
                        "(attributie + EN-vertaalslots). Houd KNHB- en "
                        "FIH-bronnen bij de hand; deze module is een "
                        "besliskader, geen vervanging van bondscursussen."
                    ),
                    en=(
                        "Take the quiz below. Save progress via your course "
                        "session. Next: the KNHB interpretation layer "
                        "(attribution + EN translation slots). Keep KNHB and "
                        "FIH sources handy; this module is a decision frame, "
                        "not a replacement for federation courses."
                    ),
                ),
            ],
        ),
    ],
    visuals=PATHWAY_VISUALS,
    quiz_id=PATHWAY_QUIZ.id,
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
                nl="KNHB — opleiding & scheidsrechters (link/plaatshouder)",
                en="KNHB — education & umpires (link/placeholder)",
            ),
            url=KNHB_HOME_URL,
            attribution=Attribution(
                source_name="KNHB — opleiding & scheidsrechters",
                source_url=KNHB_HOME_URL,
                note=LocalizedText(
                    nl=(
                        "Geen KNHB-illustraties inbegrepen. Link naar "
                        "officiële KNHB-opleidings-/scheidsrechtersbronnen; "
                        "EN-vertaling: TODO."
                    ),
                    en=(
                        "No KNHB illustrations included. Link to official "
                        "KNHB education / umpire sources; EN translation: TODO."
                    ),
                ),
                knhb_illustration_placeholder=True,
                translation_needed=True,
            ),
        ),
    ],
    order=4,
)
