# Contributing

## Adding a module

1. Prefer a dedicated seed file under `backend/app/data/` (see `module_intro_role.py`, `module_field_rules.py`, `module_indoor_rules.py`), then register it from `course_seed.py`.
2. Append a `ModuleStub` with:
   - stable `id` (kebab-case)
   - `kind`: `field` | `indoor` | `shared`
   - bilingual `title`, `summary`, `learning_objectives`, `instruction_outline`
   - `content_status`: `stub` (outline only) or `full` (requires `sections`)
   - for full modules: bilingual `sections` + `visuals` (`svg_animation` or attributed `official_link_slot`)
   - optional `quiz_id`
   - `further_reading` with real official URLs + `Attribution` hooks
   - `order` for curriculum sequence
3. For KNHB illustrations/interpretations: set `knhb_illustration_placeholder=True` and `translation_needed=True`. **Do not** paste copyrighted rule text or ship assets you do not have rights to. Original CSS/SVG course animations are fine; attribute and link official FIH/KNHB sources for anything that is not original.
4. Add/adjust backend tests if the outline shape changes.
5. The frontend loads modules from `GET /api/course` — wire new `animation_key` values in `ModuleVisual` when you add SVG animations.

## Adding a quiz

1. Define a `Quiz` in a seed module (or `course_seed.py`).
2. Use `multiple_choice` and/or `written` questions.
3. Provide `feedback_correct` and per-option `feedback_incorrect` (plus a default).
4. Optional `visualization_hint` values should match known SPA animation keys (e.g. `safety-triangle`, `danger-cone`, `pitch-zones`, `court-boards`, `lift-limit`, `board-play`) or stay free-form (UI shows a muted fallback).
5. Register the quiz in `CourseOutline.quizzes` and link via `ModuleStub.quiz_id`.
6. Answers are graded by `POST /api/quizzes/{quiz_id}/submit` — keep correct keys off the public GET payload (`CourseOutlinePublic` / `QuizPublic`). **Never** put accepted answers inside public `prompt` text.
7. Progress APIs require session auth (Bearer and/or httpOnly cookie from `POST /api/progress/sessions`).

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
