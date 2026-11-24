# Contributing

## Adding a module

1. Open `backend/app/data/course_seed.py`.
2. Append a `ModuleStub` to `MODULES` with:
   - stable `id` (kebab-case)
   - `kind`: `field` | `indoor` | `shared`
   - bilingual `title`, `summary`, `learning_objectives`, `instruction_outline`
   - optional `quiz_id`
   - `further_reading` with real official URLs + `Attribution` hooks
   - `order` for curriculum sequence
3. For KNHB illustrations/interpretations: set `knhb_illustration_placeholder=True` and `translation_needed=True`. **Do not** paste copyrighted rule text or ship assets you do not have rights to.
4. Add/adjust backend tests if the outline shape changes.
5. The frontend loads modules from `GET /api/course` — no frontend hardcoding required for stubs.

## Adding a quiz

1. Define a `Quiz` in `course_seed.py` (or a dedicated seed module later).
2. Use `multiple_choice` and/or `written` questions.
3. Provide `feedback_correct` and per-option `feedback_incorrect` (plus a default).
4. Optional `visualization_hint` strings are rendered as stubs; replace later with real viz/animations.
5. Register the quiz in `CourseOutline.quizzes` and link via `ModuleStub.quiz_id`.
6. Answers are graded by `POST /api/quizzes/{quiz_id}/submit` — keep correct keys off the public GET payload.

## i18n

- Content strings use `{ nl, en }` objects.
- UI chrome lives in `frontend/src/i18n/messages.ts`.
- To add a language later: extend `LocalizedText` / `Locale`, seed content, and UI dictionaries.

## Tests

```bash
# backend
cd backend && python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest

# frontend
cd frontend && npm install && npm test
```
