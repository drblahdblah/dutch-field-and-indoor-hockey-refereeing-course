"""Practice scenario bank endpoints (separate from module lessons)."""

from fastapi import APIRouter, HTTPException

from app.data.practice_scenarios import get_practice_bank
from app.quiz_public import to_public_quiz
from app.schemas import PracticeBankPublic, PracticeScenarioPublic

router = APIRouter(prefix="/api/practice", tags=["practice"])


def _to_public_bank() -> PracticeBankPublic:
    bank = get_practice_bank()
    return PracticeBankPublic(
        id=bank.id,
        title=bank.title,
        description=bank.description,
        scenarios=[
            PracticeScenarioPublic(
                id=s.id,
                kind=s.kind,
                title=s.title,
                situation=s.situation,
                focus=s.focus,
                order=s.order,
                visual_key=s.visual_key,
                quiz=to_public_quiz(s.quiz),
            )
            for s in sorted(bank.scenarios, key=lambda item: item.order)
        ],
    )


@router.get("", response_model=PracticeBankPublic)
def read_practice_bank() -> PracticeBankPublic:
    return _to_public_bank()


@router.get("/{scenario_id}", response_model=PracticeScenarioPublic)
def read_practice_scenario(scenario_id: str) -> PracticeScenarioPublic:
    bank = _to_public_bank()
    for scenario in bank.scenarios:
        if scenario.id == scenario_id:
            return scenario
    raise HTTPException(status_code=404, detail=f"Scenario not found: {scenario_id}")
