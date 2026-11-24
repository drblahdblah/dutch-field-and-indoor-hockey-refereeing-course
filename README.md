# Dutch Field & Indoor Hockey Umpiring Course

Browser-based course for Netherlands referees (field + indoor), bilingual **NL / EN** from day one, building toward professional standard (e.g. Hoofdklasse).

This repository is a **v0 scaffold**: module stubs, graded quizzes with explanations, session progress API (SQLite), and clean package layout. It does **not** reproduce copyrighted FIH/KNHB rule text or illustrations.

## Architecture

```
frontend/          React + Vite SPA (i18n UI, modules, quiz)
backend/           FastAPI + SQLAlchemy + SQLite
  app/data/        Bilingual course seed (modules, quiz, attributions)
  app/routers/     /api/course, /api/progress, /api/quizzes
  app/services/    Quiz grading
  app/security.py  Bearer session tokens for progress
docker-compose.yml Optional local stack
```

- **Course content** is seeded in Python (`backend/app/data/course_seed.py`) and served via `GET /api/course` with **answer keys stripped**.
- **Quizzes** expose prompts on GET; grading + bilingual feedback via `POST /api/quizzes/{id}/submit` (solutions only after submit).
- **Progress** requires a bearer `access_token` issued once at `POST /api/progress/sessions`. The SPA stores the token in `localStorage` to resume.

## Requirements

- Python 3.11+
- Node.js 20+
- Optional: Docker Compose

## Run locally

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

API docs: http://127.0.0.1:8000/docs  
Health: http://127.0.0.1:8000/api/health

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open http://127.0.0.1:5173 — Vite proxies `/api` to the backend.

### Docker Compose (optional)

```bash
docker compose up
```

- Web: http://localhost:5173  
- API: http://localhost:8000  

## Tests

```bash
# Backend (pytest)
cd backend
source .venv/bin/activate
pytest -q

# Frontend (vitest smoke)
cd frontend
npm test
```

## Security notes (v0)

- Progress read/write and quiz progress save require a session capability token via `Authorization: Bearer <access_token>` **or** the httpOnly `course_access_token` cookie (set on session create; works with the Vite `/api` proxy).
- Quiz scores and `completed` status are set only by graded `POST /api/quizzes/.../submit` — clients cannot forge scores on `PUT /api/progress/session`.
- CORS allowlist is env-driven (`COURSE_CORS_ORIGINS`); wildcard origins are rejected when credentials are used.
- Input validation covers locale, display name length, module ids, and quiz answer payloads.
- GET course/quiz paths never include `correct_option_id`, `accepted_answers`, or feedback maps.
- Submit reveals `correct_option_id` only for questions the learner actually attempted.
- The SPA may also keep a bearer copy in `localStorage` as a Vite/dev fallback; prefer the httpOnly cookie in production deployments behind a same-origin proxy.

## i18n notes

- All learner-facing course strings are `{ nl, en }` pairs in the seed and API.
- UI chrome is in `frontend/src/i18n/messages.ts` with a locale toggle.
- Structure is ready for more locales: extend `LocalizedText`, seed data, and UI dictionaries.
- **KNHB interpretations**: NL source links/placeholders only; mark `translation_needed` / `knhb_illustration_placeholder` — do not invent EN legal text or claim assets you do not have.

## Attribution & license

- Software: **[MIT](./LICENSE)** — see also **[NOTICE](./NOTICE)** for the boundary with FIH/KNHB materials.
- Official sources are linked, not copied:

| Source | Notes |
|--------|--------|
| [FIH Rules of Hockey](https://www.fih.hockey/inside-fih/our-official-documents/rules-of-hockey) | Official outdoor/indoor rules — link out |
| [KNHB](https://www.knhb.nl/) | Interpretations / umpire materials — **placeholder** hooks; no KNHB illustrations bundled; EN translation TODO |

See also in-app **Sources & attribution** and fields on `Attribution` in the API.

## Adding modules / quizzes

See [CONTRIBUTING.md](./CONTRIBUTING.md).

## Remote

Canonical remote: `origin` → https://github.com/drblahdblah/dutch-field-and-indoor-hockey-refereeing-course
