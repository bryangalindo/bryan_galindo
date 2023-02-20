"""
Unit tests for Flask endpoints
"""
from typing import Iterator

import pytest
from flask.testing import FlaskClient

import core.config as cfg
from webapp.app import app  # pylint: disable=import-error


@pytest.fixture
def client() -> Iterator[FlaskClient]:  # pylint: disable=redefined-outer-name
    """
    Initializes a Flask testing client.

    :return: app for testing (e.g., <class 'flask.testing.FlaskClient'>)
    """
    yield app.test_client()


def test_home_page(
    client: FlaskClient,  # pylint: disable=redefined-outer-name
) -> None:
    """
    Tests landing page for major html sections/tags.

    :return: None
    """
    with client as test_client:
        response = test_client.get("/")
        assert response.status_code == 200
        html = response.data.decode()
        assert '<section id="about-me">' in html
        assert '<section id="hobbies">' in html
        assert '<meta http-equiv="Cache-Control"' in html


def test_resume_endpoint(
    client: FlaskClient,  # pylint: disable=redefined-outer-name
) -> None:
    """
    Tests resume endpoint to make sure redirects are ok.

    :return: None
    """
    with client as test_client:
        response = test_client.get("/resume")
        assert response.status_code == 302
        assert response.request.path == "/resume"
        assert response.location == cfg.RESUME_URL
