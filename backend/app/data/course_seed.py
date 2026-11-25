"""Bilingual course outline: full modules through capstone assessment.

Do NOT invent copyrighted FIH/KNHB rule text or illustrations.
Attribution hooks and official-source links only.
"""

from app.data.module_capstone import CAPSTONE_MODULE, CAPSTONE_QUIZ
from app.data.module_field_hard_decisions import FIELD_HARD_MODULE, FIELD_HARD_QUIZ
from app.data.module_field_rules import FIELD_MODULE, FIELD_QUIZ
from app.data.module_indoor_hard_decisions import INDOOR_HARD_MODULE, INDOOR_HARD_QUIZ
from app.data.module_indoor_rules import INDOOR_MODULE, INDOOR_QUIZ
from app.data.module_intro_role import INTRO_MODULE, INTRO_QUIZ
from app.data.module_knhb_interpretations import (
    INTERPRETATION_MODULE,
    INTERPRETATION_QUIZ,
)
from app.data.module_pathway_professional import PATHWAY_MODULE, PATHWAY_QUIZ
from app.data.practice_scenarios import practice_quizzes
from app.schemas import (
    Attribution,
    CourseOutline,
    LocalizedText,
    ModuleStub,
    Quiz,
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
    FIELD_HARD_MODULE,
    INDOOR_HARD_MODULE,
    PATHWAY_MODULE,
    INTERPRETATION_MODULE,
    CAPSTONE_MODULE,
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
                "Volledige modules (intro rol, veld- en zaalkern, veld- en "
                "zaal harde beslissingen, pad naar professioneel niveau, "
                "KNHB-interpretatielaag, capstone-toets) met quiz, feedback, "
                "navigatieoverzicht en sessievoortgang. " + KNHB_RULES_NOTE.nl
            ),
            en=(
                "Full modules (intro role, field and indoor core, field and "
                "indoor hard decisions, pathway toward professional standard, "
                "KNHB interpretation layer, capstone assessment) with quiz, "
                "feedback, navigation overview and session progress. "
                + KNHB_RULES_NOTE.en
            ),
        ),
        modules=MODULES,
        quizzes=_all_quizzes(),
        attributions=OFFICIAL_ATTRIBUTIONS,
    )


def _all_quizzes() -> dict[str, Quiz]:
    """Module quizzes plus practice-bank quizzes (for GET/submit)."""
    return {
        INTRO_QUIZ.id: INTRO_QUIZ,
        FIELD_QUIZ.id: FIELD_QUIZ,
        INDOOR_QUIZ.id: INDOOR_QUIZ,
        FIELD_HARD_QUIZ.id: FIELD_HARD_QUIZ,
        INDOOR_HARD_QUIZ.id: INDOOR_HARD_QUIZ,
        PATHWAY_QUIZ.id: PATHWAY_QUIZ,
        INTERPRETATION_QUIZ.id: INTERPRETATION_QUIZ,
        CAPSTONE_QUIZ.id: CAPSTONE_QUIZ,
        **practice_quizzes(),
    }
