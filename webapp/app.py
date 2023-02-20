"""
Main entrypoint for Flask app
"""
import os

from dotenv import load_dotenv
from flask import render_template, Flask, redirect
from werkzeug.wrappers.response import Response

load_dotenv()

RESUME_URL = os.environ["RESUME_URL"]

app: Flask = Flask(__name__)


@app.route("/")
def home() -> str:
    """
    Renders the home template from the template folder as a str.

    :returns: html as str (e.g., '<!doctype html><html lang="en"><body>...</body></html>')
    """
    return render_template("home.html")


@app.route("/resume")
def resume() -> Response:
    """
    Redirects the client to my resume.

    :returns: Werkzeug response object (e.g., <Response 370 bytes [302 FOUND]>)
    """
    return redirect(RESUME_URL)


@app.route("/tamalemkt")
def tamalemkt() -> Response:
    """
    Redirects the client to the tamale ordering website I built for my mom.

    :returns: Werkzeug response object (e.g., <Response 370 bytes [302 FOUND]>)
    """
    return redirect("https://tamalemkt.com")
