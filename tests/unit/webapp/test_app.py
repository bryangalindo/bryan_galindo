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


def test_landing_page(client: FlaskClient):
    landing = client.get("/")
    assert landing.status_code == 200
    html = landing.data.decode()
    assert '<section id="about-me">' in html
    assert '<section id="hobbies">' in html
    assert '<meta http-equiv="Cache-Control"' in html
