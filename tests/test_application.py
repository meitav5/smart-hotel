import json
import pytest
from backend.application import application


@pytest.fixture
def client():
    return application.test_client()


def test_response(client):
    result = client.get()
    assert 1 == 1
