import pytest
from flask.testing import FlaskClient

from webapp.app import app


@pytest.fixture
def client() -> FlaskClient:
    """
    Initializes a Flask testing client.

    :return: app for testing (e.g., <class 'flask.testing.FlaskClient'>)
    """
    yield app.test_client()
