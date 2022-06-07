from flask import render_template, Flask, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/resume')
def resume():
    return redirect('https://drive.google.com/file/d/1xlDYXAdjLRmQvtt7GFkY30j_X8gcEEri/view?usp=sharing')
