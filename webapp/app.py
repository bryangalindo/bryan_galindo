"""
Main entrypoint for Flask app
"""
import sentry_sdk
from flask import Flask
from flask import redirect
from flask import render_template
from flask import send_from_directory
from sentry_sdk.integrations.flask import FlaskIntegration
from werkzeug.wrappers.response import Response

import core.config as cfg
from core.constants import CSP_SCRIPT_EXCLUSION_HEADERS

sentry_sdk.init(
    dsn=cfg.SENTRY_DSN,
    integrations=[
        FlaskIntegration(),
    ],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
    _experiments={
        "profiles_sample_rate": 1.0,
    },
)


app: Flask = Flask(__name__)


@app.after_request
def add_security_headers(response: Response) -> Response:
    """
    Adds security headers to response to prevent attacks (e.g., cross-site scripting,
    man-in-the-middle (MITM)).

    :param response: Werkzeug response object (e.g., <Response 370 bytes [302 FOUND]>)
    :return: Werkzeug response object (e.g., <Response 370 bytes [302 FOUND]>)
    """
    response.headers[
        "Content-Security-Policy"
    ] = f"script-src {CSP_SCRIPT_EXCLUSION_HEADERS}"
    response.headers[
        "Strict-Transport-Security"
    ] = "max-age=31536000; includeSubDomains"
    return response


@app.route("/")
def home() -> str:
    """
    Renders the home template from the template folder as a str.

    :returns: html as str (e.g., '<!doctype html>...<body>...</body></html>')
    """
    return render_template("home.html")


@app.route("/resume")
def resume() -> Response:
    """
    Redirects the client to my resume.

    :returns: Werkzeug response object (e.g., <Response 370 bytes [302 FOUND]>)
    """
    return redirect(cfg.RESUME_URL)


@app.route("/tamalemkt")
def tamalemkt() -> Response:
    """
    Redirects the client to the tamale ordering website I built for my mom.

    :returns: Werkzeug response object (e.g., <Response 370 bytes [302 FOUND]>)
    """
    return redirect("https://tamalemkt.com")


@app.route("/robots.txt")
def robotstxt() -> Response:
    """
    Loads robot.txt from Flask static folder.

    :returns: Werkzeug response object (e.g., <Response 370 bytes [302 FOUND]>)
    """
    return send_from_directory(app.static_folder, "robots.txt")


@app.route("/rankmebby")
def rankmebby() -> Response:
    """
    Redirects the client to the NFT ranking website clone I built.

    :returns: Werkzeug response object (e.g., <Response 370 bytes [302 FOUND]>)
    """
    return redirect("https://rankmebby.com")


@app.route("/bloom")
def bloom() -> Response:
    """
    Redirects the client to the ELI5 Bloom Filter article I wrote.

    :return: Werkzeug response object (e.g., <Response 370 bytes [302 FOUND]>)
    """
    return redirect(
        "https://medium.com/gitconnected/eli5-what-the-f-is-a-bloom-filter-4a58a160833d"
    )


@app.route("/termsofuse")
def termsofuse() -> str:
    """
    Displays terms of use as string.

    :return: string (e.g., "No scraping")
    """
    return "<h1>No Scraping</h1>"
