import pytest

from hooks import app


@pytest.fixture(scope='session')
def test_client():
    return app.test_client()
