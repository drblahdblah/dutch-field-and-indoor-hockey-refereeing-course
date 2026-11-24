"""Backend API smoke and behavior tests."""


def test_health(client):
    res = client.get("/api/health")
    assert res.status_code == 200
    body = res.json()
    assert body["status"] == "ok"


def test_course_outline_bilingual(client):
    res = client.get("/api/course")
    assert res.status_code == 200
    body = res.json()
    assert body["title"]["nl"]
    assert body["title"]["en"]
    assert len(body["modules"]) >= 3
    assert "quiz-dangerous-play-basics" in body["quizzes"]
    assert any(a.get("knhb_illustration_placeholder") for a in body["attributions"])


def test_quiz_get_hides_answers(client):
    res = client.get("/api/course/quizzes/quiz-dangerous-play-basics")
    assert res.status_code == 200
    quiz = res.json()
    for q in quiz["questions"]:
        assert q["correct_option_id"] is None
        assert q["accepted_answers"] is None


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
    wrong = next(r for r in body["results"] if r["question_id"] == "q1-raised-ball")
    assert wrong["correct"] is False
    assert wrong["explanation"]["en"]
    assert wrong["correct_option_id"] == "b"


def test_session_progress_roundtrip(client):
    created = client.post("/api/progress/sessions", json={"display_name": "Test", "locale": "nl"})
    assert created.status_code == 201
    session_id = created.json()["id"]

    updated = client.put(
        f"/api/progress/sessions/{session_id}",
        json={"module_id": "mod-field-danger", "status": "in_progress"},
    )
    assert updated.status_code == 200
    assert updated.json()["status"] == "in_progress"

    submit = client.post(
        "/api/quizzes/quiz-dangerous-play-basics/submit",
        json={
            "session_id": session_id,
            "answers": [
                {"question_id": "q1-raised-ball", "selected_option_id": "b"},
                {"question_id": "q2-advantage-keyword", "written_answer": "Advantage!"},
            ],
        },
    )
    assert submit.status_code == 200
    assert submit.json()["progress_saved"] is True
    assert submit.json()["score"] == 2

    progress = client.get(f"/api/progress/sessions/{session_id}")
    assert progress.status_code == 200
    modules = {p["module_id"]: p for p in progress.json()["progress"]}
    assert modules["mod-field-danger"]["status"] == "completed"
    assert modules["mod-field-danger"]["quiz_score"] == 2
