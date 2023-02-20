import pytest
from flask.testing import FlaskClient

from webapp.app import app  # pylint: disable=import-error actually imports ok


@pytest.fixture
def client() -> FlaskClient:  # pylint: disable=redefined-outer-name necessary for flask unit test
    """
    Initializes a Flask testing client.

    :return: app for testing (e.g., <class 'flask.testing.FlaskClient'>)
    """
    yield app.test_client()


def test_landing_page(client: FlaskClient) -> None:
    """
    Tests landing page for major html sections/tags.

    :return: None
    """
    landing = client.get("/")
    assert landing.status_code == 200
    html = landing.data.decode()
    assert '<section id="about-me">' in html
    assert '<section id="hobbies">' in html
    assert '<meta http-equiv="Cache-Control"' in html
