import json
import pytest
from backend.application import app


@pytest.fixture
def client():
    return app.test_client()


def test_response(client):
    result = client.get()
    assert 1 == 1
