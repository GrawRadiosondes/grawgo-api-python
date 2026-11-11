from typing import Any

import pytest
from requests import Response

from grawgo import api as api_module
from grawgo.api import Api


@pytest.fixture
def captured_kwargs(monkeypatch: pytest.MonkeyPatch) -> list[dict[str, Any]]:
    calls: list[dict[str, Any]] = []

    def fake_request(**kwargs: Any) -> Response:
        calls.append(kwargs)
        response = Response()
        response.status_code = 200
        return response

    monkeypatch.setattr(api_module, "get", fake_request)
    monkeypatch.setattr(api_module, "post", fake_request)
    return calls


def test_default_timeout():
    assert Api(base_url="https://example.com/api").timeout == 30


def test_get_uses_timeout(captured_kwargs: list[dict[str, Any]]):
    Api(base_url="https://example.com/api", timeout=5).status()
    assert captured_kwargs[-1]["timeout"] == 5


def test_post_uses_timeout(captured_kwargs: list[dict[str, Any]]):
    Api(base_url="https://example.com/api", timeout=2.5).attach_station_to_user(
        user_id=1, station_id=1
    )
    assert captured_kwargs[-1]["timeout"] == 2.5
