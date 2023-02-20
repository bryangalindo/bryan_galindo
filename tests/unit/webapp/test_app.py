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


def test_tamalemkt_endpoint(
    client: FlaskClient,  # pylint: disable=redefined-outer-name
) -> None:
    """
    Tests resume endpoint to make sure redirects are ok.

    :return: None
    """
    with client:
        response = client.get("/tamalemkt")
        assert response.status_code == 302
        assert response.request.path == "/tamalemkt"
        assert response.location == "https://tamalemkt.com"


def test_robotstxt_endpoint(
    client: FlaskClient,  # pylint: disable=redefined-outer-name
) -> None:
    """
    Tests robots.txt endpoint to make sure txt file is loaded correctly.

    :return: None
    """
    with client:
        response = client.get("/robots.txt")
        html = response.data.decode()
        assert response.status_code == 200
        assert "User-agent: *" in html
        assert "Disallow: /" in html


def test_content_security_policy_header_exists(
    client: FlaskClient,  # pylint: disable=redefined-outer-name
) -> None:
    """
    Confirms that the 'Content-Security-Policy' header value exists.

    :return: None
    """
    with client:
        response = client.get("/")
        assert response.status_code == 200
        assert "Content-Security-Policy" in response.headers


def test_strict_transport_security_header_exists(
    client: FlaskClient,  # pylint: disable=redefined-outer-name
) -> None:
    """
    Confirms that the 'Strict-Transport-Security' header value exists.

    :return: None
    """
    with client:
        response = client.get("/")
        assert response.status_code == 200
        assert "Strict-Transport-Security" in response.headers
        assert (
            response.headers["Strict-Transport-Security"]
            == "max-age=31536000; includeSubDomains"
        )
