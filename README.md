# Dutch Field & Indoor Hockey Umpiring Course

Browser-based course for Netherlands referees (field + indoor), bilingual **NL / EN** from day one, building toward professional standard (e.g. Hoofdklasse).

This repository ships **full bilingual learning modules** (umpire role + field rules core + indoor rules core + professional / Hoofdklasse pathway + KNHB interpretation layer + **capstone assessment**) plus a separate **practice scenario bank** (`#/practice`): field and indoor decision scenarios with MC + written grading and explanations, original CSS/SVG visuals (no copyrighted KNHB art), course-path progress overview, session progress API (SQLite), and clean package layout. It does **not** reproduce copyrighted FIH/KNHB rule text or illustrations.

## Architecture

```
frontend/          React + Vite SPA (i18n UI, modules, practice bank, quiz, SVG viz)
backend/           FastAPI + SQLAlchemy + SQLite
  app/data/        Bilingual course seed + practice scenarios
  app/routers/     /api/course, /api/practice, /api/progress, /api/quizzes
  app/services/    Quiz grading
  app/security.py  Bearer/cookie session tokens for progress
docker-compose.yml Optional local stack
```

- **Course content** is seeded in Python (`backend/app/data/`) and served via `GET /api/course` with **answer keys stripped**. Full modules include `sections` + `visuals` (`content_status: full`).
- **Practice bank** is a separate flow (`GET /api/practice`, SPA `#/practice`) — not module lessons — with field/indoor decision scenarios.
- **Quizzes** expose prompts on GET; grading + bilingual feedback via `POST /api/quizzes/{id}/submit` (solutions only after submit). Feedback may include visualization hooks rendered as original SVG animations.
- **Progress** requires a bearer `access_token` issued once at `POST /api/progress/sessions` (or the httpOnly cookie). The SPA can resume with cookie/session auth (modules + optional practice scenario ids).

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
uvicorn app.main:app --reload --host 127.0.0.1 --port 8010
```

API docs: http://127.0.0.1:8010/docs  
Health: http://127.0.0.1:8010/api/health

Default local ports are **8010** (API) and **5174** (Vite) to avoid clashes with other apps on 8000/5173.

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open http://127.0.0.1:5174 — Vite proxies `/api` to http://127.0.0.1:8010.

### Docker Compose (optional)

Local hot-reload stack:

```bash
docker compose up
```

- Web: http://localhost:5174  
- API: http://localhost:8010  

Prod-ish single-host demo (no API reload, `COURSE_ENVIRONMENT=production`, Vite production build + preview, one uvicorn worker for SQLite). The overlay keeps `COURSE_COOKIE_SECURE=false` so httpOnly cookies work on local HTTP — set `COURSE_COOKIE_SECURE=true` (and HTTPS) for a real deploy. First boot installs deps into bind mounts and may take longer than the API health `start_period`.

```bash
docker compose -f docker-compose.yml -f docker-compose.prod.yml up --build
```

Copy `backend/.env.example` → `backend/.env` (and `frontend/.env.example` as needed) before changing CORS, cookie, or proxy settings. Never set `COURSE_CORS_ORIGINS=*`.

## Tests

```bash
# Backend (pytest)
cd backend
source .venv/bin/activate
pytest -q

# Frontend (vitest + production build)
cd frontend
npm test
npm run build
```

CI (`.github/workflows/ci.yml`) runs on pull requests and pushes to `main`: pytest, `npm test`, `npm run build`, and `docker compose … config`.

## Deploy notes

This repo is a **single-host / demo-friendly** stack, not a multi-region HA template.

1. **API** — run uvicorn with `--workers 1` while using SQLite and the in-process rate limiter (or move limits to the edge and use a shared DB).
2. **SPA** — `cd frontend && npm ci && npm run build`, then serve `frontend/dist/` behind your reverse proxy (or use the Compose prod overlay preview for a quick demo).
3. **Env** — set `COURSE_ENVIRONMENT=production`, an explicit `COURSE_CORS_ORIGINS` allowlist matching the SPA origin, `COURSE_EXPOSE_ACCESS_TOKEN=false`, and `COURSE_COOKIE_SECURE=true` on HTTPS. Enable `COURSE_TRUST_PROXY` only behind a proxy that strips spoofed `X-Forwarded-For`.
4. **Cookies** — production omits bearer tokens from JSON; the SPA resumes via the httpOnly `course_access_token` cookie (`credentials: "include"`). Cross-site needs `SameSite=None` + Secure.
5. **Health** — `GET /api/health` for readiness probes.
6. **Secrets** — no API keys are required for v0 defaults; keep real `.env` files out of git (see `.gitignore`).

## Security notes (v0)

- Progress read/write and quiz progress save require a session capability token via `Authorization: Bearer <access_token>` **or** the httpOnly `course_access_token` cookie (set on session create; works with the Vite `/api` proxy).
- Sessions have a TTL (`COURSE_SESSION_TTL_SECONDS`, default 30 days) and can be revoked with `DELETE /api/progress/session`.
- Production (`COURSE_ENVIRONMENT=production`): cookie defaults to `Secure` and JSON omits `access_token` (cookie-only). Override with `COURSE_COOKIE_SECURE=false` only for local HTTP demos (as in `docker-compose.prod.yml`). Dev may expose a bearer for TestClient / debugging.
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
- **KNHB interpretations**: module `mod-knhb-interpretations` exposes structured `interpretation_references` (NL pedagogical summaries + EN translation slots). Mark `translation_needed` / `knhb_illustration_placeholder` — do not invent EN legal text or claim assets you do not have.

## Attribution & license

- Software: **[MIT](./LICENSE)** — see also **[NOTICE](./NOTICE)** for the boundary with FIH/KNHB materials.
- Official sources are linked, not copied:

| Source | Notes |
|--------|--------|
| [FIH Rules of Hockey](https://www.fih.hockey/inside-fih/our-official-documents/rules-of-hockey) | Official outdoor/indoor rules — link out |
| [KNHB](https://www.knhb.nl/) | Interpretations / umpire materials — structured refs + EN slots; no KNHB illustrations bundled |

See also in-app **Sources & attribution** and fields on `Attribution` in the API.

## Adding modules / quizzes

See [CONTRIBUTING.md](./CONTRIBUTING.md).

## Remote

Canonical remote: `origin` → https://github.com/drblahdblah/dutch-field-and-indoor-hockey-refereeing-course
