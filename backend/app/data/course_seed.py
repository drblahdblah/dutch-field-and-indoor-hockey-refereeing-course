"""Bilingual course outline: full modules (intro, field, indoor, pathway, interpretations).

Do NOT invent copyrighted FIH/KNHB rule text or illustrations.
Attribution hooks and official-source links only.
"""

from app.data.module_field_rules import FIELD_MODULE, FIELD_QUIZ
from app.data.module_indoor_rules import INDOOR_MODULE, INDOOR_QUIZ
from app.data.module_intro_role import INTRO_MODULE, INTRO_QUIZ
from app.data.module_knhb_interpretations import (
    INTERPRETATION_MODULE,
    INTERPRETATION_QUIZ,
)
from app.data.module_pathway_professional import PATHWAY_MODULE, PATHWAY_QUIZ
from app.schemas import (
    Attribution,
    CourseOutline,
    LocalizedText,
    ModuleStub,
)

KNHB_RULES_NOTE = LocalizedText(
    nl=(
        "Verwijs altijd naar de officiële FIH-regels en KNHB-interpretaties. "
        "Deze cursus bevat geen overgenomen auteursrechtelijk beschermde "
        "regeltekst of KNHB-illustraties. De interpretatielaag biedt "
        "NL-samenvattingen met EN-vertalingsslots (translation_needed)."
    ),
    en=(
        "Always refer to the official FIH Rules and KNHB interpretations. "
        "This course does not reproduce copyrighted rule text or KNHB "
        "illustrations. The interpretation layer provides NL summaries with "
        "EN translation slots (translation_needed)."
    ),
)

OFFICIAL_ATTRIBUTIONS: list[Attribution] = [
    Attribution(
        source_name="FIH Rules of Hockey",
        source_url="https://www.fih.hockey/inside-fih/our-official-documents/rules-of-hockey",
        note=LocalizedText(
            nl="Officiële FIH Rules of Hockey — bron voor veldhockeyregels.",
            en="Official FIH Rules of Hockey — source for outdoor hockey rules.",
        ),
        knhb_illustration_placeholder=False,
        translation_needed=False,
    ),
    Attribution(
        source_name="FIH Indoor Hockey Rules",
        source_url="https://www.fih.hockey/inside-fih/our-official-documents/rules-of-hockey",
        note=LocalizedText(
            nl="Officiële FIH Indoor Hockey Rules — bron voor zaalhockeyregels.",
            en="Official FIH Indoor Hockey Rules — source for indoor hockey rules.",
        ),
        knhb_illustration_placeholder=False,
        translation_needed=False,
    ),
    Attribution(
        source_name="KNHB — regels & interpretaties",
        source_url="https://www.knhb.nl/",
        note=LocalizedText(
            nl=(
                "Link naar KNHB-interpretaties / scheidsrechtersmateriaal. "
                "Geen KNHB-illustraties inbegrepen. Zie module "
                "mod-knhb-interpretations voor NL-samenvattingen + EN-slots."
            ),
            en=(
                "Link to KNHB interpretations / umpire materials. "
                "No KNHB illustrations included. See module "
                "mod-knhb-interpretations for NL summaries + EN slots."
            ),
        ),
        knhb_illustration_placeholder=True,
        translation_needed=True,
    ),
]

MODULES: list[ModuleStub] = [
    INTRO_MODULE,
    FIELD_MODULE,
    INDOOR_MODULE,
    PATHWAY_MODULE,
    INTERPRETATION_MODULE,
]


def get_course_outline() -> CourseOutline:
    return CourseOutline(
        id="nl-hockey-umpire-v0",
        title=LocalizedText(
            nl="Nederlandse veld- & zaalhockey scheidsrechterscursus",
            en="Dutch field & indoor hockey umpiring course",
        ),
        description=LocalizedText(
            nl=(
                "Volledige modules (intro rol, veld- en zaalkernregels, pad "
                "naar professioneel niveau, KNHB-interpretatielaag) met quiz, "
                "feedback en sessievoortgang. " + KNHB_RULES_NOTE.nl
            ),
            en=(
                "Full modules (intro role, field and indoor core rules, "
                "pathway toward professional standard, KNHB interpretation "
                "layer) with quiz, feedback and session progress. "
                + KNHB_RULES_NOTE.en
            ),
        ),
        modules=MODULES,
        quizzes={
            INTRO_QUIZ.id: INTRO_QUIZ,
            FIELD_QUIZ.id: FIELD_QUIZ,
            INDOOR_QUIZ.id: INDOOR_QUIZ,
            PATHWAY_QUIZ.id: PATHWAY_QUIZ,
            INTERPRETATION_QUIZ.id: INTERPRETATION_QUIZ,
        },
        attributions=OFFICIAL_ATTRIBUTIONS,
    )
