"""Backend API smoke and behavior tests."""


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
    assert "quiz-dangerous-play-basics" in body["quizzes"]
    assert "quiz-indoor-context-basics" in body["quizzes"]
    assert any(a.get("knhb_illustration_placeholder") for a in body["attributions"])
    for quiz in body["quizzes"].values():
        for q in quiz["questions"]:
            assert "correct_option_id" not in q
            assert "accepted_answers" not in q
            assert "feedback_correct" not in q
            assert "feedback_incorrect" not in q


def test_quiz_get_hides_answers(client):
    res = client.get("/api/course/quizzes/quiz-dangerous-play-basics")
    assert res.status_code == 200
    quiz = res.json()
    for q in quiz["questions"]:
        assert "correct_option_id" not in q
        assert "accepted_answers" not in q


def test_quiz_submit_grades_and_explains(client):
    res = client.post(
        "/api/quizzes/quiz-dangerous-play-basics/submit",
        json={
            "answers": [
                {"question_id": "q1-raised-ball", "selected_option_id": "c"},
                {"question_id": "q2-advantage-keyword", "written_answer": "advantage"},
            ]
        },
    )
    assert res.status_code == 200
    body = res.json()
    assert body["score"] == 1
    assert body["total"] == 2
    assert body["progress_saved"] is False
    wrong = next(r for r in body["results"] if r["question_id"] == "q1-raised-ball")
    assert wrong["correct"] is False
    assert wrong["explanation"]["en"]
    assert wrong["correct_option_id"] == "b"


def test_quiz_submit_rejects_unknown_question(client):
    res = client.post(
        "/api/quizzes/quiz-dangerous-play-basics/submit",
        json={"answers": [{"question_id": "not-a-real-question", "selected_option_id": "a"}]},
    )
    assert res.status_code == 400


def test_progress_requires_bearer_token(client):
    res = client.get("/api/progress/session")
    assert res.status_code == 401

    created = client.post("/api/progress/sessions", json={"display_name": "Test", "locale": "nl"})
    assert created.status_code == 201
    body = created.json()
    assert body["access_token"]
    token = body["access_token"]

    denied = client.get(f"/api/progress/sessions/{body['id']}")
    assert denied.status_code == 404

    ok = client.get("/api/progress/session", headers=_auth_headers(token))
    assert ok.status_code == 200
    assert ok.json()["session"]["id"] == body["id"]


def test_session_progress_roundtrip(client):
    created = client.post("/api/progress/sessions", json={"display_name": "Test", "locale": "nl"})
    assert created.status_code == 201
    token = created.json()["access_token"]
    headers = _auth_headers(token)

    updated = client.put(
        "/api/progress/session",
        headers=headers,
        json={"module_id": "mod-field-danger", "status": "in_progress"},
    )
    assert updated.status_code == 200
    assert updated.json()["status"] == "in_progress"

    bad_module = client.put(
        "/api/progress/session",
        headers=headers,
        json={"module_id": "not-a-module", "status": "in_progress"},
    )
    assert bad_module.status_code == 400

    submit = client.post(
        "/api/quizzes/quiz-dangerous-play-basics/submit",
        headers=headers,
        json={
            "save_progress": True,
            "answers": [
                {"question_id": "q1-raised-ball", "selected_option_id": "b"},
                {"question_id": "q2-advantage-keyword", "written_answer": "Advantage!"},
            ],
        },
    )
    assert submit.status_code == 200
    assert submit.json()["progress_saved"] is True
    assert submit.json()["score"] == 2

    progress = client.get("/api/progress/session", headers=headers)
    assert progress.status_code == 200
    modules = {p["module_id"]: p for p in progress.json()["progress"]}
    assert modules["mod-field-danger"]["status"] == "completed"
    assert modules["mod-field-danger"]["quiz_score"] == 2


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
