"""Backend API smoke and behavior tests."""

from datetime import datetime, timedelta, timezone

from app.config import settings
from app.rate_limit import limiter


def _auth_headers(access_token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {access_token}"}


def test_health(client):
    res = client.get("/api/health")
    assert res.status_code == 200
    body = res.json()
    assert body["status"] == "ok"


def test_course_outline_bilingual_and_strips_answers(client):
    res = client.get("/api/course")
    assert res.status_code == 200
    body = res.json()
    assert body["title"]["nl"]
    assert body["title"]["en"]
    assert len(body["modules"]) >= 3
    assert "quiz-intro-umpire-role" in body["quizzes"]
    assert "quiz-field-rules-core" in body["quizzes"]
    assert "quiz-indoor-context-basics" in body["quizzes"]
    module_ids = {m["id"] for m in body["modules"]}
    assert "mod-intro-role" in module_ids
    assert "mod-field-rules-core" in module_ids
    assert any(a.get("knhb_illustration_placeholder") for a in body["attributions"])
    for quiz in body["quizzes"].values():
        for q in quiz["questions"]:
            assert "correct_option_id" not in q
            assert "accepted_answers" not in q
            assert "feedback_correct" not in q
            assert "feedback_incorrect" not in q


def test_full_intro_module_has_sections_and_visuals(client):
    res = client.get("/api/course/modules/mod-intro-role")
    assert res.status_code == 200
    module = res.json()
    assert module["content_status"] == "full"
    assert module["quiz_id"] == "quiz-intro-umpire-role"
    assert len(module["sections"]) >= 4
    assert len(module["visuals"]) >= 2
    assert all(s["title"]["nl"] and s["title"]["en"] for s in module["sections"])
    assert all(len(s["paragraphs"]) >= 1 for s in module["sections"])
    visual_ids = {v["id"] for v in module["visuals"]}
    for section in module["sections"]:
        if section["visual_id"]:
            assert section["visual_id"] in visual_ids
    assert any(v["kind"] == "svg_animation" for v in module["visuals"])
    assert any(v["knhb_illustration_placeholder"] for v in module["visuals"])


def test_intro_quiz_grades_mc_and_written_with_explanations(client):
    res = client.post(
        "/api/quizzes/quiz-intro-umpire-role/submit",
        json={
            "answers": [
                {"question_id": "q1-priority-order", "selected_option_id": "a"},
                {"question_id": "q2-scan-partner", "selected_option_id": "b"},
                {"question_id": "q3-safety-keyword", "written_answer": "safety"},
                {"question_id": "q4-calm-communication", "written_answer": "loud"},
            ]
        },
    )
    assert res.status_code == 200
    body = res.json()
    assert body["total"] == 4
    assert body["score"] == 2
    by_id = {r["question_id"]: r for r in body["results"]}
    assert by_id["q1-priority-order"]["correct"] is False
    assert by_id["q1-priority-order"]["explanation"]["nl"]
    assert by_id["q1-priority-order"]["explanation"]["en"]
    assert by_id["q1-priority-order"]["visualization_hint"] == "safety-triangle"
    assert by_id["q1-priority-order"]["correct_option_id"] == "b"
    assert by_id["q2-scan-partner"]["correct"] is True
    assert by_id["q3-safety-keyword"]["correct"] is True
    assert by_id["q4-calm-communication"]["correct"] is False


def test_intro_quiz_progress_save_and_resume(client):
    created = client.post("/api/progress/sessions", json={"locale": "nl"})
    token = created.json()["access_token"]
    headers = _auth_headers(token)

    opened = client.put(
        "/api/progress/session",
        headers=headers,
        json={"module_id": "mod-intro-role", "status": "in_progress"},
    )
    assert opened.status_code == 200

    submit = client.post(
        "/api/quizzes/quiz-intro-umpire-role/submit",
        headers=headers,
        json={
            "save_progress": True,
            "answers": [
                {"question_id": "q1-priority-order", "selected_option_id": "b"},
                {"question_id": "q2-scan-partner", "selected_option_id": "b"},
                {"question_id": "q3-safety-keyword", "written_answer": "Safety"},
                {"question_id": "q4-calm-communication", "written_answer": "calm"},
            ],
        },
    )
    assert submit.status_code == 200
    assert submit.json()["progress_saved"] is True
    assert submit.json()["score"] == 4

    progress = client.get("/api/progress/session", headers=headers)
    assert progress.status_code == 200
    row = next(p for p in progress.json()["progress"] if p["module_id"] == "mod-intro-role")
    assert row["status"] == "completed"
    assert row["quiz_score"] == 4
    assert row["quiz_total"] == 4


def test_full_field_module_has_sections_and_visuals(client):
    res = client.get("/api/course/modules/mod-field-rules-core")
    assert res.status_code == 200
    module = res.json()
    assert module["content_status"] == "full"
    assert module["kind"] == "field"
    assert module["quiz_id"] == "quiz-field-rules-core"
    assert len(module["sections"]) >= 4
    assert len(module["visuals"]) >= 3
    assert all(s["title"]["nl"] and s["title"]["en"] for s in module["sections"])
    visual_ids = {v["id"] for v in module["visuals"]}
    for section in module["sections"]:
        if section["visual_id"]:
            assert section["visual_id"] in visual_ids
    assert any(v["kind"] == "svg_animation" for v in module["visuals"])
    assert any(v["animation_key"] == "danger-cone" for v in module["visuals"])
    assert any(v["knhb_illustration_placeholder"] for v in module["visuals"])


def test_field_quiz_grades_mc_and_written_with_explanations(client):
    res = client.post(
        "/api/quizzes/quiz-field-rules-core/submit",
        json={
            "answers": [
                {"question_id": "q1-raised-ball", "selected_option_id": "c"},
                {"question_id": "q2-restart-space", "selected_option_id": "c"},
                {"question_id": "q3-scoring-area-keyword", "written_answer": "circle"},
                {"question_id": "q4-advantage-keyword", "written_answer": "nope"},
            ]
        },
    )
    assert res.status_code == 200
    body = res.json()
    assert body["total"] == 4
    assert body["score"] == 2
    by_id = {r["question_id"]: r for r in body["results"]}
    assert by_id["q1-raised-ball"]["correct"] is False
    assert by_id["q1-raised-ball"]["explanation"]["nl"]
    assert by_id["q1-raised-ball"]["explanation"]["en"]
    assert by_id["q1-raised-ball"]["visualization_hint"] == "danger-cone"
    assert by_id["q1-raised-ball"]["correct_option_id"] == "b"
    assert by_id["q2-restart-space"]["correct"] is True
    assert by_id["q2-restart-space"]["correct_option_id"] == "c"
    assert by_id["q3-scoring-area-keyword"]["correct"] is True
    assert by_id["q4-advantage-keyword"]["correct"] is False


def test_quiz_get_hides_answers(client):
    res = client.get("/api/course/quizzes/quiz-field-rules-core")
    assert res.status_code == 200
    quiz = res.json()
    for q in quiz["questions"]:
        assert "correct_option_id" not in q
        assert "accepted_answers" not in q


def test_written_prompts_do_not_spoil_accepted_answers(client):
    """Public prompts must not embed answer keys (PR #1 answer-strip spirit)."""
    from app.data.course_seed import get_course_outline

    course = get_course_outline()
    public = client.get("/api/course").json()
    for quiz_id, quiz in course.quizzes.items():
        public_questions = {
            q["id"]: q for q in public["quizzes"][quiz_id]["questions"]
        }
        for question in quiz.questions:
            if question.type != "written" or not question.accepted_answers:
                continue
            prompt_blob = (
                public_questions[question.id]["prompt"]["nl"]
                + " "
                + public_questions[question.id]["prompt"]["en"]
            ).lower()
            for answer in question.accepted_answers:
                token = answer.strip().lower().rstrip("!.")
                assert token not in prompt_blob, (
                    f"{quiz_id}/{question.id} prompt leaks accepted answer {token!r}"
                )


def test_intro_quiz_get_hides_answers(client):
    res = client.get("/api/course/quizzes/quiz-intro-umpire-role")
    assert res.status_code == 200
    quiz = res.json()
    assert len(quiz["questions"]) == 4
    for q in quiz["questions"]:
        assert "correct_option_id" not in q
        assert "accepted_answers" not in q
        assert "feedback_correct" not in q


def test_quiz_submit_grades_and_explains(client):
    res = client.post(
        "/api/quizzes/quiz-field-rules-core/submit",
        json={
            "answers": [
                {"question_id": "q1-raised-ball", "selected_option_id": "c"},
                {"question_id": "q2-restart-space", "selected_option_id": "c"},
                {"question_id": "q3-scoring-area-keyword", "written_answer": "circle"},
                {"question_id": "q4-advantage-keyword", "written_answer": "advantage"},
            ]
        },
    )
    assert res.status_code == 200
    body = res.json()
    assert body["score"] == 3
    assert body["total"] == 4
    assert body["progress_saved"] is False
    wrong = next(r for r in body["results"] if r["question_id"] == "q1-raised-ball")
    assert wrong["correct"] is False
    assert wrong["explanation"]["en"]
    assert wrong["correct_option_id"] == "b"


def test_quiz_submit_omits_key_for_unanswered(client):
    res = client.post(
        "/api/quizzes/quiz-field-rules-core/submit",
        json={
            "answers": [
                {"question_id": "q1-raised-ball"},
                {"question_id": "q2-restart-space", "selected_option_id": "c"},
                {"question_id": "q3-scoring-area-keyword", "written_answer": "circle"},
                {"question_id": "q4-advantage-keyword", "written_answer": "advantage"},
            ]
        },
    )
    assert res.status_code == 200
    unanswered = next(r for r in res.json()["results"] if r["question_id"] == "q1-raised-ball")
    assert unanswered["correct"] is False
    assert unanswered["correct_option_id"] is None


def test_quiz_submit_rejects_unknown_question(client):
    res = client.post(
        "/api/quizzes/quiz-field-rules-core/submit",
        json={"answers": [{"question_id": "not-a-real-question", "selected_option_id": "a"}]},
    )
    assert res.status_code == 400


def test_progress_requires_auth(client):
    res = client.get("/api/progress/session")
    assert res.status_code == 401

    created = client.post("/api/progress/sessions", json={"display_name": "Test", "locale": "nl"})
    assert created.status_code == 201
    body = created.json()
    assert body["access_token"]
    assert body["expires_at"]
    assert "course_access_token" in created.cookies
    token = body["access_token"]

    denied = client.get(f"/api/progress/sessions/{body['id']}")
    assert denied.status_code == 404

    ok = client.get("/api/progress/session", headers=_auth_headers(token))
    assert ok.status_code == 200
    assert ok.json()["session"]["id"] == body["id"]


def test_invalid_bearer_rejected_without_cookie(client):
    res = client.get(
        "/api/progress/session",
        headers={"Authorization": "Bearer not-a-real-token"},
    )
    assert res.status_code == 401

    basic = client.get(
        "/api/progress/session",
        headers={"Authorization": "Basic abc"},
    )
    assert basic.status_code == 401

    empty = client.get(
        "/api/progress/session",
        headers={"Authorization": "Bearer "},
    )
    assert empty.status_code == 401


def test_non_bearer_authorization_falls_back_to_cookie(client):
    created = client.post("/api/progress/sessions", json={"locale": "nl"})
    assert created.status_code == 201
    # Cookie present; non-Bearer Authorization must not block cookie auth.
    res = client.get(
        "/api/progress/session",
        headers={"Authorization": "Basic abc"},
    )
    assert res.status_code == 200


_FIELD_PERFECT_ANSWERS = [
    {"question_id": "q1-raised-ball", "selected_option_id": "b"},
    {"question_id": "q2-restart-space", "selected_option_id": "c"},
    {"question_id": "q3-scoring-area-keyword", "written_answer": "circle"},
    {"question_id": "q4-advantage-keyword", "written_answer": "advantage"},
]


def test_save_progress_auth_failure_still_returns_grades(client):
    missing = client.post(
        "/api/quizzes/quiz-field-rules-core/submit",
        json={
            "save_progress": True,
            "answers": _FIELD_PERFECT_ANSWERS,
        },
    )
    assert missing.status_code == 200
    assert missing.json()["progress_saved"] is False
    assert missing.json()["score"] == 4

    bad = client.post(
        "/api/quizzes/quiz-field-rules-core/submit",
        headers=_auth_headers("bogus"),
        json={
            "save_progress": True,
            "answers": _FIELD_PERFECT_ANSWERS,
        },
    )
    assert bad.status_code == 200
    assert bad.json()["progress_saved"] is False


def test_completed_module_not_demoted_on_worse_resubmit(client):
    created = client.post("/api/progress/sessions", json={"locale": "nl"})
    token = created.json()["access_token"]
    headers = _auth_headers(token)

    perfect = client.post(
        "/api/quizzes/quiz-field-rules-core/submit",
        headers=headers,
        json={
            "save_progress": True,
            "answers": _FIELD_PERFECT_ANSWERS,
        },
    )
    assert perfect.json()["progress_saved"] is True

    worse = client.post(
        "/api/quizzes/quiz-field-rules-core/submit",
        headers=headers,
        json={
            "save_progress": True,
            "answers": [
                {"question_id": "q1-raised-ball", "selected_option_id": "a"},
                {"question_id": "q2-restart-space", "selected_option_id": "a"},
                {"question_id": "q3-scoring-area-keyword", "written_answer": "nope"},
                {"question_id": "q4-advantage-keyword", "written_answer": "nope"},
            ],
        },
    )
    assert worse.status_code == 200
    assert worse.json()["score"] == 0

    progress = client.get("/api/progress/session", headers=headers)
    row = next(
        p for p in progress.json()["progress"] if p["module_id"] == "mod-field-rules-core"
    )
    assert row["status"] == "completed"
    assert row["quiz_score"] == 4
    assert row["completed_at"] is not None


def test_progress_put_rejects_client_quiz_scores(client):
    created = client.post("/api/progress/sessions", json={"locale": "nl"})
    token = created.json()["access_token"]
    res = client.put(
        "/api/progress/session",
        headers=_auth_headers(token),
        json={
            "module_id": "mod-field-rules-core",
            "status": "completed",
            "quiz_score": 99,
            "quiz_total": 99,
        },
    )
    assert res.status_code == 422


def test_session_progress_roundtrip(client):
    created = client.post("/api/progress/sessions", json={"display_name": "Test", "locale": "nl"})
    assert created.status_code == 201
    token = created.json()["access_token"]
    headers = _auth_headers(token)

    updated = client.put(
        "/api/progress/session",
        headers=headers,
        json={"module_id": "mod-field-rules-core", "status": "in_progress"},
    )
    assert updated.status_code == 200
    assert updated.json()["status"] == "in_progress"
    assert updated.json()["quiz_score"] is None

    bad_module = client.put(
        "/api/progress/session",
        headers=headers,
        json={"module_id": "not-a-module", "status": "in_progress"},
    )
    assert bad_module.status_code == 400

    submit = client.post(
        "/api/quizzes/quiz-field-rules-core/submit",
        headers=headers,
        json={
            "save_progress": True,
            "answers": [
                {"question_id": "q1-raised-ball", "selected_option_id": "b"},
                {"question_id": "q2-restart-space", "selected_option_id": "c"},
                {"question_id": "q3-scoring-area-keyword", "written_answer": "Circle"},
                {"question_id": "q4-advantage-keyword", "written_answer": "Advantage!"},
            ],
        },
    )
    assert submit.status_code == 200
    assert submit.json()["progress_saved"] is True
    assert submit.json()["score"] == 4

    progress = client.get("/api/progress/session", headers=headers)
    assert progress.status_code == 200
    modules = {p["module_id"]: p for p in progress.json()["progress"]}
    assert modules["mod-field-rules-core"]["status"] == "completed"
    assert modules["mod-field-rules-core"]["quiz_score"] == 4


def test_cookie_auth_works_without_bearer(client):
    created = client.post("/api/progress/sessions", json={"locale": "en"})
    assert created.status_code == 201
    progress = client.get("/api/progress/session")
    assert progress.status_code == 200
    assert progress.json()["session"]["locale"] == "en"


def test_revoke_session(client):
    created = client.post("/api/progress/sessions", json={"locale": "nl"})
    token = created.json()["access_token"]
    headers = _auth_headers(token)
    assert client.get("/api/progress/session", headers=headers).status_code == 200

    revoked = client.delete("/api/progress/session", headers=headers)
    assert revoked.status_code == 204

    assert client.get("/api/progress/session", headers=headers).status_code == 401


def test_expired_session_rejected(client):
    from app.database import get_db
    from app.main import app
    from app.models import UserSession
    from app.security import hash_access_token

    created = client.post("/api/progress/sessions", json={"locale": "nl"})
    token = created.json()["access_token"]
    headers = _auth_headers(token)

    db_gen = app.dependency_overrides[get_db]()
    db = next(db_gen)
    try:
        row = (
            db.query(UserSession)
            .filter(UserSession.token_hash == hash_access_token(token))
            .one()
        )
        row.expires_at = datetime.now(timezone.utc) - timedelta(seconds=5)
        db.commit()
    finally:
        try:
            next(db_gen)
        except StopIteration:
            pass

    assert client.get("/api/progress/session", headers=headers).status_code == 401


def test_production_omits_access_token_in_body(client, monkeypatch):
    monkeypatch.setattr(settings, "environment", "production")
    monkeypatch.setattr(settings, "expose_access_token", None)
    # Keep Secure off so HTTP TestClient can round-trip the cookie.
    monkeypatch.setattr(settings, "cookie_secure", False)
    created = client.post("/api/progress/sessions", json={"locale": "nl"})
    assert created.status_code == 201
    assert created.json()["access_token"] is None
    assert "course_access_token" in created.cookies
    assert client.get("/api/progress/session").status_code == 200


def test_production_sets_secure_cookie(client, monkeypatch):
    monkeypatch.setattr(settings, "environment", "production")
    monkeypatch.setattr(settings, "cookie_secure", None)
    created = client.post("/api/progress/sessions", json={"locale": "nl"})
    assert created.status_code == 201
    set_cookie = created.headers.get("set-cookie", "")
    assert "Secure" in set_cookie or "secure" in set_cookie.lower()
    assert created.json()["access_token"] is None


def test_session_create_rate_limit(client, monkeypatch):
    monkeypatch.setattr(settings, "rate_limit_session_create", 3)
    monkeypatch.setattr(settings, "rate_limit_window_seconds", 60)
    limiter.reset()
    for _ in range(3):
        assert client.post("/api/progress/sessions", json={"locale": "nl"}).status_code == 201
    limited = client.post("/api/progress/sessions", json={"locale": "nl"})
    assert limited.status_code == 429


def test_rate_limit_ignores_spoofed_xff_by_default(client, monkeypatch):
    monkeypatch.setattr(settings, "rate_limit_session_create", 2)
    monkeypatch.setattr(settings, "rate_limit_window_seconds", 60)
    monkeypatch.setattr(settings, "trust_proxy", False)
    limiter.reset()
    assert client.post("/api/progress/sessions", json={"locale": "nl"}).status_code == 201
    assert client.post("/api/progress/sessions", json={"locale": "nl"}).status_code == 201
    # Spoofed XFF must not open a new bucket when trust_proxy is false.
    spoofed = client.post(
        "/api/progress/sessions",
        json={"locale": "nl"},
        headers={"X-Forwarded-For": "203.0.113.99"},
    )
    assert spoofed.status_code == 429


def test_indoor_quiz_submit(client):
    res = client.post(
        "/api/quizzes/quiz-indoor-context-basics/submit",
        json={
            "answers": [
                {"question_id": "q1-indoor-space", "selected_option_id": "b"},
                {"question_id": "q2-indoor-keyword", "written_answer": "Indoor"},
            ]
        },
    )
    assert res.status_code == 200
    assert res.json()["score"] == 2


def test_invalid_locale_rejected(client):
    res = client.post("/api/progress/sessions", json={"locale": "de"})
    assert res.status_code == 422
