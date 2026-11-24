# Dutch Field & Indoor Hockey Umpiring Course

Browser-based course for Netherlands referees (field + indoor), bilingual **NL / EN** from day one, building toward professional standard (e.g. Hoofdklasse).

This repository is a **v0 scaffold**: module stubs, one sample graded quiz with explanations, session progress API (SQLite), and clean package layout. It does **not** reproduce copyrighted FIH/KNHB rule text or illustrations.

## Architecture

```
frontend/          React + Vite SPA (i18n UI, modules, quiz)
backend/           FastAPI + SQLAlchemy + SQLite
  app/data/        Bilingual course seed (modules, quiz, attributions)
  app/routers/     /api/course, /api/progress, /api/quizzes
  app/services/    Quiz grading
docker-compose.yml Optional local stack
```

- **Course content** is seeded in Python (`backend/app/data/course_seed.py`) and served via `GET /api/course`.
- **Quizzes** expose prompts on GET; grading + bilingual feedback via `POST /api/quizzes/{id}/submit`.
- **Progress** is backend-persisted per session (`POST/GET/PUT /api/progress/sessions...`). The SPA stores the session id in `localStorage` to resume.

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

## i18n notes

- All learner-facing course strings are `{ nl, en }` pairs in the seed and API.
- UI chrome is in `frontend/src/i18n/messages.ts` with a locale toggle.
- Structure is ready for more locales: extend `LocalizedText`, seed data, and UI dictionaries.
- **KNHB interpretations**: NL source links/placeholders only; mark `translation_needed` / `knhb_illustration_placeholder` — do not invent EN legal text or claim assets you do not have.

## Attribution

Official sources are linked, not copied:

| Source | Notes |
|--------|--------|
| [FIH Rules of Hockey](https://www.fih.hockey/inside-fih/our-official-documents/rules-of-hockey) | Official outdoor/indoor rules — link out |
| [KNHB](https://www.knhb.nl/) | Interpretations / umpire materials — **placeholder** hooks; no KNHB illustrations bundled; EN translation TODO |

See also in-app **Sources & attribution** and fields on `Attribution` in the API.

## Adding modules / quizzes

See [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

[MIT](./LICENSE)

## Push to GitHub (first time)

There is no linked remote yet. Create an empty repo under **drblahdblah**, then push this local `main`.

### Option A — GitHub CLI (if authenticated as drblahdblah)

```bash
cd dutch-field-and-indoor-hockey-refereeing-course
gh auth login   # if needed
gh repo create drblahdblah/dutch-field-and-indoor-hockey-refereeing-course \
  --public --source=. --remote=origin --push
```

### Option B — Manual (github.com UI)

1. Sign in as **drblahdblah** on GitHub.
2. Create an **empty** repository named  
   `dutch-field-and-indoor-hockey-refereeing-course`  
   (no README/license — this repo already has them).
3. From this directory:

```bash
git remote add origin https://github.com/drblahdblah/dutch-field-and-indoor-hockey-refereeing-course.git
git push -u origin main
```

SSH alternative:

```bash
git remote add origin git@github.com:drblahdblah/dutch-field-and-indoor-hockey-refereeing-course.git
git push -u origin main
```

Target URL: https://github.com/drblahdblah/dutch-field-and-indoor-hockey-refereeing-course

## Handoff

A short project handoff also lives at the Cursor Project store path  
`docs/repo-init-handoff.md` (mirrored summary of this init).
