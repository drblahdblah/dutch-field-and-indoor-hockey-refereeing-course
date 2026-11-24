# Dutch Field & Indoor Hockey Umpiring Course

Browser-based course for Netherlands referees (field + indoor), bilingual **NL / EN** from day one, building toward professional standard (e.g. Hoofdklasse).

This repository ships a **first full bilingual learning module** (umpire role) plus remaining stubs: graded quizzes with explanations, original CSS/SVG visuals (no copyrighted KNHB art), session progress API (SQLite), and clean package layout. It does **not** reproduce copyrighted FIH/KNHB rule text or illustrations.

## Architecture

```
frontend/          React + Vite SPA (i18n UI, modules, quiz, SVG viz)
backend/           FastAPI + SQLAlchemy + SQLite
  app/data/        Bilingual course seed (full intro module + stubs)
  app/routers/     /api/course, /api/progress, /api/quizzes
  app/services/    Quiz grading
  app/security.py  Bearer/cookie session tokens for progress
docker-compose.yml Optional local stack
```

- **Course content** is seeded in Python (`backend/app/data/`) and served via `GET /api/course` with **answer keys stripped**. Full modules include `sections` + `visuals` (`content_status: full`).
- **Quizzes** expose prompts on GET; grading + bilingual feedback via `POST /api/quizzes/{id}/submit` (solutions only after submit). Feedback may include visualization hooks rendered as original SVG animations.
- **Progress** requires a bearer `access_token` issued once at `POST /api/progress/sessions` (or the httpOnly cookie). The SPA can resume with cookie/session auth.

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
- Sessions have a TTL (`COURSE_SESSION_TTL_SECONDS`, default 30 days) and can be revoked with `DELETE /api/progress/session`.
- Production (`COURSE_ENVIRONMENT=production`): cookie is `Secure`; JSON omits `access_token` (cookie-only). Dev may expose a bearer for TestClient / debugging.
- Cookie `SameSite` is configurable (`COURSE_COOKIE_SAMESITE`); `none` requires Secure.
- Per-IP rate limits apply to session create and quiz submit (`COURSE_RATE_LIMIT_*`). Default uses the direct peer IP (not client-supplied `X-Forwarded-For`); set `COURSE_TRUST_PROXY=true` only behind a trusted proxy. Limits are in-process (single worker); use edge limiting for multi-worker/prod scale.
- Quiz scores and `completed` status are set only by graded `POST /api/quizzes/.../submit` — clients cannot forge scores on `PUT /api/progress/session`.
- CORS allowlist is env-driven (`COURSE_CORS_ORIGINS`); wildcard origins are rejected when credentials are used.
- Input validation covers locale, display name length, module ids, and quiz answer payloads.
- GET course/quiz paths never include `correct_option_id`, `accepted_answers`, or feedback maps.
- Submit reveals `correct_option_id` only for questions the learner actually attempted.
- Non-Bearer `Authorization` headers fall through to cookie auth instead of hard-failing.
- SPA uses `credentials: "include"` (httpOnly cookie is the resume path). A bearer is stored in `localStorage` only when the API returns `access_token` (development); production omits it.

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
