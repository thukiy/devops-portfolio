from types import SimpleNamespace

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.routes import routes
from app.routes.routes import Stats, bp


def make_task(done):
    return SimpleNamespace(done=done)


def test_counts_done_and_open():
    tasks = [make_task(done=True), make_task(done=False), make_task(done=True)]
    stats = Stats(tasks)
    assert stats.total == 3
    assert stats.done == 2
    assert stats.open == 1


@pytest.mark.parametrize("flags, expected_total, expected_done, expected_open", [
    ([], 0, 0, 0),
    ([True], 1, 1, 0),
    ([False], 1, 0, 1),
    ([True, False], 2, 1, 1),
    ([True, True], 2, 2, 0),
    ([False, False], 2, 0, 2),
])
def test_stats(flags, expected_total, expected_done, expected_open):
    stats = Stats([make_task(done=flag) for flag in flags])
    assert stats.total == expected_total
    assert stats.done == expected_done
    assert stats.open == expected_open


def test_stats_endpoint(monkeypatch):
    monkeypatch.setattr(routes, "TASKS", [make_task(done=True), make_task(done=False)])
    app = FastAPI()
    app.include_router(bp)
    client = TestClient(app)

    response = client.get("/api/todos/stats")

    assert response.status_code == 200
    assert response.json() == {"total": 2, "done": 1, "open": 1}
