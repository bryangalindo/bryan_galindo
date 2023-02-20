from flask import render_template, Flask, redirect
from werkzeug.wrappers.response import Response

app = Flask(__name__)


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
    return redirect(
        "https://drive.google.com/file/d/1kTTryC5yijLwlhN7mldimq2y46l__hFn/view?usp=sharing"
    )


@app.route("/breakoutlevels")
def breakouts():
    return redirect("https://archive.ph/YNd5H")


@app.route("/ebayscraper")
def ebayscraper():
    return redirect("https://github.com/bryangalindo/scrape/blob/master/ebayscrape.py")


@app.route("/tamalemkt")
def tamalemkt():
    return redirect("https://tamalemkt.com")
