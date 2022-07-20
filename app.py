from flask import render_template, Flask, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/resume')
def resume():
    return redirect('https://drive.google.com/file/d/1QRPfRh5tIq86xZE-ODQR6f6GQnR5UAlN/view?usp=sharing')


@app.route('/breakoutlevels')
def breakouts():
    return redirect('https://archive.ph/YNd5H')
