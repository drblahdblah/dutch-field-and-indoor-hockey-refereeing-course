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
    assert "quiz-indoor-rules-core" in body["quizzes"]
    assert "quiz-hard-decisions" in body["quizzes"]
    assert "quiz-pathway-professional" in body["quizzes"]
    assert "quiz-knhb-interpretations" in body["quizzes"]
    assert "quiz-capstone-assessment" in body["quizzes"]
    assert "quiz-indoor-context-basics" not in body["quizzes"]
    module_ids = {m["id"] for m in body["modules"]}
    assert "mod-intro-role" in module_ids
    assert "mod-field-rules-core" in module_ids
    assert "mod-indoor-rules-core" in module_ids
    assert "mod-hard-decisions" in module_ids
    assert "mod-pathway-hoofdklasse" in module_ids
    assert "mod-knhb-interpretations" in module_ids
    assert "mod-capstone-assessment" in module_ids
    assert "mod-indoor-basics" not in module_ids
    hard = next(m for m in body["modules"] if m["id"] == "mod-hard-decisions")
    assert hard["content_status"] == "full"
    assert hard["order"] == 4
    pathway = next(m for m in body["modules"] if m["id"] == "mod-pathway-hoofdklasse")
    assert pathway["content_status"] == "full"
    assert pathway["order"] == 5
    interp = next(m for m in body["modules"] if m["id"] == "mod-knhb-interpretations")
    assert interp["content_status"] == "full"
    assert interp["order"] == 6
    assert len(interp["interpretation_references"]) >= 3
    capstone = next(m for m in body["modules"] if m["id"] == "mod-capstone-assessment")
    assert capstone["content_status"] == "full"
    assert capstone["order"] == 7
    assert any(a.get("knhb_illustration_placeholder") for a in body["attributions"])
    assert any(a.get("translation_needed") for a in body["attributions"])
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
    assert len(module["sections"]) >= 6
    assert len(module["visuals"]) >= 5
    assert all(s["title"]["nl"] and s["title"]["en"] for s in module["sections"])
    assert all(len(s["paragraphs"]) >= 1 for s in module["sections"])
    visual_ids = {v["id"] for v in module["visuals"]}
    for section in module["sections"]:
        if section["visual_id"]:
            assert section["visual_id"] in visual_ids
    anim_keys = {
        v["animation_key"] for v in module["visuals"] if v["kind"] == "svg_animation"
    }
    assert {
        "safety-triangle",
        "scan-cycle",
        "calm-signal",
        "context-split",
        "presence-arc",
        "call-clarity",
    } <= anim_keys
    assert any(v["kind"] == "svg_animation" for v in module["visuals"])
    assert not any(v["knhb_illustration_placeholder"] for v in module["visuals"])
    assert all(v["kind"] == "svg_animation" for v in module["visuals"])


def test_intro_quiz_grades_mc_and_written_with_explanations(client):
    res = client.post(
        "/api/quizzes/quiz-intro-umpire-role/submit",
        json={
            "answers": [
                {"question_id": "q1-priority-order", "selected_option_id": "a"},
                {"question_id": "q2-scan-partner", "selected_option_id": "b"},
                {"question_id": "q3-safety-keyword", "written_answer": "safety"},
                {"question_id": "q4-calm-communication", "written_answer": "loud"},
                {"question_id": "q5-context-cadence", "selected_option_id": "b"},
            ]
        },
    )
    assert res.status_code == 200
    body = res.json()
    assert body["total"] == 5
    assert body["score"] == 3
    by_id = {r["question_id"]: r for r in body["results"]}
    assert by_id["q1-priority-order"]["correct"] is False
    assert by_id["q1-priority-order"]["explanation"]["nl"]
    assert by_id["q1-priority-order"]["explanation"]["en"]
    assert by_id["q1-priority-order"]["visualization_hint"] == "safety-triangle"
    assert by_id["q1-priority-order"]["correct_option_id"] == "b"
    assert by_id["q2-scan-partner"]["correct"] is True
    assert by_id["q3-safety-keyword"]["correct"] is True
    assert by_id["q4-calm-communication"]["correct"] is False
    assert by_id["q5-context-cadence"]["correct"] is True
    assert by_id["q5-context-cadence"]["visualization_hint"] == "context-split"


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
                {"question_id": "q5-context-cadence", "selected_option_id": "b"},
            ],
        },
    )
    assert submit.status_code == 200
    assert submit.json()["progress_saved"] is True
    assert submit.json()["score"] == 5

    progress = client.get("/api/progress/session", headers=headers)
    assert progress.status_code == 200
    row = next(p for p in progress.json()["progress"] if p["module_id"] == "mod-intro-role")
    assert row["status"] == "completed"
    assert row["quiz_score"] == 5
    assert row["quiz_total"] == 5


def test_full_field_module_has_sections_and_visuals(client):
    res = client.get("/api/course/modules/mod-field-rules-core")
    assert res.status_code == 200
    module = res.json()
    assert module["content_status"] == "full"
    assert module["kind"] == "field"
    assert module["quiz_id"] == "quiz-field-rules-core"
    assert len(module["sections"]) >= 6
    assert len(module["visuals"]) >= 5
    assert all(s["title"]["nl"] and s["title"]["en"] for s in module["sections"])
    assert all(len(s["paragraphs"]) >= 1 for s in module["sections"])
    visual_ids = {v["id"] for v in module["visuals"]}
    for section in module["sections"]:
        if section["visual_id"]:
            assert section["visual_id"] in visual_ids
    anim_keys = {
        v["animation_key"] for v in module["visuals"] if v["kind"] == "svg_animation"
    }
    assert {
        "pitch-zones",
        "danger-cone",
        "restart-bubble",
        "field-attack",
        "advantage-lens",
    } <= anim_keys
    section_ids = {s["id"] for s in module["sections"]}
    assert "sec-advantage-lens" in section_ids
    advantage = next(s for s in module["sections"] if s["id"] == "sec-advantage-lens")
    assert advantage["visual_id"] == "viz-advantage-lens"
    assert any(v["kind"] == "svg_animation" for v in module["visuals"])
    assert not any(v["knhb_illustration_placeholder"] for v in module["visuals"])
    assert all(v["kind"] == "svg_animation" for v in module["visuals"])


def test_field_quiz_grades_mc_and_written_with_explanations(client):
    res = client.post(
        "/api/quizzes/quiz-field-rules-core/submit",
        json={
            "answers": [
                {"question_id": "q1-raised-ball", "selected_option_id": "c"},
                {"question_id": "q2-restart-space", "selected_option_id": "c"},
                {"question_id": "q3-scoring-area-keyword", "written_answer": "circle"},
                {"question_id": "q4-advantage-keyword", "written_answer": "nope"},
                {"question_id": "q5-advantage-when", "selected_option_id": "b"},
            ]
        },
    )
    assert res.status_code == 200
    body = res.json()
    assert body["total"] == 5
    assert body["score"] == 3
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
    assert by_id["q5-advantage-when"]["correct"] is True
    assert by_id["q5-advantage-when"]["visualization_hint"] == "advantage-lens"


def test_quiz_get_hides_answers(client):
    res = client.get("/api/course/quizzes/quiz-field-rules-core")
    assert res.status_code == 200
    quiz = res.json()
    assert len(quiz["questions"]) == 5
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
    assert len(quiz["questions"]) == 5
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
                {"question_id": "q5-advantage-when", "selected_option_id": "b"},
            ]
        },
    )
    assert res.status_code == 200
    body = res.json()
    assert body["score"] == 4
    assert body["total"] == 5
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
                {"question_id": "q5-advantage-when", "selected_option_id": "b"},
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
    {"question_id": "q5-advantage-when", "selected_option_id": "b"},
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
    assert missing.json()["score"] == 5

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
                {"question_id": "q5-advantage-when", "selected_option_id": "a"},
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
    assert row["quiz_score"] == 5
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
                {"question_id": "q5-advantage-when", "selected_option_id": "b"},
            ],
        },
    )
    assert submit.status_code == 200
    assert submit.json()["progress_saved"] is True
    assert submit.json()["score"] == 5

    progress = client.get("/api/progress/session", headers=headers)
    assert progress.status_code == 200
    modules = {p["module_id"]: p for p in progress.json()["progress"]}
    assert modules["mod-field-rules-core"]["status"] == "completed"
    assert modules["mod-field-rules-core"]["quiz_score"] == 5


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


def test_full_indoor_module_has_sections_and_visuals(client):
    res = client.get("/api/course/modules/mod-indoor-rules-core")
    assert res.status_code == 200
    module = res.json()
    assert module["content_status"] == "full"
    assert module["kind"] == "indoor"
    assert module["quiz_id"] == "quiz-indoor-rules-core"
    assert len(module["sections"]) >= 5
    assert len(module["visuals"]) >= 5
    assert all(s["title"]["nl"] and s["title"]["en"] for s in module["sections"])
    visual_ids = {v["id"] for v in module["visuals"]}
    for section in module["sections"]:
        if section["visual_id"]:
            assert section["visual_id"] in visual_ids
    assert any(v["kind"] == "svg_animation" for v in module["visuals"])
    keys = {
        v["animation_key"] for v in module["visuals"] if v["kind"] == "svg_animation"
    }
    assert keys >= {
        "court-boards",
        "lift-limit",
        "board-play",
        "indoor-rebound",
        "tempo-proximity",
    }
    assert len(module["sections"]) >= 6
    assert "sec-tempo-proximity" in {s["id"] for s in module["sections"]}
    tempo = next(s for s in module["sections"] if s["id"] == "sec-tempo-proximity")
    assert tempo["visual_id"] == "viz-tempo-proximity"
    board_sec = next(s for s in module["sections"] if s["id"] == "sec-board-play")
    assert board_sec["visual_id"] == "viz-board-play"
    assert not any(v["kind"] == "official_link_slot" for v in module["visuals"])
    assert not any(v["knhb_illustration_placeholder"] for v in module["visuals"])
    reading_urls = {r["url"] for r in module["further_reading"]}
    assert any("fih.hockey" in u for u in reading_urls)
    assert any("knhb.nl" in u for u in reading_urls)


def test_indoor_quiz_grades_mc_and_written_with_explanations(client):
    res = client.post(
        "/api/quizzes/quiz-indoor-rules-core/submit",
        json={
            "answers": [
                {"question_id": "q1-board-anticipation", "selected_option_id": "a"},
                {"question_id": "q2-lift-emphasis", "selected_option_id": "d"},
                {"question_id": "q3-boards-keyword", "written_answer": "boards"},
                {"question_id": "q4-indoor-keyword", "written_answer": "nope"},
                {"question_id": "q5-tempo-when", "selected_option_id": "b"},
            ]
        },
    )
    assert res.status_code == 200
    body = res.json()
    assert body["total"] == 5
    assert body["score"] == 3
    by_id = {r["question_id"]: r for r in body["results"]}
    assert by_id["q1-board-anticipation"]["correct"] is False
    assert by_id["q1-board-anticipation"]["explanation"]["nl"]
    assert by_id["q1-board-anticipation"]["explanation"]["en"]
    assert by_id["q1-board-anticipation"]["visualization_hint"] == "court-boards"  # option a
    assert by_id["q1-board-anticipation"]["correct_option_id"] == "c"
    assert by_id["q2-lift-emphasis"]["correct"] is True
    assert by_id["q2-lift-emphasis"]["correct_option_id"] == "d"
    assert by_id["q3-boards-keyword"]["correct"] is True
    assert by_id["q4-indoor-keyword"]["correct"] is False
    assert by_id["q5-tempo-when"]["correct"] is True
    assert by_id["q5-tempo-when"]["visualization_hint"] == "tempo-proximity"


def test_indoor_quiz_progress_save_and_resume(client):
    created = client.post("/api/progress/sessions", json={"locale": "nl"})
    token = created.json()["access_token"]
    headers = _auth_headers(token)

    opened = client.put(
        "/api/progress/session",
        headers=headers,
        json={"module_id": "mod-indoor-rules-core", "status": "in_progress"},
    )
    assert opened.status_code == 200

    submit = client.post(
        "/api/quizzes/quiz-indoor-rules-core/submit",
        headers=headers,
        json={
            "save_progress": True,
            "answers": [
                {"question_id": "q1-board-anticipation", "selected_option_id": "c"},
                {"question_id": "q2-lift-emphasis", "selected_option_id": "d"},
                {"question_id": "q3-boards-keyword", "written_answer": "Boards"},
                {"question_id": "q4-indoor-keyword", "written_answer": "Indoor!"},
                {"question_id": "q5-tempo-when", "selected_option_id": "b"},
            ],
        },
    )
    assert submit.status_code == 200
    assert submit.json()["progress_saved"] is True
    assert submit.json()["score"] == 5

    progress = client.get("/api/progress/session", headers=headers)
    assert progress.status_code == 200
    row = next(
        p for p in progress.json()["progress"] if p["module_id"] == "mod-indoor-rules-core"
    )
    assert row["status"] == "completed"
    assert row["quiz_score"] == 5
    assert row["quiz_total"] == 5


# Keep in sync with frontend visuals/animationKeys.ts KNOWN_ANIMATION_KEYS.
_SPA_ANIMATION_KEYS = frozenset(
    {
        "safety-triangle",
        "scan-cycle",
        "pitch-zones",
        "danger-cone",
        "restart-bubble",
        "court-boards",
        "lift-limit",
        "board-play",
        "match-cadence",
        "partner-handoff",
        "consistency-loop",
        "source-stack",
        "translation-slot",
        "attribution-chain",
        "capstone-weave",
        "field-attack",
        "indoor-rebound",
        "match-pressure",
        "calm-signal",
        "context-split",
        "presence-arc",
        "call-clarity",
        "advantage-lens",
        "tempo-proximity",
        "standard-ladder",
        "practice-circle-entry",
        "practice-freehit-23",
        "practice-advantage-wave",
        "practice-board-lift",
        "practice-indoor-restart",
        "practice-side-board",
        "hard-decision-frame",
        "hard-raised-danger",
        "hard-pressure-clear",
        "hard-contested",
        "hard-gk-dive",
    }
)


def test_seed_animation_keys_match_spa_allowlist():
    from app.data.course_seed import get_course_outline

    course = get_course_outline()
    for module in course.modules:
        for visual in module.visuals:
            if visual.kind != "svg_animation":
                continue
            assert visual.animation_key in _SPA_ANIMATION_KEYS, (
                f"{module.id}/{visual.id} unknown animation_key {visual.animation_key!r}"
            )
    for quiz in course.quizzes.values():
        for question in quiz.questions:
            for feedback in [
                question.feedback_correct,
                question.feedback_incorrect_default,
                *(question.feedback_incorrect or {}).values(),
            ]:
                if feedback is None or not feedback.visualization_hint:
                    continue
                assert feedback.visualization_hint in _SPA_ANIMATION_KEYS, (
                    f"{quiz.id}/{question.id} unknown visualization_hint "
                    f"{feedback.visualization_hint!r}"
                )


def test_full_hard_decisions_module_has_sections_and_visuals(client):
    res = client.get("/api/course/modules/mod-hard-decisions")
    assert res.status_code == 200
    module = res.json()
    assert module["content_status"] == "full"
    assert module["kind"] == "shared"
    assert module["quiz_id"] == "quiz-hard-decisions"
    assert module["order"] == 4
    assert len(module["sections"]) >= 6
    assert len(module["visuals"]) >= 5
    assert all(s["title"]["nl"] and s["title"]["en"] for s in module["sections"])
    visual_ids = {v["id"] for v in module["visuals"]}
    for section in module["sections"]:
        if section["visual_id"]:
            assert section["visual_id"] in visual_ids
    keys = {
        v["animation_key"] for v in module["visuals"] if v["kind"] == "svg_animation"
    }
    assert keys >= {
        "hard-decision-frame",
        "hard-raised-danger",
        "hard-pressure-clear",
        "hard-contested",
        "hard-gk-dive",
    }
    section_ids = {s["id"] for s in module["sections"]}
    assert "sec-raised-dangerous" in section_ids
    assert "sec-clear-possession-pressure" in section_ids
    assert "sec-contested-possession" in section_ids
    assert "sec-gk-sliding" in section_ids
    raised = next(s for s in module["sections"] if s["id"] == "sec-raised-dangerous")
    assert raised["visual_id"] == "viz-hard-raised"
    assert len(raised["paragraphs"]) >= 4
    raised_blob = " ".join(
        f"{p['nl']} {p['en']}" for p in raised["paragraphs"]
    ).lower()
    assert "worked example" in raised_blob or "uitgewerkt voorbeeld" in raised_blob
    assert "decision and why" in raised_blob or "besluit en waarom" in raised_blob
    assert "rules framework" in raised_blob or "regelkader" in raised_blob
    for sec_id in (
        "sec-clear-possession-pressure",
        "sec-contested-possession",
        "sec-gk-sliding",
    ):
        sec = next(s for s in module["sections"] if s["id"] == sec_id)
        assert len(sec["paragraphs"]) >= 4
        blob = " ".join(f"{p['nl']} {p['en']}" for p in sec["paragraphs"]).lower()
        assert "worked example" in blob or "uitgewerkt voorbeeld" in blob
        assert "decision and why" in blob or "besluit en waarom" in blob
    why = next(s for s in module["sections"] if s["id"] == "sec-hard-why")
    assert why["visual_id"] == "viz-hard-frame"
    why_blob = " ".join(f"{p['nl']} {p['en']}" for p in why["paragraphs"]).lower()
    assert "worked example" in why_blob or "uitgewerkt voorbeeld" in why_blob
    assert not any(v["kind"] == "official_link_slot" for v in module["visuals"])
    assert not any(v["knhb_illustration_placeholder"] for v in module["visuals"])
    assert module["further_reading"]
    assert any("fih.hockey" in fr["url"] for fr in module["further_reading"])


def test_hard_decisions_quiz_grades_mc_and_written_with_explanations(client):
    res = client.post(
        "/api/quizzes/quiz-hard-decisions/submit",
        json={
            "answers": [
                {"question_id": "q1-raised-first", "selected_option_id": "a"},
                {"question_id": "q2-clear-pressure", "selected_option_id": "d"},
                {"question_id": "q3-contested", "selected_option_id": "a"},
                {"question_id": "q4-gk-dive", "selected_option_id": "a"},
                {"question_id": "q5-pathway-refine", "written_answer": "nope"},
            ]
        },
    )
    assert res.status_code == 200
    body = res.json()
    assert body["total"] == 5
    assert body["score"] == 2
    by_id = {r["question_id"]: r for r in body["results"]}
    assert by_id["q1-raised-first"]["correct"] is False
    assert by_id["q1-raised-first"]["explanation"]["nl"]
    assert by_id["q1-raised-first"]["explanation"]["en"]
    assert by_id["q1-raised-first"]["visualization_hint"] == "hard-raised-danger"
    assert by_id["q1-raised-first"]["correct_option_id"] == "c"
    assert by_id["q2-clear-pressure"]["correct"] is True
    assert by_id["q3-contested"]["correct"] is True
    assert by_id["q3-contested"]["visualization_hint"] == "hard-contested"
    assert by_id["q4-gk-dive"]["correct"] is False
    assert by_id["q4-gk-dive"]["visualization_hint"] == "hard-gk-dive"
    assert by_id["q5-pathway-refine"]["correct"] is False
    assert by_id["q5-pathway-refine"]["visualization_hint"] == "hard-decision-frame"

    normalized = client.post(
        "/api/quizzes/quiz-hard-decisions/submit",
        json={
            "answers": [
                {"question_id": "q5-pathway-refine", "written_answer": "Pathway!"},
            ]
        },
    )
    assert normalized.status_code == 200
    n_by_id = {r["question_id"]: r for r in normalized.json()["results"]}
    assert n_by_id["q5-pathway-refine"]["correct"] is True


def test_hard_decisions_quiz_progress_save_and_resume(client):
    created = client.post("/api/progress/sessions", json={"locale": "en"})
    token = created.json()["access_token"]
    headers = _auth_headers(token)

    opened = client.put(
        "/api/progress/session",
        headers=headers,
        json={"module_id": "mod-hard-decisions", "status": "in_progress"},
    )
    assert opened.status_code == 200

    submit = client.post(
        "/api/quizzes/quiz-hard-decisions/submit",
        headers=headers,
        json={
            "save_progress": True,
            "answers": [
                {"question_id": "q1-raised-first", "selected_option_id": "c"},
                {"question_id": "q2-clear-pressure", "selected_option_id": "d"},
                {"question_id": "q3-contested", "selected_option_id": "a"},
                {"question_id": "q4-gk-dive", "selected_option_id": "c"},
                {
                    "question_id": "q5-pathway-refine",
                    "written_answer": "Hoofdklasse.",
                },
            ],
        },
    )
    assert submit.status_code == 200
    assert submit.json()["progress_saved"] is True
    assert submit.json()["score"] == 5

    progress = client.get("/api/progress/session", headers=headers)
    assert progress.status_code == 200
    row = next(
        p for p in progress.json()["progress"] if p["module_id"] == "mod-hard-decisions"
    )
    assert row["status"] == "completed"
    assert row["quiz_score"] == 5
    assert row["quiz_total"] == 5


def test_full_pathway_module_has_sections_and_visuals(client):
    res = client.get("/api/course/modules/mod-pathway-hoofdklasse")
    assert res.status_code == 200
    module = res.json()
    assert module["content_status"] == "full"
    assert module["kind"] == "shared"
    assert module["quiz_id"] == "quiz-pathway-professional"
    assert len(module["sections"]) >= 5
    assert len(module["visuals"]) >= 5
    assert all(s["title"]["nl"] and s["title"]["en"] for s in module["sections"])
    visual_ids = {v["id"] for v in module["visuals"]}
    for section in module["sections"]:
        if section["visual_id"]:
            assert section["visual_id"] in visual_ids
    assert any(v["kind"] == "svg_animation" for v in module["visuals"])
    keys = {
        v["animation_key"] for v in module["visuals"] if v["kind"] == "svg_animation"
    }
    assert keys >= {
        "match-cadence",
        "match-pressure",
        "partner-handoff",
        "consistency-loop",
        "standard-ladder",
    }
    assert "sec-standard-ladder" in {s["id"] for s in module["sections"]}
    ladder = next(s for s in module["sections"] if s["id"] == "sec-standard-ladder")
    assert ladder["visual_id"] == "viz-standard-ladder"
    why = next(s for s in module["sections"] if s["id"] == "sec-pathway-why")
    assert why["visual_id"] == "viz-match-cadence"
    assert not any(v["kind"] == "official_link_slot" for v in module["visuals"])
    assert not any(v["knhb_illustration_placeholder"] for v in module["visuals"])
    assert module["further_reading"]
    assert any("knhb.nl" in fr["url"] for fr in module["further_reading"])


def test_pathway_quiz_grades_mc_and_written_with_explanations(client):
    res = client.post(
        "/api/quizzes/quiz-pathway-professional/submit",
        json={
            "answers": [
                {"question_id": "q1-match-management", "selected_option_id": "a"},
                {"question_id": "q2-collaboration", "selected_option_id": "d"},
                {"question_id": "q3-consistency-keyword", "written_answer": "consistency"},
                {"question_id": "q4-pathway-keyword", "written_answer": "nope"},
                {"question_id": "q5-standard-when", "selected_option_id": "b"},
            ]
        },
    )
    assert res.status_code == 200
    body = res.json()
    assert body["total"] == 5
    assert body["score"] == 3
    by_id = {r["question_id"]: r for r in body["results"]}
    assert by_id["q1-match-management"]["correct"] is False
    assert by_id["q1-match-management"]["explanation"]["nl"]
    assert by_id["q1-match-management"]["explanation"]["en"]
    assert by_id["q1-match-management"]["visualization_hint"] == "match-pressure"
    assert by_id["q1-match-management"]["correct_option_id"] == "c"
    assert by_id["q2-collaboration"]["correct"] is True
    assert by_id["q2-collaboration"]["correct_option_id"] == "d"
    assert by_id["q3-consistency-keyword"]["correct"] is True
    assert by_id["q4-pathway-keyword"]["correct"] is False
    assert by_id["q5-standard-when"]["correct"] is True
    assert by_id["q5-standard-when"]["visualization_hint"] == "standard-ladder"


def test_pathway_quiz_progress_save_and_resume(client):
    created = client.post("/api/progress/sessions", json={"locale": "nl"})
    token = created.json()["access_token"]
    headers = _auth_headers(token)

    opened = client.put(
        "/api/progress/session",
        headers=headers,
        json={"module_id": "mod-pathway-hoofdklasse", "status": "in_progress"},
    )
    assert opened.status_code == 200

    submit = client.post(
        "/api/quizzes/quiz-pathway-professional/submit",
        headers=headers,
        json={
            "save_progress": True,
            "answers": [
                {"question_id": "q1-match-management", "selected_option_id": "c"},
                {"question_id": "q2-collaboration", "selected_option_id": "d"},
                {"question_id": "q3-consistency-keyword", "written_answer": "Consistency"},
                {"question_id": "q4-pathway-keyword", "written_answer": "Pathway!"},
                {"question_id": "q5-standard-when", "selected_option_id": "b"},
            ],
        },
    )
    assert submit.status_code == 200
    assert submit.json()["progress_saved"] is True
    assert submit.json()["score"] == 5

    progress = client.get("/api/progress/session", headers=headers)
    assert progress.status_code == 200
    row = next(
        p for p in progress.json()["progress"] if p["module_id"] == "mod-pathway-hoofdklasse"
    )
    assert row["status"] == "completed"
    assert row["quiz_score"] == 5
    assert row["quiz_total"] == 5


def test_full_interpretation_module_has_refs_and_visuals(client):
    res = client.get("/api/course/modules/mod-knhb-interpretations")
    assert res.status_code == 200
    module = res.json()
    assert module["content_status"] == "full"
    assert module["kind"] == "shared"
    assert module["quiz_id"] == "quiz-knhb-interpretations"
    assert len(module["sections"]) >= 4
    assert len(module["visuals"]) >= 3
    assert len(module["interpretation_references"]) >= 3
    assert all(s["title"]["nl"] and s["title"]["en"] for s in module["sections"])
    visual_ids = {v["id"] for v in module["visuals"]}
    for section in module["sections"]:
        if section["visual_id"]:
            assert section["visual_id"] in visual_ids
    for ref in module["interpretation_references"]:
        assert ref["topic"]["nl"] and ref["topic"]["en"]
        assert ref["summary"]["nl"] and ref["summary"]["en"]
        assert ref["official_source_url"]
        assert ref["attribution"]["source_name"]
        if ref["visual_id"]:
            assert ref["visual_id"] in visual_ids
    assert any(r["translation_needed"] for r in module["interpretation_references"])
    for ref in module["interpretation_references"]:
        if ref["translation_needed"]:
            assert "[EN translation slot]" in ref["summary"]["en"]
    assert any(v["animation_key"] == "source-stack" for v in module["visuals"])
    assert any(v["animation_key"] == "translation-slot" for v in module["visuals"])
    assert any(v["animation_key"] == "attribution-chain" for v in module["visuals"])
    assert any(v["knhb_illustration_placeholder"] for v in module["visuals"])


def test_interpretation_quiz_grades_mc_and_written_with_explanations(client):
    res = client.post(
        "/api/quizzes/quiz-knhb-interpretations/submit",
        json={
            "answers": [
                {"question_id": "q1-official-source", "selected_option_id": "a"},
                {"question_id": "q2-no-knhb-art", "selected_option_id": "c"},
                {"question_id": "q3-translation-keyword", "written_answer": "translation"},
                {"question_id": "q4-attribution-keyword", "written_answer": "nope"},
            ]
        },
    )
    assert res.status_code == 200
    body = res.json()
    assert body["total"] == 4
    assert body["score"] == 2
    by_id = {r["question_id"]: r for r in body["results"]}
    assert by_id["q1-official-source"]["correct"] is False
    assert by_id["q1-official-source"]["explanation"]["nl"]
    assert by_id["q1-official-source"]["explanation"]["en"]
    assert by_id["q1-official-source"]["visualization_hint"] == "source-stack"
    assert by_id["q1-official-source"]["correct_option_id"] == "b"
    assert by_id["q2-no-knhb-art"]["correct"] is True
    assert by_id["q2-no-knhb-art"]["correct_option_id"] == "c"
    assert by_id["q3-translation-keyword"]["correct"] is True
    assert by_id["q3-translation-keyword"]["visualization_hint"] == "translation-slot"
    assert by_id["q4-attribution-keyword"]["correct"] is False


def test_interpretation_quiz_progress_save_and_resume(client):
    created = client.post("/api/progress/sessions", json={"locale": "nl"})
    token = created.json()["access_token"]
    headers = _auth_headers(token)

    opened = client.put(
        "/api/progress/session",
        headers=headers,
        json={"module_id": "mod-knhb-interpretations", "status": "in_progress"},
    )
    assert opened.status_code == 200

    submit = client.post(
        "/api/quizzes/quiz-knhb-interpretations/submit",
        headers=headers,
        json={
            "save_progress": True,
            "answers": [
                {"question_id": "q1-official-source", "selected_option_id": "b"},
                {"question_id": "q2-no-knhb-art", "selected_option_id": "c"},
                {"question_id": "q3-translation-keyword", "written_answer": "Placeholder"},
                {"question_id": "q4-attribution-keyword", "written_answer": "Attribution!"},
            ],
        },
    )
    assert submit.status_code == 200
    assert submit.json()["progress_saved"] is True
    assert submit.json()["score"] == 4

    progress = client.get("/api/progress/session", headers=headers)
    assert progress.status_code == 200
    row = next(
        p for p in progress.json()["progress"] if p["module_id"] == "mod-knhb-interpretations"
    )
    assert row["status"] == "completed"
    assert row["quiz_score"] == 4
    assert row["quiz_total"] == 4


def test_full_capstone_module_has_sections_and_visuals(client):
    res = client.get("/api/course/modules/mod-capstone-assessment")
    assert res.status_code == 200
    module = res.json()
    assert module["content_status"] == "full"
    assert module["kind"] == "shared"
    assert module["quiz_id"] == "quiz-capstone-assessment"
    assert len(module["sections"]) >= 4
    assert len(module["visuals"]) >= 3
    assert all(s["title"]["nl"] and s["title"]["en"] for s in module["sections"])
    visual_ids = {v["id"] for v in module["visuals"]}
    for section in module["sections"]:
        if section["visual_id"]:
            assert section["visual_id"] in visual_ids
    assert any(v["animation_key"] == "capstone-weave" for v in module["visuals"])
    assert any(v["animation_key"] == "field-attack" for v in module["visuals"])
    assert any(v["animation_key"] == "indoor-rebound" for v in module["visuals"])
    assert any(v["animation_key"] == "match-pressure" for v in module["visuals"])
    assert any(v["knhb_illustration_placeholder"] for v in module["visuals"])
    assert len(module["interpretation_references"]) >= 1
    for ref in module["interpretation_references"]:
        if ref["translation_needed"]:
            assert "[EN translation slot]" in ref["summary"]["en"]


def test_capstone_quiz_grades_mc_and_written_with_explanations(client):
    res = client.post(
        "/api/quizzes/quiz-capstone-assessment/submit",
        json={
            "answers": [
                {"question_id": "q1-field-danger-priority", "selected_option_id": "a"},
                {"question_id": "q2-indoor-lift-boards", "selected_option_id": "c"},
                {"question_id": "q3-pathway-management", "selected_option_id": "c"},
                {"question_id": "q4-interpretation-source", "selected_option_id": "b"},
                {"question_id": "q5-safety-keyword", "written_answer": "safety"},
                {"question_id": "q6-capstone-keyword", "written_answer": "nope"},
            ]
        },
    )
    assert res.status_code == 200
    body = res.json()
    assert body["total"] == 6
    assert body["score"] == 4
    by_id = {r["question_id"]: r for r in body["results"]}
    assert by_id["q1-field-danger-priority"]["correct"] is False
    assert by_id["q1-field-danger-priority"]["explanation"]["nl"]
    assert by_id["q1-field-danger-priority"]["explanation"]["en"]
    assert by_id["q1-field-danger-priority"]["visualization_hint"] == "field-attack"
    assert by_id["q1-field-danger-priority"]["correct_option_id"] == "b"
    assert by_id["q2-indoor-lift-boards"]["correct"] is True
    assert by_id["q2-indoor-lift-boards"]["visualization_hint"] == "indoor-rebound"
    assert by_id["q3-pathway-management"]["correct"] is True
    assert by_id["q3-pathway-management"]["visualization_hint"] == "match-pressure"
    assert by_id["q4-interpretation-source"]["correct"] is True
    assert by_id["q4-interpretation-source"]["visualization_hint"] == "source-stack"
    assert by_id["q5-safety-keyword"]["correct"] is True
    assert by_id["q5-safety-keyword"]["visualization_hint"] == "safety-triangle"
    assert by_id["q6-capstone-keyword"]["correct"] is False
    assert by_id["q6-capstone-keyword"]["visualization_hint"] == "capstone-weave"


def test_capstone_quiz_progress_save_and_resume(client):
    created = client.post("/api/progress/sessions", json={"locale": "nl"})
    token = created.json()["access_token"]
    headers = _auth_headers(token)

    opened = client.put(
        "/api/progress/session",
        headers=headers,
        json={"module_id": "mod-capstone-assessment", "status": "in_progress"},
    )
    assert opened.status_code == 200

    submit = client.post(
        "/api/quizzes/quiz-capstone-assessment/submit",
        headers=headers,
        json={
            "save_progress": True,
            "answers": [
                {"question_id": "q1-field-danger-priority", "selected_option_id": "b"},
                {"question_id": "q2-indoor-lift-boards", "selected_option_id": "c"},
                {"question_id": "q3-pathway-management", "selected_option_id": "c"},
                {"question_id": "q4-interpretation-source", "selected_option_id": "b"},
                {"question_id": "q5-safety-keyword", "written_answer": "Safety"},
                {"question_id": "q6-capstone-keyword", "written_answer": "Capstone!"},
            ],
        },
    )
    assert submit.status_code == 200
    assert submit.json()["progress_saved"] is True
    assert submit.json()["score"] == 6

    progress = client.get("/api/progress/session", headers=headers)
    assert progress.status_code == 200
    row = next(
        p for p in progress.json()["progress"] if p["module_id"] == "mod-capstone-assessment"
    )
    assert row["status"] == "completed"
    assert row["quiz_score"] == 6
    assert row["quiz_total"] == 6


def test_invalid_locale_rejected(client):
    res = client.post("/api/progress/sessions", json={"locale": "de"})
    assert res.status_code == 422


def test_practice_bank_lists_field_and_indoor_without_answers(client):
    res = client.get("/api/practice")
    assert res.status_code == 200
    body = res.json()
    assert body["title"]["nl"]
    assert body["title"]["en"]
    assert len(body["scenarios"]) >= 6
    kinds = {s["kind"] for s in body["scenarios"]}
    assert kinds == {"field", "indoor"}
    module_ids = {m["id"] for m in client.get("/api/course").json()["modules"]}
    for scenario in body["scenarios"]:
        assert scenario["id"] not in module_ids
        assert scenario["situation"]["nl"] and scenario["situation"]["en"]
        assert scenario["visual_key"] in _SPA_ANIMATION_KEYS
        quiz = scenario["quiz"]
        assert quiz["questions"]
        types = {q["type"] for q in quiz["questions"]}
        assert "multiple_choice" in types
        assert "written" in types
        for q in quiz["questions"]:
            assert "correct_option_id" not in q
            assert "accepted_answers" not in q
            assert "feedback_correct" not in q


def test_practice_scenario_grades_and_saves_progress(client):
    detail = client.get("/api/practice/practice-field-raised-circle")
    assert detail.status_code == 200
    scenario = detail.json()
    assert scenario["kind"] == "field"
    quiz_id = scenario["quiz"]["id"]

    created = client.post("/api/progress/sessions", json={"locale": "en"})
    token = created.json()["access_token"]
    headers = _auth_headers(token)

    opened = client.put(
        "/api/progress/session",
        headers=headers,
        json={"module_id": "practice-field-raised-circle", "status": "in_progress"},
    )
    assert opened.status_code == 200

    submit = client.post(
        f"/api/quizzes/{quiz_id}/submit",
        headers=headers,
        json={
            "save_progress": True,
            "answers": [
                {"question_id": "q1-first-read", "selected_option_id": "b"},
                {"question_id": "q2-danger-axes", "written_answer": "direction"},
            ],
        },
    )
    assert submit.status_code == 200
    body = submit.json()
    assert body["score"] == 2
    assert body["total"] == 2
    assert body["progress_saved"] is True
    by_id = {r["question_id"]: r for r in body["results"]}
    assert by_id["q1-first-read"]["correct"] is True
    assert by_id["q1-first-read"]["explanation"]["nl"]
    assert by_id["q1-first-read"]["explanation"]["en"]
    assert by_id["q1-first-read"]["visualization_hint"] == "practice-circle-entry"
    assert by_id["q2-danger-axes"]["correct"] is True

    progress = client.get("/api/progress/session", headers=headers)
    row = next(
        p
        for p in progress.json()["progress"]
        if p["module_id"] == "practice-field-raised-circle"
    )
    assert row["status"] == "completed"
    assert row["quiz_score"] == 2
    assert row["quiz_total"] == 2


def test_practice_scenario_not_found(client):
    res = client.get("/api/practice/does-not-exist")
    assert res.status_code == 404
